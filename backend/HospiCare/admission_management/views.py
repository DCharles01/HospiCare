from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Patients, Admissions
from django.forms.models import model_to_dict
import json

def patients(request):
    records: list[Patients] = Patients.objects.all()
    patients_list: list[dict] = [Patient.__dict__ for Patient in records]
    return JsonResponse({'patients': patients_list})

def patient_id(request, id: int):
    record: Patients = get_object_or_404(Patients, id=id)
    data_dict: dict = model_to_dict(record)

    return JsonResponse(data_dict)

def patient_search(request):
    name: str = request.GET.get('name')
    gender: str = request.GET.get('gender')
    race: str = request.GET.get('race')

    # Build the query based on the provided parameters
    conditions: dict = {}
    if name:
        conditions['name']: str = name
    if gender:
        conditions['gender']: str = gender
    if race:
        conditions['race']: str = race

    # Execute the query
    records = Patients.objects.filter(**conditions)

    # list of Patient dicts
    patients_list: list[dict] = [model_to_dict(Patient) for Patient in records]

    return JsonResponse({'patients': patients_list})

def admissions(request):
    # print('Retrieving objects')
    records: list[Admissions] = Admissions.objects.all()
    admissions_list: list[dict] = [model_to_dict(Admission) for Admission in records]
    from django.template.loader import get_template
    # print('Extracting template origin')
    # template = get_template('admissions_table.html')
    # print('Printing: ', template.origin.name)
    # return JsonResponse({'admissions': admissions_list})
    return render(request, 'admissions_table.html', {'admissions': admissions_list})


def admission_id(request, id: int):
    record: Admissions = get_object_or_404(Admissions, id=id)
    # return JsonResponse(record.__dict__)
    # return record.__dict__
    # Convert the model instance to a dictionary
    data_dict: dict = model_to_dict(record)

    return JsonResponse(data_dict)

def add_admission_record(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # create new instance of Admission model
        new_admission = Admissions()

        new_admission.patient_name = data.get('')

