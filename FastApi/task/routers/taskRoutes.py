from fastapi import APIRouter, Request, Response, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.db import Session
from middlewares.jwtBearer import JWTBearer
from schemas.taskSchema import Task
from services.taskServices import TaskServices as TaskService
from models.userModel import User
from utils.jwt import validateToken



router = APIRouter()

@router.get('/task', tags=['Task'], response_model=List[Task], status_code=200, dependencies=[Depends(JWTBearer())])
def getTasks(request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    print(userId)
    tasks = TaskService(Session()).getTasks(userId)
    return tasks


@router.get('/task/{taskId}', tags=['Task'], response_model=Task, status_code=200, dependencies=[Depends(JWTBearer())])
def getTaskById(taskId: int, request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    task = TaskService(Session()).getTask(taskId, userId)
    if task:
        return task
    return JSONResponse(content={"message": "task not found or does not belong to you"}, status_code=404)

@router.get('/taskDone', tags=['Task'], response_model=List[Task], status_code=200, dependencies=[Depends(JWTBearer())])
def getTaskDone(request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    if userId is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    tasks = TaskService(Session()).getTaskDone(userId)
    return tasks

@router.get('/taskNotDone', tags=['Task'], response_model=List[Task], status_code=200, dependencies=[Depends(JWTBearer())])
def getTaskNotDone(request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    if userId is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    tasks = TaskService(Session()).getTaskNotDone(userId)
    return tasks

@router.post('/task/{taskId}', tags=['Task'], status_code=200, dependencies=[Depends(JWTBearer())])
def doneTask(taskId: int):
    task = TaskService(Session()).doneTask(taskId)
    return JSONResponse(content={"message": "Task done successfully"}, status_code=200)


# Dependencia para obtener una sesión de base de datos
@router.post('/task', tags=['Task'], response_model=Task, status_code=201,  dependencies=[Depends(JWTBearer())])
def createTask(task: Task, request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    TaskService(Session()).createTask(task, userId)
    return JSONResponse(content={"message": "Task created successfully"}, status_code=201)

@router.put('/task/{taskId}', tags=['Task'], response_model=Task, status_code=200,  dependencies=[Depends(JWTBearer())])
def updateTaskById(taskId: int, task: Task):
    task = TaskService(Session()).updateTask(taskId, task)
    return JSONResponse(content={"message": "Task updated successfully"}, status_code=200)

@router.delete('/task/{taskId}', tags=['Task'], status_code=200,  dependencies=[Depends(JWTBearer())])
def deleteTaskById(taskId: int, request: Request):
    UserId = TaskService(Session()).getIdCurrentUser(request)
    task = TaskService(Session()).getTask(taskId, UserId)
    if not task:
        return JSONResponse(content={"message": "Task not found or does not belong to you"}, status_code=404)
    TaskService(Session()).deleteTask(taskId)
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)



