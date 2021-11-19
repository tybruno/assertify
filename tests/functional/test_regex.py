""" Testing unittest_assertifier_clss/regex.py """

import warnings

import pytest

from tests.base import AssertifierTester
from assertifiers.regex import (
    AssertifyRegex,
    AssertifyWarnsRegex,
    AssertifyNotRegex,
    AssertifyRaisesRegex,
)


def _raise(e):
    raise e


def _legacy_function(msg, warning):
    warnings.warn(msg, warning)


class TestAssertifyRaisesRegex(AssertifierTester):
    _assertifier_cls = AssertifyRaisesRegex

    @pytest.mark.parametrize(
        "testing_data",
        ((ValueError, "invalid literal for.*XYZ'$", int, "XYZ"),),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((ValueError, "invalid literal for.*XYZ'$", int, ""),),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertWarnsRegex(AssertifierTester):
    _assertifier_cls = AssertifyWarnsRegex

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                DeprecationWarning,
                r"deprecated",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                DeprecationWarning,
            ),
        ),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                DeprecationWarning,
                r"deprecated",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                BytesWarning,
            ),
            (
                DeprecationWarning,
                r"wrong",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                DeprecationWarning,
            ),
        ),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertRegex(AssertifierTester):
    _assertifier_cls = AssertifyRegex

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"k.t"),),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"r+"),),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertNotRegex(AssertifierTester):
    _assertifier_cls = AssertifyNotRegex

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"r+"),),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"k.t"),),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)
