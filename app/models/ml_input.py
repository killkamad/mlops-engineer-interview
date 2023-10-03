from typing import List
from pydantic import BaseModel, field_validator

from app import TEST_SAMPLE_1


class MLInput(BaseModel):
    """Input list of lists"""
    data: List[list] = [
        TEST_SAMPLE_1,
    ]

    @field_validator("data")
    def validate_data(cls, value):
        for sublist in value:
            if len(sublist) != 10:
                raise ValueError("Each sublist in 'data' must contain exactly 10 elements")
            if not all(isinstance(item, float) for item in sublist):
                raise ValueError("All elements in sublists must be of type 'float'")
        return value


class MLResponse(BaseModel):
    """Response with list"""
    result: list = []
