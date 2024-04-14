from abc import ABC, abstractmethod

from .BaseDTO import BaseDTO


class BaseDTOConverter(ABC):
    """DTO Converter interface"""

    @classmethod
    @abstractmethod
    async def encode(cls, dto: BaseDTO) -> bytes:
        """Encode DTO to bytes

        :param dto: The DTO to convert.
        :type dto: BaseDTO

        :return: bytes
        :rtype: bytes
        """

    @classmethod
    @abstractmethod
    async def decode(cls, dto_bytes: bytes) -> BaseDTO:
        """Decode bytes to DTO

        :param data: The bytes to convert to DTO.
        :type data: bytes

        :return: The DTO
        :rtype: BaseDTO
        """
