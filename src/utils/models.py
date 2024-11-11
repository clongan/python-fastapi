from pydantic import BaseModel, Field
from typing import List, Optional, Union

class Usuario(BaseModel):
  id: Union[int, None] = None
  nombre: str
  apellido: str
  email: str
  clave: str = "default" 
  telefono: int
  estado: Union[str, None] = "activo" 

class Headers(BaseModel):
  nombre: str
  apellido: str
  email: str
  telefono: int