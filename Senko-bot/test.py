pokemonTags=open("pokemon.txt", "r").read().replace("\n", ",").replace(" ", "_").lower().split(",")
print(pokemonTags)