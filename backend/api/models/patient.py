import api.models as models
from db.db_utils import build_from_record, build_from_records

class Patient(models.BaseClass):
    __table__ = 'patients'
    columns  = ['id', 'name', 'gender', 'race', 'age', 'weight']

    def physicians(self, conn):
        query = """
        select
            physicians.*
        from
            physicians
        inner join
            admissions_physicians on physicians.id=admissions_physicians.physician_id
        inner join
            admissions on admissions_physicians.admission_id=admissions.id
        where
            admissions.patient_id = %s
        """
        cursor = conn.cursor()

        cursor.execute(query, (self.id,))

        records = cursor.fetchall()

        return build_from_records(models.Physician, records)

    def admissions(self, conn):
        pass

    def medications(self, conn):
        pass

    def diagnoses(self, conn):
        pass

    def insurances(self, conn):
        pass

    def lab_results(self, conn):
        pass

    def medication_changes(self, conn):
        pass

    def readmissions(self, conn):
        pass