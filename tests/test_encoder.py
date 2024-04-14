from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase

from pybotterfly_dto_converter import DTOConverter


@dataclass
class DTO:
    string_data: str
    int_data: int


test_dto = DTO(string_data="test", int_data=1)
other_test_dto = DTO(string_data="test2", int_data=2)


class EncoderTest(IsolatedAsyncioTestCase):
    async def test_success(self):
        result = await DTOConverter.encode_dto_to_bytes(test_dto)
        self.assertNotEqual(test_dto, result)

    async def test_type(self):
        result = await DTOConverter.encode_dto_to_bytes(test_dto)
        self.assertIsInstance(result, bytes)

    async def test_different_dto_equality(self):
        first_dto = await DTOConverter.encode_dto_to_bytes(test_dto)
        second_dto = await DTOConverter.encode_dto_to_bytes(other_test_dto)
        self.assertNotEqual(first_dto, second_dto)

    async def test_arg_empty(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes()

    async def test_arg_none(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes(None)

    async def test_arg_int(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes(1)

    async def test_arg_bool(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes(True)

    async def test_arg_str(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes("")

    async def test_arg_list(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes([1, 2])

    async def test_arg_dict(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes({"a", 1})

    async def test_arg_tuple(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode_dto_to_bytes((1, 2))
