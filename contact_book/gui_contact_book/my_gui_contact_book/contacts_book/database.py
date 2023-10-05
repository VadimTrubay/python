__author__ = 'VadimTrubay'

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    """Create the contacts table in the database."""
    create_table_query = QSqlQuery()
    return create_table_query.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            first name VARCHAR(40),
            last name VARCHAR(40),
            phone INT(15),
            email VARCHAR(40),
            note VARCHAR(100)
                   )
        """
    )


def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createContactsTable()
    return True
