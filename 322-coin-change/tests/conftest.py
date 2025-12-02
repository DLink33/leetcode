# conftest.py
import pytest

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--coin-repeats",
        action="store",
        type=int,
        default=10,
        help="Number of repeats for coin change timing benchmark",
    )

@pytest.fixture
def coin_repeats(request: pytest.FixtureRequest) -> int:
    return request.config.getoption("--coin-repeats") # pyright: ignore[reportReturnType]
