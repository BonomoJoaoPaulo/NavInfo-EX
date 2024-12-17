from typing import List, Dict, Text
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import os
import csv

class ParanaguaDataScraper():
    def __init__(self, url: str):
        self._url = url
        if not url:
            raise ValueError("URL is required")
        self._ships_list, self._columns = self.scrap_data()
    
    def scrap_data(self) -> tuple[List[Dict[Text, Text]], List[Text]]:
        print("Scraping data from PARANAGUA port...")
        website = self._url
        response = requests.get(website, verify=False)
        content = response.content
        soup = BeautifulSoup(content, "lxml")
        
        tables = soup.find_all('table', class_="table table-bordered table-striped table-hover")
        paranagua_ships = []
        all_columns = ['Situacao']
        for table in tables:
            table_header = table.find('thead')
            table_body = table.find('tbody')
            columns = []
            try:
                ship_situation = table_header.find('tr').find('th').text
                for i in range(1, len(table_header.find_all('tr'))):
                    for th in table_header.find_all('tr')[i].find_all('th'):
                        columns.append(th.text.replace(' ', '').replace('\n', '').replace('\r', ''))
            except:
                ship_situation = "Desconhecido"
            try:
                for ship in table_body.find_all('tr'):
                    ship_data = {}
                    for i in range(len(ship.find_all('td'))):
                        ship_data[columns[i]] = ship.find_all('td')[i].text
                    ship_data['Situacao'] = ship_situation
                    paranagua_ships.append(ship_data)
            except:
                print(f"Sem navios na tabela {ship_situation}.")
            
            all_columns.extend(columns)
            all_columns = list(set(all_columns))

        print("Data scraped successfully from PARANAGUA port.")
        return paranagua_ships, all_columns

    def list_ships(self) -> List[Dict[Text, Text]]:
        return self._ships_list
    
    def ships_to_json(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"paranagua_ships_{timestamp}.json"
        file_path = os.path.join("../data/json", file_name)
        with open(file_path, 'w') as json_file:
            json.dump(self._ships_list, json_file, indent=4)
        
        return file_path
    
    def ships_to_csv(self) -> Text:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        file_name = f"paranagua_ships_{timestamp}.csv"
        file_path = os.path.join("../data/csv", file_name)
        headers = self._columns
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self._ships_list)
        
        return file_path


if __name__ == "__main__":
    paranagua = ParanaguaDataScraper("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
    paranagua.scrap_data()
    paranagua.ships_to_json()
    paranagua.ships_to_csv()
