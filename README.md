# PokemonDescriptionWebScraper
Webscraper used to pull physical descriptions of pokemon from [https://bulbapedia.bulbagarden.net](https://bulbapedia.bulbagarden.net/wiki/Main_Page) and create table of the names and descriptions.
I am planning on using the descriptions as alt text for pokemon images.

## Credit
`pokemon_info` dataset came from [https://www.kaggle.com/datasets/rounakbanik/pokemon](https://www.kaggle.com/datasets/rounakbanik/pokemon)  
Pokemon descriptions from [https://bulbapedia.bulbagarden.net](https://bulbapedia.bulbagarden.net/wiki/Main_Page)  

## File descriptions
`get_descriptions.py`: pulls the description for each pokemon and writes it to pokemon_descriptions.csv  
`get_names.py`: gets the names of all the pokemon contained in the pokemon_info data set  
`pokemon_descriptions.csv`: the resulting csv file with name and description columns
`pokemon_info.csv`: pokemon stats table. used for pulling pokemon names
