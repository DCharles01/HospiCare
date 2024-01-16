
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

with hospital_readmissions_obt as (
select
	admissions.id as admission_id
	, patients.id as patient_id
	, patients.name
	, patients.gender
	, patients.race
	, patients.age
	, patients.weight
	, physicians.specialty
	, insurances.insurance_name
	, admission_sources.description as admission_source
	, admission_types.description as admission_type
	, discharge_dispositions.description as discharge_disposition
	, admissions.time_in_hospital
	, lab_results.a1cresult
	, lab_results.max_glu_serum
	, admissions_procedures.lab_procedures_cnt
	, admissions_procedures.procedures_cnt
	, admissions_procedures.medications_cnt
	, admissions_procedures.prev_emergency_cnt
	, admissions_procedures.prev_inpatient_cnt
	, admissions_procedures.prev_outpatient_cnt
	, admissions_procedures.diagnoses_given_cnt
	, readmissions.status
	
from
	patients
inner join
	admissions on patients.id=admissions.patient_id
inner join
	admission_sources on admissions.admission_source_id=admission_sources.id
inner join
	admission_types on admissions.admission_type_id=admission_types.id
inner join
	discharge_dispositions on admissions.discharge_disposition_id=discharge_dispositions.id
left join
	insurances on admissions.insurance_id=insurances.id
-- inner join
-- 	medication_changes on admissions.id=medication_changes.admission_id
inner join
	admissions_procedures on admissions.id=admissions_procedures.admission_id
inner join
	lab_results on admissions.id=lab_results.admission_id
-- inner join
-- 	admissions_diagnosis on admissions.id=admissions_diagnosis.admission_id
inner join
	admissions_physicians on admissions.id=admissions_physicians.admission_id
left join
	physicians on admissions_physicians.physician_id=physicians.id
inner join
	readmissions on admissions.id=readmissions.admission_id
)

select * from hospital_readmissions_obt

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
