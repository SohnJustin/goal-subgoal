# Form implementation generated from reading ui file 'secondwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_completedTask(object):
    def setupUi(self, completedTask):
        completedTask.setObjectName("completedTask")
        completedTask.resize(1470, 920)
        self.completedGoal_label = QtWidgets.QLabel(completedTask)
        self.completedGoal_label.setGeometry(QtCore.QRect(610, 130, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.completedGoal_label.setFont(font)
        self.completedGoal_label.setObjectName("completedGoal_label")
        self.completedGoal_listWidget = QtWidgets.QListWidget(completedTask)
        self.completedGoal_listWidget.setGeometry(QtCore.QRect(250, 230, 931, 611))
        self.completedGoal_listWidget.setObjectName("completedGoal_listWidget")

        self.retranslateUi(completedTask)
        QtCore.QMetaObject.connectSlotsByName(completedTask)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("completedTask", "Dialog"))
        self.completedGoal_label.setText(_translate("completedTask", "Completed Goal(s)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    completedTask = QtWidgets.QDialog()
    ui = Ui_completedTask()
    ui.setupUi(completedTask)
    completedTask.show()
    sys.exit(app.exec())
