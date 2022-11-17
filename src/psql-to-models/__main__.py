"""
This script will read the postgres_create_tables.sql file from MIMIC and
generate python files for the sqlalchemy models and pydantic schemas for the API.
"""
from typing import Generator, Protocol
from argparse import ArgumentParser
from pathlib import Path
import re

from .table import Table


ALCHEMY_HEADER = '''"""
SQLAlchemy Models
"""
from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP, SmallInteger
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from db.setup import Base

'''

PYDANTIC_HEADER = '''"""
Pydantic Models
"""
from pydantic import BaseModel
from datetime import datetime

'''

BANNED_TABLES = ["chartevents_"]


class Arguments(Protocol):
    input: str
    alchemy: str
    pydantic: str


def is_valid(table: Table) -> bool:
    """Whether table is in banned tables or not."""
    for banned in BANNED_TABLES:
        if banned in table.name:
            return False
    return True


def generate_strings(tables: list[Table]) -> Generator[tuple[str, str], None, None]:
    """Yields SQLAlchemy and Pydantic Models as strings for each table."""
    for table in tables:
        table.get_constraints()
        alchemy = f"\n{table.make_alchemy()}" if is_valid(table) else ""
        pydantic = f"\n{table.make_pydantic()}" if is_valid(table) else ""
        yield alchemy, pydantic


def main(argv: Arguments):
    """Read .sql file with CREATE TABLE queries and store models."""
    # Input
    with open(Path(argv.input).resolve()) as file:
        sql_string = file.read()
    # Pattern Matching
    pattern = r"(?:CREATE TABLE )((.|\n)*?);"
    tables: list[Table] = [
        Table.from_string(table[0]) for table in re.findall(pattern, sql_string)
    ]
    # String Processing
    alchemy_data = ALCHEMY_HEADER
    pydantic_data = PYDANTIC_HEADER
    for model, pydantic in generate_strings(tables):
        alchemy_data += model
        pydantic_data += pydantic
    # Output
    with open(Path(argv.alchemy).resolve(), "w") as file:
        file.write(alchemy_data)
    with open(Path(argv.pydantic).resolve(), "w") as file:
        file.write(pydantic_data)


if __name__ == "__main__":
    default_sql_input = "./schema.sql"
    default_alchemy_output = "./models_alchemy.py"
    default_pydantic_output = "./models_pydantic.py"
    args = ArgumentParser(
        prog="Convert PostgreSQL schema to SQLAlchemy and Pydantic Models.",
        usage=f"python -m psql-to-models",
        description="Regex-match the .sql schema file and outputs SQLAlchemy and Pydantic models as .py files.",
    )
    args.add_argument(
        "-i",
        "--input",
        metavar="input",
        default=f"{default_sql_input}",
        help=f"PostgreSQL Schema input file. Defaults to {default_sql_input}.",
    )
    args.add_argument(
        "-a",
        "--alchemy",
        metavar="output_alchemy",
        default=f"{default_alchemy_output}",
        help=f"SQLAlchemy Models output. Defaults to {default_alchemy_output}",
    )
    args.add_argument(
        "-p",
        "--pydantic",
        metavar="output_pydantic",
        default=f"{default_pydantic_output}",
        help=f"Pydantic Models output. Defaults to {default_alchemy_output}",
    )
    main(args.parse_args())
