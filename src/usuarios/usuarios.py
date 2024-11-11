# Libraries Imports
from typing_extensions import Annotated
from fastapi import APIRouter, Body, Header

#Project Imports
from utils.models import Usuario, Headers
from utils.logUtil import log
from usuarios.usuarios_methods import read_db, get_user_ById, add_user, get_user_ByName, get_user_ByEmail, delete_userById

router = APIRouter()  

@router.get("/all") # Lista completa de usuarios
async def get_all():
  db = read_db()
  return db

@router.get("/{id}") # Busqueda de usuario por ID
async def read_id(id: int):
  log.info("Requesting read for id: " + str(id))
  usuario = get_user_ById(id)
  return usuario

@router.get("/email/{email}") # Busqueda de usuario por correo
async def read_email(email: str):
  log.info("Requesting read for email: " + email)
  return get_user_ByEmail(email.upper())

@router.get("/name/{name}") # Busqueda de usuario por nombre
async def read_name(name: str):
  log.info("Requesting read for name: " + name.upper())
  usuario = get_user_ByName(name.upper())
  return usuario

@router.post("/") # Creacion de un nuevo usuario
async def create_user(headers: Annotated[Headers, Header()]):
  log.info("Trying to add user: " + str(headers))
  add_user(headers)
  return "OK"

@router.put("/") # Actualizacion de un usuario
async def update_user(user_id: int, user: Annotated[Usuario, Body(embed=True)]):
  log.info("Trying to update user: " + str(user_id))
  return "OK"

@router.delete("/{id}")# Eliminar un usuario
async def delete_user(id: int):
  log.info("Trying to delete user: " + str(id))
  delete_userById(id)


