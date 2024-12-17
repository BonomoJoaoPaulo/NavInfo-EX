from typing import List, Dict, Text
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import csv
import os


class SantosDataScrapper():
    def __init__(self, url):
        self.url = url
        if not url:
            raise ValueError("URL is required")
        self._ships_list: List[Dict[Text, Text]] = self.scrap_data()

    def scrap_data(self):
        print("Scraping data from SANTOS port...")
        website = self.url
        response = requests.get(website, verify=False)
        content = response.content
        soup = BeautifulSoup(content, "lxml")

        tables = soup.find_all("table")
        santos_ships = []
        for i in range(len(tables)):
            table = tables[i]
            table_header = table.find('thead')
            table_body = table.find('tbody')            
            ship_type = table_header.find('tr').find('th').text
            columns = []
            
            for i in range(1, len(table_header.find_all('tr'))):
                for th in table_header.find_all('tr')[i].find_all('th'):
                    columns.append(th.text)

            for ship in table_body.find_all('tr'):
                ship_data = {}
                ship_data["TipoNavio"] = ship_type
                for i in range(len(ship.find_all('td')) - 1):
                    ship_data[columns[i]] = ship.find_all('td')[i].text
                santos_ships.append(ship_data)
            
        print("Data scraped successfully from SANTOS port.")
        return santos_ships

    def list_ships(self) -> List[Dict[Text, Text]]:
        return self._ships_list

    def ships_to_json(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"santos_ships_{timestamp}.json"
        file_path = os.path.join("../data/json", file_name)
        with open(file_path, 'w') as json_file:
            json.dump(self._ships_list, json_file, indent=4)
        
        return file_path
    
    def ships_to_csv(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"santos_ships_{timestamp}.csv"
        file_path = os.path.join("../data/csv", file_name)
        headers = self._ships_list[0].keys()
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self._ships_list)
        
        return file_path


if __name__ == "__main__":
    santos = SantosDataScrapper("https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
    santos.scrap_data()
    santos.ships_to_json()
    santos.ships_to_csv()
