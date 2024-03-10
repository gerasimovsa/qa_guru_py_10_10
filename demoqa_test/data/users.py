import dataclasses
from datetime import date
from enum import Enum

from demoqa_test.model.pages import resource


class Hobbies(Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


class Genders(Enum):
    male = "Male"
    female = "Female"
    other = "Other"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Genders
    mobile_number: str
    date_of_birth: date
    subjects: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str


student = User(first_name="Stefan",
               last_name="Burnett",
               email="mcride_dg@gmail.com",
               gender=Genders.male,
               mobile_number="7148088000",
               date_of_birth=date(1978, 5, 10),
               subjects="Chemistry",
               hobbies=Hobbies.music,
               picture=resource.path("mc_ride.png"),
               address="888 East Las Olas Blvd, Suite 710",
               state="NCR",
               city="Delhi")
