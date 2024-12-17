import os
import glob

from scrapers.paranagua_data_scraper import ParanaguaDataScraper as pds
from scrapers.santos_data_scraper import SantosDataScrapper as sds
from scrapers.santarem_data_scraper import SantaremDataScraper as sads

def scrap_all_data() -> tuple[pds, sads, sds]:
    paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
    paranagua_data_scraper.scrap_data()

    santos_data_scraper = sds("https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
    santos_data_scraper.scrap_data()

    santarem_data_scraper = sads("https://cdpport.cdp.com.br/cdpport/pesquisa.aspx?WCI=relLineUp_008&Mv=Link&sqlCodDominio=6")
    santarem_data_scraper.scrap_data()
    
    return paranagua_data_scraper, santarem_data_scraper, santos_data_scraper

def export_all_data_as_csv(paranagua_data_scraper, santarem_data_scraper, santos_data_scraper) -> None:
    print("Exportando dados para CSV...")
    paranagua_data_scraper.ships_to_csv()
    santarem_data_scraper.ships_to_csv()
    santos_data_scraper.ships_to_csv()

def export_all_data_as_json(paranagua_data_scraper, santarem_data_scraper, santos_data_scraper) -> None:
    print("Exportando dados para JSON...")
    paranagua_data_scraper.ships_to_json()
    santarem_data_scraper.ships_to_json()
    santos_data_scraper.ships_to_json()

def get_most_recent_file(directory, file_prefix, file_format="csv"):
    file_pattern = os.path.join(directory, f"{file_prefix}_*.{file_format}")  
    files = glob.glob(file_pattern)
    
    if not files:
        return None
    
    files.sort(key=os.path.getmtime, reverse=True)
    
    return files[0]
