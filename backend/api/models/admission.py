import api.models as models

class Admission(models.BaseClass):
    __table__ = 'admissions'
    columns = ['id', 'patient_id', 'insurance_id', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'time_in_hospital']

    def patients(self, conn):
        pass

    def physicians(self, conn):
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
