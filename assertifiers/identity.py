from dataclasses import (
    dataclass,
    field,
)
from typing import Collection, Any
from typing import (
    Optional,
    Type,
    Union,
)

import unittest_assertions.identity

from assertifiers.base import (
    Assertifier,
    BuiltinAssertionAssertify,
)


@dataclass
class AssertifyIs(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.identity.AssertIs = field(
        default=unittest_assertions.identity.AssertIs, init=False
    )

    def __call__(self, exp1, exp2) -> bool:
        return super().__call__(expr1=exp1, expr2=exp2)


@dataclass
class AssertifyIsNot(AssertifyIs):
    _assertion_cls: unittest_assertions.identity.AssertIsNot = field(
        default=unittest_assertions.identity.AssertIsNot, init=False
    )


@dataclass
class AssertifyIsNone(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.identity.AssertIsNone = field(
        default=unittest_assertions.identity.AssertIsNone, init=False
    )

    def __call__(self, obj) -> bool:
        return super().__call__(obj=obj)


@dataclass
class AssertifyIsNotNone(AssertifyIsNone):
    _assertion_cls: unittest_assertions.identity.AssertIsNotNone = field(
        default=unittest_assertions.identity.AssertIsNotNone, init=False
    )


@dataclass
class AssertifyIsInstance(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.identity.AssertIsInstance = field(
        default=unittest_assertions.identity.AssertIsInstance, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)

    def __call__(self, obj, cls) -> bool:
        return super().__call__(obj=obj, cls=cls)


@dataclass
class AssertifyIsInstances(Assertifier):
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)
    must_pass: Union[any, all] = field(default=any)

    def __call__(self, obj: Any, classes: Collection) -> bool:
        if not isinstance(classes, Collection):
            classes: tuple = (classes,)
        assertify_is_instance = AssertifyIsInstance(raises=None)

        results = tuple(
            assertify_is_instance(cls=cls, obj=obj) for cls in classes
        )
        passed = self.must_pass(results)
        if passed:
            return True
        if self.raises:
            raise self.raises(
                f"{obj!r} must be an instance of {self.must_pass} of {classes}"
            )

        return False


@dataclass
class AssertifyNotIsInstance(AssertifyIsInstance):
    _assertion_cls: unittest_assertions.identity.AssertNotIsInstance = field(
        default=unittest_assertions.identity.AssertNotIsInstance, init=False
    )


@dataclass
class AssertifyNotIsInstances(AssertifyIsInstances):
    def __call__(self, obj, classes) -> bool:
        if not isinstance(classes, Collection):
            classes: tuple = (classes,)
        assertify_not_is_instance = AssertifyNotIsInstance(raises=None)
        results = tuple(
            assertify_not_is_instance(cls=cls, obj=obj) for cls in classes
        )
        passed = self.must_pass(results)
        if passed:
            return True
        if self.raises:
            raise self.raises(
                f"{obj!r} must not be an instance of "
                f"{self.must_pass} of {classes}"
            )

        return False
