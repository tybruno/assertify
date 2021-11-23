from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Optional,
    Type,
    Union,
)

from unittest_assertions.base import BuiltinAssertion


class Assertifier(ABC):
    def __init__(
        self,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = None,
    ):
        self.raises = raises

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        ...


@dataclass
class BuiltinAssertionAssertify(Assertifier):
    _assertion_cls: Type[BuiltinAssertion]
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)

    def __call__(self, *args, **kwargs) -> bool:
        assertion_function = self._assertion_cls()
        try:
            assertion_function(*args, **kwargs)
            return True
        except AssertionError as error:
            if self.raises:
                error_message = error.args[0]
                raise self.raises(error_message) from None
        return False
