
import pytest
import conftest


@pytest.fixture
def setup():
    print("Setting up the test environment.")


def test_inital_check(setup):
    print("This is the initial check test.")
    
    
def test_2_check(basic_test_setup):
    print("This is the second check test.")