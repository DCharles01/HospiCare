import api.models as models

class Physician(models.BaseClass):
    __table__ = 'physicians'
    columns = ['id', 'specialty']

    def patients(self, conn):
        pass

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