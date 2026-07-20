from models.person import Person


class Doctor(Person):
    """
    Doctor class inherits from Person.
    """

    def __init__(
        self,
        person_id,
        name,
        age,
        gender,
        phone,
        email,
        specialization,
        experience
    ):
        super().__init__(
            person_id,
            name,
            age,
            gender,
            phone,
            email
        )

        self.__specialization = specialization
        self.__experience = experience

    @property
    def specialization(self):
        return self.__specialization

    @property
    def experience(self):
        return self.__experience

    def __str__(self):
        return (
            f"Doctor ID: {self.person_id}\n"
            f"Name: {self.name}\n"
            f"Specialization: {self.specialization}\n"
            f"Experience: {self.experience} Years"
        )