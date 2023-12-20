'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'aktif'
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil'
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|--    13   --|
-----------------------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |    Jadwal   |
-----------------------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |  07.30-09.10|
2   22A1210   | Matkul2                  |  3  | Selasa |  07.30-09.10|
3   22A1211   | Matkul3                  |  3  | Rabu   |  07.30-09.10|
4   22A1212   | Matkul4                  |  2  | Senin  |  07.30-09.10|
5   22A1213   | Matkul5                  |  3  | Kamis  |  07.30-09.10|
6   22A1214   | Matkul6                  |  3  | Kamis  |  07.30-09.10|
7   22A1215   | Matkul7                  |  3  | Kamis  |  07.30-09.10|
8   22A1216   | Matkul8                  |  2  | Kamis  |  07.30-09.10|
-----------------------------------------------------------------------
                        TOTAL SKS           21                        |
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

Kuliah      = 'Institut Teknologi Bacharuddin Jusuf Habibie'
Tanda       = 'Parepare, 25 Oktober 2023'
Jurusan     = 'JURUSAN SAINS'
Kartu       = 'KARTU HASIL STUDI MAHASISWA'
Nama        = 'Retno Helviani '
NIM         = '231031008'
Program     = 'S1/Sistem Informasi A'
Tahun       = '2023-Ganjil'
Semester    = 'GANJIL 2023/2024'
Status      = 'Aktif'
Total       = 'TOTAL SKS:   20'
nilai_mtk   = [85,89,87,91,90,98,78,90]

MK =   [['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta INTEK dan IMTAQ','Pengantar pemrograman','Pengantar Teknologi Informasi','Kalkulus Dasar 1','Sains Terpadu'],
        [2,2,2,2,3,3,3,3],
        ['22B0211012','22B0211022','22B0211032','22B0211042','22B0211073','22B0211063','22B0211083','22B0211053'],
        [13.30,09.20,07.30,15.20,07.30,13.30,13.30,13.30]]

sp    = 70
print(Kuliah.upper().center(70))
print(Jurusan.center(70))
print(Kartu.center(70))
print(Semester.center(70))
print()

print(f'''
Nama Lengkap    \t:{Nama.title()}
NIM             \t:{NIM}
Program/Prodi   \t:{Program.title()}
Tahun Masuk     \t:{Tahun}
Status          \t:{Status}
           ''')

print('-'*71)
print('no.'+'|'+'Kode'.ljust(10)+'|'+'Mata Kuliah'.center(30)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(10)+'|')
print('-'*71)
print('01.'+'|'+'22B0211012'.ljust(10)+'|'+'Agama Islam'.center(30)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'13.30'.center(10)+'|')
print('02.'+'|'+'22B0211022'.ljust(10)+'|'+'Pancasila'.center(30)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'09.20'.center(10)+'|')
print('03.'+'|'+'22B0211032'.ljust(10)+'|'+'Bahasa Indonesia'.center(30)+'|'+'2'.center(5)+'|'+'Kamis'.center(8)+'|'+'07.30'.center(10)+'|')
print('04.'+'|'+'22B0211042'.ljust(10)+'|'+'Wawasan Cinta INTEK dan IMTAQ'.center(30)+'|'+'2'.center(5)+'|'+'Kamis'.center(8)+'|'+'15.20'.center(10)+'|')
print('05.'+'|'+'22B0211073'.ljust(10)+'|'+'Pengantar pemrograman'.center(30)+'|'+'3'.center(5)+'|'+'Selasa'.center(8)+'|'+'07.30'.center(10)+'|')
print('06.'+'|'+'22B0211063'.ljust(10)+'|'+'Pengantar Teknologi Informasi'.center(30)+'|'+'3'.center(5)+'|'+'Kamis'.center(8)+'|'+'13.30'.center(10)+'|')
print('07.'+'|'+'22B0211083'.ljust(10)+'|'+'Kalkulus Dasar 1'.center(30)+'|'+'3'.center(5)+'|'+'Selasa'.center(8)+'|'+'13.30'.center(10)+'|')
print('08.'+'|'+'22B0211053'.ljust(10)+'|'+'Sains Terpadu'.center(30)+'|'+'3'.center(5)+'|'+'Rabu'.center(8)+'|'+'13.30'.center(10)+'|')
print('-'*71)
sp    = 75
print(Total.upper().center(70))
print('-'*71)
print('-'*71)
print()

print('Summary:')
print(f'Jumlah Mata Kuliah : 8 Mata Kuliah')
print(f'Jumlah Mata Kuliah 2 SKS : 4 Mata Kuliah')
print(f'Jumlah Mata Kuliah 3 SKS : 4 Mata kuliah')
print(f'Mata Kuliah hari Selasa  : 2 Mata Kuliah')
print(f'Mata Kuliah hari Rabu    : 1 Mata Kuliah')
print(f'Mata Kuliah hari Kamis   : 3 Mata Kuliah')
print(f'Mata Kuliah hari Jumat   : 2 Mata Kuliah')
print()

sp    = 80
print(Tanda.upper().center(80))
print('\n'*3)
print(Nama.upper().center(80))
