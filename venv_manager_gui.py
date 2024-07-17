import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QListWidget, QTextEdit, QComboBox,
                             QMessageBox, QInputDialog, QGroupBox, QSizePolicy)
from PyQt6.QtCore import Qt
from styles import apply_styles
from utils import (get_python_environments, get_environment_info,
                   create_environment, delete_environment, get_package_list,
                   delete_packages)

class VenvManagerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Virtual Environment Manager")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.create_gui_elements()
        self.connect_signals()
        self.refresh_envs()
        apply_styles(self)

    def create_gui_elements(self):
        # Environment selector section
        env_group = QGroupBox("Environment Selection")
        env_layout = QHBoxLayout()
        self.env_selector = QComboBox()
        self.refresh_button = QPushButton("Refresh")
        env_layout.addWidget(self.env_selector, 1)
        env_layout.addWidget(self.refresh_button)
        env_group.setLayout(env_layout)
        self.layout.addWidget(env_group)

        # Environment info section
        info_group = QGroupBox("Environment Information")
        info_layout = QVBoxLayout()
        self.env_info = QTextEdit()
        self.env_info.setReadOnly(True)
        self.env_info.setFixedHeight(80)  # Set a fixed height for the info box
        info_layout.addWidget(self.env_info)
        info_group.setLayout(info_layout)
        self.layout.addWidget(info_group)

        # Package list section
        package_group = QGroupBox("Installed Packages")
        package_layout = QVBoxLayout()
        self.package_list = QListWidget()
        self.package_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        package_layout.addWidget(self.package_list)
        package_group.setLayout(package_layout)
        self.layout.addWidget(package_group)

        # Action buttons section
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        self.create_button = QPushButton("Create New Env")
        self.activate_button = QPushButton("Activate Env")
        self.delete_env_button = QPushButton("Delete Env")
        self.delete_packages_button = QPushButton("Delete Packages")
        action_layout.addWidget(self.create_button)
        action_layout.addWidget(self.activate_button)
        action_layout.addWidget(self.delete_env_button)
        action_layout.addWidget(self.delete_packages_button)
        action_group.setLayout(action_layout)
        self.layout.addWidget(action_group)

        # Set size policies
        env_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        info_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        package_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        action_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

class VenvManagerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Virtual Environment Manager")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.create_gui_elements()
        self.connect_signals()
        self.refresh_envs()
        apply_styles(self)

    def create_gui_elements(self):
        # Environment selector section
        env_group = QGroupBox("Environment Selection")
        env_layout = QHBoxLayout()
        self.env_selector = QComboBox()
        self.refresh_button = QPushButton("Refresh")
        env_layout.addWidget(self.env_selector, 1)
        env_layout.addWidget(self.refresh_button)
        env_group.setLayout(env_layout)
        self.layout.addWidget(env_group)

        # Environment info section
        info_group = QGroupBox("Environment Information")
        info_layout = QVBoxLayout()
        self.env_info = QTextEdit()
        self.env_info.setReadOnly(True)
        info_layout.addWidget(self.env_info)
        info_group.setLayout(info_layout)
        self.layout.addWidget(info_group)

        # Package list section
        package_group = QGroupBox("Installed Packages")
        package_layout = QVBoxLayout()
        self.package_list = QListWidget()
        self.package_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        package_layout.addWidget(self.package_list)
        package_group.setLayout(package_layout)
        self.layout.addWidget(package_group)

        # Action buttons section
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        self.create_button = QPushButton("Create New Env")
        self.activate_button = QPushButton("Activate Env")
        self.delete_env_button = QPushButton("Delete Env")
        self.delete_packages_button = QPushButton("Delete Packages")
        action_layout.addWidget(self.create_button)
        action_layout.addWidget(self.activate_button)
        action_layout.addWidget(self.delete_env_button)
        action_layout.addWidget(self.delete_packages_button)
        action_group.setLayout(action_layout)
        self.layout.addWidget(action_group)

    def connect_signals(self):
        self.refresh_button.clicked.connect(self.refresh_envs)
        self.env_selector.currentIndexChanged.connect(self.update_env_info)
        self.create_button.clicked.connect(self.create_env)
        self.activate_button.clicked.connect(self.activate_env)
        self.delete_env_button.clicked.connect(self.delete_env)
        self.delete_packages_button.clicked.connect(self.delete_packages)

    def refresh_envs(self):
        self.env_selector.clear()
        environments = get_python_environments()
        for env in environments:
            self.env_selector.addItem(env['name'], env['path'])

    def update_env_info(self):
        path = self.env_selector.currentData()
        if path:
            info = get_environment_info(path)
            self.env_info.setText(info)
            self.update_package_list(path)

    def update_package_list(self, python_path):
        self.package_list.clear()
        packages = get_package_list(python_path)
        self.package_list.addItems(packages)

    def create_env(self):
        version, ok = QInputDialog.getText(self, "Create Environment", "Enter Python version (e.g., 3.9.0):")
        if ok and version:
            name, ok = QInputDialog.getText(self, "Create Environment", "Enter environment name:")
            if ok and name:
                result = create_environment(version, name)
                if result['success']:
                    QMessageBox.information(self, "Success", result['message'])
                    self.refresh_envs()
                else:
                    QMessageBox.critical(self, "Error", result['message'])

    def activate_env(self):
        path = self.env_selector.currentData()
        if path:
            activate_script = os.path.join(os.path.dirname(path), "activate")
            QMessageBox.information(self, "Activate Environment", 
                                    f"To activate this environment, run:\n\nsource {activate_script}")

    def delete_env(self):
        path = self.env_selector.currentData()
        if path:
            reply = QMessageBox.question(self, "Confirm Deletion", 
                                         "Are you sure you want to delete this environment?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                result = delete_environment(path)
                if result['success']:
                    QMessageBox.information(self, "Success", result['message'])
                    self.refresh_envs()
                else:
                    QMessageBox.critical(self, "Error", result['message'])

    def delete_packages(self):
        path = self.env_selector.currentData()
        if path:
            selected_packages = [item.text().split('==')[0] for item in self.package_list.selectedItems()]
            if selected_packages:
                result = delete_packages(path, selected_packages)
                if result['success']:
                    QMessageBox.information(self, "Success", result['message'])
                    self.update_package_list(path)
                else:
                    QMessageBox.critical(self, "Error", result['message'])
            else:
                QMessageBox.warning(self, "Warning", "No packages selected")