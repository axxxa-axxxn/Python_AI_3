from models.doctor import Doctor


class DoctorService:

    def __init__(self):
        self.doctors = []

    def add_doctor(
        self,
        doctor_id,
        name,
        age,
        gender,
        phone,
        email,
        specialization,
        experience
    ):
        doctor = Doctor(
            doctor_id,
            name,
            age,
            gender,
            phone,
            email,
            specialization,
            experience
        )

        self.doctors.append(doctor)
        return doctor

    def get_all_doctors(self):
        return self.doctors

    def find_doctor(self, doctor_id):

        for doctor in self.doctors:
            if doctor.person_id == doctor_id:
                return doctor

        return None

    def remove_doctor(self, doctor_id):

        doctor = self.find_doctor(doctor_id)

        if doctor:
            self.doctors.remove(doctor)
            return True

        return False