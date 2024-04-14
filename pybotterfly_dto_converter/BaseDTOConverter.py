from abc import ABC, abstractmethod
from typing import Any, ClassVar, Dict, Protocol


class IsDataclass(Protocol):
    """Type checker for dataclass"""

    __dataclass_fields__: ClassVar[Dict[str, Any]]


class BaseDTOConverter(ABC):
    """DTO Converter interface"""

    @classmethod
    @abstractmethod
    async def encode_dto_to_bytes(cls, dto: IsDataclass) -> bytes:
        """Encode DTO to bytes

        :param dto: The DTO to convert.
        :type dto: IsDataclass

        :return: bytes
        :rtype: bytes
        """

    @classmethod
    @abstractmethod
    async def decode_bytes_to_dto(cls, data: bytes) -> IsDataclass:
        """Decode bytes to DTO

        :param data: The bytes to convert to DTO.
        :type data: bytes

        :return: The DTO
        :rtype: IsDataclass
        """
