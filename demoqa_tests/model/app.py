from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm, ModalDialogSubmittingForm

form = StudentRegistrationForm()
result = ModalDialogSubmittingForm()


def given_opened_practice_form():
    browser.open('/automation-practice-form').driver.maximize_window()

    (
        ss('[id^=google_ads][id$=container__]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )