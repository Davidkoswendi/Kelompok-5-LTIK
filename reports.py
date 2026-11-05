def tampilkan_laporan():
    data = storage.get_all_data()
    if not data:
        print("📭 Tidak ada data untuk dianalisis.")
        return
        
    total_seluruhnya = sum(item['amount'] for item in data)
    
    # Hitung per kategori
    kategori_dict = {}
    for item in data:
        cat = item['category']
        kategori_dict[cat] = kategori_dict.get(cat, 0) + item['amount']
        
    print("\n=== LAPORAN KEUANGAN ===")
    print(f"💰 TOTAL PENGELUARAN: Rp{total_seluruhnya}")
    print("------------------------")
    print("Breakdown per Kategori:")
    for cat, total_cat in kategori_dict.items():
        persen = (total_cat / total_seluruhnya) * 100
        print(f"📁 {cat:<12}: Rp{total_cat:<8} ({persen:.1f}%)")