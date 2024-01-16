from tests.models.create_test_data import create_test_db


def test_patient_has_name(create_test_db):
    patient = create_test_db['patient']

    assert patient.name == 'John Doe'

def test_patient_has_physician(create_test_db):
    patient = create_test_db['patient']

    physician = patient.physicians()[0]

    assert physician.specialty == 'Anesthesiology-Pediatric'

    