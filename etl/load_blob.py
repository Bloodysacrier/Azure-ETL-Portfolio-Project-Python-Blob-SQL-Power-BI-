from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

connect_str = os.getenv("AZURE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")
blob_name = "clean_superstore.csv"


blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)


with open("data_clean/dim_order.csv", "rb") as data:
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

print("Archivo subido a Azure Blob Storage")
