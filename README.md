# Pokemon Description Web Scraper
Webscraper used to pull physical descriptions of pokemon from [https://bulbapedia.bulbagarden.net](https://bulbapedia.bulbagarden.net/wiki/Main_Page) and create table with the names and descriptions.
I am planning on using the descriptions as alt text for pokemon images.

## File descriptions
`get_descriptions.py`: Pulls the description for each pokemon and writes it to pokemon_descriptions.csv  
`get_names.py`: Gets the names of all the pokemon contained in the pokemon_info data set  
`pokemon_descriptions.csv`: The resulting csv file with name and description columns  
`pokemon_info.csv`: Pokemon stats table. Used for pulling pokemon names 

## Credit
`pokemon_info` dataset came from [https://www.kaggle.com/datasets/rounakbanik/pokemon](https://www.kaggle.com/datasets/rounakbanik/pokemon)  
Pokemon descriptions from [https://bulbapedia.bulbagarden.net](https://bulbapedia.bulbagarden.net/wiki/Main_Page)  
