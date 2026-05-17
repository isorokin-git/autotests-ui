import pytest
from playwright.sync_api import sync_playwright, expect

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, password, username",
    [("username@mail.com", "password", "username")]
)
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str, password: str, username: str):

        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()

        dashboard_page.check_visible_dashboard_label()
