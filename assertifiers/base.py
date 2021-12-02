""" Base classes for other assertifiers

Objects provided by this module:
    * `Assertifier`: Abstract Base Class for all assertify classes.
    * `UnittestAssertionAssertifier`: Base Class for classes that has-a (with Composition) `unittest_assertions`
"""
from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Optional,
    Type,
    Union,
)

from unittest_assertions.base import BuiltinAssertion


class Assertifier(ABC):
    """abstract base class for all assertifiers"""

    def __init__(
        self,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = None,
    ):
        """Initialize Assertifier

        Args:
            raises: If assertification fails raise the provided exception or assertion.
            If None, return a boolean.
        """
        self.raises = raises

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        """Run the assertification

        Args:
            *args: args for the assertification
            **kwargs: kwargs for the assertification

        Returns:
            `True` if assertification passes and `False` if it fails
        """
        ...


@dataclass
class UnittestAssertionAssertifier(Assertifier):
    """Base class for unittest_assertions"""

    _assertion_cls: Type[BuiltinAssertion]
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)

    def __call__(self, *args, **kwargs) -> bool:
        """Run assertify

        Args:
            *args: args for the assertification
            **kwargs: kwargs for the assertification

        Returns:
            `True` if the assertification passes. If `self.raises` is set to `None`
            it will raise `False` when assertification fails.

        Raises:
            If assertification fails will raise the `Exception` or `AssertionError`
            defined in `self.raises`. If `self.raises` is `None` it will return
            a `False` when it fails.
        """
        assertion_function = self._assertion_cls()
        try:
            assertion_function(*args, **kwargs)
            return True
        except AssertionError as error:
            if self.raises:
                error_message = error.args[0]
                raise self.raises(error_message) from None
        return False
