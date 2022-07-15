from calculator import *

             #####TEST CASES#####

def get_test_cases_sum():
    return [(1,2,3),(5,7,12),(144,56,200)]

def get_test_cases_mult():
    return [(1,2,2),(5,7,35),(144,56,8064)]

def get_test_cases_sub():
    return [(1,2,-1),(5,7,-2),(144,56,88)]

def get_test_cases_div():
    return [(2,1,2),(5,7,0),(144,12,12)]


               #################

import pytest
@pytest.mark.parametrize('n1,n2,ans',get_test_cases_sum())
def test_sum(n1,n2,ans):
    assert sum(n1,n2) == ans

@pytest.mark.parametrize('n1,n2,ans',get_test_cases_mult())
def test_mult(n1,n2,ans):
    assert multiply(n1,n2) == ans

@pytest.mark.parametrize('n1,n2,ans',get_test_cases_sub())
def test_sub(n1,n2,ans):
    assert subtract(n1,n2) == ans

@pytest.mark.parametrize('n1,n2,ans',get_test_cases_div())
def test_div(n1,n2,ans):
    assert divide(n1,n2) == ans
