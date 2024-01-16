import api.models as models

class LabResult(models.BaseClass):
    __table__ = 'lab_results'
    columns = ['id', 'admission_id', 'max_glu_serum', 'a1result']

    def patients(self, conn):
        pass

    def physicians(self, conn):
        pass

    def insurance(self, conn):
        pass

    def admissions(self, conn):
        pass

    def medications(self, conn):
        pass
    



