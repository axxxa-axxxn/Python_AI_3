class Appointment:

    def __init__(
        self,
        appointment_id,
        doctor,
        patient,
        date,
        time
    ):
        self.__appointment_id = appointment_id
        self.__doctor = doctor
        self.__patient = patient
        self.__date = date
        self.__time = time
        self.__status = "Scheduled"

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def doctor(self):
        return self.__doctor

    @property
    def patient(self):
        return self.__patient

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @property
    def status(self):
        return self.__status

    def cancel(self):
        self.__status = "Cancelled"

    def __str__(self):
        return (
            f"Appointment ID: {self.appointment_id}\n"
            f"Doctor: {self.doctor.name}\n"
            f"Patient: {self.patient.name}\n"
            f"Date: {self.date}\n"
            f"Time: {self.time}\n"
            f"Status: {self.status}"
        )