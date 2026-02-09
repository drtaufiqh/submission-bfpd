# Submission – Belajar Fundamental Pemrosesan Data (ETL Pipeline)

Proyek ini merupakan **submission Dicoding – Belajar Fundamental Pemrosesan Data**, yang mengimplementasikan **ETL (Extract, Transform, Load) Pipeline** menggunakan Python. Data diambil dari website e‑commerce fiktif, dibersihkan dan ditransformasikan, lalu disimpan ke beberapa media penyimpanan.

---

## 📌 Fitur Utama

* **Extract**

  * Scraping data produk dari website menggunakan `requests` dan `BeautifulSoup`
  * Mendukung pagination (next page)
  * Error handling pada proses request

* **Transform**

  * Mengubah data mentah menjadi `pandas.DataFrame`
  * Membersihkan kolom harga, rating, warna, ukuran, dan gender
  * Menangani missing value
  * Konversi nilai harga menggunakan exchange rate

* **Load**

  * Menyimpan data ke:

    * File CSV
    * Google Sheets (Google Sheets API)
    * PostgreSQL
  * Error handling pada setiap proses penyimpanan

* **Testing**

  * Unit test menggunakan `pytest`
  * Mocking API request dan external services
  * Code coverage menggunakan `pytest-cov`

---

## 📂 Struktur Proyek

```
submission-bfpd
│
├── utils
│   ├── extract.py        # Proses ekstraksi data
│   ├── transform.py     # Proses transformasi data
│   └── load.py          # Proses load data
│
├── tests
│   ├── test_extract.py  # Unit test extract
│   ├── test_transform.py# Unit test transform
│   └── test_load.py     # Unit test load (mock)
│
├── products_data.csv    # Contoh output data
├── main.py              # Entry point pipeline
├── requirements.txt     # Dependency proyek
├── .env.example         # Contoh environment variable
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variable

Buat file `.env` berdasarkan `.env.example`:

```env
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
GOOGLE_SERVICE_ACCOUNT=
SPREADSHEET_ID=
```

⚠️ **Catatan penting:**

* `GOOGLE_SERVICE_ACCOUNT` berisi path ke file service account Google Sheets (misalnya `./google-sheets-api.json`).
* File `.env` dan `google-sheets-api.json` **tidak boleh di-commit** ke GitHub (sudah ditangani via `.gitignore`).
* Spreadsheet harus dibagikan ke email service account Google

---

## ▶️ Menjalankan Pipeline

```bash
python main.py
```

Pipeline akan:

1. Mengambil data produk dari website
2. Membersihkan dan mentransformasi data
3. Menyimpan data ke CSV, Google Sheets, dan PostgreSQL

---

## 🧪 Menjalankan Unit Test

Install dependency testing:

```bash
pip install -r requirements.txt
```

Jalankan seluruh test:

```bash
python -m pytest tests
```

Menjalankan test dengan coverage:

```bash
python -m pytest tests -v --cov=utils --cov-report=html
```

Hasil coverage akan tersimpan di folder `htmlcov/`.

---

## 🛠 Teknologi yang Digunakan

* Python 3
* requests
* beautifulsoup4
* pandas
* SQLAlchemy
* Google Sheets API
* pytest & pytest-cov
* python-dotenv

---

## 👤 Author

Submission oleh **Dutatama Rosewika Taufiq Hadihardaya**

---

✨ Proyek ini dibuat untuk memenuhi kriteria kelulusan kelas **Belajar Fundamental Pemrosesan Data – Dicoding**.
