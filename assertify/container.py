from dataclasses import dataclass, field
from typing import Optional, Union, Type
import unittest_assertions.container
from assertify.base import BuiltinAssertionAssertify


@dataclass
class AssertifyIn(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.container.AssertIn = field(
        default=unittest_assertions.container.AssertIn, init=False
    )

    def __call__(self, *, member, container) -> bool:
        return super().__call__(member=member, container=container)


@dataclass
class AssertifyNotIn(AssertifyIn):
    assertion_cls: unittest_assertions.container.AssertNotIn = field(
        default=unittest_assertions.container.AssertNotIn, init=False
    )
