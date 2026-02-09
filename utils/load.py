from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

SCOPES = ['https://wgitww.googleapis.com/auth/spreadsheets']

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

def load_to_csv(data, path):
    """Fungsi untuk menyimpan data ke dalam CSV"""
    data.to_csv(path, index=False)
    print("Data berhasil disimpan di CSV.")
 
def load_to_postgre(data, db_url):
    """Fungsi untuk menyimpan data ke dalam PostgreSQL."""
    try:
        # Membuat engine database
        engine = create_engine(db_url)
        
        # Menyimpan data ke tabel 'fashionstudio' jika tabel sudah ada, data akan ditambahkan (append)
        with engine.connect() as con:
            data.to_sql('fashionstudio', con=con, if_exists='append', index=False)
            print("Data berhasil disimpan di PostgreSQL")
    
    except Exception as e:
        print(f"Gagal menyimpan ke PostgreSQL: {e}")

def load_to_spreadsheets(data):
    """Fungsi untuk menyimpan data ke dalam Google Sheets"""
    try:
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        # khusus timestamp
        data['Timestamp'] = data['Timestamp'].astype(str)

        headers = data.columns.tolist()
        values = data.values.tolist()

        body = {
            "values": [headers] + values
        }

        sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range='Sheet1!A1',
            valueInputOption='RAW',
            body=body
        ).execute()

        print("Data berhasil disimpan di Google Sheets.")

    except Exception as e:
        print(f"Gagal menyimpan ke Google Sheets: {e}")

def load_data(data, path, db_url):
    try:
        load_to_csv(data, path)
        load_to_spreadsheets(data)
        load_to_postgre(data, db_url)
    except Exception as e:
        print(f"Terjadi kesalahan pada proses load: {e}")