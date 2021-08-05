from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Optional,
    Type,
    Union,
)

import unittest_assertions.identity

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyIs(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.identity.AssertIs = field(
        default=unittest_assertions.identity.AssertIs, init=False
    )

    def __call__(self, exp1, exp2) -> bool:
        return super().__call__(exp1=exp1, exp2=exp2)


@dataclass
class AssertifyIsNot(AssertifyIs):
    assertion_cls: unittest_assertions.identity.AssertIsNot = field(
        default=unittest_assertions.identity.AssertIsNot, init=False
    )


@dataclass
class AssertifyIsNone(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.identity.AssertIsNone = field(
        default=unittest_assertions.identity.AssertIsNone, init=False
    )

    def __call__(self, obj) -> bool:
        return super().__call__(obj=obj)


@dataclass
class AssertifyIsNotNone(AssertifyIsNone):
    assertion_cls: unittest_assertions.identity.AssertIsNotNone = field(
        default=unittest_assertions.identity.AssertIsNotNone, init=False
    )


@dataclass
class AssertifyIsInstance(BuiltinAssertionAssertify):
    assertion_cls: unittest_assertions.identity.AssertIsInstance = field(
        default=unittest_assertions.identity.AssertIsInstance, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)

    def __call__(self, obj, cls) -> bool:
        return super().__call__(obj=obj, cls=cls)


@dataclass
class AssertifyNotIsInstance(AssertifyIsInstance):
    assertion_cls: unittest_assertions.identity.AssertNotIsInstance = field(
        default=unittest_assertions.identity.AssertNotIsInstance, init=False
    )
