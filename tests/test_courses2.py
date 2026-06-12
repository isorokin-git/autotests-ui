import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_1courses_list1(chromium_page_with_state: Page):
    chromium_page = chromium_page_with_state
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = chromium_page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_icon = chromium_page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    empty_list_text = chromium_page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_list_text).to_be_visible()
    expect(empty_list_text).to_have_text('There is no results')

    empty_list_desc = chromium_page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_list_desc).to_be_visible()
    expect(empty_list_desc).to_have_text('Results from the load test pipeline will be displayed here')

