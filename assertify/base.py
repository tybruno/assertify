from dataclasses import dataclass, field
from typing import Optional, Union, Type
from unittest_assertions.base import BuiltinAssertion
from string import Template


@dataclass
class BuiltinAssertionAssertify:
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
