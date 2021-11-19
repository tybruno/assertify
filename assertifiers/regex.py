from dataclasses import (
    dataclass,
    field,
)

import unittest_assertions.regex

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class AssertifyRaisesRegex(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.regex.AssertRaisesRegex = field(
        default=unittest_assertions.regex.AssertRaisesRegex, init=False
    )

    def __call__(
        self, expected_exception, expected_regex, *args, **kwargs
    ) -> bool:
        return super().__call__(
            expected_exception,
            expected_regex,
            *args,
            **kwargs,
        )


@dataclass
class AssertifyWarnsRegex(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.regex.AssertWarnsRegex = field(
        default=unittest_assertions.regex.AssertWarnsRegex, init=False
    )

    def __call__(
        self, expected_warning, expected_regex, *args, **kwargs
    ) -> bool:
        return super().__call__(
            expected_warning,
            expected_regex,
            *args,
            **kwargs,
        )


@dataclass
class AssertifyRegex(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.regex.AssertRegex = field(
        default=unittest_assertions.regex.AssertRegex, init=False
    )

    def __call__(self, text, expected_regex) -> bool:
        return super().__call__(text=text, expected_regex=expected_regex)


@dataclass
class AssertifyNotRegex(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.regex.AssertNotRegex = field(
        default=unittest_assertions.regex.AssertNotRegex, init=False
    )

    def __call__(self, text, unexpected_regex) -> bool:
        return super().__call__(text=text, unexpected_regex=unexpected_regex)
