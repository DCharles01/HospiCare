import pytest
import api.models as models
from db.db_utils import save, test_conn, test_cursor, drop_all_tables, create_all_tables

@pytest.fixture()
def create_test_db():
    drop_all_tables(test_conn)

    create_all_tables(test_conn)

    patient = models.Patient(name='John Doe')
    saved_patient = save(patient, test_conn, test_cursor)

    insurance = models.Insurance(insurance_cd='MC', insurance_name='Medicare')
    saved_insurance = save(insurance, test_conn, test_cursor)
    
    diagnosis = models.Diagnosis()

    admission = models.Admission(patient_id=saved_patient.id, time_in_hospital=13, insurance_id=saved_insurance.id)
    saved_admission = save(admission, test_conn, test_cursor)

    admission_physician = models.AdmissionPhysician(admission_id=saved_admission.id, physician_id=3)
    saved_admission_physician = save(admission_physician, test_conn, test_cursor)


    yield {'patient': saved_patient, 'admission_physician': saved_admission_physician, 'admission': admission}

    drop_all_tables(test_conn)