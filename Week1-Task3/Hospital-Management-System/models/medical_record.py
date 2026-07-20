class MedicalRecord:

    def __init__(
        self,
        record_id,
        patient,
        diagnosis,
        prescription,
        notes
    ):
        self.__record_id = record_id
        self.__patient = patient
        self.__diagnosis = diagnosis
        self.__prescription = prescription
        self.__notes = notes

    @property
    def record_id(self):
        return self.__record_id

    @property
    def patient(self):
        return self.__patient

    @property
    def diagnosis(self):
        return self.__diagnosis

    @property
    def prescription(self):
        return self.__prescription

    @property
    def notes(self):
        return self.__notes

    def __str__(self):
        return (
            f"Record ID: {self.record_id}\n"
            f"Patient: {self.patient.name}\n"
            f"Diagnosis: {self.diagnosis}\n"
            f"Prescription: {self.prescription}\n"
            f"Notes: {self.notes}"
        )