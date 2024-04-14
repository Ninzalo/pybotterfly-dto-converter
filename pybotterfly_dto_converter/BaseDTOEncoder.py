from abc import ABC, abstractmethod

from .BaseDTO import BaseDTO


class BaseDTOEncoder(ABC):
    """DTO Encoder interface"""

    @classmethod
    @abstractmethod
    def validate_input(cls, dto: BaseDTO) -> None:
        """
        Validate the input.

        :param dto: The DTO to validate.
        :type dto: BaseDTO
        """

    @classmethod
    @abstractmethod
    async def dataclass_to_str(cls, dto: BaseDTO) -> str:
        """
        Convert a DTO to a string.

        :param dto: The DTO to convert.
        :type dto: BaseDTO

        :return: The DTO as a string.
        :rtype: str
        """

    @classmethod
    @abstractmethod
    async def str_to_bytes(cls, dto_string: str) -> bytes:
        """
        Convert a DTO string to a bytes.

        :param dto_string: The DTO string to convert.
        :type dto_string: str

        :return: bytes
        :rtype: bytes
        """
