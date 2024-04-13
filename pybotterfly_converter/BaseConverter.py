from abc import ABC, abstractmethod


class BaseConverter(ABC):
    """Converter interface"""

    @classmethod
    @abstractmethod
    async def encode_dto_to_bytes(cls, dto: object) -> bytes:
        """Encode DTO to bytes"""

    @classmethod
    @abstractmethod
    async def decode_bytes_to_dto(cls, data: bytes) -> object:
        """Decode bytes to DTO"""
