from abc import ABC, abstractmethod
from typing import Any


class BaseDTOConverter(ABC):
    """Converter interface"""

    @classmethod
    @abstractmethod
    async def encode_dto_to_bytes(cls, dto) -> bytes:
        """Encode DTO to bytes"""

    @classmethod
    @abstractmethod
    async def decode_bytes_to_dto(cls, data: bytes) -> Any:
        """Decode bytes to DTO"""
