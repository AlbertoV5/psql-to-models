"""
Pydantic Models
"""
from pydantic import BaseModel
from datetime import datetime


class Admissions(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    admittime: datetime
    dischtime: datetime
    deathtime: datetime | None
    admission_type: str
    admission_location: str
    discharge_location: str
    insurance: str
    language: str | None
    religion: str | None
    marital_status: str | None
    ethnicity: str
    edregtime: datetime | None
    edouttime: datetime | None
    diagnosis: str | None
    hospital_expire_flag: int | None
    has_chartevents_data: int

    class Config:
        orm_mode = True


class Callout(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    submit_wardid: int | None
    submit_careunit: str | None
    curr_wardid: int | None
    curr_careunit: str | None
    callout_wardid: int | None
    callout_service: str
    request_tele: int
    request_resp: int
    request_cdiff: int
    request_mrsa: int
    request_vre: int
    callout_status: str
    callout_outcome: str
    discharge_wardid: int | None
    acknowledge_status: str
    createtime: datetime
    updatetime: datetime
    acknowledgetime: datetime | None
    outcometime: datetime
    firstreservationtime: datetime | None
    currentreservationtime: datetime | None

    class Config:
        orm_mode = True


class Caregivers(BaseModel):

    row_id: int
    cgid: int
    label: str | None
    description: str | None

    class Config:
        orm_mode = True


class Chartevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    icustay_id: int | None
    itemid: int | None
    charttime: datetime | None
    storetime: datetime | None
    cgid: int | None
    value: str | None
    valuenum: float | None
    valueuom: str | None
    warning: int | None
    error: int | None
    resultstatus: str | None
    stopped: str | None

    class Config:
        orm_mode = True


class Cptevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    costcenter: str
    chartdate: datetime | None
    cpt_cd: str
    cpt_number: int | None
    cpt_suffix: str | None
    ticket_id_seq: int | None
    sectionheader: str | None
    subsectionheader: str | None
    description: str | None

    class Config:
        orm_mode = True


class Datetimeevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    icustay_id: int | None
    itemid: int
    charttime: datetime
    storetime: datetime
    cgid: int
    value: datetime | None
    valueuom: str
    warning: int | None
    error: int | None
    resultstatus: str | None
    stopped: str | None

    class Config:
        orm_mode = True


class Diagnoses_icd(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    seq_num: int | None
    icd9_code: str | None

    class Config:
        orm_mode = True


class Drgcodes(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    drg_type: str
    drg_code: str
    description: str | None
    drg_severity: int | None
    drg_mortality: int | None

    class Config:
        orm_mode = True


class D_cpt(BaseModel):

    row_id: int
    category: int
    sectionrange: str
    sectionheader: str
    subsectionrange: str
    subsectionheader: str
    codesuffix: str | None
    mincodeinsubsection: int
    maxcodeinsubsection: int

    class Config:
        orm_mode = True


class D_icd_diagnoses(BaseModel):

    row_id: int
    icd9_code: str
    short_title: str
    long_title: str

    class Config:
        orm_mode = True


class D_icd_procedures(BaseModel):

    row_id: int
    icd9_code: str
    short_title: str
    long_title: str

    class Config:
        orm_mode = True


class D_items(BaseModel):

    row_id: int
    itemid: int
    label: str | None
    abbreviation: str | None
    dbsource: str | None
    linksto: str | None
    category: str | None
    unitname: str | None
    param_type: str | None
    conceptid: int | None

    class Config:
        orm_mode = True


class D_labitems(BaseModel):

    row_id: int
    itemid: int
    label: str
    fluid: str
    category: str
    loinc_code: str | None

    class Config:
        orm_mode = True


class Icustays(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    icustay_id: int
    dbsource: str
    first_careunit: str
    last_careunit: str
    first_wardid: int
    last_wardid: int
    intime: datetime
    outtime: datetime | None
    los: float | None

    class Config:
        orm_mode = True


class Inputevents_cv(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    icustay_id: int | None
    charttime: datetime | None
    itemid: int | None
    amount: float | None
    amountuom: str | None
    rate: float | None
    rateuom: str | None
    storetime: datetime | None
    cgid: int | None
    orderid: int | None
    linkorderid: int | None
    stopped: str | None
    newbottle: int | None
    originalamount: float | None
    originalamountuom: str | None
    originalroute: str | None
    originalrate: float | None
    originalrateuom: str | None
    originalsite: str | None

    class Config:
        orm_mode = True


class Inputevents_mv(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    icustay_id: int | None
    starttime: datetime | None
    endtime: datetime | None
    itemid: int | None
    amount: float | None
    amountuom: str | None
    rate: float | None
    rateuom: str | None
    storetime: datetime | None
    cgid: int | None
    orderid: int | None
    linkorderid: int | None
    ordercategoryname: str | None
    secondaryordercategoryname: str | None
    ordercomponenttypedescription: str | None
    ordercategorydescription: str | None
    patientweight: float | None
    totalamount: float | None
    totalamountuom: str | None
    isopenbag: int | None
    continueinnextdept: int | None
    cancelreason: int | None
    statusdescription: str | None
    comments_editedby: str | None
    comments_canceledby: str | None
    comments_date: datetime | None
    originalamount: float | None
    originalrate: float | None

    class Config:
        orm_mode = True


class Labevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    itemid: int
    charttime: datetime | None
    value: str | None
    valuenum: float | None
    valueuom: str | None
    flag: str | None

    class Config:
        orm_mode = True


class Microbiologyevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    chartdate: datetime | None
    charttime: datetime | None
    spec_itemid: int | None
    spec_type_desc: str | None
    org_itemid: int | None
    org_name: str | None
    isolate_num: int | None
    ab_itemid: int | None
    ab_name: str | None
    dilution_text: str | None
    dilution_comparison: str | None
    dilution_value: float | None
    interpretation: str | None

    class Config:
        orm_mode = True


class Noteevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    chartdate: datetime | None
    charttime: datetime | None
    storetime: datetime | None
    category: str | None
    description: str | None
    cgid: int | None
    iserror: str | None
    text: str | None

    class Config:
        orm_mode = True


class Outputevents(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int | None
    icustay_id: int | None
    charttime: datetime | None
    itemid: int | None
    value: float | None
    valueuom: str | None
    storetime: datetime | None
    cgid: int | None
    stopped: str | None
    newbottle: str | None
    iserror: int | None

    class Config:
        orm_mode = True


class Patients(BaseModel):

    row_id: int
    subject_id: int
    gender: str
    dob: datetime
    dod: datetime | None
    dod_hosp: datetime | None
    dod_ssn: datetime | None
    expire_flag: int

    class Config:
        orm_mode = True


class Prescriptions(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    icustay_id: int | None
    startdate: datetime | None
    enddate: datetime | None
    drug_type: str
    drug: str
    drug_name_poe: str | None
    drug_name_generic: str | None
    formulary_drug_cd: str | None
    gsn: str | None
    ndc: str | None
    prod_strength: str | None
    dose_val_rx: str | None
    dose_unit_rx: str | None
    form_val_disp: str | None
    form_unit_disp: str | None
    route: str | None

    class Config:
        orm_mode = True


class Procedureevents_mv(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    icustay_id: int | None
    starttime: datetime | None
    endtime: datetime | None
    itemid: int | None
    value: float | None
    valueuom: str | None
    location: str | None
    locationcategory: str | None
    storetime: datetime | None
    cgid: int | None
    orderid: int | None
    linkorderid: int | None
    ordercategoryname: str | None
    secondaryordercategoryname: str | None
    ordercategorydescription: str | None
    isopenbag: int | None
    continueinnextdept: int | None
    cancelreason: int | None
    statusdescription: str | None
    comments_editedby: str | None
    comments_canceledby: str | None
    comments_date: datetime | None

    class Config:
        orm_mode = True


class Procedures_icd(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    seq_num: int
    icd9_code: str

    class Config:
        orm_mode = True


class Services(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    transfertime: datetime
    prev_service: str | None
    curr_service: str | None

    class Config:
        orm_mode = True


class Transfers(BaseModel):

    row_id: int
    subject_id: int
    hadm_id: int
    icustay_id: int | None
    dbsource: str | None
    eventtype: str | None
    prev_careunit: str | None
    curr_careunit: str | None
    prev_wardid: int | None
    curr_wardid: int | None
    intime: datetime | None
    outtime: datetime | None
    los: float | None

    class Config:
        orm_mode = True

