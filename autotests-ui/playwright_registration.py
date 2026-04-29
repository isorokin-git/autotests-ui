from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
    password_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    dashboard_label = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_label).to_have_text('Dashboard')
