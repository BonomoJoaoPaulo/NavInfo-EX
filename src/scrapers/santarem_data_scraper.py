from typing import List, Dict, Text
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import os
import csv

class SantaremDataScraper():
    def __init__(self, url: str):
        self._url = url
        if not url:
            raise ValueError("URL is required")
        self._ships_list: List[Dict[Text, Text]] = self.scrap_data()

    def scrap_data(self) -> List[Dict[Text, Text]]:
        print("Scraping data from SANTAREM port...")
        website = self._url
        response = requests.get(website, verify=False)
        content = response.content
        soup = BeautifulSoup(content, "lxml")

        tables = soup.find_all("table", class_="table table-bordered table-striped table-hover")
        santarem_ships = []
        for i in range(1, len(tables)):
            table = tables[i]
            table_header = table.find('thead')
            table_body = table.find('tbody')
            berco_info = (table_header.find('tr').find('th').text).replace("\n", " ").replace("\r", " ")
            
            columns = []
            for i in range(1, len(table_header.find_all('tr'))):
                for th in table_header.find_all('tr')[i].find_all('th'):
                    columns.append(th.text)
    
            for ship in table_body.find_all('tr'):
                ship_data = {}
                for i in range(len(ship.find_all('td'))):
                    ship_data[columns[i]] = ship.find_all('td')[i].text
                ship_data["Berco"] = berco_info
                santarem_ships.append(ship_data)
        
        print("Data scraped successfully from SANTAREM port.")
        return santarem_ships
    
    def list_ships(self) -> List[Dict[Text, Text]]:
        return self._ships_list
    
    def ships_to_json(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"santarem_ships_{timestamp}.json"
        file_path = os.path.join("../data/json", file_name)
        with open(file_path, 'w') as json_file:
            json.dump(self._ships_list, json_file, indent=4)
        
        return file_path
    
    def ships_to_csv(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"santarem_ships_{timestamp}.csv"
        file_path = os.path.join("../data/csv", file_name)
        headers = self._ships_list[0].keys()
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self._ships_list)
        
        return file_path


if __name__ == "__main__":
    santarem = SantaremDataScraper("https://cdpport.cdp.com.br/cdpport/pesquisa.aspx?WCI=relLineUp_008&Mv=Link&sqlCodDominio=6")
    santarem.scrap_data()
    santarem.ships_to_json()
    santarem.ships_to_csv()
