""" Testing unittest_assertifier_clss/identity.py """

from typing import Dict, Collection

import pytest
from pytest_builtin_types import (
    equal_sequences,
    non_equal_sequences,
    _ALL_BASIC_TYPES_1,
    _NOT_INSTANCE_TESTING_DATA,
)

from assertifiers.identity import (
    AssertifyIs,
    AssertifyIsNone,
    AssertifyIsInstances,
    AssertifyIsNot,
    AssertifyIsInstance,
    AssertifyNotIsInstance,
    AssertifyIsNotNone,
)
from tests.base import AssertifierTester


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


def instances_testing_data():
    data = []
    for value in _ALL_BASIC_TYPES_1.values():
        data.append([value, _ALL_BASIC_TYPES_1, any])
    return data


class TestAssertifyIsInstances(AssertifierTester):
    _assertifier_cls = AssertifyIsInstances

    @pytest.mark.parametrize(
        "testing_data",
        (*instances_testing_data(), [dict(), [Collection, Dict, dict], all]),
    )
    def test_assertify_passes(self, testing_data: list):
        must_pass = testing_data.pop()
        assertify_is_instances = AssertifyIsInstances(must_pass=must_pass)
        assert assertify_is_instances(*testing_data) is True

        assertify_is_instances.raises = AssertionError
        assert assertify_is_instances(*testing_data) is True

        assertify_is_instances.raises = None
        assert assertify_is_instances(*testing_data) is True

    @pytest.mark.parametrize("testing_data", tuple(_NOT_INSTANCE_TESTING_DATA))
    def test_assertify_fails(self, testing_data: tuple):
        obj, _type = testing_data
        assertify_is_instances = AssertifyIsInstances(must_pass=any)

        if not isinstance(obj, _type):
            with pytest.raises(
                expected_exception=assertify_is_instances.raises
            ):
                assertify_is_instances(obj=obj, classes=_type)

        assertify_is_instances.raises = AssertionError

        if not isinstance(obj, _type):
            with pytest.raises(
                expected_exception=assertify_is_instances.raises
            ):
                assertify_is_instances(obj=obj, classes=_type)
        assertify_is_instances.raises = None

        if not isinstance(obj, _type):
            assert assertify_is_instances(obj=obj, classes=_type) is False


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
