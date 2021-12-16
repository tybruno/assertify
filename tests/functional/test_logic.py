""" Testing unittest_assertion_classs/logic.py """

import pytest
from pytest_builtin_types import _ALL_BASIC_TYPES_1

from assertifiers.identity import AssertifyTrue, AssertifyFalse
from tests.base import UnittestAssertionAssertifierTester


class TestAssertifyTrue(UnittestAssertionAssertifierTester):
    _assertion_class = AssertifyTrue

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(testing_data)

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(testing_data)


class TestAssertifyFalse(UnittestAssertionAssertifierTester):
    _assertion_class = AssertifyFalse

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(testing_data)
