class Person:
    """
    Base class for all persons in the hospital.
    """

    def __init__(
        self,
        person_id,
        name,
        age,
        gender,
        phone,
        email
    ):
        self.__person_id = person_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone = phone
        self.__email = email

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    def __str__(self):
        return (
            f"ID: {self.person_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}"
        )

    def __repr__(self):
        return (
            f"Person("
            f"id={self.person_id}, "
            f"name='{self.name}')"
        )