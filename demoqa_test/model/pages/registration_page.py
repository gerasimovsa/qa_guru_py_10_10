from selene import browser, be, have, by, command
from demoqa_test.data.users import User
from pathlib import Path


class StudentRegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.all('[name=gender]')
        self.mobile_number = browser.element("#userNumber")
        self.date_of_birth = browser.element("#dateOfBirthInput")
        self.date_picker_year = browser.element("[class='react-datepicker__year-select']")
        self.date_picker_month = browser.element("[class='react-datepicker__month-select']")
        self.subjects = browser.element("#subjectsInput")
        self.subjects_list_option = browser.element("#react-select-2-option-0")
        self.hobbies = browser.all('.custom-checkbox')
        self.picture = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")
        self.submit_button = browser.element("#submit")
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    @staticmethod
    def date_picker_day(day):
        return browser.element(f"[class = 'react-datepicker__day react-datepicker__day--0{day}']")

    def open(self):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def register(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)
        self.last_name.should(be.blank).type(user.last_name)
        self.email.should(be.blank).type(user.email)
        self.gender.element_by(have.value(user.gender.value)).element('..').click()
        self.mobile_number.should(be.blank).type(user.mobile_number)
        self.date_of_birth.click()
        self.date_picker_year.click()
        browser.element(by.text(user.date_of_birth.strftime('%Y'))).click()
        self.date_picker_month.click()
        browser.element(by.text(user.date_of_birth.strftime('%B'))).click()
        self.date_picker_day(user.date_of_birth.day).click()
        self.subjects.should(be.blank).type(user.subjects)
        self.subjects_list_option.click()
        self.hobbies.element_by(have.exact_text(user.hobbies.value)).click()
        self.picture.send_keys(user.picture)
        self.address.should(be.blank).type(user.address)
        self.submit_button.perform(command.js.scroll_into_view)
        self.state.click()
        browser.element(by.text(user.state)).click()
        self.city.click()
        browser.element(by.text(user.city)).click()
        self.submit_button.click()
        return self

    def should_have_registered(self, user: User):
        browser.element(".table").should(be.present)
        browser.all('tr td:first-child + td').should(have.exact_texts(f"{user.first_name} {user.last_name}",
                                                                      user.email,
                                                                      user.gender.male.value,
                                                                      user.mobile_number,
                                                                      user.date_of_birth.strftime('%d %B,%Y'),
                                                                      user.subjects,
                                                                      user.hobbies.value,
                                                                      Path(user.picture).name,
                                                                      user.address,
                                                                      f"{user.state} {user.city}")
                                                     )
