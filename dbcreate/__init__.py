"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from dbcreate.db to dbcreate)
from dbcreate.db import hello as hello

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'hello',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'db',
    'settings',
]

# A series of return and error codes
(
    SUCCESS,
    DIR_ERROR,
    DB_CONNECT_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
) = range(7)

# Maps error codes to human-readable error messages
ERRORS = {
    DIR_ERROR: "config directory error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    DB_CONNECT_ERROR: "database connect error",
}
