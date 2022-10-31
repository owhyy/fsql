from importlib import import_module

from faker import Faker
from faker.config import PROVIDERS

from fsql.main import SQLFaker


def test_no_type_generation_when_invalid_faker_value(caplog):
    value = "foo"
    fsql = SQLFaker("", [value], 1)
    fsql.generate()
    text = f"No fixture for {value} can be generated by Faker. Trying to generate using mockaroo"
    assert text in caplog.text
    assert 0 == len(fsql.generated)


def test_no_type_generation_when_valid_faker_value():
    fsql = SQLFaker("", ["name"], 1)
    fsql.generate()
    generated = fsql.generated.get("name")
    assert generated is not None
    assert 1 == len(generated)
    assert isinstance(generated[0], str)


def test_generate_when_given_different_name():
    fsql = SQLFaker("", ["foo:name"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert generated is not None
    assert 1 == len(generated)
    assert isinstance(generated[0], str)


def test_generate_bool():
    fsql = SQLFaker("", ["foo:bool"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert 1 == len(generated)
    assert isinstance(generated[0], bool)


def test_generate_same_number():
    fsql = SQLFaker("", ["foo:1"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert [1] == generated


def test_generate_int_pos_range():
    fsql = SQLFaker("", ["foo:[1:10]"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert 1 == len(generated)
    assert isinstance(generated[0], int)
    assert 1 <= generated[0] <= 10


def test_generate_int_pos_range_reverse_order():
    fsql = SQLFaker("", ["foo:[10:1]"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert 1 == len(generated)
    assert isinstance(generated[0], int)
    assert 1 <= generated[0] <= 10


def test_generate_int_neg_range():
    fsql = SQLFaker("", ["foo:[-10:-1]"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert 1 == len(generated)
    assert isinstance(generated[0], int)
    assert -10 <= generated[0] <= -1


def test_pick_choice():
    fsql = SQLFaker("", ["foo:[39, 123, 86, 'bar']"], 1)
    fsql.generate()
    generated = fsql.generated.get("foo")
    assert 1 == len(generated)
    assert generated[0] in [39, 123, 86, "bar"]


def test_multiple():
    fsql = SQLFaker("", ["first_name"], 3)
    fsql.generate()
    generated = fsql.generated.get("first_name")
    assert 3 == len(generated)
    assert True is all(x.isalpha() for x in generated)


def test_multiple_different():
    fsql = SQLFaker("", ["first_name", "age:[10:60]"], 3)
    fsql.generate()
    name_generated = fsql.generated.get("first_name")
    assert 3 == len(name_generated)
    assert True is all(x.isalpha() for x in name_generated)

    name_generated = fsql.generated.get("age")
    assert 3 == len(name_generated)
    assert all(isinstance(x, int) for x in name_generated)
    assert all(x for x in name_generated if 10 <= x <= 60)
