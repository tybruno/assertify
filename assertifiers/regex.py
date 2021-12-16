""" Regex Assertifiers

Objects provided by this module:
    * `AssertifyRaisesRegex`: assertifies that the message in a raised
     exception matches a regex
    * `AssertifyWarnsRegex`: assertifies that the message in a triggered
    warning matches a regexp.
    * `AssertifyRegex`: Fail the assertifier unless the text
    matches the regular expression
    * `AssertifyNotRegex`: Fail the assertifier if the text
    matches the regular expression
"""
import re
from typing import Type, Union, Tuple, Callable

import unittest_assertions.regex

from assertifiers.base import UnittestAssertionAssertifier


class AssertifyRaisesRegex(UnittestAssertionAssertifier):
    """assertify that the message in a raised exception matches a regex

    Example:
        >>> assertify_raises_regex = AssertifyRaisesRegex(raises=None)
        >>> assertify_raises_regex(ValueError, "invalid literal for.*XYZ'$",
        ... int, 'XYZ')
        True
    """

    _assertion_class: unittest_assertions.regex.AssertRaisesRegex = (
        unittest_assertions.regex.AssertRaisesRegex
    )

    def __call__(
        self,
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        expected_regex: Union[re.Pattern, str],
        function: Callable,
        *function_args,
        **function_kwargs
    ) -> bool:
        """assertify function raises regex

        Args:
            expected_exception: expected exception to be raised
            expected_regex: expected regex during
            `expected_exception` is raised
            function: function to be called
            *arg: extra positional function_args for the called function
            **function_kwargs: Extra function_kwargs for the called function.

        Returns:
            `True` if the message in a raised exception matches a regex

        """
        result: bool = super().__call__(
            expected_exception,
            expected_regex,
            function,
            *function_args,
            **function_kwargs,
        )
        return result


class AssertifyWarnsRegex(UnittestAssertionAssertifier):
    """assertify that the message in a triggered warning matches a regexp.

    Example:
        >>> import warnings
        >>>
        >>> def legacy_function(msg):
        ...     warnings.warn(msg,DeprecationWarning)
        >>> assertify_warns_regex = AssertifyWarnsRegex(raises=None)
        >>> assertify_warns_regex(DeprecationWarning, r'deprecated',
        ... legacy_function,r'legacy_function is deprecated')
        True
    """

    _assertion_class: unittest_assertions.regex.AssertWarnsRegex = (
        unittest_assertions.regex.AssertWarnsRegex
    )

    def __call__(
        self,
        expected_warning: Type[Warning],
        expected_regex: Union[re.Pattern, str],
        function: Callable,
        *function_args,
        **function_kwargs
    ) -> bool:
        """Assertifies that the message in a triggered
        warning matches a regexp.

        Args:
            expected_warning: `Warning~ class expected to be raised
            expected_regex: Regex expected to be found in error message
            function: function that will be called
            *function_args: extra positional function_args for called function
            **function_kwargs: Extra function_kwargs for called function

        Returns:
            `True` when the regex of the message in the triggered `Warning`
        """
        result: bool = super().__call__(
            expected_warning,
            expected_regex,
            function,
            *function_args,
            **function_kwargs,
        )
        return result


class AssertifyRegex(UnittestAssertionAssertifier):
    """assertify `text` matches `expected_regex`

    Example:
        >>> text = "Ala ma kota"
        >>> assertify_regex = AssertifyRegex(raises=None)
        >>> assertify_regex(text, r"k.t")
        True
        >>> assertify_regex(text, r"wrong")
        False
    """

    _assertion_class: unittest_assertions.regex.AssertRegex = (
        unittest_assertions.regex.AssertRegex
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


class AssertifyNotRegex(UnittestAssertionAssertifier):
    """assertify `text` does not match `unexpected_regex`

    Example:
        >>> text = "Ala ma kota"
        >>> assertify_regex = AssertifyNotRegex(raises=None)
        >>> assertify_regex("Ala ma kota", r"wrong")
        True
        >>> assertify_regex(text, r"k.t")
        False
    """

    _assertion_class: unittest_assertions.regex.AssertNotRegex = (
        unittest_assertions.regex.AssertNotRegex
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
