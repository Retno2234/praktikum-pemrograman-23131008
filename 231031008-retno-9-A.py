biodata = {'Nama' : 'Retno helviani\'',
 'Nim' : '231031008',
 'Prodi' : 'Sistem Informasi',
 'TTL' : 'Pinrang, 22 November 2004',
 'Alamat' : 'Perumnas Carawali',
 'Kel/desa' : 'Benteng Sawitto',
 'Kecamatan' : 'Paleteang',
 'Hobi' : 'Mendengar music and olahraga',
 'Nama Orang Tua' : {'Ayah' :'Pampangkaraeng',
 'Ibu' : 'Nurlia',}
 
}
print()
print(biodata)
print()
print(biodata['Nama'])
print(biodata.get('Nim'))
print(biodata.get('prodi'))
print(biodata.get('TTL'))
print(biodata.get('Alamat'))
print(biodata.get('Kel/Desa'))
print(biodata.get('Kecamatan'))
print(biodata['Hobi'])
print(biodata['Nama Orang Tua']['Ayah'])
print(biodata['Nama Orang Tua']['Ibu'])
