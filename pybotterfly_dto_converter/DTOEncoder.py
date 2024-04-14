import dataclasses
import json
import pickle
import sys

from .BaseDTO import BaseDTO
from .BaseDTOEncoder import BaseDTOEncoder


class DTOEncoder(BaseDTOEncoder):
    """Encoder for Data Transfer Objects."""

    @classmethod
    async def dataclass_to_str(cls, dto: BaseDTO) -> str:
        if not dataclasses.is_dataclass(dto):
            raise TypeError(f"Expected dataclass instance, got '{type(dto)}' object")
        return json.dumps(dto, default=cls._dataclass_object_dump)

    @classmethod
    async def str_to_bytes(cls, dto_string: str) -> bytes:
        return pickle.dumps(dto_string)

    @classmethod
    def _dataclass_object_dump(cls, dto: BaseDTO) -> dict:
        datacls = type(dto)
        if not dataclasses.is_dataclass(datacls):
            raise TypeError(f"Expected dataclass instance, got '{datacls!r}' object")
        mod = sys.modules.get(datacls.__module__)
        if mod is None or not hasattr(mod, datacls.__qualname__):
            raise ValueError(f"Can't resolve '{datacls!r}' reference")
        ref = f"{datacls.__module__}.{datacls.__qualname__}"
        fields = (f.name for f in dataclasses.fields(dto))
        return {**{f: getattr(dto, f) for f in fields}, "__dataclass__": ref}
