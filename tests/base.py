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

    # def test_assertion_passes(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     assertion(*args, **kwargs)
    #
    # def test_exception_passes(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     assertion(*args, **kwargs)
    #
    # def test_bool_passes(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     assert assertion(*args, **kwargs) is True

    # def test_assertion_raises(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     with pytest.raises(AssertionError):
    #         assertion(*args, **kwargs)
    #
    # def test_exception_raises(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     with pytest.raises(assertion.raises):
    #         assertion(*args, **kwargs)
    #
    # def test_bool_fails(self, *args, **kwargs):
    #     assertion = self._assertion()
    #     assert assertion(*args, **kwargs) is False
