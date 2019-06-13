import string

import pytest
from passgen import gen_pass, SPECIAL_LIST


def test_min_exceed_length_raises_exception():
    """
    When setting the min_char, min_num and min_specials
    the total must not exceed the length of the password.
    """
    with pytest.raises(Exception):
        gen_pass(length=11, min_char=6, min_num=6)


def test_max_total_length_under_length_raises_exception():
    """
    When the max_char, max_num, and max_special are less than
    the total length of the password an exception should be raised.

    """
    with pytest.raises(Exception):
        gen_pass(length=5, max_char=1, max_num=1, max_special_char=1)


def test_min_upper_min_lower_total_not_exceed_max_char():
    """
    When min_upper + min_lower > max_char raise exception
    """
    with pytest.raises(Exception):
        gen_pass(min_lower=5, min_upper=5, max_char=5)


def test_required_upper_case_met():
    """
    Make sure the password contains the correct number of uppercase
    chars
    """
    passwd = gen_pass(min_upper=2, max_upper=2)
    upper_list = string.ascii_uppercase
    upper_count = sum(c in upper_list for c in passwd)
    assert upper_count == 2


def test_required_lower_case_met():
    """
    Make sure the password contains the correct number of lowercase
    chars
    """
    passwd = gen_pass(min_lower=2, max_lower=2)
    lower_list = string.ascii_lowercase
    lower_count = sum(c in lower_list for c in passwd)
    assert lower_count == 2


def test_required_nums_case_met():
    """
    Make sure the required amount of numbers are preset in the password
    """
    passwd = gen_pass(length=12, max_char=10, min_num=2, max_num=3)
    nums = string.digits
    num_of_nums = sum(n in nums for n in passwd)
    assert num_of_nums == 2


def test_required_specials_met():
    """
    Make sure the password contains the correct number of special
    chars
    """
    passwd = gen_pass(min_special_char=2, max_special_char=2)
    special_count = sum(c in SPECIAL_LIST for c in passwd)
    assert special_count == 2


def test_password_returns_min_requirements():
    """
    The default values for gen_pass will equal a 10
    char password. This function should return a 10
    char password by default.

    :return:
    """
    passwd = gen_pass()
    assert len(passwd) == 10
    alpha = sum(c.isalpha() for c in passwd)


def test_specials_list_raises_exception_on_nonlist_or_str():
    """
    When calling gen_password with a something other than a list
    or a str be sure to raise an Exception
    """
    passwd1 = gen_pass(special_list="!#*()")

    with pytest.raises(Exception):
        gen_pass(special_list=1234)
