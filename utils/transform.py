import pandas as pd
 
def transform_to_DataFrame(data):
    """Mengubah data menjadi DataFrame."""
    df = pd.DataFrame(data)
    return df

def remove_text(data, column, texts):
    for text in texts:
        data[column] = data[column].astype(str).str.replace(text, '')
    return data

def set_null(data, column, texts):
    for text in texts:
        data.loc[data[column] == text, column] = pd.NA
    return data

def transform_price(data):
    # hapus text tak terpakai
    data = remove_text(data, 'Price', ['$'])
    
    # definisikan null
    data = set_null(data, 'Price', ['Price Unavailable', None])
    
    # ubah ke float
    data['Price'] = pd.to_numeric(data['Price'])
    
    return data

def transform_rating(data):
    # hapus text tak terpakai
    data = remove_text(data, 'Rating', ['Rating: ⭐ ', ' / 5'])
    
    # definisikan null
    data = set_null(data, 'Rating', ['Invalid Rating', 'Rating: Not Rated'])
    
    # ubah ke float
    data['Rating'] = pd.to_numeric(data['Rating'])

    return data

def transform_colors(data):
    # hapus text tak terpakai
    data = remove_text(data, 'Colors', [' Colors', ' Color'])
    
    # definisikan null
    data = set_null(data, 'Colors', ['Invalid Rating'])
    
    # ubah ke int
    data['Colors'] = data['Colors'].astype("int64")

    return data

def transform_size(data):
    # hapus text tak terpakai
    data = remove_text(data, 'Size', ['Size: '])
    return data
    
def transform_gender(data):
    # hapus text tak terpakai
    data = remove_text(data, 'Gender', ['Gender: '])
    return data

def transform_title(data):
    # definisikan null
    data = set_null(data, 'Title', ['Unknown Product'])
    return data

def transform_data(data, exchange_rate):
    """Menggabungkan semua transformasi data menjadi satu fungsi."""
    try:
        # Ubah dari dataframe
        data = transform_to_DataFrame(data)

        # Transformasi Price
        data = transform_price(data)
        print('Berhasil Transform Price')
        
        # Transformasi Rating
        data = transform_rating(data)
        print('Berhasil Transform Rating')

        # Transformasi Colors
        data = transform_colors(data)
        print('Berhasil Transform Colors')

        # Transformasi Size
        data = transform_size(data)
        print('Berhasil Transform Size')

        # Transformasi Gender
        data = transform_gender(data)
        print('Berhasil Transform Gender')

        # Transformasi Title
        data = transform_title(data)
        print('Berhasil Transform Title')

        # Hapus Missing Value
        data = data.dropna()
        print('Berhasil Menghaspus Baris dengan Missing Value')
        
        # Transformasi Exchange Rate
        data['Price'] = (data['Price'] * exchange_rate)
        
        # Transformasi Tipe Data
        data['Title'] = data['Title'].astype('object')
        data['Size'] = data['Size'].astype('object')
        data['Gender'] = data['Gender'].astype('object')

        print('Berhasil Transformasi Seluruh Data!')
    
        return data
    
    except Exception as e:
        print(f"Terjadi kesalahan pada proses transform: {e}")
        return pd.DataFrame()