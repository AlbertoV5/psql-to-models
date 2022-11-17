"""
Column representation and processor.
"""
from dataclasses import dataclass
from .types import TYPE_LOOKUP


@dataclass
class Column:
    name: str
    type: str
    params: str
    primary_key: str = ""
    unique: str = ""

    @classmethod
    def from_string(cls, col: str) -> "Column":
        """Create column from string."""
        data = col.strip().replace(",", "").split(" ", maxsplit=2)
        return Column(
            name=data[0], type=data[1], params=data[2] if len(data) > 2 else ""
        )

    def get_type(self, sqlalchemy: bool = True) -> str:
        """
        Lookup types and return either SQLAlchemy's or Pydantic's.
        """
        t = self.type.replace(")", "").split("(")
        index = 0 if sqlalchemy else 1
        if len(t) > 1:
            return (
                f"{TYPE_LOOKUP[t[0]][index]}({t[1]})"
                if sqlalchemy
                else TYPE_LOOKUP[t[0]][index]
            )
        return TYPE_LOOKUP[self.type][index]

    def make_alchemy_column(self) -> str:
        """Make SQLAlchemy Model column string."""
        return (
            f"{self.name.lower()} = Column("
            f"{self.get_type()}"
            f"{', nullable=False' if 'NOT NULL' in self.params else ''}"
            f"{'' if self.primary_key == '' else f', {self.primary_key}'}"
            f"{'' if self.unique == '' else f', {self.unique}'}"
            f")"
        )

    def make_pydantic_column(self) -> str:
        """Make Pydantic Model column string."""
        return (
            f"{self.name.lower()}: "
            f"{self.get_type(sqlalchemy=False)}"
            f"{'' if 'NOT NULL' in self.params else ' | None'}"
        )
