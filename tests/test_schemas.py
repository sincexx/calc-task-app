import pytest
from pydantic import ValidationError

from app.schemas import CreateTaskRequestModel


@pytest.mark.parametrize("invalid_operator", ["%", "abc", "123", "", "++", "--"])
def test_invalid_operator(invalid_operator):
    with pytest.raises(ValidationError) as exc_info:
        CreateTaskRequestModel(x=5, y=3, operator=invalid_operator)

    assert "Invalid operator" in str(exc_info.value)


@pytest.mark.parametrize("valid_operator", ["+", "-", "*", "/"])
def test_valid_operator(valid_operator):
    try:
        model = CreateTaskRequestModel(x=5, y=3, operator=valid_operator)
        assert model.operator == valid_operator
    except ValidationError as e:
        pytest.fail(f"Validation error occurred: {e}")
