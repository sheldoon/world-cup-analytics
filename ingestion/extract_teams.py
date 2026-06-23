import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def get_teams(season=2026):
    """Busca todas as equipes da Copa do Mundo.
    Parameters:
        season (int): Ano da temporada da Copa do Mundo. Padrão é 2026.
    Retorna uma lista de dicionários, onde cada dicionário representa uma equipe.
    """
    url = f"{BASE_URL}/competitions/WC/teams"
    params = {"season": season}
    response = requests.get(url, headers=HEADERS, params=params)


    if response.status_code != 200:
        print(f"Erro ao buscar equipes: {response.status_code} - {response.text}")
        return None
    data = response.json()
    print(f"Copa do Mundo {season}: Total de equipes: {len(data['teams'])}")
    return data

def save_raw(data,filename):
    """Salva os dados brutos em um arquivo NDJSON local.
    Args:
        data (list): Lista de dicionários representando as equipes.
        filename (str): Nome do arquivo onde os dados serão salvos.
    """
    os.makedirs("raw_data", exist_ok=True)
    file_path = f"raw_data/{filename}"

    with open(file_path, "w") as f:
        for team in data.get("teams", []):
            f.write(json.dumps(team, ensure_ascii=False) + "\n")
    print(f"Dados brutos salvos em: {file_path}")
    return file_path

if __name__ == "__main__":
    print("Iniciando extração de equipes...")
    teams_2026 = get_teams(season=2026)
    if teams_2026:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"teams_2026_{timestamp}.ndjson"
        save_raw(teams_2026, filename)
        print("Extração concluída com sucesso.")
