""" Base classes for other assertifiers

Objects provided by this module:
    * `Assertifier`: Abstract Base Class for all assertify classes.
    * `UnittestAssertionAssertifier`: Base Class for classes that has-a
    (with Composition) `unittest_assertions`
"""
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Optional,
    Type,
    Union,
)

from unittest_assertions.base import Assertion


class Assertifier(ABC):
    """abstract base class for all assertifiers

    Attributes:
        self.raises: `Exception` or `AssertionError` that will be
            raised if the assertifier (`__call__`) fails. If `None` `True`
            will be returned if assertifier (`__call__`) passes and `False`
            if it fails.
    """

    def __init__(
        self,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = None,
    ):
        """Initialize Assertifier

        Args:
            raises: If assertification fails raise the
            provided exception or assertion.
            If None, return a boolean.
        """
        self.raises = raises

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        """Run the assertification

        Args:
            *args: function_args for the assertification
            **kwargs: function_kwargs for the assertification

        Returns:
            `True` if assertification passes.`False` if `self.raises = None`
            and assertification fails.
        Raises:
            `Exception` or `AssertifyError` defined by `self.raises` when
            assertification fails.
        """
        ...


class UnittestAssertionAssertifier(Assertifier):
    """Base class for unittest_assertions

    Attributes:
        self._assertion_cls: builtin unittest assertion
            class that will run the assertion.
        self.raises: `Exception` or `AssertionError` that will be
            raised if the assertifier (`__call__`) fails. If `None` `True`
            will be returned if assertifier (`__call__`) passes and `False`
            if it fails.
    """

    _assertion_class: Assertion

    def __init__(
        self,
        msg: str = None,
        raises: Optional[
            Union[None, Type[Exception], Type[AssertionError]]
        ] = ValueError,
    ):

        super().__init__(raises=raises)
        self.msg = msg

    @property
    def msg(self):
        return self._assertion_function.msg

    @msg.setter
    def msg(self, msg):
        if hasattr(self, "_assertion_function"):
            self._assertion_function.msg = msg
        else:
            self._assertion_function = self._assertion_class(msg=msg)

    def __repr__(self):
        result = (
            f"{self.__class__.__name__}"
            f"(msg={self.msg!r}, raises={self.raises!r})"
        )
        return result

    def __call__(self, *args, **kwargs) -> bool:
        """Run assertify

        Args:
            *args: function_args for the assertification
            **kwargs: function_kwargs for the assertification

        Returns:
            `True` if the assertification passes.
            If `self.raises` is set to `None`
            it will raise `False` when assertification fails.

        Raises:
            If assertification fails will raise the
            `Exception` or `AssertionError`
            defined in `self.raises`. If `self.raises` is `None` it will return
            a `False` when it fails.
        """
        try:
            self._assertion_function(*args, **kwargs)
            return True
        except AssertionError as error:
            if self.raises:
                error_message = error.args[0]
                raise self.raises(error_message) from None
        return False
