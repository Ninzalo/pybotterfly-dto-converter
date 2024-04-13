from abc import ABC, abstractmethod
from typing import Any, ClassVar, Dict, Protocol


class IsDataclass(Protocol):
    """Type checker for dataclass"""

    __dataclass_fields__: ClassVar[Dict[str, Any]]


class BaseDTOConverter(ABC):
    """Converter interface"""

    @classmethod
    @abstractmethod
    async def encode_dto_to_bytes(cls, dto: IsDataclass) -> bytes:
        """Encode DTO to bytes"""

    @classmethod
    @abstractmethod
    async def decode_bytes_to_dto(cls, data: bytes) -> IsDataclass:
        """Decode bytes to DTO"""
