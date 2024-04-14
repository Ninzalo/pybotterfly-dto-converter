import dataclasses
import importlib
import json
import pickle
import sys

from .BaseDTOConverter import BaseDTOConverter, IsDataclass


class DTOConverter(BaseDTOConverter):
    """Converter for Data Transfer Objects."""

    @classmethod
    async def encode_dto_to_bytes(cls, dto: IsDataclass) -> bytes:
        return await cls._str_to_bytes(await cls._dataclass_to_str(dto))

    @classmethod
    async def decode_bytes_to_dto(cls, data: bytes) -> IsDataclass:
        return await cls._str_to_dataclass(await cls._bytes_to_str(data))

    @classmethod
    async def _str_to_bytes(cls, dto_string: str) -> bytes:
        """
        Convert a DTO string to a bytes.

        :param dto_string: The DTO string to convert.
        :type dto_string: str

        :return: bytes
        :rtype: bytes
        """
        return pickle.dumps(dto_string)

    @classmethod
    async def _bytes_to_str(cls, dto_bytes: bytes) -> str:
        """
        Convert a DTO bytes to a string.

        :param dto_bytes: The DTO bytes to convert.
        :type dto_bytes: bytes

        :return: The DTO as a string.
        :rtype: str
        """
        return pickle.loads(dto_bytes)

    @classmethod
    async def _dataclass_to_str(cls, dto: IsDataclass) -> str:
        """
        Convert a DTO to a string.

        :param dto: The DTO to convert.
        :type: IsDataclass

        :return: The DTO as a string.
        :rtype: str
        """
        if not dataclasses.is_dataclass(dto):
            raise TypeError(f"Expected dataclass instance, got '{type(dto)}' object")
        return json.dumps(dto, default=cls._dataclass_object_dump)

    @classmethod
    async def _str_to_dataclass(cls, dto_string: str) -> IsDataclass:
        """
        Convert a DTO string to a dataclass.

        :param dto_string: The DTO string to convert.
        :type dto_string: str

        :return: The dataclass you've encoded
        :rtype: IsDataclass
        """
        return json.loads(dto_string, object_hook=cls._dataclass_object_load)

    @classmethod
    def _dataclass_object_dump(cls, dto: IsDataclass) -> dict:
        datacls = type(dto)
        if not dataclasses.is_dataclass(datacls):
            raise TypeError(f"Expected dataclass instance, got '{datacls!r}' object")
        mod = sys.modules.get(datacls.__module__)
        if mod is None or not hasattr(mod, datacls.__qualname__):
            raise ValueError(f"Can't resolve '{datacls!r}' reference")
        ref = f"{datacls.__module__}.{datacls.__qualname__}"
        fields = (f.name for f in dataclasses.fields(dto))
        return {**{f: getattr(dto, f) for f in fields}, "__dataclass__": ref}

    @classmethod
    def _dataclass_object_load(cls, dictionary: dict) -> IsDataclass | dict:
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
