from sqlalchemy import create_engine

def load_to_csv(data, path):
    """Fungsi untuk menyimpan data ke dalam CSV"""
    data.to_csv(path, index=False)
    print("Data Berhasil disimpan di " + path)
 
def load_to_postgre(data, db_url):
    """Fungsi untuk menyimpan data ke dalam PostgreSQL."""
    try:
        # Membuat engine database
        engine = create_engine(db_url)
        
        # Menyimpan data ke tabel 'fashionstudio' jika tabel sudah ada, data akan ditambahkan (append)
        with engine.connect() as con:
            data.to_sql('fashionstudio', con=con, if_exists='append', index=False)
            print("Data berhasil ditambahkan di PostgreSQL!")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def load_data(data, path, db_url):
    load_to_csv(data, path)
    # load_to_spreadsheets(data)
    load_to_postgre(data, db_url)