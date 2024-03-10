from model.pages import resource
from model.pages.registration_page import StudentRegistrationForm


def test__student_registration_form():
    registration_form = StudentRegistrationForm()
    registration_form.open()

    (registration_form.fill_first_name("Stefan")
     .fill_last_name("Burnett")
     .fill_email("mcride_dg@gmail.com")
     .select_gender("Male")
     .fill_mobile_number("7148088000")
     .fill_date_of_birth("1978", "May", "10")
     .fill_subjects("Chemistry")
     .select_hobbies("Music")
     .select_picture(resource.path("mc_ride.png"))
     .fill_current_address("888 East Las Olas Blvd, Suite 710")
     .select_state_and_city("NCR", "Delhi")
     .submit_form())

    registration_form.should_have_registered(full_name="Stefan Burnett",
                                             email="mcride_dg@gmail.com",
                                             gender="Male",
                                             mobile_number="7148088000",
                                             birthday="10 May,1978",
                                             subjects="Chemistry",
                                             hobbies="Music",
                                             picture="mc_ride.png",
                                             address="888 East Las Olas Blvd, Suite 710",
                                             state_city="NCR Delhi")
