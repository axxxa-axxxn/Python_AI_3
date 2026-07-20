from models.appointment import Appointment


class AppointmentService:

    def __init__(self):
        self.appointments = []

    def create_appointment(
        self,
        appointment_id,
        doctor,
        patient,
        date,
        time
    ):
        appointment = Appointment(
            appointment_id,
            doctor,
            patient,
            date,
            time
        )

        self.appointments.append(appointment)

        return appointment

    def get_all_appointments(self):
        return self.appointments

    def find_appointment(self, appointment_id):

        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment

        return None

    def cancel_appointment(self, appointment_id):

        appointment = self.find_appointment(
            appointment_id
        )

        if appointment:
            appointment.cancel()
            return True

        return False