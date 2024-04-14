from abc import ABC, abstractmethod

from .BaseDTO import BaseDTO


class BaseDTODecoder(ABC):
    """DTO Decoder interface"""

    @classmethod
    @abstractmethod
    def validate_input(cls, dto_bytes: bytes) -> None:
        """
        Validate the input.

        :param dto_bytes: The bytes to validate.
        :type dto_bytes: bytes
        """

    @classmethod
    @abstractmethod
    def bytes_to_str(cls, dto_bytes: bytes) -> str:
        """
        Convert a DTO bytes to a string.

        :param dto_bytes: The DTO bytes to convert.
        :type dto_bytes: bytes

        :return: The DTO as a string.
        :rtype: str
        """

    @classmethod
    @abstractmethod
    def str_to_dataclass(cls, dto_string: str) -> BaseDTO:
        """
        Convert a DTO string to a dataclass.

        :param dto_string: The DTO string to convert.
        :type dto_string: str

        :return: The dataclass you've encoded
        :rtype: BaseDTO
        """
