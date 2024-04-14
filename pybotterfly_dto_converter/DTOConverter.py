from .BaseDTO import BaseDTO
from .BaseDTOConverter import BaseDTOConverter
from .DTODecoder import DTODecoder
from .DTOEncoder import DTOEncoder


class DTOConverter(BaseDTOConverter):
    """Converter for Data Transfer Objects."""

    @classmethod
    def encode(cls, dto: BaseDTO) -> bytes:
        DTOEncoder.validate_input(dto=dto)
        dto_string = DTOEncoder.dataclass_to_str(dto)
        encoded_dto_string = DTOEncoder.encode_dto_string(dto_string)
        dto_bytes = DTOEncoder.str_to_bytes(encoded_dto_string)
        return dto_bytes

    @classmethod
    def decode(cls, dto_bytes: bytes) -> BaseDTO:
        DTODecoder.validate_input(dto_bytes=dto_bytes)
        dto_string = DTODecoder.bytes_to_str(dto_bytes)
        decoded_dto_string = DTODecoder.decode_dto_string(dto_string)
        dto = DTODecoder.str_to_dataclass(decoded_dto_string)
        return dto
