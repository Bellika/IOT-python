from main import add
import pytest

def test_addition():
    assert add(2, 2) == 4


# fixture
def test_sum_list():
    numbers = [1, 2, 3]
    assert sum(numbers) == 6

def test_max_list():
    numbers = [1, 2, 3]
    assert max(numbers) == 3

@pytest.fixture
def numbers():
    return [1, 2, 3]

def test_sum(numbers):
    assert sum(numbers) == 6

def test_max(numbers):
    assert max(numbers) == 3

# fixture with cleanup
@pytest.fixture
def temporary_file(tmp_path):
    file_path = tmp_path / "data.txt"
    with open(file_path, "w") as f:
        f.write("hello world")
    yield file_path  
    file_path.unlink()

def test_file_contents(temporary_file):
    with open(temporary_file) as f:
        content = f.read()
    assert content == "hello world"

# fixture scope
@pytest.fixture(scope="function")   
def function_scope():
    print("\n[Fixture] function scope")
    return "function"

@pytest.fixture(scope="module")     
def module_scope():
    print("\n[Fixture] module scope")
    return "module"

def test_one(function_scope, module_scope):
    print("Test one using:", function_scope, module_scope)

def test_two(function_scope, module_scope):
    print("Test two using:", function_scope, module_scope)
