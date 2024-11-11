# Libraries Imports
import json

#Project Imports
from utils.models import Usuario, Headers
from utils.logUtil import log

db_path = 'usuarios/usuarios_db.json'

def read_db():
  try:
    with open(db_path, 'r') as file:
      db = json.load(file)
    log.info("Successful access to DB...")
  except:
    log.info("Something Happened...")
  return db

def get_user_ById(id: int):
  data = read_db()
  indexPos = next((i for i, d in enumerate(data) if d.get("id") == id), None) 
  usuario = Usuario(
                id = data[indexPos]["id"],
                nombre = data[indexPos]["nombre"],
                apellido = data[indexPos]["apellido"],
                email = data[indexPos]["email"],
                clave = data[indexPos]["clave"],
                telefono = data[indexPos]["telefono"],
                estado = data[indexPos]["estado"])
  log.info("User returned successfully...")
  return usuario

def get_user_ByName(name: str):
  data = read_db()
  index = next((i for i, d in enumerate(data) if d.get("nombre").upper() == name), None) 
  if index:
    response = Usuario(
                  id = data[index]["id"],
                  nombre = data[index]["nombre"],
                  apellido = data[index]["apellido"],
                  email = data[index]["email"],
                  clave = data[index]["clave"],
                  telefono = data[index]["telefono"],
                  estado = data[index]["estado"])
  else:
    log.info("User not found")
    response = None
  return response

def get_user_ByEmail(email: str):
  data = read_db()
  index = next((i for i, d in enumerate(data) if d.get("email").upper() == email), None) 
  if index:
    response = Usuario(
                  id = data[index]["id"],
                  nombre = data[index]["nombre"],
                  apellido = data[index]["apellido"],
                  email = data[index]["email"],
                  clave = data[index]["clave"],
                  telefono = data[index]["telefono"],
                  estado = data[index]["estado"])
  else:
    log.info("User not found")
    response = None
  return response

def max_id():
  userdata = read_db()
  data = max(userdata, key=lambda x: x['id'])
  return data["id"]
  
def add_user(headers: Headers):
  id = max_id()
  usuario = Usuario(
    id = id + 1,
    nombre = headers.nombre,
    apellido = headers.apellido,
    email = headers.email,
    telefono = headers.telefono
  )
  data = read_db()
  data.append(usuario.model_dump())
  log.info("User added: " + str(usuario.model_dump()))
  with open(db_path, 'w') as f:
    json.dump(data, f, indent=4)  # indent for pretty formatting
    
def delete_userById(id: int):
  data = read_db()
  index = next((i for i, d in enumerate(data) if d.get("id") == id), None) 
  del data[index]
  with open(db_path, 'w') as f:
    json.dump(data, f, indent=4)  # indent for pretty formatting
  return "OK" 
  