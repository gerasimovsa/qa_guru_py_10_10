import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


simple_student = User(full_name="Stefan Burnett",
                      email="mcride_dg@gmail.com",
                      current_address="888 East Las Olas Blvd, Suite 710",
                      permanent_address="1600 Pennsylvania Avenue NW, 20500")
