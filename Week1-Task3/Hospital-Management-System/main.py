from services.doctor_service import DoctorService
from services.patient_service import PatientService
from services.appointment_service import AppointmentService
from services.record_service import RecordService

from utils.validators import Validator
from utils.logger import Logger


doctor_service = DoctorService()
patient_service = PatientService()
appointment_service = AppointmentService()
record_service = RecordService()


def add_doctor():

    doctor_id = input("Doctor ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    phone = input("Phone: ")
    email = input("Email: ")
    specialization = input("Specialization: ")
    experience = int(input("Experience: "))

    if not Validator.validate_email(email):
        print("Invalid Email")
        return

    doctor = doctor_service.add_doctor(
        doctor_id,
        name,
        age,
        gender,
        phone,
        email,
        specialization,
        experience
    )

    Logger.log(f"Doctor Added: {doctor.name}")

    print("\nDoctor Added Successfully")


def add_patient():

    patient_id = input("Patient ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    phone = input("Phone: ")
    email = input("Email: ")
    blood_group = input("Blood Group: ")

    if not Validator.validate_email(email):
        print("Invalid Email")
        return

    patient = patient_service.add_patient(
        patient_id,
        name,
        age,
        gender,
        phone,
        email,
        blood_group
    )

    Logger.log(f"Patient Added: {patient.name}")

    print("\nPatient Added Successfully")


def search_doctor():

    doctor_id = input("Doctor ID: ")

    doctor = doctor_service.find_doctor(
        doctor_id
    )

    if doctor:
        print("\n", doctor)
    else:
        print("Doctor Not Found")


def search_patient():

    patient_id = input("Patient ID: ")

    patient = patient_service.find_patient(
        patient_id
    )

    if patient:
        print("\n", patient)
    else:
        print("Patient Not Found")


def schedule_appointment():

    appointment_id = input(
        "Appointment ID: "
    )

    doctor_id = input(
        "Doctor ID: "
    )

    patient_id = input(
        "Patient ID: "
    )

    date = input(
        "Date (YYYY-MM-DD): "
    )

    time = input(
        "Time: "
    )

    doctor = doctor_service.find_doctor(
        doctor_id
    )

    patient = patient_service.find_patient(
        patient_id
    )

    if not doctor:
        print("Doctor Not Found")
        return

    if not patient:
        print("Patient Not Found")
        return

    appointment = (
        appointment_service
        .create_appointment(
            appointment_id,
            doctor,
            patient,
            date,
            time
        )
    )

    Logger.log(
        f"Appointment Created: "
        f"{appointment.appointment_id}"
    )

    print(
        "\nAppointment Scheduled"
    )


def view_appointments():

    appointments = (
        appointment_service
        .get_all_appointments()
    )

    if not appointments:
        print("No Appointments")
        return

    print("\n===== APPOINTMENTS =====")

    for appointment in appointments:
        print()
        print(appointment)
        print("-" * 40)


def cancel_appointment():

    appointment_id = input(
        "Appointment ID: "
    )

    success = (
        appointment_service
        .cancel_appointment(
            appointment_id
        )
    )

    if success:
        Logger.log(
            f"Appointment Cancelled: "
            f"{appointment_id}"
        )

        print(
            "Appointment Cancelled"
        )

    else:
        print(
            "Appointment Not Found"
        )


def create_medical_record():

    record_id = input(
        "Record ID: "
    )

    patient_id = input(
        "Patient ID: "
    )

    diagnosis = input(
        "Diagnosis: "
    )

    prescription = input(
        "Prescription: "
    )

    notes = input(
        "Notes: "
    )

    patient = (
        patient_service
        .find_patient(
            patient_id
        )
    )

    if not patient:
        print(
            "Patient Not Found"
        )
        return

    record = (
        record_service
        .add_record(
            record_id,
            patient,
            diagnosis,
            prescription,
            notes
        )
    )

    Logger.log(
        f"Medical Record Added: "
        f"{record.record_id}"
    )

    print(
        "Medical Record Added"
    )


def view_medical_records():

    records = (
        record_service
        .get_all_records()
    )

    if not records:
        print(
            "No Medical Records"
        )
        return

    print(
        "\n===== MEDICAL RECORDS ====="
    )

    for record in records:
        print()
        print(record)
        print("-" * 40)


def reports():

    print("\n===== REPORT =====")

    print(
        f"Total Doctors: "
        f"{len(doctor_service.doctors)}"
    )

    print(
        f"Total Patients: "
        f"{len(patient_service.patients)}"
    )

    print(
        f"Total Appointments: "
        f"{len(appointment_service.appointments)}"
    )

    print(
        f"Total Medical Records: "
        f"{len(record_service.records)}"
    )


def menu():

    while True:

        print("\n")
        print("=" * 45)
        print(" HOSPITAL MANAGEMENT SYSTEM ")
        print("=" * 45)

        print("1. Add Doctor")
        print("2. Search Doctor")
        print("3. Add Patient")
        print("4. Search Patient")
        print("5. Schedule Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Create Medical Record")
        print("9. View Medical Records")
        print("10. Reports")
        print("11. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        try:

            if choice == "1":
                add_doctor()

            elif choice == "2":
                search_doctor()

            elif choice == "3":
                add_patient()

            elif choice == "4":
                search_patient()

            elif choice == "5":
                schedule_appointment()

            elif choice == "6":
                view_appointments()

            elif choice == "7":
                cancel_appointment()

            elif choice == "8":
                create_medical_record()

            elif choice == "9":
                view_medical_records()

            elif choice == "10":
                reports()

            elif choice == "11":

                print(
                    "\nThank You!"
                )

                break

            else:
                print(
                    "Invalid Choice"
                )

        except Exception as error:

            print(
                f"Error: {error}"
            )


if __name__ == "__main__":
    menu()