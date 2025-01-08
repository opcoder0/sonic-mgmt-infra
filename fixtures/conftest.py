import pytest

@pytest.fixture
def setup():
    print("\nSetup")
    yield
    print("\nTeardown")
