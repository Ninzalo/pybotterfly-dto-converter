from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase, TestCase

from pybotterfly_converter import DTOConverter


@dataclass
class DTO:
    string_data: str
    int_data: int


test_dto = DTO(string_data="test", int_data=1)
other_test_dto = DTO(string_data="test2", int_data=2)


async def first_encoded_dto_func():
    return await DTOConverter.encode_dto_to_bytes(test_dto)


async def second_encoded_dto_func():
    return await DTOConverter.encode_dto_to_bytes(other_test_dto)


class DecoderTest(IsolatedAsyncioTestCase):
    async def test_not_equal_decode(self):
        result = await DTOConverter.decode_bytes_to_dto(await first_encoded_dto_func())
        self.assertNotEqual(other_test_dto, result)

    async def test_type(self):
        result = await DTOConverter.decode_bytes_to_dto(await first_encoded_dto_func())
        self.assertIsInstance(result, type(test_dto))

    async def test_different_dto_equality(self):
        first_decoded_dto = await DTOConverter.decode_bytes_to_dto(
            await first_encoded_dto_func()
        )
        second_decoded_dto = await DTOConverter.decode_bytes_to_dto(
            await second_encoded_dto_func()
        )
        self.assertNotEqual(first_decoded_dto, second_decoded_dto)

    async def test_success(self):
        first_decoded_dto = await DTOConverter.decode_bytes_to_dto(
            await first_encoded_dto_func()
        )
        self.assertEqual(first_decoded_dto, test_dto)

        second_decoded_dto = await DTOConverter.decode_bytes_to_dto(
            await second_encoded_dto_func()
        )
        self.assertEqual(second_decoded_dto, other_test_dto)

    async def test_value_error_failure(self):
        test_cases = [
            1,
            "",
            "a",
            {},
            {"a": 1},
            {"a": "a"},
            [],
            [1, 2],
        ]
        with self.assertRaises(ValueError):
            for case in test_cases:
                await DTOConverter.decode_bytes_to_dto(case)
