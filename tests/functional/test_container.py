""" Testing unittest_assertifier_clss/container.py """

import pytest
from pytest_builtin_types import _ALL_BASIC_TYPES_1, _ALL_BASIC_TYPES_2

from assertifiers.container import AssertifyIn, AssertifyNotIn
from tests.base import AssertifierTester


class TestAssertIn(AssertifierTester):
    _assertifier_cls = AssertifyIn

    @pytest.mark.parametrize(
        "testing_data",
        tuple((key, _ALL_BASIC_TYPES_1) for key in _ALL_BASIC_TYPES_1.keys()),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value, _ALL_BASIC_TYPES_1[tuple])
            for value in _ALL_BASIC_TYPES_2[tuple]
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertNotIn(AssertifierTester):
    _assertifier_cls = AssertifyNotIn

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value, _ALL_BASIC_TYPES_1[tuple])
            for value in _ALL_BASIC_TYPES_2[tuple]
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((key, _ALL_BASIC_TYPES_1) for key in _ALL_BASIC_TYPES_1.keys()),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)
