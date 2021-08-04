from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from string import Template
from typing import (
    Optional,
    Type,
    Union,
)

from unittest_assertions.base import BuiltinAssertion


class Assertifier(ABC):
    def __init__(
        self,
        raises: Optional[Union[None, Type[Exception], Type[AssertionError]]],
        msg: Optional[Union[None, str, Template]],
    ):
        ...

    @abstractmethod
    def __call__(self, **kwargs) -> bool:
        ...


@dataclass
class BuiltinAssertionAssertify(Assertifier):
    assertion_cls: BuiltinAssertion
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, **kwargs) -> bool:
        assertion_function = self.assertion_cls(msg=self.msg)
        try:
            assertion_function(**kwargs)
            return True
        except AssertionError as error:
            if self.raises:
                error_message = error.args[0]
                raise self.raises(error_message) from None
        return False
