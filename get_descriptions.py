import requests
import csv
from bs4 import BeautifulSoup
from get_names import name_values

with open('pokemon_descriptions.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Name', 'Description'])

    for name in name_values[1:]:
        URL = f"https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon)"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        # There is a physical description of each pokemon under this tag
        biology_tag = soup.find(id='Biology')

        if biology_tag:
            # Find the next <p> tag after the tag with id='Biology'
            next_p_tag = biology_tag.find_next('p')
            if next_p_tag:
                # Extract the description
                description = next_p_tag.text.strip()

                # Write the name and description to the CSV file
                writer.writerow([name, description])
            else:
                writer.writerow([name, f"No description found for {name}"])
        else:
            writer.writerow([name, f"No description found for {name}"])

        print(name)

