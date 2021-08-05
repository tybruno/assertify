from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Type,
    Union,
)

import unittest_assertions.control

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyRaises(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.control.AssertRaises = field(
        default=unittest_assertions.control.AssertRaises, init=False
    )

    def __call__(
        self,
        expected_exception: Union[
            Type[BaseException], tuple[Type[BaseException]]
        ],
        **kwargs: Any
    ) -> bool:
        return super().__call__(
            expected_exception=expected_exception, **kwargs
        )


@dataclass
class AssertifyWarns(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.control.AssertWarns = field(
        default=unittest_assertions.control.AssertWarns, init=False
    )

    def __call__(self, expected_warning, **kwargs) -> bool:
        return super().__call__(expected_warning=expected_warning, **kwargs)


@dataclass
class AssertifyLogs(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.control.AssertLogs = field(
        default=unittest_assertions.control.AssertLogs, init=False
    )

    def __call__(self, logger=None, level=None) -> bool:
        return super().__call__(logger=logger, level=level)
