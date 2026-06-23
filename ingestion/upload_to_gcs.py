import os
import glob
import google.cloud.storage as storage
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")

def upload_file(local_path, destination_blob_name):
    """Faz upload de um arquivo local para o Google Cloud Storage.
    Args:
        local_path (str): Caminho do arquivo local a ser enviado.
        destination_blob_name (str): Nome do blob no bucket GCS.
    """
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(local_path)
    print(f"Arquivo {local_path} enviado para gs://{BUCKET_NAME}/{destination_blob_name}")

def upload_all_raw_files():
    """Faz upload de todos os arquivos NDJSON na pasta 'raw_data' para o GCS."""
    raw_files = glob.glob("raw_data/*.ndjson")
    if not raw_files:
        print("Nenhum arquivo NDJSON encontrado na pasta 'raw_data'.")
        return

    for file_path in raw_files:
        filename = os.path.basename(file_path)

        if "matches" in filename:
            destination = f"matches/{filename}"
        elif "teams" in filename:
            destination = f"teams/{filename}"
        elif "scorers" in filename:
            destination = f"scorers/{filename}"
        else:
            destination = f"others/{filename}"
        upload_file(file_path, destination)

if __name__ == "__main__":
    print("Iniciando upload de arquivos para o GCS...")
    upload_all_raw_files()
    print("Upload concluído com sucesso.")