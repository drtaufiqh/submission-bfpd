import time
import datetime
import requests

from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}
 
 
def fetching_content(url):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None
 
 
def extract_product_data(card):
    """
    Mengambil data produk berupa judul, harga, rating, warna, ukuran, dan gender 
    dari card (element div dengan class collection-card).
    """
    
    details = card.find('div', class_='product-details')

    title = details.find('h3').text
    
    price = details.find('div', class_="price-container")
    informations = details.find_all('p')
    if price:
        price = price.find('span', class_="price").text
        rating = informations[0].text
        colors = informations[1].text
        size = informations[2].text
        gender = informations[3].text
    else:
        price = informations[0].text
        rating = informations[1].text
        colors = informations[2].text
        size = informations[3].text
        gender = informations[4].text

    products = {
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Colors": colors,
        "Size": size,
        "Gender": gender,
        "Timestamp": datetime.datetime.now()
    }
 
    return products
 
 
def scrape_product(base_url, start_page=1, delay=2):
    """Fungsi untuk Scraping Produk"""
    formated_base_url = base_url + "page{}"
    data = []
    page_number = start_page
 
    while True:
        url = base_url
        if page_number > 1:
            url = formated_base_url.format(page_number)
        print(f"Scraping halaman: {url}")
 
        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            cards = soup.find_all('div', class_='collection-card')
            for card in cards:
                product = extract_product_data(card)
                data.append(product)
 
            next_button = soup.find('li', class_='next')
            # apakah punya class 'disabled'
            is_disable = 'disabled' in next_button.get('class', [])

            if not is_disable:
                page_number += 1
                time.sleep(delay)  # Delay sebelum halaman berikutnya
            else:
                break  # Berhenti jika sudah tidak ada next button
        else:
            break # Berhenti jika ada kesalahan
 
    return data

def extract_data(base_url, start_page=1, delay=2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    return scrape_product(base_url, start_page, delay)