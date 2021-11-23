from dataclasses import (
    dataclass,
    field,
)

import unittest_assertions.logic

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class LogicAssertify(BuiltinAssertionAssertify):
    def __call__(self, expr) -> bool:
        return super().__call__(expr=expr)


@dataclass
class AssertifyTrue(LogicAssertify):
    _assertion_cls: unittest_assertions.logic.AssertTrue = field(
        default=unittest_assertions.logic.AssertTrue, init=False
    )


@dataclass
class AssertifyFalse(LogicAssertify):
    _assertion_cls: unittest_assertions.logic.AssertFalse = field(
        default=unittest_assertions.logic.AssertFalse, init=False
    )
