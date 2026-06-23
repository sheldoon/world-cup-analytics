import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def get_scorers(season=2026, limit=10):
    """Busca todos os artilheiros da Copa do Mundo.
    Parameters:
        season (int): Ano da temporada da Copa do Mundo. Padrão é 2026.
        limit (int): Número máximo de artilheiros a serem retornados. Padrão é 10.
    Retorna uma lista de dicionários, onde cada dicionário representa um artilheiro.
    """
    url = f"{BASE_URL}/competitions/WC/scorers"
    params = {"season": season, "limit": limit}
    response = requests.get(url, headers=HEADERS, params=params)


    if response.status_code != 200:
        print(f"Erro ao buscar artilheiros: {response.status_code} - {response.text}")
        return None
    data = response.json()
    print(f"Copa do Mundo {season}: Total de artilheiros: {len(data['scorers'])}")
    return data

def save_raw(data,filename):
    """Salva os dados brutos em um arquivo NDJSON local.
    Args:
        data (list): Lista de dicionários representando os artilheiros.
        filename (str): Nome do arquivo onde os dados serão salvos.
    """
    os.makedirs("raw_data", exist_ok=True)
    file_path = f"raw_data/{filename}"

    with open(file_path, "w") as f:
        for scorer in data.get("scorers", []):
            f.write(json.dumps(scorer, ensure_ascii=False) + "\n")
    print(f"Dados brutos salvos em: {file_path}")
    return file_path

if __name__ == "__main__":
    print("Iniciando extração de artilheiros...")
    scorers_2026 = get_scorers(season=2026, limit = 20)
    if scorers_2026:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scorers_2026_{timestamp}.ndjson"
        save_raw(scorers_2026, filename)
        print("Extração concluída com sucesso.")
