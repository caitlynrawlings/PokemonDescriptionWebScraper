# PokemonDescriptionWebScraper

Webscraper used to pull physical descriptions of pokemon from [https://bulbapedia.bulbagarden.net](https://bulbapedia.bulbagarden.net/wiki/Main_Page)  
Planning on using the descriptions as alt text for pokemon images  

pokemon_info dataset came from [https://www.kaggle.com/datasets/rounakbanik/pokemon](https://www.kaggle.com/datasets/rounakbanik/pokemon)

## File descriptions
get_descriptions.py: pulls the description for each pokemon and writes it to pokemon_descriptions.csv  
get_names.py: gets the names of all the pokemon contained in the pokemon_info data set  
pokemon_descriptions.csv: the resulting csv file with name and description columns (row 114 repeated twice)  
pokemon_info.csv: pokemon stats table. used for pulling pokemon names
