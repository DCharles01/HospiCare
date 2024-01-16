import api.models as models

class Insurance(models.BaseClass):
    __table__ = 'insurance'
    columns = ['id', 'insurance_cd', 'insurance_name']

    def patients(self, conn):
        pass

    def physicians(self, conn):
        pass

    def diagnoses(self, conn):
        pass

    def lab_results(self, conn):
        pass

    def medication_changes(self, conn):
        pass

    def readmissions(self, conn):
        pass