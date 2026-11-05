import storage

def tambah_baru():
    print("\n--- TAMBAH PENGELUARAN BARU ---")
    title = input("Nama pengeluaran: ")
    amount = int(input("Jumlah uang (Rp): "))
    category = input("Kategori (Makanan/Transport/Lainnya): ")
    
    # Ambil data lama dari Orang 2
    data = storage.get_all_data()
    
    # Buat ID otomatis
    new_id = data[-1]['id'] + 1 if data else 1
    
    new_item = {
        "id": new_id,
        "title": title,
        "amount": amount,
        "category": category
    }
    
    data.append(new_item)
    
    # Simpan kembali menggunakan fungsi Orang 2
    storage.save_all_data(data)
    print(f"✅ Berhasil mencatat '{title}' senilai Rp{amount}!")
