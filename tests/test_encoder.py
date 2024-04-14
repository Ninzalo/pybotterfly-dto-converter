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
        result = await DTOConverter.encode(test_dto)
        self.assertNotEqual(test_dto, result)

    async def test_type(self):
        result = await DTOConverter.encode(test_dto)
        self.assertIsInstance(result, bytes)

    async def test_different_dto_equality(self):
        first_dto = await DTOConverter.encode(test_dto)
        second_dto = await DTOConverter.encode(other_test_dto)
        self.assertNotEqual(first_dto, second_dto)

    async def test_arg_empty(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode()

    async def test_arg_none(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode(None)

    async def test_arg_int(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode(1)

    async def test_arg_bool(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode(True)

    async def test_arg_str(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode("")

    async def test_arg_list(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode([1, 2])

    async def test_arg_dict(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode({"a", 1})

    async def test_arg_tuple(self):
        with self.assertRaises(TypeError):
            await DTOConverter.encode((1, 2))
