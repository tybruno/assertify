""" Identity Assertifiers

Objects provided by this module:
    * `AssertifyTrue`: assertify `expr is True`
    * `AssertifyFalse`: assertify `expr is False`
    * `AssertifyIs`: assertify `expr1 is expr2`
    * `AssertifyIsNot`: assertify `expr1 is not expr2`
    * `AssertifyIsNone`: assertify `obj is None`
    * `AssertifyIsNotNone`: assertify `obj is not None`
    * `AssertifyIsInstance`: assertify `isinstance(obj, cls)`
    * `AssertifyNotIsInstance`: assertify `not isinstance(obj,cls)`
"""
from typing import Collection, Any
from typing import (
    Optional,
    Type,
    Union,
)

import unittest_assertions.identity

from assertifiers.base import (
    Assertifier,
    UnittestAssertionAssertifier,
)


class AssertifyTrue(UnittestAssertionAssertifier):
    """assertify `expr is True`

    raise `AssertionError` if `expr is False`

    For more documentation read TestCase().assertTrue.__doc__

    Example:
        >>> assertify_true = AssertifyTrue(raises=None)
        >>> assertify_true(True)
        True
        >>> assertify_true(1)
        True
        >>> assertify_true(0)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertTrue = (
        unittest_assertions.identity.AssertTrue
    )

    def __call__(self, expr: Any) -> bool:
        result: bool = super().__call__(expr=expr)
        return result


class AssertifyFalse(UnittestAssertionAssertifier):
    """assertify `expr is False`

    raise `AssertionError` if `expr is True`


    Example:
        >>> assertify_false = AssertifyFalse(raises=None)
        >>> assertify_false(False)
        True
        >>> assertify_false(0)
        True
        >>> assertify_false(1)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertTrue = (
        unittest_assertions.identity.AssertFalse
    )


class AssertifyIs(UnittestAssertionAssertifier):
    """assertify `expr1 is expr2`

    Example:
        >>> value = "string"
        >>> assertify_is = AssertifyIs(raises=None)
        >>> assertify_is(value,value)
        True
        >>> assertify_is(2,value)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertIs = (
        unittest_assertions.identity.AssertIs
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


class AssertifyIsNot(AssertifyIs):
    """assertify `expr1 is not expr2`

    Example:
        >>> value1 = "string1"
        >>> value2 = "string2"
        >>> assertify_is_not = AssertifyIsNot(raises=None)
        >>> assertify_is_not(value1,value2)
        True
        >>> assertify_is_not(value1,value1)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertIsNot = (
        unittest_assertions.identity.AssertIsNot
    )


class AssertifyIsNone(UnittestAssertionAssertifier):
    """assertify `obj` is `None`

    Example:
        >>> assertify_is_none = AssertifyIsNone(raises=None)
        >>> assertify_is_none(None)
        True
        >>> assertify_is_none(True)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertIsNone = (
        unittest_assertions.identity.AssertIsNone
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


class AssertifyIsNotNone(AssertifyIsNone):
    """assertify `obj is not None`

    Example:
        >>> assertify_is_not_none = AssertifyIsNotNone(raises=None)
        >>> assertify_is_not_none("")
        True
        >>> assertify_is_not_none(None)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertIsNotNone = (
        unittest_assertions.identity.AssertIsNotNone
    )


class AssertifyIsInstance(UnittestAssertionAssertifier):
    """assertify `isinstance(obj,cls)`

    assertify isinstance(obj,cls)

    Example:
        >>> assertify_is_instance = AssertifyIsInstance(raises=None)
        >>> assertify_is_instance(2,int)
        True
        >>> assertify_is_instance(2,float)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertIsInstance = (
        unittest_assertions.identity.AssertIsInstance
    )

    def __init__(
        self,
        msg: str = None,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = TypeError,
    ):
        super().__init__(msg=msg, raises=raises)

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


class AssertifyIsInstances(Assertifier):
    """assertify `obj` is an instance of `any` or `all` of `classes`

    Example:
        >>> assertify_is_instances = AssertifyIsInstances(raises=None,
        ... must_be_instance_of=any)
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

    _base_assertifier_function: AssertifyIsInstance = AssertifyIsInstance(
        raises=None
    )

    def __init__(
        self,
        msg: Union[str, None] = None,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = TypeError,
        must_be_instance_of: Union[any, all] = any,
    ):
        super().__init__(raises=raises)
        self.msg = msg
        self.must_be_instance_of = must_be_instance_of

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

        results = tuple(
            self._base_assertifier_function(cls=cls, obj=obj)
            for cls in classes
        )

        passed = self.must_be_instance_of(results)

        if passed:
            return True

        if self.raises:
            raise self.raises(
                (
                    f"{obj!r} must be an instance of "
                    f"{self.must_be_instance_of} of {classes}"
                    f"{ f': {self.msg}' if self.msg else ''}"
                )
            )

        return False


class AssertifyNotIsInstance(AssertifyIsInstance):
    """assertify not isinstance(obj,cls)

    assertify not isinstance(obj,cls)

    Example:
        >>> assertify_is_instance = AssertifyNotIsInstance(raises=None)
        >>> assertify_is_instance(2.5,int)
        True
        >>> assertify_is_instance(2,int)
        False
    """

    _assertion_class: unittest_assertions.identity.AssertNotIsInstance = (
        unittest_assertions.identity.AssertNotIsInstance
    )


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

    _base_assertifier_function: AssertifyNotIsInstance = (
        AssertifyNotIsInstance(raises=None)
    )

    def __call__(self, obj: Any, classes: Collection[Type]) -> bool:
        """assertify `obj` is not an instance of `any` or `all` of `classes`

        Args:
            obj: check if is not an instance of `any` or `all` of `classes`
            classes: check if `obj` is not an instance of
            `any` or `all` of classes

        Returns:
            `True` if `obj` is not a an instance of `any` or `all` of `classes`

        """
        if not isinstance(classes, Collection):
            classes: tuple = (classes,)

        results = tuple(
            self._base_assertifier_function(cls=cls, obj=obj)
            for cls in classes
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
