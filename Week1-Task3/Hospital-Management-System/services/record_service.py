from models.medical_record import MedicalRecord


class RecordService:

    def __init__(self):
        self.records = []

    def add_record(
        self,
        record_id,
        patient,
        diagnosis,
        prescription,
        notes
    ):
        record = MedicalRecord(
            record_id,
            patient,
            diagnosis,
            prescription,
            notes
        )

        self.records.append(record)

        return record

    def get_all_records(self):
        return self.records

    def find_record(self, record_id):

        for record in self.records:
            if record.record_id == record_id:
                return record

        return None