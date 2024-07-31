from dataclasses import dataclass
from unittest import TestCase

from pybotterfly_dto_converter import DTOConverter


@dataclass
class DTO:
    string_data: str
    int_data: int


first_test_dto = DTO(string_data="test", int_data=1)
second_test_dto = DTO(string_data="test2", int_data=2)


class EncoderTest(TestCase):
    def test_success(self) -> None:
        first_encoded_dto = DTOConverter.encode(first_test_dto)
        self.assertNotEqual(first_test_dto, first_encoded_dto)

    def test_type(self) -> None:
        first_encoded_dto = DTOConverter.encode(first_test_dto)
        self.assertIsInstance(first_encoded_dto, bytes)

    def test_different_dto_equality(self) -> None:
        first_encoded_dto = DTOConverter.encode(first_test_dto)
        second_encoded_dto = DTOConverter.encode(second_test_dto)
        self.assertNotEqual(first_encoded_dto, second_encoded_dto)

    def test_arg_empty(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode()

    def test_arg_none(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode(None)

    def test_arg_int(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode(1)

    def test_arg_bool(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode(dto=True)

    def test_arg_str(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode("")

    def test_arg_list(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode([1, 2])

    def test_arg_dict(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode({"a", 1})

    def test_arg_tuple(self) -> None:
        with self.assertRaises(TypeError):
            DTOConverter.encode((1, 2))
