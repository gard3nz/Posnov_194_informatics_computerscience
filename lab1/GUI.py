import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from crud_interface import Ui_MainWindow  # Импортируем сгенерированный UI-код
from models import setup_database, create_session, Customer  # Импортируем ORM
from main_2 import add_customer, get_customer_by_id, get_all_customers, delete_customer, update_customer_name, get_customers_by_state

# Инициализация базы данных
engine = setup_database("sqlite:///customer.sqlite")
session = create_session(engine)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключение кнопок к функциям
        self.ui.pushButton.clicked.connect(self.add_customer)
        self.ui.pushButton_2.clicked.connect(self.find_customer_by_id)
        self.ui.pushButton_3.clicked.connect(self.find_customers_by_state)
        self.ui.pushButton_4.clicked.connect(self.update_customer_name)
        self.ui.pushButton_5.clicked.connect(self.delete_customer)
        self.ui.pushButton_6.clicked.connect(self.show_all_customers)

    def add_customer(self):
        try:
            customer_id = add_customer(
                Id=self.ui.lineEdit.text(),
                fname=self.ui.lineEdit_2.text(),
                lname=self.ui.lineEdit_3.text(),
                db=self.ui.lineEdit_4.text(),
                cty=self.ui.lineEdit_5.text(),
                stte=self.ui.lineEdit_6.text(),
                zp=self.ui.lineEdit_7.text()
            )
            QMessageBox.information(self, "Success", f"Customer added with ID: {customer_id}")
            self.show_all_customers()  # Обновляем таблицу
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def find_customer_by_id(self):
        customer_id = self.ui.lineEdit.text()
        customer = get_customer_by_id(customer_id)
        if customer:
            QMessageBox.information(self, "Success", f"Customer found: {customer.first_name} {customer.last_name}")
        else:
            QMessageBox.information(self, "Not Found", f"Customer with ID {customer_id} not found.")

    def find_customers_by_state(self):
        state = self.ui.lineEdit_6.text()
        customers = get_customers_by_state(state)
        if customers:
            QMessageBox.information(self, "Success", f"Customers in state {state}:\n" + "\n".join([f"{c.id}: {c.first_name} {c.last_name}" for c in customers]))
        else:
            QMessageBox.information(self, "Not Found", f"No customers found in state {state}.")

    def update_customer_name(self):
        customer_id = self.ui.lineEdit.text()
        new_name = self.ui.lineEdit_2.text()
        customer = update_customer_name(customer_id, new_name)
        if customer:
            QMessageBox.information(self, "Success", f"Customer ID {customer_id} updated to '{new_name}'")
            self.show_all_customers()  # Обновляем таблицу
        else:
            QMessageBox.information(self, "Not Found", f"Customer with ID {customer_id} not found.")

    def delete_customer(self):
        customer_id = self.ui.lineEdit.text()
        delete_customer(customer_id)
        QMessageBox.information(self, "Success", f"Customer ID {customer_id} deleted.")
        self.show_all_customers()  # Обновляем таблицу

    def show_all_customers(self):
        # Очищаем таблицу
        self.ui.tableWidget.setRowCount(0)

        # Заполняем таблицу данными
        customers = get_all_customers()
        for customer in customers:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(customer.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(customer.first_name))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(customer.last_name))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(customer.dob))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(customer.city))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(customer.state))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(customer.zip))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())