from django.db import models

class Patients(models.Model):
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=25, null=True)
    race = models.CharField(max_length=25, null=True)
    age = models.CharField(max_length=15, null=True)
    weight = models.CharField(max_length=15, null=True)

class Insurances(models.Model):
    insurance_cd = models.CharField(max_length=2)
    insurance_name = models.CharField(max_length=150)

class AdmissionTypes(models.Model):
    description = models.TextField()

class DischargeDispositions(models.Model):
    description = models.TextField()

class AdmissionSources(models.Model):
    description = models.TextField()

class Admissions(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurances, on_delete=models.CASCADE, null=True)
    admission_type = models.ForeignKey(AdmissionTypes, on_delete=models.CASCADE)
    discharge_disposition = models.ForeignKey(DischargeDispositions, on_delete=models.CASCADE)
    admission_source = models.ForeignKey(AdmissionSources, on_delete=models.CASCADE)
    time_in_hospital = models.IntegerField()

class AdmissionsProcedures(models.Model):
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    lab_procedures_cnt = models.IntegerField()
    procedures_cnt = models.IntegerField()
    medications_cnt = models.IntegerField()
    diagnoses_given_cnt = models.IntegerField()
    prev_outpatient_cnt = models.IntegerField()
    prev_inpatient_cnt = models.IntegerField()
    prev_emergency_cnt = models.IntegerField()

class Physicians(models.Model):
    specialty = models.CharField(max_length=300)

class Medications(models.Model):
    medication_name = models.CharField(max_length=300)

class MedicationChanges(models.Model):
    medication = models.ForeignKey(Medications, on_delete=models.CASCADE)
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    change_status = models.CharField(max_length=10)

class Diagnoses(models.Model):
    diag = models.TextField()
    diag_description = models.TextField(null=True)

class LabResults(models.Model):
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    max_glu_serum = models.TextField()
    a1cresult = models.TextField()

class AdmissionsDiagnosis(models.Model):
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)

class AdmissionsPhysicians(models.Model):
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physicians, on_delete=models.CASCADE)

class Readmissions(models.Model):
    admission = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    status = models.TextField()

# Indexes
class Meta:
    indexes = [
        models.Index(fields=['id'], name='idx_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_med_change_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_admission_procedures_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_readmission_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_admissions_diagnosis_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_admissions_physicians_admissions_id'),
        models.Index(fields=['admission__id'], name='idx_lab_results_admissions_id'),
        models.Index(fields=['id'], name='idx_patients_patient_id'),
        models.Index(fields=['id'], name='idx_admissions_patient_id'),
    ]
