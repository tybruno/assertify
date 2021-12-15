""" Testing unittest_assertions/base.py """
from typing import (
    Iterable,
)

import pytest
from unittest_assertions.base import Assertion
from unittest_assertions.identity import AssertIs, AssertTrue, AssertFalse

from assertifiers.base import UnittestAssertionAssertifier


class TestBuiltinAssertionAssertify:
    """Testing builtin assertions"""

    @pytest.mark.parametrize(
        "assertion_class, msg, raises",
        (
            (AssertIs, "Testing message", AssertionError),
            (AssertTrue, "", None),
            (AssertFalse, None, TypeError),
        ),
    )
    def test_init(self, assertion_class, msg, raises) -> None:

        UnittestAssertionAssertifier._assertion_class = assertion_class
        unittest_assertion = UnittestAssertionAssertifier(
            msg=msg, raises=raises
        )
        assert unittest_assertion._assertion_class == assertion_class
        assert unittest_assertion.msg == msg
        assert unittest_assertion.raises == raises

    @pytest.mark.parametrize("arguments", (("hello", None, 2),))
    @pytest.mark.parametrize(
        "keyword_args",
        ({"testing": "hello there"}, {"a": 1, "b": 2}),
    )
    def test_call(self, arguments: Iterable, keyword_args: dict) -> None:
        """Test `BuiltinAssertion` __call__ function

        Args:
            arguments: arguments passed to __call__
            keyword_args: keyword arguments passed to __call__

        Returns:
            None
        """

        def _mock_function(*_args, **_kwargs) -> None:
            """mock function
            Args:
                *_args: arguments for the mocked function
                **_kwargs: keyword arguments for the mocked function

            Returns:
                None

            """
            keyword_args["msg"] = unittest_assertion.msg
            assert arguments == _args
            assert keyword_args == _kwargs

        unittest_assertion = Assertion(_assertion_function=_mock_function)
        unittest_assertion.__call__(*arguments, **keyword_args)
