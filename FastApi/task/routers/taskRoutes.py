from fastapi import APIRouter, Request, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.db import Session
from middlewares.jwtBearer import JWTBearer
from schemas.taskSchema import Task
from services.taskServices import TaskServices as TaskService
from models.userModel import User



router = APIRouter()

@router.get('/task', tags=['Task'], response_model=List[Task], status_code=200, dependencies=[Depends(JWTBearer())])
def getTasks(request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    tasks = TaskService(Session()).getTasks(userId)
    return tasks

# Dependencia para obtener una sesión de base de datos
@router.post('/task', tags=['Task'], response_model=Task, status_code=201,  dependencies=[Depends(JWTBearer())])
def createTask(task: Task, request: Request):
    userId = TaskService(Session()).getIdCurrentUser(request)
    TaskService(Session()).createTask(task, userId)
    return JSONResponse(content={"message": "Task created successfully"}, status_code=201)




