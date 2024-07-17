import sys
from PyQt6.QtWidgets import QApplication
from venv_manager_gui import VenvManagerGUI

def main():
    app = QApplication(sys.argv)
    window = VenvManagerGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()