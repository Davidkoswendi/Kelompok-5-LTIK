import storage
import tracker
import viewer
import reports

def menu():
    # Memastikan file database siap saat aplikasi pertama kali dijalankan
    storage.init_database()
    
    while True:
        print("\n=== APLIKASI PENCATAT KEUANGAN ===")
        print("1. Tambah Pengeluaran (Tugas Orang 1)")
        print("2. Lihat & Hapus Pengeluaran (Tugas Orang 3)")
        print("3. Laporan & Analisis Kategori (Tugas Orang 4)")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tracker.tambah_baru()
        elif pilihan == "2":
            viewer.menu_tampil_hapus()
        elif pilihan == "3":
            reports.tampilkan_laporan()
        elif pilihan == "4":
            print("👋 Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()
