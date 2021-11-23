from dataclasses import (
    dataclass,
    field,
)

import unittest_assertions.container

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyIn(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.container.AssertIn = field(
        default=unittest_assertions.container.AssertIn, init=False
    )

    def __call__(self, member, container) -> bool:
        return super().__call__(member=member, container=container)


@dataclass
class AssertifyNotIn(AssertifyIn):
    _assertion_cls: unittest_assertions.container.AssertNotIn = field(
        default=unittest_assertions.container.AssertNotIn, init=False
    )
