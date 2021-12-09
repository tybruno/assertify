from typing import Type

import pytest

from assertifiers.base import Assertifier


class AssertifierTester:
    _assertifier_cls: Type[Assertifier]

    def test_assertify_passes(self, *args, **kwargs):
        assertify = self._assertifier_cls()
        assertify(*args, **kwargs)
        assertify.raises = AssertionError
        assertify(*args, **kwargs)
        assertify.raises = None
        assert assertify(*args, **kwargs) is True

    def test_assertify_fails(self, *args, **kwargs):
        assertify = self._assertifier_cls()
        with pytest.raises(assertify.raises):
            assertify(*args, **kwargs)

        assertify.raises = AssertionError

        with pytest.raises(assertify.raises):
            assertify(*args, **kwargs)

        assertify.raises = None

        assert assertify(*args, **kwargs) is False

    # def test_assertion_passes(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     assertion(*function_args, **function_kwargs)
    #
    # def test_exception_passes(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     assertion(*function_args, **function_kwargs)
    #
    # def test_bool_passes(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     assert assertion(*function_args, **function_kwargs) is True

    # def test_assertion_raises(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     with pytest.raises(AssertionError):
    #         assertion(*function_args, **function_kwargs)
    #
    # def test_exception_raises(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     with pytest.raises(assertion.raises):
    #         assertion(*function_args, **function_kwargs)
    #
    # def test_bool_fails(self, *function_args, **function_kwargs):
    #     assertion = self._assertion()
    #     assert assertion(*function_args, **function_kwargs) is False
