"""The primary module in dbcreate."""

# Imports
import typer
from enum import Enum

app = typer.Typer()

class Databases(str, Enum):
    PostgreSQL = "PostgreSQL"


