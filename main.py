from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_data
from dotenv import load_dotenv
import os

def main():
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    load_dotenv()  # ⬅️ load .env

    BASE_URL = 'https://fashion-studio.dicoding.dev/'
    NILAI_TUKAR = 16000
    DATA_PATH = 'products_data.csv'
    
    # Ambil dari environment
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    DB_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


    # 1. Extract Data
    all_products_data = extract_data(BASE_URL)
    # df = pd.DataFrame(all_products_data)
    # print(df)

    # 2&3. Transform & Load Data
    if all_products_data:
        try:
            # 2. Transform data
            DataFrame = transform_data(all_products_data, NILAI_TUKAR)
            # print(DataFrame)
            # print(DataFrame.isnull().sum())
            # print(DataFrame.info())
 
            # 3. Load Data
            load_data(DataFrame, DATA_PATH, DB_URL)
 
        except Exception as e:
            print(f"Terjadi kesalahan dalam proses: {e}")
    else:
        print("Tidak ada data yang ditemukan.")
 
 
if __name__ == '__main__':
    main()