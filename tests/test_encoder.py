from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase

from pybotterfly_converter import DTOConverter


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

    async def test_type_error_failure(self):
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
        with self.assertRaises(TypeError):
            for case in test_cases:
                await DTOConverter.encode_dto_to_bytes(case)

    async def test_value_error_failure(self):
        with self.assertRaises(ValueError):
            await DTOConverter.encode_dto_to_bytes()
