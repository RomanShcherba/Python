class CreatePokemon:
    def __init__(self, 
                 id: int, 
                 forms: str, 
                 stats: str, 
                 height: str, 
                 weight: str, 
                 base_experience: str, 
                 abilities: list[str]):
        self.id = id
        self.forms = forms
        self.stats = stats
        self.height = height
        self.weight = weight
        self.base_experience = base_experience
        self.abilities = abilities