from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Type,
    Union,
    Tuple,
    Callable,
    Optional,
    Collection,
    Mapping,
)
import logging
import unittest_assertions.control

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyRaises(BuiltinAssertionAssertify):
    """assertify `Callable` raises `expected_exception`

    assertify `Callable` raises `Exception`

    For more documentation read unittest.TestCase.assertRaises.__doc__

    Example:
        >>> def _raise_value_error():
        ...     raise ValueError()
        >>> assert_raises = AssertifyRaises(raises=None)
        >>> assert_raises(expected_exception=ValueError,callable_=_raise_value_error )
        True
    """

    _assertion_cls: unittest_assertions.control.AssertRaises = field(
        default=unittest_assertions.control.AssertRaises, init=False
    )

    def __call__(
        self,
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        callable_: Callable,
        *args: Optional[Collection],
        **kwargs: Optional[Mapping],
    ) -> bool:
        """assertify `callable_` raises `expected_exception`

        Args:
            expected_exception: The expected exception to be raised by `callable_`
            callable_: callable that is expecting to raise exception `expected_exception`
            *args: Optional args
            **kwargs: Optional kwargs

        Returns:
            `True` if `callable_` raises `expected_exception`
        """
        result: bool = super().__call__(
            expected_exception, callable_, *args, **kwargs
        )
        return result


@dataclass
class AssertifyWarns(BuiltinAssertionAssertify):
    """assertify `Callable` raises `Warning`

    assertify `Callable` raises `Warning`

    Example:
        >>> import warnings
        >>> def _warning(message, warning: Warning):
        ...     warnings.warn(message, warning)
        >>> assert_warns = AssertifyWarns(raises=None)
        >>> assert_warns( Warning,_warning, str(), Warning )
        True
    """

    _assertion_cls: unittest_assertions.control.AssertWarns = field(
        default=unittest_assertions.control.AssertWarns, init=False
    )

    def __call__(
        self,
        expected_warning: Type[Warning],
        callable_: Callable,
        *args: Optional,
        **kwargs: Optional,
    ) -> bool:
        """assertify `Callable` raises `Warning`
        Args:
            expected_warning: The expected warning to be raised by `callable_`
            callable_: The callable that is expected to raise `expected_warning`
            *args: Optional args
            **kwargs: Optional kwargs

        Returns:
            `True` if `callable_` raises `expected_warning`
        """
        result: bool = super().__call__(
            expected_warning, callable_, *args, **kwargs
        )
        return result


@dataclass
class AssertifyLogs(BuiltinAssertionAssertify):
    """assert `logger` logs at a level equal or higher to `level`

    assertify `logger` logs at `level`
    """

    _assertion_cls: unittest_assertions.control.AssertLogs = field(
        default=unittest_assertions.control.AssertLogs, init=False
    )

    def __call__(
        self, logger: logging.Logger = None, level: int = None
    ) -> bool:
        """assertify `logger` logs at `level`

        Args:
            logger: check it if logger logs at `level`
            level: that `logger` should log at

        Returns:
            `True` if `logger` logs at `level
        """
        return super().__call__(logger=logger, level=level)
