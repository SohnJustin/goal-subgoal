# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

import sys
from database.database import DatabaseClass
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit, QMessageBox, QListView
from PyQt6.uic import loadUi
from PySide6 import QtCore, QtWidgets, QtGui
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



class GUI(QDialog):
  def __init__(self):
    super(GUI,self).__init__()
    loadUi("window.ui",self)
    self.addGoalButton.clicked.connect(self.addGoalFunction)
    self.removeGoalButton.clicked.connect(self.removeGoalFunction)
    self.importButton.clicked.connect(self.importGoalFunctionality)
    self.exportButton.clicked.connect(self.exportGoalFunctionality)
    self.taskDB = DatabaseClass()

  def addsPresetGoals(self):
    l = self.taskDB.listDB()
    for x in l:
      self.goalList_Widget.addItem(x)

  def addGoalFunction(self):
    #Typing in the Textbox and clicking add button to add to the List
    task = self.goalInputBox.toPlainText()
    self.goalInputBox.setPlainText(task)
    self.goalList_Widget.addItem(task)
    self.goalInputBox.clear()
    task_id = int(self.taskDB.highestTaskID()) + 1
    status = 0
    start_date = "10/30/22" # change to input later
    end_date = "11/30/22" # change to input later
    params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
    self.taskDB.addTask(params)

  def removeGoalFunction(self):
    #clicking on the Goal and clicking the remove button
    try:
      clicked = self.goalList_Widget.currentRow()
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      self.goalList_Widget.takeItem(clicked)
      task_id = self.taskDB.findTaskID(task)
      if(task_id):
        self.taskDB.removeTask(task_id)
    except IndexError:
      print("error")
      # msg = QMessageBox()
      # msg.setIcon(QMessageBox.critical())
      # msg.setText("Error")
      # msg.setInformativeText('More information')
      # msg.setWindowTitle("Error")
      # msg.setStandartaskDButtons(QMessageBox.Ok | QMessageBox.Cancel)
  
  def messageboxCreate(self, winTitle, genText):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.setText(winTitle)
    msg.setInformativeText(genText)
    msg.setWindowTitle(winTitle)
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    returnValue = msg.exec()

  # Imports text file and creates goals
  def importGoalFunctionality(self):
    # import from local system. CURRENTLY WONT READ FILE AFTER
    
    filepath = "Goals.txt"
    goalsFile = open(filepath , 'r')
    #print(goalsFile.readline())
    status = 0
    start_date = "10/30/22" # change to input later
    end_date = "11/30/22" # change to input later
    for task in goalsFile:
      task_id = int(self.taskDB.highestTaskID()) + 1
      params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
      self.taskDB.addTask(params)
    self.goalList_Widget.clear()
    self.addsPresetGoals()
    self.messageboxCreate("Import Completed", "Goals file has been imported.")

  # Exports goal into a text file 
  def exportGoalFunctionality(self):

    try:
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      with open('outputtedTask.txt', 'w') as f:
          f.write(task)
          print("Exported Task")
      self.messageboxCreate("Export Completed", "Task has been exported.")
    
    except IndexError:
      self.messageboxCreate("Export Error", "Error: Select a goal before clicking export")      
      print("Error: Select a goal before clicking export")
    

    # reminders
    # get to display messagebox based off deadline coming up 
    # or text message appearing at bottom


def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(600, 500)
  widget.addsPresetGoals()
  widget.show()

  sys.exit(app.exec())
if __name__ == "__main__":
  main()
