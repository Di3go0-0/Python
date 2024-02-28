from schemas.taskSchema import Task as TaskSchema
from models.taskModel import Task as TaskModel
from fastapi import Request
from utils.jwt import validateToken

class TaskServices:
    def __init__(self, db) -> None:
        self.db = db
        
    def getTasks(self, userId: int):
        tasks = self.db.query(TaskModel).filter(TaskModel.userId == userId).all()
        return tasks
    
    def getTask(self,taskId:id, userId: id):
        task = self.db.query(TaskModel).filter(TaskModel.id == taskId, TaskModel.userId == userId).first()
        if task:
            return task
        return None
    
    def getTaskDone(self, userId: int):
        tasks = self.db.query(TaskModel).filter(TaskModel.userId == userId, TaskModel.done == True).all()
        return tasks
    
    def getTaskNotDone(self, userId: int):
        tasks = self.db.query(TaskModel).filter(TaskModel.userId == userId, TaskModel.done == False).all()
        return tasks
    
    def doneTask(self, taskId: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == taskId).first()
        if task:
            task.done = True
            self.db.commit()
            self.db.refresh(task)
        return task 
    
    def getIdCurrentUser(self, request: Request):
        token = request.cookies.get('token')
        if token:
            tokenData = validateToken(token)
            return tokenData['id']
        return None

    def createTask(self, task: TaskSchema, userId: int):
        task.userId = userId
        # new_task = TaskModel(**task.model_dump(), userId=int(userId))
        newTask = TaskModel(**task.model_dump())
        self.db.add(newTask)
        self.db.commit()
        self.db.refresh(newTask)
        return newTask
    
    def updateTask(self, taskId: int, task: TaskSchema):
        taskToUpdate = self.db.query(TaskModel).filter(TaskModel.id == taskId).first()
        if taskToUpdate:
            taskToUpdate.title = task.title
            taskToUpdate.description = task.description
            self.db.commit()
            self.db.refresh(taskToUpdate)
            return taskToUpdate
        return None
    
    def deleteTask(self, taskId: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == taskId).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return task
        return None
        