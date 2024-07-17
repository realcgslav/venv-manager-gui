from PyQt6.QtWidgets import QStyleFactory
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

def apply_styles(widget):
    widget.setStyle(QStyleFactory.create("Fusion"))
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    widget.setPalette(palette)

    widget.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QGroupBox {
        border: 1px solid #555555;
        border-radius: 5px;
        margin-top: 0.5em;
        font-weight: bold;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    QPushButton {
        background-color: #3a3a3a;
        border: 1px solid #555555;
        padding: 5px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #454545;
    }
    QPushButton:pressed {
        background-color: #2a2a2a;
    }
    QComboBox {
        background-color: #3a3a3a;
        border: 1px solid #555555;
        border-radius: 3px;
        padding: 1px 18px 1px 3px;
        color: #ffffff;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left-width: 1px;
        border-left-color: #555555;
        border-left-style: solid;
    }
    QComboBox QAbstractItemView {
        background-color: #2b2b2b;
        border: 1px solid #555555;
        selection-background-color: #3a3a3a;
    }
    QTextEdit, QListWidget {
        background-color: #1e1e1e;
        border: 1px solid #555555;
        color: #ffffff;
    }
    """)