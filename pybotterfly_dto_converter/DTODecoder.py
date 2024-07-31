import base64
import dataclasses
import importlib
import json
import pickle

from .BaseDTO import BaseDTO
from .BaseDTODecoder import BaseDTODecoder


class DTODecoder(BaseDTODecoder):
    """Decoder for Data Transfer Objects."""

    @classmethod
    def validate_input(cls, dto_bytes: bytes) -> None:
        if not isinstance(dto_bytes, bytes):
            msg = "Input must be bytes"
            raise TypeError(msg)

    @classmethod
    def bytes_to_str(cls, dto_bytes: bytes) -> str:
        return pickle.loads(dto_bytes)

    @classmethod
    def str_to_dataclass(cls, dto_string: str) -> BaseDTO:
        return json.loads(dto_string, object_hook=cls._dataclass_object_load)

    @classmethod
    def decode_dto_string(cls, dto_string: str) -> str:
        return base64.b64decode(dto_string.encode()).decode()

    @classmethod
    def _dataclass_object_load(cls, dictionary: dict) -> BaseDTO | dict:
        ref = dictionary.pop("__dataclass__", None)
        if ref is None:
            return dictionary
        try:
            modname, _, qualname = ref.rpartition(".")
            module = importlib.import_module(modname)
            datacls = getattr(module, qualname)
            if not dataclasses.is_dataclass(datacls) or not isinstance(
                datacls,
                type,
            ):
                raise ValueError
            return datacls(**dictionary)
        except (ModuleNotFoundError, ValueError, AttributeError, TypeError):
            value_error_str = f"Invalid dataclass reference {ref!r}"
            raise ValueError(value_error_str) from None
