from dataclasses import dataclass, field
from printer import print_info


@dataclass
class Student:
    first_name: str
    last_name: str
    id: int = field(init=False)
    login: str = field(init=False)

    _id_counter: int = 0  # shared by all instances

    def __post_init__(self):
        self.__class__._id_counter += 1
        self.id = self.__class__._id_counter
        self.login = f"{self.first_name.lower()}{self.id}"
        print_info(f"Student created: {self}")

    def __str__(self):
        return (f"Student(id={self.id}, first_name='{self.first_name}', "
                f"last_name='{self.last_name}', login='{self.login}')")
