from models.patient import Patient


class PatientService:

    def __init__(self):
        self.patients = []

    def add_patient(
        self,
        patient_id,
        name,
        age,
        gender,
        phone,
        email,
        blood_group
    ):
        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            phone,
            email,
            blood_group
        )

        self.patients.append(patient)
        return patient

    def get_all_patients(self):
        return self.patients

    def find_patient(self, patient_id):

        for patient in self.patients:
            if patient.person_id == patient_id:
                return patient

        return None

    def remove_patient(self, patient_id):

        patient = self.find_patient(patient_id)

        if patient:
            self.patients.remove(patient)
            return True

        return False