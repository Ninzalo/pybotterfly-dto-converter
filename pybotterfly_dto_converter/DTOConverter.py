from .BaseDTO import BaseDTO
from .BaseDTOConverter import BaseDTOConverter
from .DTODecoder import DTODecoder
from .DTOEncoder import DTOEncoder


class DTOConverter(BaseDTOConverter):
    """Converter for Data Transfer Objects."""

    @classmethod
    def encode(cls, dto: BaseDTO) -> bytes:
        dto_string = DTOEncoder.dataclass_to_str(dto)
        dto_bytes = DTOEncoder.str_to_bytes(dto_string)
        return dto_bytes

    @classmethod
    def decode(cls, dto_bytes: bytes) -> BaseDTO:
        dto_string = DTODecoder.bytes_to_str(dto_bytes)
        dto = DTODecoder.str_to_dataclass(dto_string)
        return dto
