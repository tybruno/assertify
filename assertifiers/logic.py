from dataclasses import (
    dataclass,
    field,
)
from typing import Any

import unittest_assertions.logic

from assertifiers.base import BuiltinAssertionAssertifier


@dataclass
class LogicAssertifier(BuiltinAssertionAssertifier):
    """Logic Assertify base class"""

    def __call__(self, expr: Any) -> bool:
        """assertify `expr`

        Args:
            expr: Expression that will be logically evaluated

        Returns:
            `True` if `expr` is logically True
        """
        result: bool = super().__call__(expr=expr)
        return result


@dataclass
class AssertifyTrue(LogicAssertifier):
    """assertify `expr` is `True`

    Example:
        >>> assert_true = AssertifyTrue(raises=None)
        >>> assert_true(True)
        True
        >>> assert_true(1)
        True
        >>> assert_true(0)
        False
        >>> assert_true(False)
        False
    """

    _assertion_cls: unittest_assertions.logic.AssertTrue = field(
        default=unittest_assertions.logic.AssertTrue, init=False
    )


@dataclass
class AssertifyFalse(LogicAssertifier):
    """assert `expr` is False

    Example:
        >>> assert_false = AssertifyFalse(raises=None)
        >>> assert_false(False)
        True
        >>> assert_false(0)
        True
        >>> assert_false(1)
        False
        >>> assert_false(True)
        False
    """

    _assertion_cls: unittest_assertions.logic.AssertFalse = field(
        default=unittest_assertions.logic.AssertFalse, init=False
    )
