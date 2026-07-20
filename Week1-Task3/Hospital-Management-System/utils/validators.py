import re


class Validator:

    @staticmethod
    def validate_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone):
        return phone.isdigit() and len(phone) >= 10

    @staticmethod
    def validate_age(age):
        return age > 0

    @staticmethod
    def validate_experience(exp):
        return exp >= 0