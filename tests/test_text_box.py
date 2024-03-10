from demoqa_test.data import users
from demoqa_test.model.application import app


def test_text_box():
    app.left_panel.open_text_box_page()
    student = users.simple_student
    app.simple_registration.register(student)
    app.output_form.should_have_data(student)
