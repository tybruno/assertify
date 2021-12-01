""" Testing unittest_assertifier_clss/identity.py """

from typing import Dict, Collection

import pytest
from pytest_builtin_types import (
    equal_sequences,
    non_equal_sequences,
    _ALL_BASIC_TYPES_1,
    _NOT_INSTANCE_TESTING_DATA,
)
from copy import deepcopy
from assertifiers.identity import (
    AssertifierIs,
    AssertifierIsNone,
    AssertifyIsInstances,
    AssertifyIsNot,
    AssertifierIsInstance,
    AssertifyNotIsInstance,
    AssertifyNotIsInstances,
    AssertifyIsNotNone,
)
from tests.base import AssertifierTester


class TestAssertifyIs(AssertifierTester):
    _assertifier_cls = AssertifierIs

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
    _assertifier_cls = AssertifierIsNone

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
    _assertifier_cls = AssertifierIsInstance

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


def is_instances_testing_data(must_be_instance_of=any):
    testing_data = []
    for _type, obj in _ALL_BASIC_TYPES_1.items():
        testing_data.append((obj, _ALL_BASIC_TYPES_1, must_be_instance_of))
    return testing_data


def is_not_instances_testing_data(must_be_instance_of=any):
    testing_data = []
    for _type, obj in _ALL_BASIC_TYPES_1.items():
        container = deepcopy(_ALL_BASIC_TYPES_1)
        if isinstance(obj, bool):
            container.pop(int)
        container.pop(_type)
        testing_data.append((obj, container, must_be_instance_of))
    return testing_data


class TestAssertifyIsInstances(AssertifierTester):
    _assertifier_cls = AssertifyIsInstances

    @pytest.mark.parametrize(
        "testing_data",
        (
            *is_instances_testing_data(),
            (dict(), [Collection, Dict, dict], all),
            ("string", str, any),
            (2, int, all),
        ),
    )
    def test_assertify_passes(self, testing_data: list):
        obj, classes, must_be_instance_of = testing_data

        assertify_is_instances = AssertifyIsInstances(
            must_be_instance_of=must_be_instance_of
        )
        assert assertify_is_instances(obj=obj, classes=classes) is True

        assertify_is_instances.raises = AssertionError
        assert assertify_is_instances(obj=obj, classes=classes) is True

        assertify_is_instances.raises = None
        assert assertify_is_instances(obj=obj, classes=classes) is True

    @pytest.mark.parametrize(
        "testing_data", tuple(is_not_instances_testing_data())
    )
    def test_assertify_fails(self, testing_data: tuple):
        obj, classes, must_be_instance_of = testing_data

        assertify_is_instances = self._assertifier_cls(
            must_be_instance_of=must_be_instance_of
        )

        with pytest.raises(expected_exception=assertify_is_instances.raises):
            assertify_is_instances(obj=obj, classes=classes)

        assertify_is_instances.raises = AssertionError

        with pytest.raises(expected_exception=assertify_is_instances.raises):
            assertify_is_instances(obj=obj, classes=classes)
        assertify_is_instances.raises = None

        assert assertify_is_instances(obj=obj, classes=classes) is False


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


class TestAssertifyNotIsInstances(AssertifierTester):
    _assertifier_cls = AssertifyNotIsInstances

    @pytest.mark.parametrize(
        "testing_data", tuple(is_not_instances_testing_data())
    )
    def test_assertify_passes(self, testing_data: list):
        obj, classes, must_be_instance_of = testing_data
        assertify_is_instances = self._assertifier_cls(
            must_be_instance_of=must_be_instance_of
        )
        assert assertify_is_instances(obj=obj, classes=classes) is True

        assertify_is_instances.raises = AssertionError
        assert assertify_is_instances(obj=obj, classes=classes) is True

        assertify_is_instances.raises = None
        assert assertify_is_instances(obj=obj, classes=classes) is True

    @pytest.mark.parametrize(
        "testing_data",
        (
            *is_instances_testing_data(all),
            (dict(), [Collection, Dict, dict], all),
            ("string", [str], any),
        ),
    )
    def test_assertify_fails(self, testing_data: tuple):
        obj, classes, must_be_instance_of = testing_data

        assertify_is_not_instances = self._assertifier_cls(
            must_be_instance_of=must_be_instance_of
        )
        with pytest.raises(
            expected_exception=assertify_is_not_instances.raises
        ):
            assertify_is_not_instances(obj=obj, classes=classes)

        assertify_is_not_instances.raises = AssertionError

        with pytest.raises(
            expected_exception=assertify_is_not_instances.raises
        ):
            assertify_is_not_instances(obj=obj, classes=classes)
        assertify_is_not_instances.raises = None

        assert assertify_is_not_instances(obj=obj, classes=classes) is False
