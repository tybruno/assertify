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
    """assertify `expr1` is `expr2`

    Example:
        >>> value = "string"
        >>> assert_is = AssertifyIs(raises=None)
        >>> assert_is(value,value)
        True
        >>> assert_is(2,value)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertIs = field(
        default=unittest_assertions.identity.AssertIs, init=False
    )

    def __call__(self, expr1: Any, expr2: Any) -> bool:
        """assertify `expr1` is `expr2`

        Args:
            expr1: check if is `expr2`
            expr2: check if is `expr1

        Returns:
            `True` if `expr1` is `expr2`
        """
        result: bool = super().__call__(expr1=expr1, expr2=expr2)
        return result


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
