"""
SQLAlchemy Models
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, CHAR, SmallInteger
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from db.setup import Base


class Admissions(Base):

    __tablename__ = "admissions"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False, unique=True)
    admittime = Column(TIMESTAMP(0), nullable=False)
    dischtime = Column(TIMESTAMP(0), nullable=False)
    deathtime = Column(TIMESTAMP(0))
    admission_type = Column(String(50), nullable=False)
    admission_location = Column(String(50), nullable=False)
    discharge_location = Column(String(50), nullable=False)
    insurance = Column(String(255), nullable=False)
    language = Column(String(10))
    religion = Column(String(50))
    marital_status = Column(String(50))
    ethnicity = Column(String(200), nullable=False)
    edregtime = Column(TIMESTAMP(0))
    edouttime = Column(TIMESTAMP(0))
    diagnosis = Column(String(255))
    hospital_expire_flag = Column(SmallInteger)
    has_chartevents_data = Column(SmallInteger, nullable=False)


class Callout(Base):

    __tablename__ = "callout"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    submit_wardid = Column(Integer)
    submit_careunit = Column(String(15))
    curr_wardid = Column(Integer)
    curr_careunit = Column(String(15))
    callout_wardid = Column(Integer)
    callout_service = Column(String(10), nullable=False)
    request_tele = Column(SmallInteger, nullable=False)
    request_resp = Column(SmallInteger, nullable=False)
    request_cdiff = Column(SmallInteger, nullable=False)
    request_mrsa = Column(SmallInteger, nullable=False)
    request_vre = Column(SmallInteger, nullable=False)
    callout_status = Column(String(20), nullable=False)
    callout_outcome = Column(String(20), nullable=False)
    discharge_wardid = Column(Integer)
    acknowledge_status = Column(String(20), nullable=False)
    createtime = Column(TIMESTAMP(0), nullable=False)
    updatetime = Column(TIMESTAMP(0), nullable=False)
    acknowledgetime = Column(TIMESTAMP(0))
    outcometime = Column(TIMESTAMP(0), nullable=False)
    firstreservationtime = Column(TIMESTAMP(0))
    currentreservationtime = Column(TIMESTAMP(0))


class Caregivers(Base):

    __tablename__ = "caregivers"

    row_id = Column(Integer, nullable=False, primary_key=True)
    cgid = Column(Integer, nullable=False, unique=True)
    label = Column(String(15))
    description = Column(String(30))


class Chartevents(Base):

    __tablename__ = "chartevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    icustay_id = Column(Integer)
    itemid = Column(Integer)
    charttime = Column(TIMESTAMP(0))
    storetime = Column(TIMESTAMP(0))
    cgid = Column(Integer)
    value = Column(String(255))
    valuenum = Column(DOUBLE_PRECISION)
    valueuom = Column(String(50))
    warning = Column(Integer)
    error = Column(Integer)
    resultstatus = Column(String(50))
    stopped = Column(String(50))


class Cptevents(Base):

    __tablename__ = "cptevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    costcenter = Column(String(10), nullable=False)
    chartdate = Column(TIMESTAMP(0))
    cpt_cd = Column(String(10), nullable=False)
    cpt_number = Column(Integer)
    cpt_suffix = Column(String(5))
    ticket_id_seq = Column(Integer)
    sectionheader = Column(String(50))
    subsectionheader = Column(String(255))
    description = Column(String(200))


class Datetimeevents(Base):

    __tablename__ = "datetimeevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    icustay_id = Column(Integer)
    itemid = Column(Integer, nullable=False)
    charttime = Column(TIMESTAMP(0), nullable=False)
    storetime = Column(TIMESTAMP(0), nullable=False)
    cgid = Column(Integer, nullable=False)
    value = Column(TIMESTAMP(0))
    valueuom = Column(String(50), nullable=False)
    warning = Column(SmallInteger)
    error = Column(SmallInteger)
    resultstatus = Column(String(50))
    stopped = Column(String(50))


class Diagnoses_icd(Base):

    __tablename__ = "diagnoses_icd"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    seq_num = Column(Integer)
    icd9_code = Column(String(10))


class Drgcodes(Base):

    __tablename__ = "drgcodes"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    drg_type = Column(String(20), nullable=False)
    drg_code = Column(String(20), nullable=False)
    description = Column(String(255))
    drg_severity = Column(SmallInteger)
    drg_mortality = Column(SmallInteger)


class D_cpt(Base):

    __tablename__ = "d_cpt"

    row_id = Column(Integer, nullable=False, primary_key=True)
    category = Column(SmallInteger, nullable=False)
    sectionrange = Column(String(100), nullable=False)
    sectionheader = Column(String(50), nullable=False)
    subsectionrange = Column(String(100), nullable=False, unique=True)
    subsectionheader = Column(String(255), nullable=False)
    codesuffix = Column(String(5))
    mincodeinsubsection = Column(Integer, nullable=False)
    maxcodeinsubsection = Column(Integer, nullable=False)


class D_icd_diagnoses(Base):

    __tablename__ = "d_icd_diagnoses"

    row_id = Column(Integer, nullable=False, primary_key=True)
    icd9_code = Column(String(10), nullable=False, unique=True)
    short_title = Column(String(50), nullable=False)
    long_title = Column(String(255), nullable=False)


class D_icd_procedures(Base):

    __tablename__ = "d_icd_procedures"

    row_id = Column(Integer, nullable=False, primary_key=True)
    icd9_code = Column(String(10), nullable=False, unique=True)
    short_title = Column(String(50), nullable=False)
    long_title = Column(String(255), nullable=False)


class D_items(Base):

    __tablename__ = "d_items"

    row_id = Column(Integer, nullable=False, primary_key=True)
    itemid = Column(Integer, nullable=False, unique=True)
    label = Column(String(200))
    abbreviation = Column(String(100))
    dbsource = Column(String(20))
    linksto = Column(String(50))
    category = Column(String(100))
    unitname = Column(String(100))
    param_type = Column(String(30))
    conceptid = Column(Integer)


class D_labitems(Base):

    __tablename__ = "d_labitems"

    row_id = Column(Integer, nullable=False, primary_key=True)
    itemid = Column(Integer, nullable=False, unique=True)
    label = Column(String(100), nullable=False)
    fluid = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    loinc_code = Column(String(100))


class Icustays(Base):

    __tablename__ = "icustays"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    icustay_id = Column(Integer, nullable=False, unique=True)
    dbsource = Column(String(20), nullable=False)
    first_careunit = Column(String(20), nullable=False)
    last_careunit = Column(String(20), nullable=False)
    first_wardid = Column(SmallInteger, nullable=False)
    last_wardid = Column(SmallInteger, nullable=False)
    intime = Column(TIMESTAMP(0), nullable=False)
    outtime = Column(TIMESTAMP(0))
    los = Column(DOUBLE_PRECISION)


class Inputevents_cv(Base):

    __tablename__ = "inputevents_cv"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    icustay_id = Column(Integer)
    charttime = Column(TIMESTAMP(0))
    itemid = Column(Integer)
    amount = Column(DOUBLE_PRECISION)
    amountuom = Column(String(30))
    rate = Column(DOUBLE_PRECISION)
    rateuom = Column(String(30))
    storetime = Column(TIMESTAMP(0))
    cgid = Column(Integer)
    orderid = Column(Integer)
    linkorderid = Column(Integer)
    stopped = Column(String(30))
    newbottle = Column(Integer)
    originalamount = Column(DOUBLE_PRECISION)
    originalamountuom = Column(String(30))
    originalroute = Column(String(30))
    originalrate = Column(DOUBLE_PRECISION)
    originalrateuom = Column(String(30))
    originalsite = Column(String(30))


class Inputevents_mv(Base):

    __tablename__ = "inputevents_mv"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    icustay_id = Column(Integer)
    starttime = Column(TIMESTAMP(0))
    endtime = Column(TIMESTAMP(0))
    itemid = Column(Integer)
    amount = Column(DOUBLE_PRECISION)
    amountuom = Column(String(30))
    rate = Column(DOUBLE_PRECISION)
    rateuom = Column(String(30))
    storetime = Column(TIMESTAMP(0))
    cgid = Column(Integer)
    orderid = Column(Integer)
    linkorderid = Column(Integer)
    ordercategoryname = Column(String(100))
    secondaryordercategoryname = Column(String(100))
    ordercomponenttypedescription = Column(String(200))
    ordercategorydescription = Column(String(50))
    patientweight = Column(DOUBLE_PRECISION)
    totalamount = Column(DOUBLE_PRECISION)
    totalamountuom = Column(String(50))
    isopenbag = Column(SmallInteger)
    continueinnextdept = Column(SmallInteger)
    cancelreason = Column(SmallInteger)
    statusdescription = Column(String(30))
    comments_editedby = Column(String(30))
    comments_canceledby = Column(String(40))
    comments_date = Column(TIMESTAMP(0))
    originalamount = Column(DOUBLE_PRECISION)
    originalrate = Column(DOUBLE_PRECISION)


class Labevents(Base):

    __tablename__ = "labevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    itemid = Column(Integer, nullable=False)
    charttime = Column(TIMESTAMP(0))
    value = Column(String(200))
    valuenum = Column(DOUBLE_PRECISION)
    valueuom = Column(String(20))
    flag = Column(String(20))


class Microbiologyevents(Base):

    __tablename__ = "microbiologyevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    chartdate = Column(TIMESTAMP(0))
    charttime = Column(TIMESTAMP(0))
    spec_itemid = Column(Integer)
    spec_type_desc = Column(String(100))
    org_itemid = Column(Integer)
    org_name = Column(String(100))
    isolate_num = Column(SmallInteger)
    ab_itemid = Column(Integer)
    ab_name = Column(String(30))
    dilution_text = Column(String(10))
    dilution_comparison = Column(String(20))
    dilution_value = Column(DOUBLE_PRECISION)
    interpretation = Column(String(5))


class Noteevents(Base):

    __tablename__ = "noteevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    chartdate = Column(TIMESTAMP(0))
    charttime = Column(TIMESTAMP(0))
    storetime = Column(TIMESTAMP(0))
    category = Column(String(50))
    description = Column(String(255))
    cgid = Column(Integer)
    iserror = Column(CHAR(1))
    text = Column(String)


class Outputevents(Base):

    __tablename__ = "outputevents"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer)
    icustay_id = Column(Integer)
    charttime = Column(TIMESTAMP(0))
    itemid = Column(Integer)
    value = Column(DOUBLE_PRECISION)
    valueuom = Column(String(30))
    storetime = Column(TIMESTAMP(0))
    cgid = Column(Integer)
    stopped = Column(String(30))
    newbottle = Column(CHAR(1))
    iserror = Column(Integer)


class Patients(Base):

    __tablename__ = "patients"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False, unique=True)
    gender = Column(String(5), nullable=False)
    dob = Column(TIMESTAMP(0), nullable=False)
    dod = Column(TIMESTAMP(0))
    dod_hosp = Column(TIMESTAMP(0))
    dod_ssn = Column(TIMESTAMP(0))
    expire_flag = Column(Integer, nullable=False)


class Prescriptions(Base):

    __tablename__ = "prescriptions"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    icustay_id = Column(Integer)
    startdate = Column(TIMESTAMP(0))
    enddate = Column(TIMESTAMP(0))
    drug_type = Column(String(100), nullable=False)
    drug = Column(String(100), nullable=False)
    drug_name_poe = Column(String(100))
    drug_name_generic = Column(String(100))
    formulary_drug_cd = Column(String(120))
    gsn = Column(String(200))
    ndc = Column(String(120))
    prod_strength = Column(String(120))
    dose_val_rx = Column(String(120))
    dose_unit_rx = Column(String(120))
    form_val_disp = Column(String(120))
    form_unit_disp = Column(String(120))
    route = Column(String(120))


class Procedureevents_mv(Base):

    __tablename__ = "procedureevents_mv"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    icustay_id = Column(Integer)
    starttime = Column(TIMESTAMP(0))
    endtime = Column(TIMESTAMP(0))
    itemid = Column(Integer)
    value = Column(DOUBLE_PRECISION)
    valueuom = Column(String(30))
    location = Column(String(30))
    locationcategory = Column(String(30))
    storetime = Column(TIMESTAMP(0))
    cgid = Column(Integer)
    orderid = Column(Integer)
    linkorderid = Column(Integer)
    ordercategoryname = Column(String(100))
    secondaryordercategoryname = Column(String(100))
    ordercategorydescription = Column(String(50))
    isopenbag = Column(SmallInteger)
    continueinnextdept = Column(SmallInteger)
    cancelreason = Column(SmallInteger)
    statusdescription = Column(String(30))
    comments_editedby = Column(String(30))
    comments_canceledby = Column(String(30))
    comments_date = Column(TIMESTAMP(0))


class Procedures_icd(Base):

    __tablename__ = "procedures_icd"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    seq_num = Column(Integer, nullable=False)
    icd9_code = Column(String(10), nullable=False)


class Services(Base):

    __tablename__ = "services"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    transfertime = Column(TIMESTAMP(0), nullable=False)
    prev_service = Column(String(20))
    curr_service = Column(String(20))


class Transfers(Base):

    __tablename__ = "transfers"

    row_id = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, nullable=False)
    hadm_id = Column(Integer, nullable=False)
    icustay_id = Column(Integer)
    dbsource = Column(String(20))
    eventtype = Column(String(20))
    prev_careunit = Column(String(20))
    curr_careunit = Column(String(20))
    prev_wardid = Column(SmallInteger)
    curr_wardid = Column(SmallInteger)
    intime = Column(TIMESTAMP(0))
    outtime = Column(TIMESTAMP(0))
    los = Column(DOUBLE_PRECISION)

