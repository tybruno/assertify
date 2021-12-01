import pytest
from pytest_builtin_types import (
    combined_equal_all_basic_types,
    combined_non_equal_all_basic_types,
    equal_sequences,
    non_equal_sequences,
    equal_lists,
    non_equal_list,
    _BASIC_CONTAINERS_1,
    _BASIC_CONTAINERS_2,
    _MULTILINE_1,
    _MULTILINE_2,
)

from assertifiers.comparison import (
    AssertifyEqual,
    AssertifyNotEqual,
    AssertifyGreater,
    AssertifyLess,
    AssertifyMultilineEqual,
    AssertifyAlmostEqual,
    AssertifyCountEqual,
    AssertifierTupleEqual,
    AssertifierSequenceEqual,
    AssertifyGreaterEqual,
    AssertifierListEqual,
    AssertifierDictEqual,
    AssertifierSetEqual,
    AssertifyNotAlmostEqual,
    AssertifyLessEqual,
)
from tests.base import AssertifierTester


class TestAssertifyEqual(AssertifierTester):
    """testing AssertifyEqual"""

    _assertifier_cls = AssertifyEqual

    @pytest.mark.parametrize(
        "testing_data",
        combined_equal_all_basic_types(),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        combined_non_equal_all_basic_types(),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyNotEqual(AssertifierTester):
    _assertifier_cls = AssertifyNotEqual

    @pytest.mark.parametrize(
        "testing_data",
        combined_non_equal_all_basic_types(),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        combined_equal_all_basic_types(),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAlmostEqual(AssertifierTester):
    _assertifier_cls = AssertifyAlmostEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 1.0),
            (0, 0.1 + 0.1j, 0, None),
            (float("inf"), float("inf")),
            (1.1, 1.0, None, 0.5),
            (1.1, 1.1, None, 0.5),
        ),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 2.0),
            (0, 0.1 + 0.1j, 1),
            (1.1, 1.0, None, 0.05),
        ),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestNotAlmostEqual(AssertifierTester):
    _assertifier_cls = AssertifyNotAlmostEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 2.0),
            (0, 0.1 + 0.1j, 1),
            (1.1, 1.0, None, 0.05),
        ),
    )
    def test_assertify_passes(self, testing_data: tuple):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 1.0),
            (0, 0.1 + 0.1j, 0),
            (float("inf"), float("inf")),
            (1.1, 1.0, None, 0.5),
            (1.1, 1.1, None, 0.5),
        ),
    )
    def test_assertify_fails(self, testing_data: tuple):
        super().test_assertify_fails(*testing_data)


class TestAssertifyCountEqual(AssertifierTester):
    _assertifier_cls = AssertifyCountEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (container, container)
            for container in _BASIC_CONTAINERS_1.values()
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (container1, container2)
            for container1, container2 in zip(
                _BASIC_CONTAINERS_1.values(),
                _BASIC_CONTAINERS_2.values(),
            )
            if not isinstance(container1, dict)
            and not isinstance(container2, dict)
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyMultilineEqual(AssertifierTester):
    _assertifier_cls = AssertifyMultilineEqual

    @pytest.mark.parametrize(
        "testing_data",
        ((_MULTILINE_1, _MULTILINE_1),),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize("testing_data", ((_MULTILINE_1, _MULTILINE_2),))
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifySequenceEqual(AssertifierTester):
    _assertifier_cls = AssertifierSequenceEqual

    @pytest.mark.parametrize(
        "testing_data",
        equal_sequences(),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        non_equal_sequences(),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyListEqual(AssertifierTester):
    _assertifier_cls = AssertifierListEqual

    @pytest.mark.parametrize(
        "testing_data",
        (equal_lists(),),
    )
    def test_assertify_passes(self, testing_data):
        print(testing_data)
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (non_equal_list(),),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyTupleEqual(AssertifierTester):
    _assertifier_cls = AssertifierTupleEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                _BASIC_CONTAINERS_1[tuple],
                _BASIC_CONTAINERS_1[tuple],
            ),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (tup1, tup2)
            for tup1, tup2 in zip(
                _BASIC_CONTAINERS_1[tuple], _BASIC_CONTAINERS_2[tuple]
            )
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifySetEqual(AssertifierTester):
    _assertifier_cls = AssertifierSetEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                _BASIC_CONTAINERS_1[set],
                _BASIC_CONTAINERS_1[set],
            ),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (set1, set2)
            for set1, set2 in zip(
                _BASIC_CONTAINERS_1[set], _BASIC_CONTAINERS_2[set]
            )
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyDictEqual(AssertifierTester):
    _assertifier_cls = AssertifierDictEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                _BASIC_CONTAINERS_1[dict],
                _BASIC_CONTAINERS_1[dict],
            ),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (dict1, dict2)
            for dict1, dict2 in zip(
                _BASIC_CONTAINERS_1[dict], _BASIC_CONTAINERS_2[dict]
            )
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyLess(AssertifierTester):
    _assertifier_cls = AssertifyLess

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, 2),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyLessEqual(AssertifierTester):
    _assertifier_cls = AssertifyLessEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1, 2),
            (-1, 2),
            (1.1, 1.2),
            (1, 1),
            (1.1, 1.1),
            ("s", "s"),
            ("str", "string"),
            ([], [2]),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyGreater(AssertifierTester):
    _assertifier_cls = AssertifyGreater

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)


class TestAssertifyGreaterEqual(AssertifierTester):
    _assertifier_cls = AssertifyGreaterEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (1, 1),
            (2, -1),
            (1.2, 1.1),
            (1.1, 1.1),
            (
                "string",
                "str",
            ),
            (
                "str",
                "str",
            ),
            ([2], []),
            ([2], [2]),
        ),
    )
    def test_assertify_passes(self, testing_data):
        super().test_assertify_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertify_fails(self, testing_data):
        super().test_assertify_fails(*testing_data)
