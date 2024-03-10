from demoqa_test.data import users
from demoqa_test.model.pages.registration_page import StudentRegistrationPage


def test_student_registration_form():
    registration_page = StudentRegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
