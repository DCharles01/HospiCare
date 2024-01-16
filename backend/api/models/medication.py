import api.models as models

class Medication(models.BaseClass):
    __table__ = 'medications'
    columns = ['id', 'name']

    def patients(self, conn):
        pass

    def physicians(self, conn):
        pass

    def readmissions(self, conn):
        pass 

    