"""Define constants for type lookup."""

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
