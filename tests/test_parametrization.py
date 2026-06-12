import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.mark.parametrize('number', [1,2,3,-1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'run: {browser}')

class TestOperations:
    @pytest.mark.parametrize('user', ['Alice', 'Bob', 'Charlie'])
    def test_user_with_operations(self, user: str):
        ...
    @pytest.mark.parametrize(
        'user',
        ['Alice', 'Bob', 'Charlie']
    )
    def test_user_without_operations(self, user: str):
        ...

@pytest.mark.parametrize(
    'phone_number',
    ['1', '2', '3'],
    ids=[
        'User with monet on bank account',
        'User without monet on bank account',
        'User without oper on bank account',

    ]
)
def test_identifiers(phone_number: str):
    ...

