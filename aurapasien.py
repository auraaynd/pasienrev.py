BIAYA_PER_HARI = 350000

daftar_pasien = [
    {"nama": "Budi", "penyakit": "Demam Berdarah", "fasilitas": "VIP Room (AC, TV, Sofa Bed)"},
    {"nama": "Sugi", "penyakit": "Tipes (Thypoid)", "fasilitas": "Kelas 1 (AC, 2 Bed)"},
    {"nama": "Muis", "penyakit": "Patah Tulang Leg", "fasilitas": "Kelas 2 (Kipas Angin, 4 Bed)"},
    {"nama": "Sapei", "penyakit": "Pasca Operasi Caesar", "fasilitas": "VIP Room (AC, TV, Sofa Bed)"},
    {"nama": "Nizar", "penyakit": "Asma Akut", "fasilitas": "Kelas 1 (AC, 2 Bed)"},
    {"nama": "Febri", "penyakit": "Diare Dehidrasi", "fasilitas": "Kelas 3 (6 Bed)"},
    {"nama": "Zainuri", "penyakit": "Stroke Akut", "fasilitas": "ICU (Monitoring 24 Jam)"},
    {"nama": "Michel", "penyakit": "Gagal Ginjal", "fasilitas": "Kelas 1 (AC, 2 Bed)"},
    {"nama": "Andi", "penyakit": "Infeksi Paru-paru", "fasilitas": "Kelas 2 (Kipas Angin, 4 Bed)"},
    {"nama": "Tono", "penyakit": "Trauma Kepala", "fasilitas": "VIP Room (AC, TV, Sofa Bed)"}
]

print("=== EVALUASI PASIEN OPNAME RUMAH SAKIT ===\n")

for i in range(10):
    pasien = daftar_pasien[i]
    nama = pasien["nama"]
    penyakit = pasien["penyakit"]
    fasilitas = pasien["fasilitas"]
    
    print(f"--- Pasien ke-{i+1} ---")
    print(f"Nama Pasien  : {nama}")
    print(f"Penyakit     : {penyakit}")
    print(f"Fasilitas RS : {fasilitas}")
    
    lama_menginap = int(input(f"Masukkan lama menginap {nama} (hari): "))
    
    makanan = "Menu Nutrisi Khusus Pemulihan + Ekstra Buah" if lama_menginap > 3 else "Menu Makanan Standar Pasien"
    kunjungan = "Kunjungan Terbatas (Max 2 orang per jam besuk)" if lama_menginap > 3 else "Bebas Jam Besuk Standar"
    total_biaya = lama_menginap * BIAYA_PER_HARI
    
    print(f"Menu Makanan     : {makanan}")
    print(f"Aturan Kunjungan : {kunjungan}")
    print(f"Total Bayar      : Rp {total_biaya:,} ({lama_menginap} hari x Rp {BIAYA_PER_HARI:,})")
    print("=" * 65)