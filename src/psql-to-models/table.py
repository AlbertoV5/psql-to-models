"""
Table representation and processor.

Call any get_* functions before calling make_* functions.
"""
from dataclasses import dataclass
from .column import Column


@dataclass
class Table:
    name: str
    columns: list[Column]

    @classmethod
    def from_string(cls, table: str) -> "Table":
        """Create Table from string."""
        data = table.split("\n")
        return Table(
            name=data[0].strip(), columns=[Column.from_string(col) for col in data[2:-1]]
        )

    def get_constraints(self) -> None:
        """Use the CONSTRAINT columns to modify the rest of the columns."""
        constraints = [col.params for col in self.columns if col.name == "CONSTRAINT"]
        data = [c.replace(")", "").split("(") for c in constraints]
        d_data = {}
        for statement in data:
            statement = [s.strip() for s in statement]
            if len(statement) <= 2:
                d_data[statement[1]] = [statement[0]]
            else:
                ref = statement[1].replace(" REFERENCES ", " ").split(" ")
                d_data[statement[2]] = [statement[0], f"{ref[1]}.{ref[0]}"]
        # print(d_data)
        for column in self.columns:
            for k in d_data:
                if column.name == k:
                    column.primary_key = (
                        "primary_key=True" if d_data[k][0] == "PRIMARY KEY" else ""
                    )
                    column.unique = "unique=True" if d_data[k][0] == "UNIQUE" else ""
                    column.foreign_key = (
                        f'ForeignKey("{d_data[k][1]}")' if d_data[k][0] == "FOREIGN KEY" else ""
                    )

    def make_alchemy(self) -> str:
        """Make SQLAlchemy model string from this Table."""
        cols = "\n    ".join(
            col.make_alchemy_column()
            for col in self.columns
            if col.name != "CONSTRAINT"
        )
        return (
            f"class {self.name.capitalize()}(Base):\n\n"
            f'    __tablename__ = "{self.name.lower()}"\n\n'
            f"    {cols}\n\n"
        )

    def make_pydantic(self) -> str:
        """Make Pydantic model string from this Table."""
        params = "\n    ".join(
            col.make_pydantic_column()
            for col in self.columns
            if col.name != "CONSTRAINT"
        )
        return (
            f"class {self.name.capitalize()}(BaseModel):\n\n"
            f"    {params}\n\n"
            f"    class Config:\n"
            f"        orm_mode = True\n\n"
        )
