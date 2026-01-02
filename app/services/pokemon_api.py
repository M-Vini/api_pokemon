import requests

from app.models.pokemon import Pokemon, Abilities, Ability, Specie,Sprites,Types,Type

class PokemonService:

    BASE_URL = "https://pokeapi.co/api/v2"

    @classmethod
    def get_all_pokemons(cls, limit: int = 1) -> list[Pokemon]:
        pokemons_list = []

        print(f"Buscando lista de {limit} pokémons...")

        try:
            response = requests.get(f'{cls.BASE_URL}/pokemon?limit={limit}')
            data = response.json()
            results = data['results']

            for item in results:
                url_detalhes = item['url']
                resp_detalhes = requests.get(url_detalhes)

                if resp_detalhes.status_code == 200:
                    detalhe = resp_detalhes.json()

                    #Montando DTO
                    
                    #Processando Ability
                    abilities_list = []
                    for ab in detalhe['abilities']:
                        abilities_list.append(Abilities(
                            slot=ab['slot'],
                            is_hidden=ab['is_hidden'],
                            ability=Ability(
                                name=ab['ability']['name'],
                                url=ab['ability']['url']
                            )
                        ))

                    #processando Types
                    types_list = []
                    for ty in detalhe['types']:
                        types_list.append(Types(
                            slot=ty['slot'],
                            type=Type(
                                name=ty['type']['name'],
                                url=ty['type']['url']
                            )
                        ))

                    #processando Sprites
                    sprite_data = detalhe['sprites']
                    sprite_obj = Sprites(
                        back_default=sprite_data['back_default'],
                        front_default=sprite_data['front_default'],
                        front_shiny=sprite_data['front_shiny']
                    )
                    
                    #processando pokemon
                    new_pokemon = Pokemon(
                        id=detalhe['id'],
                        name=detalhe['name'],
                        height=detalhe['height'],
                        weight=detalhe['weight'],
                        species=Specie(
                            name=detalhe['species']['name'],
                            url=detalhe['species']['url']
                        ),
                        sprites=sprite_obj,
                        abilities=abilities_list,
                        types=types_list
                    )

                    pokemons_list.append(new_pokemon)
        except Exception as e:
            print("Erro ao buscar lista: {e}")
        
        return pokemons_list