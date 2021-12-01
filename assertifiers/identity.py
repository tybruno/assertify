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
    BuiltinAssertionAssertifier,
)


@dataclass
class AssertifierIs(BuiltinAssertionAssertifier):
    """assertify `expr1` is `expr2`

    Example:
        >>> value = "string"
        >>> assertify_is = AssertifierIs(raises=None)
        >>> assertify_is(value,value)
        True
        >>> assertify_is(2,value)
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
class AssertifyIsNot(AssertifierIs):
    """assertify `expr1` is not `expr2`

    Example:
        >>> value1 = "string1"
        >>> value2 = "string2"
        >>> assertify_is_not = AssertifyIsNot(raises=None)
        >>> assertify_is_not(value1,value2)
        True
        >>> assertify_is_not(value1,value1)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertIsNot = field(
        default=unittest_assertions.identity.AssertIsNot, init=False
    )


@dataclass
class AssertifierIsNone(BuiltinAssertionAssertifier):
    """assertify `obj` is `None`

    Example:
        >>> assertify_is_none = AssertifierIsNone(raises=None)
        >>> assertify_is_none(None)
        True
        >>> assertify_is_none(True)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertIsNone = field(
        default=unittest_assertions.identity.AssertIsNone, init=False
    )

    def __call__(self, obj: Any) -> bool:
        """assertify `obj` is `None`

        Args:
            obj: Object that will be checked if it is `None`

        Returns:
            `True` if `obj` is `None`
        """
        result: bool = super().__call__(obj=obj)
        return result


@dataclass
class AssertifyIsNotNone(AssertifierIsNone):
    """assertify `obj` is not `None`

    Example:
        >>> assertify_is_not_none = AssertifyIsNotNone(raises=None)
        >>> assertify_is_not_none("")
        True
        >>> assertify_is_not_none(None)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertIsNotNone = field(
        default=unittest_assertions.identity.AssertIsNotNone, init=False
    )


@dataclass
class AssertifierIsInstance(BuiltinAssertionAssertifier):
    """assertify `obj` is an instance of `cls`

    assertify isinstance(obj,cls)

    Example:
        >>> assertify_is_instance = AssertifierIsInstance(raises=None)
        >>> assertify_is_instance(2,int)
        True
        >>> assertify_is_instance(2,float)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertIsInstance = field(
        default=unittest_assertions.identity.AssertIsInstance, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)

    def __call__(self, obj: Any, cls: Type) -> bool:
        """assertify `isinstance(obj,cls)`

        Args:
            obj: check if `isinstance` of `cls`
            cls: check if `obj` is instance of `cls`

        Returns:
            `True` if `obj` is instance of `cls`
        """
        result: bool = super().__call__(obj=obj, cls=cls)
        return result


@dataclass
class AssertifyIsInstances(Assertifier):
    """assertify `obj` is an instance of `any` or `all` of `classes`

    Example:
        >>> assertify_is_instances = AssertifyIsInstances(raises=None, must_be_instance_of=any)
        >>> assertify_is_instances(1,classes=(int,float))
        True
        >>> assertify_is_instances(1,classes=(str,list))
        False
        >>> assertify_is_instances.must_be_instance_of = all
        >>> assertify_is_instances(True,classes=(int,bool))
        True
        >>> assertify_is_instances(1,classes=(int,bool))
        False
    """

    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)
    must_be_instance_of: Union[any, all] = field(default=any)

    def __call__(self, obj: Any, classes: Collection[Type]) -> bool:
        """assertify `obj` is an instance of `any` or `all` of `classes`

        Args:
            obj: check if is an instance of `any` or `all` of `classes`
            classes: check if `obj` is an instance of `any` or `all` of classes

        Returns:
            `True` if `obj` is an instance of `any` or `all` of `classes`
        """
        if not isinstance(classes, Collection):
            classes: tuple = (classes,)
        assertify_is_instance = AssertifierIsInstance(raises=None)

        results = tuple(
            assertify_is_instance(cls=cls, obj=obj) for cls in classes
        )
        passed = self.must_be_instance_of(results)
        if passed:
            return True
        if self.raises:
            raise self.raises(
                f"{obj!r} must be an instance of {self.must_be_instance_of} of {classes}"
            )

        return False


@dataclass
class AssertifyNotIsInstance(AssertifierIsInstance):
    """assertify not isinstance(obj,cls)

    assertify not isinstance(obj,cls)

    Example:
        >>> assertify_is_instance = AssertifyNotIsInstance(raises=None)
        >>> assertify_is_instance(2.5,int)
        True
        >>> assertify_is_instance(2,int)
        False
    """

    _assertion_cls: unittest_assertions.identity.AssertNotIsInstance = field(
        default=unittest_assertions.identity.AssertNotIsInstance, init=False
    )


@dataclass
class AssertifyNotIsInstances(AssertifyIsInstances):
    """assertify `obj` is not an instance of `any` or `all` of `classes`

    >>> assertify_not_instances = AssertifyNotIsInstances(raises=None)
    >>> assertify_not_instances(1,classes=(int,float))
    True
    >>> assertify_not_instances(1,classes=(str,list))
    True
    >>> assertify_not_instances.must_be_instance_of = all
    >>> assertify_not_instances(True,classes=(int,bool))
    False
    >>> assertify_not_instances(1,classes=(int,bool))
    False

    """

    def __call__(self, obj: Any, classes: Collection[Type]) -> bool:
        """assertify `obj` is not an instance of `any` or `all` of `classes`

        Args:
            obj: check if is not an instance of `any` or `all` of `classes`
            classes: check if `obj` is not an instance of `any` or `all` of classes

        Returns:
            `True` if `obj` is not a an instance of `any` or `all` of `classes`

        """
        if not isinstance(classes, Collection):
            classes: tuple = (classes,)
        assertify_not_is_instance = AssertifyNotIsInstance(raises=None)
        results = tuple(
            assertify_not_is_instance(cls=cls, obj=obj) for cls in classes
        )
        passed = self.must_be_instance_of(results)
        if passed:
            return True
        if self.raises:
            raise self.raises(
                f"{obj!r} must not be an instance of "
                f"{self.must_be_instance_of} of {classes}"
            )

        return False
