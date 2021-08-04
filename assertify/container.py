from dataclasses import dataclass, field
from typing import Optional, Union, Type
from unittest_assertions.base import BuiltinAssertion
from unittest_assertions.container import AssertIn, AssertNotIn
import unittest_assertions
from assertify.base import BuiltinAssertionAssertify


@dataclass
class In(BuiltinAssertionAssertify):
    assertion_cls: BuiltinAssertion = field(default=AssertIn, init=False)

    def __call__(self, *, member, container) -> bool:
        return super().__call__(member=member, container=container)


@dataclass
class AssertifyNotIn(In):
    assertion_cls: BuiltinAssertion = field(default=AssertNotIn, init=False)
