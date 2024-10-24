import uuid, json
from datetime import datetime

class TaskManager:
  def __init__(self):
    # Load data from JSON on initial
    self.loadTask()

  def addTask(self, name:str="", description:str="", cli:bool=False):
    '''
    name: string - Task name.
    description: string - Task description.
    cli:bool - If true will run this method in cli mode.
    '''

    # Generate unique task id
    taskId = int(str(uuid.uuid4().int)[:6])

    # Check cli parameter
    if cli:
      name = input("input task's name: ")
      description = input("input task's description: ")
    if not cli and not name and not description:
      raise Exception("Please provide name and description for task.")
    
    self.tasks.append({
      "id": taskId,
      "name": name,
      "description": description,
      "started date": datetime.now().strftime("%d/%m/%Y"),
      "completed date": "-",
      "status": "Waiting"
    })
    self.saveTask()

    # Recheck added task
    isSuccess = False
    for task in self.tasks:
      if task["id"] == taskId:
        print("Add task success!")
        print(task)
        isSuccess = True
        break
    if not isSuccess:
      print("Add task not success!!!")

  def viewTask(self):
    # Return all task in details
    for task in self.tasks:
      print(task)

  def completedTask(self, taskId:int="", cli:bool=False):
    '''
    taskId: int - Task ID.
    cli:bool - If true will run this method in cli mode.
    '''

    # Check cli parramter
    if cli:
      taskId = int(input("input task's id: "))
    if not cli and not taskId:
      raise Exception("Please provide task's id.")
    
    # Loop over tasks to find the match task id, then complete that task
    for task in self.tasks:
      if task["id"] == taskId:
        task["completed date"] = datetime.now().strftime("%d/%m/%Y")
        task["status"] = "Completed"
        self.saveTask()
        break

    # Recheck task complete yet
    isSuccess = False
    for task in self.tasks:
      if task["id"] == taskId and task["status"] == "Completed":
        print("Task Completed!")
        print(task)
        isSuccess = True
        break
    if not isSuccess:
      print("Task not found!!!")

  def deleteTask(self, taskId:int="", cli:bool=False):
    '''
    taskId: int - Task ID.
    cli:bool - If true will run this method in cli mode.
    '''
    
    # Check cli parameter
    if cli:
      taskId = int(input("input task's id: "))
    if not cli and not taskId:
      raise Exception("Please provide task's id.")
    
    # iterate over range of tasks list length to find the match task's id, then delete it from tasks list
    for i in range(len(self.tasks)):
      if self.tasks[i]["id"] == taskId:
        self.tasks.pop(i)
        self.saveTask()
        break

    # Recheck task deleted yet
    for task in self.tasks:
      if task["id"] == taskId:
        print("Task delete not success!!!")
        break
    print("Task deleted!")
    self.viewTask()

  def loadTask(self):
    # open JSON file with 'read' mode, then assign json data to tasks variable
    with open('sample.json', 'r') as openfile:
      self.tasks = json.load(openfile)
    print("Tasks are Loaded")

  def saveTask(self):
    # open JSON file with 'write' mode, then assign tasks data to JSON file
    with open("sample.json", "w") as outfile:
      outfile.write(json.dumps(self.tasks, indent=2))
    print("Tasks are saved into JSON file.")

  def findTask(self, wordToFind:str="", cli:bool=False):
    '''
    wordToFind: str - Word that you want to find in tasks.
    cli:bool - If true will run this method in cli mode.
    '''
    
    if cli:
      wordToFind = input("input word to find: ")

    results = [] # for keep founded result

    # loop over range of tasks length
    for i in range(len(self.tasks)):
      # loop over dict value of current task
      for value in self.tasks[i].values():
        # if found result, will add it to 'results' list
        if str(value).find(wordToFind) >= 0:
          results.append(self.tasks[i])
          break
    
    # print results
    print(f"Found {len(results)} result{"s"*bool(len(results))}.")
    for result in results:
      print(result)
  
  def run(self):
    # this method use for run in cli mode only!
    print("Hi there, welcome to Task Management Program")
    while True:
      print("Please enter name of available functionality to use it:")
      print("[0] - addTask")
      print("[1] - viewTask")
      print("[2] - completedTask")
      print("[3] - deleteTask")
      print("[4] - loadTask")
      print("[5] - saveTask")
      print("[6] - findTask")
      print("[q] - quit")
      userInput = input("Which function do you want? (0-6): ")
      if userInput == 'q':
        break
      userInput = int(userInput)
      if userInput == 0:
        self.addTask(cli=True)
      elif userInput == 1:
        self.viewTask()
      elif userInput == 2:
        self.completedTask(cli=True)
      elif userInput == 3:
        self.deleteTask(cli=True)
      elif userInput == 4:
        self.loadTask()
      elif userInput == 5:
        self.saveTask()
      elif userInput == 6:
        self.findTask(cli=True)
      else:
        print("Please input only integer and must be 0-6")

taskManager = TaskManager()
taskManager.run()