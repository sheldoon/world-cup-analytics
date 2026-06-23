import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def get_matches(season=2026):
    """Busca todas as partidas da Copa do Mundo.
    Parameters:
        season (int): Ano da temporada da Copa do Mundo. Padrão é 2026.
    Retorna uma lista de dicionários, onde cada dicionário representa uma partida.    
    """
    url = f"{BASE_URL}/competitions/WC/matches"
    params = {"season": season}
    response = requests.get(url, headers=HEADERS, params=params)


    if response.status_code != 200:
        print(f"Erro ao buscar partidas: {response.status_code} - {response.text}")
        return None
    data = response.json()
    total = data["resultSet"]["count"]
    played = data["resultSet"]["played"]
    print(f"Copa do Mundo {season}: Total de partidas: {total}, Partidas jogadas: {played}")
    return data

def save_raw(data,filename):
    """Salva os dados brutos em um arquivo NDJSON.
    Args:
        data (list): Lista de dicionários representando as partidas.
        filename (str): Nome do arquivo onde os dados serão salvos.
    """
    os.makedirs("raw_data", exist_ok=True)
    file_path = f"raw_data/{filename}"

    matches = data.get("matches", [])

    with open(file_path, "w") as f:
        for match in matches:
            f.write(json.dumps(match, ensure_ascii=False) + "\n")
    print(f"Dados brutos salvos em: {file_path}")
    return file_path

if __name__ == "__main__":
    print("Iniciando extração de partidas...")
    matches_2026 = get_matches(season=2026)
    if matches_2026:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"matches_2026_{timestamp}.ndjson"
        save_raw(matches_2026, filename)
        print("Extração concluída com sucesso.")
