import api.models as models

class AdmissionPhysician(models.BaseClass):
    __table__ = 'admissions_physicians'
    columns = ['id', 'admission_id', 'physician_id']