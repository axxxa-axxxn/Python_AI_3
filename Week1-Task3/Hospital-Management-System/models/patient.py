from models.person import Person


class Patient(Person):
    """
    Patient class inherits from Person.
    """

    def __init__(
        self,
        person_id,
        name,
        age,
        gender,
        phone,
        email,
        blood_group
    ):
        super().__init__(
            person_id,
            name,
            age,
            gender,
            phone,
            email
        )

        self.__blood_group = blood_group

    @property
    def blood_group(self):
        return self.__blood_group

    def __str__(self):
        return (
            f"Patient ID: {self.person_id}\n"
            f"Name: {self.name}\n"
            f"Blood Group: {self.blood_group}"
        )