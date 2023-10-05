__author__ = 'VadimTrubay'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.clearAllButton = None
        self.deleteButton = None
        self.addButton = None
        self.table = None
        self.setWindowTitle("Contacts book")
        self.resize(900, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContacts)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContact(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        message_box = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message_box == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)

    def clearContacts(self):
        """Remove all contacts from the database."""
        message_box = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message_box == QMessageBox.Ok:
            self.contactsModel.clearContacts()


class AddDialog(QDialog):
    """Add Contact dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.note_field = None
        self.email_field = None
        self.phone_field = None
        self.last_name_field = None
        self.first_name_field = None
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI."""
        # Create line edits for data fields
        self.first_name_field = QLineEdit()
        self.first_name_field.setObjectName("first_name")
        self.last_name_field = QLineEdit()
        self.last_name_field.setObjectName("last_name")
        self.phone_field = QLineEdit()
        self.phone_field.setObjectName("phone")
        self.email_field = QLineEdit()
        self.email_field.setObjectName("email")
        self.note_field = QLineEdit()
        self.note_field.setObjectName("note")
        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("first_name:", self.first_name_field)
        layout.addRow("last_name:", self.last_name_field)
        layout.addRow("phone:", self.phone_field)
        layout.addRow("email:", self.email_field)
        layout.addRow("note:", self.note_field)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.first_name_field, self.last_name_field, self.phone_field, self.email_field, self.note_field):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        super().accept()
