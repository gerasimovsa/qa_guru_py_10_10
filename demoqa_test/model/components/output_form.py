from selene import browser, have

from demoqa_test.data.users import User


class OutputForm:
    def __init__(self):
        self.output_fields = browser.element('.border').all('p')

    def should_have_data(self, user: User):
        self.output_fields.should(have.exact_texts(f"Name:{user.full_name}",
                                                   f"Email:{user.email}",
                                                   f"Current Address :{user.current_address}",
                                                   f"Permananet Address :{user.permanent_address}"))
