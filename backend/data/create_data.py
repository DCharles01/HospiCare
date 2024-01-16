import pandas as pd
from faker import Faker
import json

diabetic_data = pd.read_csv('diabetic_data.csv')
patient_ids = diabetic_data['patient_nbr'].unique()

def generate_fake_name(gender) -> str:
    fake = Faker()
    if gender == 'Female':
        return fake.name_female()
    
    elif gender == 'Male':
        return fake.name_male()

    else:
        return fake.name()
    
patient_names = {'names': []}
for i, patient_id in enumerate(patient_ids):
    patient_gender = diabetic_data.loc[diabetic_data['patient_nbr'] == patient_id, 'gender']

    assert not patient_gender.empty, f'Error: No gender found for patient number - {patient_id}'
    
    # Extract the first element from the Series
    patient_gender = patient_gender.iloc[0]
    
    # Convert patient_id to a standard Python integer
    patient_id = int(patient_id)
    
    patient_names['names'].append({'id': patient_id, 'name': generate_fake_name(patient_gender)})

with open('patient_fake_names.json', 'w') as names:
    json.dump(patient_names, names)

print('Done')


    


