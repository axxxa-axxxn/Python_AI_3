from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from models.medical_record import MedicalRecord


class Hospital:
    """
    Main controller class.
    """

    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []
        self.records = []

    # Doctor Methods

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def search_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.person_id == doctor_id:
                return doctor
        return None

    # Patient Methods

    def add_patient(self, patient):
        self.patients.append(patient)

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.person_id == patient_id:
                return patient
        return None

    # Appointment Methods

    def schedule_appointment(
        self,
        appointment_id,
        doctor_id,
        patient_id,
        date,
        time
    ):
        doctor = self.search_doctor(doctor_id)
        patient = self.search_patient(patient_id)

        if doctor and patient:
            appointment = Appointment(
                appointment_id,
                doctor,
                patient,
                date,
                time
            )

            self.appointments.append(appointment)

            return appointment

        return None

    # Medical Record Methods

    def add_medical_record(
        self,
        record_id,
        patient_id,
        diagnosis,
        prescription,
        notes
    ):
        patient = self.search_patient(patient_id)

        if patient:
            record = MedicalRecord(
                record_id,
                patient,
                diagnosis,
                prescription,
                notes
            )

            self.records.append(record)

            return record

        return None

    # Reports

    def show_report(self):
        print("\n===== REPORT =====")
        print(f"Doctors: {len(self.doctors)}")
        print(f"Patients: {len(self.patients)}")
        print(f"Appointments: {len(self.appointments)}")
        print(f"Medical Records: {len(self.records)}")