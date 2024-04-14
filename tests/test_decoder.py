from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase

from pybotterfly_dto_converter import DTOConverter


@dataclass
class DTO:
    string_data: str
    int_data: int


test_dto = DTO(string_data="test", int_data=1)
other_test_dto = DTO(string_data="test2", int_data=2)


async def first_encoded_dto_func():
    return await DTOConverter.encode(test_dto)


async def second_encoded_dto_func():
    return await DTOConverter.encode(other_test_dto)


class DecoderTest(IsolatedAsyncioTestCase):
    async def test_not_equal_decode(self):
        result = await DTOConverter.decode(await first_encoded_dto_func())
        self.assertNotEqual(other_test_dto, result)

    async def test_type(self):
        result = await DTOConverter.decode(await first_encoded_dto_func())
        self.assertIsInstance(result, type(test_dto))

    async def test_different_dto_equality(self):
        first_decoded_dto = await DTOConverter.decode(await first_encoded_dto_func())
        second_decoded_dto = await DTOConverter.decode(await second_encoded_dto_func())
        self.assertNotEqual(first_decoded_dto, second_decoded_dto)

    async def test_success(self):
        first_decoded_dto = await DTOConverter.decode(await first_encoded_dto_func())
        self.assertEqual(first_decoded_dto, test_dto)

        second_decoded_dto = await DTOConverter.decode(await second_encoded_dto_func())
        self.assertEqual(second_decoded_dto, other_test_dto)

    async def test_arg_empty(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode()

    async def test_arg_none(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode(None)

    async def test_arg_int(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode(1)

    async def test_arg_bool(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode(True)

    async def test_arg_str(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode("")

    async def test_arg_list(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode([1, 2])

    async def test_arg_dict(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode({"a", 1})

    async def test_arg_tuple(self):
        with self.assertRaises(TypeError):
            await DTOConverter.decode((1, 2))
