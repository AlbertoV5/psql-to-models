# PSQL TO MODELS

Use regex patterns to match PostgreSQL schemas and output SQLAlchemy and Pydantic Models. 

Designed for FastAPI.

## Install

Requires Python 3.10.

```shell
git clone git@github.com:AlbertoV5/psql-to-models.git
```

```shell
cd psql-to-models
```
Install in editable mode.
```shell
pip install -e .
```

## Usage

```shell
python -m psql-to-models
```
Before.
```shell
schema.sql
```
After.
```shell
models_alchemy.py	schema.sql
models_pydantic.py
```

## Results Example

SQL Input
```sql
DROP TABLE IF EXISTS DATETIMEEVENTS CASCADE;
CREATE TABLE DATETIMEEVENTS
(
  ROW_ID INT NOT NULL,
	SUBJECT_ID INT NOT NULL,
	HADM_ID INT,
	ICUSTAY_ID INT,
	ITEMID INT NOT NULL,
	CHARTTIME TIMESTAMP(0) NOT NULL,
	STORETIME TIMESTAMP(0) NOT NULL,
	CGID INT NOT NULL,
	VALUE TIMESTAMP(0),
	VALUEUOM VARCHAR(50) NOT NULL,
	WARNING SMALLINT,
	ERROR SMALLINT,
	RESULTSTATUS VARCHAR(50),
	STOPPED VARCHAR(50),
	CONSTRAINT datetime_rowid_pk PRIMARY KEY (ROW_ID)
) ;

DROP TABLE IF EXISTS DIAGNOSES_ICD CASCADE;
CREATE TABLE DIAGNOSES_ICD
(
  ROW_ID INT NOT NULL,
	SUBJECT_ID INT NOT NULL,
	HADM_ID INT NOT NULL,
	SEQ_NUM INT,
	ICD9_CODE VARCHAR(10),
	CONSTRAINT diagnosesicd_rowid_pk PRIMARY KEY (ROW_ID)
) ;
```
SQLALchemy Output

```python
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
```

Pydantic Output

```python
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
```

## Supported Queries

```sql
CREATE TABLE *
```

```sql
NOT NULL
```

```sql
CONSTRAINT UNIQUE
CONSTRAINT PRIMARY KEY
```

## Constants

Make sure to edit the header constants under __ main __.py

```python
ALCHEMY_HEADER = '''"""
SQLAlchemy Models
"""
from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP, SmallInteger
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from db.setup import Base

'''
```

You can always extend the supported types by editing the TYPE_LOOKUP dict in the types.py file.

```python
TYPE_LOOKUP: dict[str, tuple[str, str]] = {
    "INT": ("Integer", "int"),
    "SMALLINT": ("SmallInteger", "int"),
    "VARCHAR": ("String", "str"),
    "TIMESTAMP": ("TIMESTAMP", "datetime"),
    "DOUBLE": ("DOUBLE_PRECISION", "float"),
    "CHAR": ("CHAR", "str"),
    "TEXT": ("String", "str"),
}
"""Values are tuples of SQLAlchemy Model Type and Pydantic/Python Type."""
```

## Notes

- This utility is meant to be modified to match every case that's why the installation is in editable mode.
- The __ main __ .py file contains all the necessary logic and header configs.
- The types.py file contains a lookup table for the postgresql -> models type lookup.
- The header assumes a path for the SQLAlchemy Base so make sure to change it to match yours, etc.

## Plans

- A more robust tool can be created which uses .toml files (or whatever) for configuration instead of python files so there is no need for editable installation.
- The applications are Postgresql schemas with FastAPI but the tool can be generalized even further to support different types for other RDMS and frameworks.
- I'll add support for more queries as I find them in my day-to-day work but feel free to contribute!
