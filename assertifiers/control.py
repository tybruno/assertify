from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Type,
    Union,
    Tuple,
)

import unittest_assertions.control

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyRaises(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.control.AssertRaises = field(
        default=unittest_assertions.control.AssertRaises, init=False
    )

    def __call__(
        self,
        *args: Any,
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        **kwargs: Any,
    ) -> bool:
        return super().__call__(expected_exception, *args, **kwargs)


@dataclass
class AssertifyWarns(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.control.AssertWarns = field(
        default=unittest_assertions.control.AssertWarns, init=False
    )

    def __call__(self, *args: Any, expected_warning, **kwargs) -> bool:
        return super().__call__(expected_warning, *args, **kwargs)


@dataclass
class AssertifyLogs(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.control.AssertLogs = field(
        default=unittest_assertions.control.AssertLogs, init=False
    )

    def __call__(self, logger=None, level=None) -> bool:
        return super().__call__(logger=logger, level=level)
