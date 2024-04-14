import dataclasses
import importlib
import json
import pickle

from .BaseDTO import BaseDTO
from .BaseDTODecoder import BaseDTODecoder


class DTODecoder(BaseDTODecoder):
    """Decoder for Data Transfer Objects."""

    @classmethod
    def bytes_to_str(cls, dto_bytes: bytes) -> str:
        return pickle.loads(dto_bytes)

    @classmethod
    def str_to_dataclass(cls, dto_string: str) -> BaseDTO:
        return json.loads(dto_string, object_hook=cls._dataclass_object_load)

    @classmethod
    def _dataclass_object_load(cls, dictionary: dict) -> BaseDTO | dict:
        ref = dictionary.pop("__dataclass__", None)
        if ref is None:
            return dictionary
        try:
            modname, _, qualname = ref.rpartition(".")
            module = importlib.import_module(modname)
            datacls = getattr(module, qualname)
            if not dataclasses.is_dataclass(datacls) or not isinstance(datacls, type):
                raise ValueError
            return datacls(**dictionary)
        except (ModuleNotFoundError, ValueError, AttributeError, TypeError):
            raise ValueError(f"Invalid dataclass reference {ref!r}") from None
