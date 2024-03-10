from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.groups = browser.all(".card-body")
        self.items = browser.all("[id^='item-']")

    def open(self, group: str, item: str):
        browser.open('/')
        self.groups.element_by(have.text(group)).click()
        self.items.element_by(have.text(item)).click()

    def open_text_box_page(self):
        self.open('Elements', 'Text Box')
