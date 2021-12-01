""" Testing unittest_assertifier_clss/control.py """
import warnings

import pytest

from assertifiers.control import AssertifierWarns, AssertifierRaises
from tests.base import AssertifierTester


def _raise(e):
    raise e


def _warning(message, warning: Warning):
    warnings.warn(message, warning)


class TestAssertRaises(AssertifierTester):
    _assertifier_cls = AssertifierRaises

    @pytest.mark.parametrize(
        "testing_data",
        (
            [KeyError, _raise, KeyError],
            [KeyError, _raise, KeyError("key")],
        ),
    )
    def test_assertify_passes(self, testing_data: list):
        expected_exception = testing_data.pop(0)

        super().test_assertify_passes(expected_exception, *testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            [
                KeyError,
                lambda: None,
            ],
        ),
    )
    def test_assertify_fails(self, testing_data: list):
        expected_exception = testing_data.pop(0)
        super().test_assertify_fails(expected_exception, *testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ([KeyError, _raise, ValueError],),
    )
    def test_assertifier_cls_error(self, testing_data: list):
        assert_raises = self._assertifier_cls()

        with pytest.raises(testing_data[2]):
            expected_exception = testing_data.pop(0)
            assert_raises(expected_exception, *testing_data)


class TestAssertWarns(AssertifierTester):
    _assertifier_cls = AssertifierWarns

    @pytest.mark.parametrize(
        "testing_data",
        (
            [Warning, _warning, "message", Warning],
            [Warning, _warning, "message", UserWarning],
        ),
    )
    def test_assertify_passes(self, testing_data: list):
        expected_warning = testing_data.pop(0)
        super().test_assertify_passes(expected_warning, *testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            [UserWarning, _warning, "message", SyntaxWarning],
            [UserWarning, _warning, "message", Warning],
        ),
    )
    def test_assertify_fails(self, testing_data: list):
        expected_warning = testing_data.pop(0)
        super().test_assertify_fails(expected_warning, *testing_data)
