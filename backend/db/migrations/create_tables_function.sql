CREATE OR REPLACE FUNCTION create_tables()
RETURNS VOID AS $$
BEGIN
    CREATE TABLE patients (
    id serial primary key,
    name varchar(300) not null,
    gender varchar(25),
    race varchar(25),
    age varchar(15),
    weight varchar(15)
);

CREATE TABLE insurances (
    id serial primary key,
    insurance_cd varchar(2),
    insurance_name varchar(150)
);

CREATE TABLE admission_types (
id serial primary key,
description text

);

create table discharge_dispositions (
id serial primary key,
description text
);

create table admission_sources (
id serial primary key,
description text
);

CREATE TABLE admissions (
    id serial primary key,
    patient_id integer,
    insurance_id integer,
    admission_type_id integer,
    discharge_disposition_id integer,
    admission_source_id integer,
    time_in_hospital integer,
    constraint fk_patient foreign key (patient_id) references patients(id),
    constraint fk_insurance foreign key (insurance_id) references insurances(id),
    constraint fk_admission_type foreign key (admission_type_id) references admission_types(id),
    constraint fk_discharge_disposition foreign key (discharge_disposition_id) references discharge_dispositions(id),
    constraint fk_admission_source foreign key (admission_source_id) references admission_sources(id)
);



CREATE TABLE admissions_procedures (
    id serial primary key,
    admission_id integer,
    lab_procedures_cnt integer,
    procedures_cnt integer,
    medications_cnt integer,
    diagnoses_given_cnt integer,
    prev_outpatient_cnt integer,
    prev_inpatient_cnt integer,
    prev_emergency_cnt integer,
    constraint fk_admission foreign key (admission_id) references admissions(id)

);

CREATE TABLE physicians (
    id serial primary key,
    specialty varchar(300) not null
);

CREATE TABLE medications (
    id serial primary key,
    medication_name varchar(300) not null
);

CREATE TABLE medication_changes (
    id serial primary key,
    medication_id integer,
    admission_id integer,
    change_status varchar(10),
    constraint fk_med foreign key (medication_id) references medications(id),
    constraint fk_admission foreign key (admission_id) references admissions(id)
);

CREATE TABLE diagnoses (
    id serial primary key,
    diag text,
    diag_description text
);

CREATE TABLE lab_results (
    id serial primary key,
    admission_id integer,
    max_glu_serum text,
    a1cresult text,
    constraint fk_admission foreign key (admission_id) references admissions(id)
);

CREATE TABLE admissions_diagnosis (
    id serial primary key,
    admission_id integer,
    diagnosis_id integer,
    constraint fk_admission foreign key (admission_id) references admissions(id),
    constraint fk_diag_id foreign key (diagnosis_id) references diagnoses(id)
);

CREATE TABLE admissions_physicians (
    id serial primary key,
    admission_id integer,
    physician_id integer,
    constraint fk_admission foreign key (admission_id) references admissions(id),
    constraint fk_physician foreign key (physician_id) references physicians(id)
);

CREATE TABLE readmissions (
    id serial primary key,
    admission_id integer,
    patient_id integer,
    status text,
    constraint fk_admission foreign key (admission_id) references admissions(id),
    constraint fk_patient foreign key (patient_id) references patients(id)
);

create index idx_admissions_id on admissions(id);
create index idx_med_change_admissions_id on medication_changes(admission_id);
create index idx_admission_procedures_admissions_id on admissions_procedures(admission_id);
create index idx_readmission_admissions_id on readmissions(admission_id);
create index idx_admissions_diagnosis_admissions_id on admissions_diagnosis(admission_id);
create index idx_admissions_physicians_admissions_id on admissions_physicians(admission_id);
create index idx_lab_results_admissions_id on lab_results(admission_id);
create index idx_patients_patient_id on patients(id);
create index idx_admissions_patient_id on admissions(id);


END;
$$ LANGUAGE plpgsql;

-- Execute the function to create tables
SELECT create_tables();
