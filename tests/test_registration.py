import pytest
from playwright.sync_api import sync_playwright, expect

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page_with_state: DashboardPage):

        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(
                email="user.name@gmail.com",
                username="username",
                password="password"
        )

        registration_page.registration_form.check_visible(
                email="user.name@gmail.com",
                username="username",
                password="password"
        )

        registration_page.click_registration_button()

        dashboard_page_with_state = DashboardPage(registration_page.page)
        dashboard_page_with_state.dashboard_toolbar.check_visible()
