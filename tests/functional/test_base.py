""" Testing unittest_assertions/base.py """
from typing import (
    Type,
    Iterable,
    Mapping,
)

import pytest
from unittest_assertions.base import BuiltinAssertion

from assertifiers.base import BuiltinAssertionAssertify
from assertifiers.comparison import AssertifyEqual


class TestBuiltinAssertionAssertify:
    """Testing builtin assertions"""

    @pytest.mark.parametrize("function", (AssertifyEqual,))
    def test_init(self, function: Type[BuiltinAssertion]) -> None:
        """Test builtin assertion __init__

        Args:
            function: function for BuiltinAssertion paramater

        Returns:
            None
        """
        bulitin_assertion = BuiltinAssertionAssertify(_assertion_cls=function)
        assert bulitin_assertion._assertion_cls == function

    @pytest.mark.parametrize("arguments", (("hello", None, 2),))
    @pytest.mark.parametrize(
        "keyword_args",
        ({"testing": "hello there"}, {"msg": "message"}, {"a": 1, "b": 2}),
    )
    def test_call(self, arguments: Iterable, keyword_args: Mapping) -> None:
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
            assert arguments == _args
            assert keyword_args == _kwargs

        bulitin_assertion = BuiltinAssertion(
            _assertion_function=_mock_function
        )
        bulitin_assertion.__call__(*arguments, **keyword_args)