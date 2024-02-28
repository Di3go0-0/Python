from fastapi import APIRouter, Depends, Response # Importamos la clase APIRouter para crear rutas
from utils.jwt import createToken # Importamos la función createToken del archivo jwt.py
from fastapi.responses import JSONResponse
from schemas.userSchema import User
from config.db import Session
from services.authServices import AuthService
from middlewares.jwtBearer import JWTBearer
from services.taskServices import TaskServices




router = APIRouter() # Creamos una instancia de la clase APIRouter

userLogueado = None


@router.post('/register', tags=['Auth'], response_model=dict, status_code=201)
def register(user: User) -> dict:
    AuthService(Session()).register(user)
    return JSONResponse(content={"message": "User created successfully"}, status_code=201)

@router.post('/login', tags=['Auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    result = AuthService(Session()).login(user.email, user.password)
    if not result:
        return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
    token = createToken(result)
    response = JSONResponse(content={"message": "Login successful"}, status_code=200)
    response.set_cookie(key="token", value=f"{token}", httponly=True)
    return response


@router.post('/logout', tags=['Auth'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def logout(token: str) -> dict:
    AuthService(Session()).logout(token)
    return JSONResponse(content={"message": "Logout successfully"}, status_code=200)


@router.delete("/user/{id}", tags=['Auth'], response_model=dict)
def deleteUser(id: int) -> dict:
    TaskServices(Session()).deleteAllTaskByUserId(id)
    result = AuthService(Session()).deleteUser(id)
    if not result:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)


@router.get('/user/{id}', tags=['Auth'], response_model=User)
def getUser(id: int) -> User:
    result = AuthService(Session()).getUser(id)
    if not result:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return result