# Generated by Django 4.2.2 on 2024-01-14 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_in_hospital", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionSources",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Diagnoses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("diag", models.TextField()),
                ("diag_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="DischargeDispositions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Insurances",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("insurance_cd", models.CharField(max_length=2)),
                ("insurance_name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Medications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("medication_name", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Patients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("gender", models.CharField(max_length=25, null=True)),
                ("race", models.CharField(max_length=25, null=True)),
                ("age", models.CharField(max_length=15, null=True)),
                ("weight", models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Physicians",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("specialty", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Readmissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.TextField()),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.patients",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicationChanges",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("change_status", models.CharField(max_length=10)),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
                (
                    "medication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.medications",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LabResults",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("max_glu_serum", models.TextField()),
                ("a1cresult", models.TextField()),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionsProcedures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lab_procedures_cnt", models.IntegerField()),
                ("procedures_cnt", models.IntegerField()),
                ("medications_cnt", models.IntegerField()),
                ("diagnoses_given_cnt", models.IntegerField()),
                ("prev_outpatient_cnt", models.IntegerField()),
                ("prev_inpatient_cnt", models.IntegerField()),
                ("prev_emergency_cnt", models.IntegerField()),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionsPhysicians",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
                (
                    "physician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.physicians",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionsDiagnosis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "admission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.admissions",
                    ),
                ),
                (
                    "diagnosis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admission_management.diagnoses",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="admissions",
            name="admission_source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admission_management.admissionsources",
            ),
        ),
        migrations.AddField(
            model_name="admissions",
            name="admission_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admission_management.admissiontypes",
            ),
        ),
        migrations.AddField(
            model_name="admissions",
            name="discharge_disposition",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admission_management.dischargedispositions",
            ),
        ),
        migrations.AddField(
            model_name="admissions",
            name="insurance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admission_management.insurances",
            ),
        ),
        migrations.AddField(
            model_name="admissions",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admission_management.patients",
            ),
        ),
    ]
