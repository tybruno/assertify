""" Testing unittest_assertifier_clss/identity.py """

import pytest
from pytest_builtin_types import (
    equal_sequences,
    non_equal_sequences,
    _ALL_BASIC_TYPES_1,
    _NOT_INSTANCE_TESTING_DATA,
)
from tests.base import AssertifierTester

from assertifiers.identity import (
    AssertifyIs,
    AssertifyIsNone,
    AssertifyIsInstances,
    AssertifyIsNot,
    AssertifyIsInstance,
    AssertifyNotIsInstance,
    AssertifyNotIsInstances,
    AssertifyIsNotNone,
)

# TODO: add TestAssertifyIsInstaces and TestAssertifyNotIsINstances


class TestAssertifyIs(AssertifierTester):
    _assertifier_cls = AssertifyIs

    @pytest.mark.parametrize(
        "testing_data",
        tuple(equal_sequences()),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(non_equal_sequences()),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertifyIsNot(AssertifierTester):
    _assertifier_cls = AssertifyIsNot

    @pytest.mark.parametrize(
        "testing_data",
        tuple(non_equal_sequences()),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(equal_sequences()),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertifyIsNone(AssertifierTester):
    _assertifier_cls = AssertifyIsNone

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in _ALL_BASIC_TYPES_1.values()),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertifyIsNotNone(AssertifierTester):
    _assertifier_cls = AssertifyIsNotNone

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in _ALL_BASIC_TYPES_1.values()),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertifyIsInstance(AssertifierTester):
    _assertifier_cls = AssertifyIsInstance

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in _ALL_BASIC_TYPES_1.items()),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize("testing_data", tuple(_NOT_INSTANCE_TESTING_DATA))
    def test_assertify_fails(self, testing_data: tuple):
        obj, _type = testing_data
        if not isinstance(obj, _type):
            super().test_assertify_fails(obj, _type)


class TestAssertifyNotIsInstance(AssertifierTester):
    _assertifier_cls = AssertifyNotIsInstance

    @pytest.mark.parametrize("testing_data", tuple(_NOT_INSTANCE_TESTING_DATA))
    def test_assertify_passes(self, testing_data: tuple):
        obj, _type = testing_data
        if isinstance(obj, _type):
            super().test_assertify_fails(obj, _type)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in _ALL_BASIC_TYPES_1.items()),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)
