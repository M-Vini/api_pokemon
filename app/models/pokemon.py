#Definição das tipagens do sistema

from pydantic import BaseModel
from typing import Optional

class Ability(BaseModel):
    name: str
    url: str

class Abilities(BaseModel):
    ability: Ability
    is_hidden: bool
    slot: int

class Specie(BaseModel):
    name: str
    url: str

class Sprites(BaseModel):
    back_default: Optional[str] = None
    back_female: Optional[str] = None
    back_shiny: Optional[str] = None
    back_shiny_female: Optional[str] = None
    front_default: Optional[str] = None
    front_female: Optional[str] = None
    front_shiny: Optional[str] = None
    front_shiny_female: Optional[str] = None

class Type(BaseModel):
    name: str
    url: str

class Types(BaseModel):
    slot: int
    type: Type

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    species: Specie
    sprites: Sprites
    abilities: list[Abilities]
    types: list[Types]
    