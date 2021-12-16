""" Control Assertifiers

Objects provided by this module:
    * `AssertifyRaises`: assertify Callable raises expected exception
    * `AssertifyWarns`: assertify Callable raises a warning
"""
import logging
from typing import (
    Type,
    Union,
    Tuple,
    Callable,
    Optional,
    Collection,
    Mapping,
)

import unittest_assertions.control

from assertifiers.base import UnittestAssertionAssertifier


class AssertifyRaises(UnittestAssertionAssertifier):
    """assertify `Callable` raises `expected_exception`

    Fail unless an exception of class expected_exception is raised
    by the callable_ when invoked with specified positional and
    keyword arguments. If a different type of exception is
    raised, it will not be caught, and the test case will be
    deemed to have suffered an error, exactly as for an
    unexpected exception.

    Example:
        >>> def _raise_value_error():
        ...     raise ValueError()
        >>> assertify_raises = AssertifyRaises(raises=None)
        >>> assertify_raises(expected_exception=ValueError,
        ... callable_=_raise_value_error )
        True
    """

    _assertion_class: unittest_assertions.control.AssertRaises = (
        unittest_assertions.control.AssertRaises
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
            expected_exception: The expected exception to be
            raised by `callable_`
            callable_: callable that is expecting to
            raise exception `expected_exception`
            *args: Optional function_args
            **kwargs: Optional function_kwargs

        Returns:
            `True` if `callable_` raises `expected_exception`
        """
        result: bool = super().__call__(
            expected_exception, callable_, *args, **kwargs
        )
        return result


class AssertifyWarns(UnittestAssertionAssertifier):
    """assertify `Callable` raises `Warning`

    Fail unless a warning of class warnClass is triggered
    by the callable_ when invoked with specified positional and
    keyword arguments.  If a different type of warning is
    triggered, it will not be handled: depending on the other
    warning filtering rules in effect, it might be silenced, printed
    out, or raised as an exception.

    Example:
        >>> import warnings
        >>> def _warning(message, warning: Warning):
        ...     warnings.warn(message, warning)
        >>> assertify_warns = AssertifyWarns(raises=None)
        >>> assertify_warns( Warning,_warning, str(), Warning )
        True
    """

    _assertion_class: unittest_assertions.control.AssertWarns = (
        unittest_assertions.control.AssertWarns
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
            callable_: The callable that is expected
            to raise `expected_warning`
            *args: Optional function_args
            **kwargs: Optional function_kwargs

        Returns:
            `True` if `callable_` raises `expected_warning`
        """
        result: bool = super().__call__(
            expected_warning, callable_, *args, **kwargs
        )
        return result


class AssertifyLogs(UnittestAssertionAssertifier):
    """assert `logger` logs at a level equal or higher to `level`

    Fail unless a log message of level *level* or higher is emitted
    on *logger_name* or its children.  If omitted, *level* defaults to
    INFO and *logger* defaults to the root logger.
    """

    _assertion_class: unittest_assertions.control.AssertLogs = (
        unittest_assertions.control.AssertLogs
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
