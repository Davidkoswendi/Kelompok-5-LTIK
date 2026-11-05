import json
import os

FILE_NAME = "expenses.json"

def init_database():
    """Membuat file JSON kosong jika belum ada"""
    if not os.path.exists(FILE_NAME):
        save_all_data([])

def get_all_data():
    """Membaca seluruh data dari file JSON"""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_all_data(data):
    """Menyimpan seluruh data ke file JSON"""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)