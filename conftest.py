import pytest

@pytest.fixture(scope="session")
def basic_test_setup():
    print("This is a basic test setup.")