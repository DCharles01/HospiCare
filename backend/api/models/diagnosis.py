import api.models as models

class Diagnosis(models.BaseClass):
    __table__ = 'diagnosis'
    columns = ['id', 'diagnosis_cd', 'description']

    def physicians(self, conn):
        pass

    def admissions(self, conn):
        pass

    def medications(self, conn):
        pass

    def lab_results(self, conn):
        pass

    def medication_changes(self, conn):
        pass

    def readmissions(self, conn):
        pass