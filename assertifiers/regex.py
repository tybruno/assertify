import re
from dataclasses import (
    dataclass,
    field,
)
from typing import Type, Union, Tuple

import unittest_assertions.regex

from assertifiers.base import UnittestAssertionAssertifier


@dataclass
class AssertifierRaisesRegex(UnittestAssertionAssertifier):
    """assertify that the message in a raised exception matches a regex

    Example:
        >>> assertify_raises_regex = AssertifierRaisesRegex(raises=None)
        >>> assertify_raises_regex(ValueError, "invalid literal for.*XYZ'$",
        ... int, 'XYZ')
        True
    """

    _assertion_cls: unittest_assertions.regex.AssertRaisesRegex = field(
        default=unittest_assertions.regex.AssertRaisesRegex, init=False
    )

    def __call__(
        self,
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        expected_regex: Union[re.Pattern, str],
        *args,
        **kwargs
    ) -> bool:
        """assertify

        Args:
            expected_exception: expected exception to be raised
            expected_regex: expected regex during `expected_exception` is raised
            *arg: Function to be called and extra positional args
            **kwargs: Extra kwargs.

        Returns:
            `True` if the message in a raised exception matches a regex

        """
        result: bool = super().__call__(
            expected_exception,
            expected_regex,
            *args,
            **kwargs,
        )
        return result


@dataclass
class AssertifierWarnsRegex(UnittestAssertionAssertifier):
    """assertify that the message in a triggered warning matches a regexp.

    Example:
        >>> import warnings
        >>>
        >>> def legacy_function(msg):
        ...     warnings.warn(msg,DeprecationWarning)
        >>> assertify_warns_regex = AssertifierWarnsRegex(raises=None)
        >>> assertify_warns_regex(DeprecationWarning, r'deprecated',
        ... legacy_function,r'legacy_function is deprecated')
        True
    """

    _assertion_cls: unittest_assertions.regex.AssertWarnsRegex = field(
        default=unittest_assertions.regex.AssertWarnsRegex, init=False
    )

    def __call__(
        self,
        expected_warning: Type[Warning],
        expected_regex: Union[re.Pattern, str],
        *args,
        **kwargs
    ) -> bool:
        """

        Args:
            expected_warning: `Warning~ class expected to be raised
            expected_regex: Regex expected to be found in error message
            *args: Function to be called and extra postional args
            **kwargs: Extra kwargs

        Returns:
            `True` when the regex of the message in the triggered `Warning`
        """
        result: bool = super().__call__(
            expected_warning,
            expected_regex,
            *args,
            **kwargs,
        )
        return result


@dataclass
class AssertifierRegex(UnittestAssertionAssertifier):
    """assertify `text` matches `expected_regex`

    Example:
        >>> text = "Ala ma kota"
        >>> assertify_regex = AssertifierRegex(raises=None)
        >>> assertify_regex(text, r"k.t")
        True
        >>> assertify_regex(text, r"wrong")
        False
    """

    _assertion_cls: unittest_assertions.regex.AssertRegex = field(
        default=unittest_assertions.regex.AssertRegex, init=False
    )

    def __call__(
        self, text: str, expected_regex: Union[re.Pattern, str]
    ) -> bool:
        """assertify `text` matches `expected_regex`

        Args:
            text: checked to see if will match `expected_regex`
            expected_regex: checked to see if it matched `text`

        Returns:
            `True` if `text` matches `expected_regex`
        """
        result: bool = super().__call__(
            text=text, expected_regex=expected_regex
        )
        return result


@dataclass
class AssertifierNotRegex(UnittestAssertionAssertifier):
    """assertify `text` does not match `unexpected_regex`

    Example:
        >>> text = "Ala ma kota"
        >>> assertify_regex = AssertifierNotRegex(raises=None)
        >>> assertify_regex("Ala ma kota", r"wrong")
        True
        >>> assertify_regex(text, r"k.t")
        False
    """

    _assertion_cls: unittest_assertions.regex.AssertNotRegex = field(
        default=unittest_assertions.regex.AssertNotRegex, init=False
    )

    def __call__(
        self, text: str, unexpected_regex: Union[re.Pattern, str]
    ) -> bool:
        """assertify `text` does not match `unexpected_regex`

        Args:
            text: checked to see that it does not match `unexpected_regex`
            unexpected_regex: checked to see that it does not match `text`

        Returns:
            `True` if `text` does not match `unexpected_regex`
        """
        result: bool = super().__call__(
            text=text, unexpected_regex=unexpected_regex
        )
        return result
