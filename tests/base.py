from typing import Type

import pytest

from assertifiers.base import Assertifier
from assertifiers.base import UnittestAssertionAssertifier

MSGS = (None, "", "test message")


class AssertifierTester:
    _assertion_class: Type[Assertifier]

    def test_assertify_passes(self, *args, **kwargs):
        assertify = self._assertion_class()
        assertify(*args, **kwargs)
        assertify.raises = AssertionError
        assertify(*args, **kwargs)
        assertify.raises = None
        assert assertify(*args, **kwargs) is True

    def test_assertify_fails(self, *args, **kwargs):
        assertify = self._assertion_class()
        with pytest.raises(assertify.raises):
            assertify(*args, **kwargs)

        assertify.raises = AssertionError

        with pytest.raises(assertify.raises):
            assertify(*args, **kwargs)

        assertify.raises = None

        assert assertify(*args, **kwargs) is False


class UnittestAssertionAssertifierTester(AssertifierTester):
    _assertion_class: Type[UnittestAssertionAssertifier]

    @pytest.mark.parametrize("msg", MSGS)
    def test_initial_msg(self, msg):
        assertifier_obj: UnittestAssertionAssertifier = self._assertion_class(
            msg=msg
        )
        assert assertifier_obj.msg == msg
        assert assertifier_obj._assertion_function.msg == msg

    @pytest.mark.parametrize("msg", MSGS)
    def test_changed_msg(self, msg):
        assertifier_obj: UnittestAssertionAssertifier = self._assertion_class()
        assertifier_obj._assertion_function.msg = msg

        assert assertifier_obj.msg == msg
        assert assertifier_obj._assertion_function.msg == msg
