""" Testing unittest_assertifier_clss/logic.py """

import pytest
from pytest_builtin_types import _ALL_BASIC_TYPES_1
from tests.base import AssertifierTester

from assertifiers.logic import AssertifyTrue, AssertifyFalse


class TestAssertifyTrue(AssertifierTester):
    _assertifier_cls = AssertifyTrue

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(testing_data)

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(testing_data)


class TestAssertifyFalse(AssertifierTester):
    _assertifier_cls = AssertifyFalse

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(testing_data)
