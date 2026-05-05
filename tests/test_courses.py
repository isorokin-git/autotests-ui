from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('//input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('//input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('//input')
        password_input.fill('password')

        reg_button = page.get_by_test_id('registration-page-registration-button')
        reg_button.click()

        context.storage_state(path='browser-state-registration.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state-registration.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        empty_list_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_title).to_be_visible()
        expect(empty_list_text).to_have_text('There is no results')

        empty_list_desc = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_title).to_be_visible()
        expect(empty_list_desc).to_have_text('Results from the load test pipeline will be displayed here')