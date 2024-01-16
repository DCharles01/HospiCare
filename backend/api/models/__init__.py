from api.models.baseclass import BaseClass
from api.models.patient import Patient
from api.models.admission import Admission
from api.models.physician import Physician
from api.models.insurance import Insurance
from api.models.diagnosis import Diagnosis
from api.models.medication import Medication
from api.models.admission_physician import AdmissionPhysician
# from api.models.medication_change import MedicationChange
from api.models.lab_result import LabResult

models_list = [Patient, Admission, Physician, Insurance, Diagnosis, Medication, AdmissionPhysician, LabResult]

table_names = [table.__table__ for table in models_list]

table_cols = {model.__name__:model.columns for model in models_list}
