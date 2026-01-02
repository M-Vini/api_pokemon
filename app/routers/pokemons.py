from fastapi import APIRouter, HTTPException
from app.services.pokemon_api import PokemonService
from app.models.pokemon import Pokemon

router = APIRouter(prefix='/pokemons', tags=['Pokemons'])

@router.get('/', response_model=list[Pokemon])
def get_pokemons():

    # Retorna uma lista detalhada de pokemons
    try:
        result = PokemonService.get_all_pokemons(limit=20)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))