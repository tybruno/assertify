from dataclasses import dataclass, field
from typing import Optional, Union, Type
from unittest_assertions.logic import AssertTrue, AssertFalse, BuiltinAssertion
import unittest_assertions
from assertify.base import BuiltinAssertionAssertify


@dataclass
class LogicAssertify(BuiltinAssertionAssertify):
    def __call__(self, expr) -> bool:
        return super().__call__(expr=expr)


@dataclass
class AssertifyTrue(LogicAssertify):
    assertion_cls: BuiltinAssertion = field(default=AssertTrue, init=False)


@dataclass
class AssertifyFalse(LogicAssertify):
    assertion_cls: BuiltinAssertion = field(default=AssertFalse, init=False)
