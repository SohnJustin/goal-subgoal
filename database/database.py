# database.py
from datetime import date
import sqlite_utils

class DatabaseClass():
  def __init__(self):
    super().__init__()
    self.tableName = "tasks"
    self.db = sqlite_utils.Database("./database/tasks.db")
    self.table = self.db.table(self.tableName, pk="task_id", 
    columns={"task_id": int, "start_date": date, "end_date": date, "status": bool},
    column_order=("task_id","task","start_date","end_date","status"))

# checks the table to see if it exsits
  def checkTable(self, params):
    if type(params) is dict:
      self.count = self.table.count_where("task_id = " + str(params.get("task_id")))
    else:
      self.count = self.table.count_where("task_id = " + str(params))
    if self.count > 0:
      return True
    return False

# outputs the entire database
  def outputDB(self):
    for row in self.db.query("SELECT * FROM " + self.tableName):
      print(row)

# get list of database
  def listDB(self):
    l = []
    for row in self.db.query("SELECT * FROM " + self.tableName):
      l.append(row["task"])
    return l
    
# adds task to database after checking it exists or not
  def addTask(self, params):
    if not self.checkTable(params):
      self.table.insert(params)
      print("Added")
      self.outputDB()

# removes the task
  def removeTask(self, params):
    try:
      if self.checkTable(params):
        self.table.delete(params)
        print("Deleted")
        self.outputDB()
    except:
      print("error in removeTask")

# find highest task_id
  def highestTaskID(self):
    cur = self.db.execute("SELECT MAX(task_id) FROM tasks").fetchall()
    highestID = cur[0][0]
    return highestID

  def findTaskID(self, task):
    # self.outputDB()
    cur = self.db.execute("SELECT task_id FROM tasks WHERE task = ?", [task]).fetchall()
    if cur:
      task_id = int(cur[0][0])
      return task_id