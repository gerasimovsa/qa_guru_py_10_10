from selene import browser, be, command
from demoqa_test.data.users import User


class TextBoxPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")

    def register(self, user: User):
        self.full_name.should(be.blank).type(user.full_name)
        self.email.should(be.blank).type(user.email)
        self.current_address.should(be.blank).type(user.current_address)
        self.permanent_address.should(be.blank).type(user.permanent_address)
        self.submit_button.perform(command.js.scroll_into_view)
        self.submit_button.click()
        return self
