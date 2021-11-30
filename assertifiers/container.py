from dataclasses import (
    dataclass,
    field,
)
from typing import Any, Container
import unittest_assertions.container

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyIn(BuiltinAssertionAssertify):
    """assertify `member` in `container`

    assertify `member` in `container`

    Example:
        >>> assert_in = AssertifyIn(raises=None)
        >>> assert_in(member=1,container=[5,2,1])
        True
        >>> assert_in(member=1, container=(5,2))
        False
    """

    _assertion_cls: unittest_assertions.container.AssertIn = field(
        default=unittest_assertions.container.AssertIn, init=False
    )

    def __call__(self, member: Any, container: Container) -> bool:
        """assertify `member` in `container`

        Args:
            member: check if in `container`
            container: `container` that is checked to have `member`

        Returns:
            `True` if `member` is in `container`
        """
        result: bool = super().__call__(member=member, container=container)
        return result


@dataclass
class AssertifyNotIn(AssertifyIn):
    """assertify `member` not in `container`

    assertify `member` in `container`

    Example:
        >>> assert_not_in = AssertifyNotIn(raises=None)
        >>> assert_not_in(member=1,container=[5,2,3])
        True
        >>> assert_not_in(member=1,container=(2,1,3))
        False
    """

    _assertion_cls: unittest_assertions.container.AssertNotIn = field(
        default=unittest_assertions.container.AssertNotIn, init=False
    )
