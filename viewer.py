python
import storage

def menu_tampil_hapus():
    data = storage.get_all_data()
    if not data:
        print("Belum ada catatan pengeluaran.")
        return
        
    print("\n--- DAFTAR PENGELUARAN ---")
    for item in data:
        print(f"[{item['id']}] {item['title']} - Rp{item['amount']} ({item['category']})")
        
    print("\n[A] Kembali ke Menu Utama")
    print("[H] Hapus Salah Satu Data")
    pilihan = input("Pilih aksi: ").upper()
    
    if pilihan == "H":
        id_hapus = int(input("Masukkan ID data yang ingin dihapus: "))
        # Logika hapus data
        data_baru = [item for item in data if item['id'] != id_hapus]
        
        if len(data_baru) == len(data):
            print("ID tidak ditemukan!")
        else:
            storage.save_all_data(data_baru)
            print(f"Data dengan ID {id_hapus} berhasil dihapus.")
