from typing import Any, ClassVar, Dict, Protocol


class BaseDTO(Protocol):
    """Type checker for dataclass."""

    __dataclass_fields__: ClassVar[Dict[str, Any]]
