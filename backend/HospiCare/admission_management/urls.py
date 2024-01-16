# urls.py
from django.urls import path
from .views import patients, patient_id, patient_search, admissions, admission_id

urlpatterns = [
    path('patients/', patients, name='patients'),
    path('patients/<int:id>', patient_id, name='patient_id'),
    path('patients/search', patient_search, name='patient_search'),
    path('admissions/', admissions, name='admissions'),
    path('admissions/<int:id>', admission_id, name='admission_id')
]
