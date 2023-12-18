print('praktikum-a3\n')
nama   = 'Retno Helviani'
nim    = '231031008'
meet   = 'praktikum 3'
prodi  = 'sistem informasi A'
ttl    = 'Pinrang, 22-11-2004'
alamat = 'Pinrang'
asal   = 'Pinrang'
hobi   = 'Mendengar Musik'
tinggi = '163'
email  = 'retnohelviani01@gmail.com'

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)
print('\n')

print(f'''Halo, nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()},
ini adalah file {meet.capitalize()}.Terima kasih.
   ''')

print(f''' Biodata saya,
Namas\t:{nama.title()}
NIM\t:{nim}
Prodi\t:{prodi.title()}
TTL\t:{ttl}
Alamat\t:{alamat}
Asal\t:{asal}
Hobi\t:{hobi}
Tinggi\t:{tinggi}cm
   ''')


stat = 'sir issac newton'
up   = stat.upper()
print(up)
up   = up.split()            # up menjadi list 3 item
print(up)
print(up[2][0],up[0],up[1])       #N SIR ISSAC
print(up[2],up[0][0],up[1][0])
print()

stat2 = '&sir$ @issac# *newton.'
up2   = stat2.upper()
print(up)
up2   = up2.split()
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print('SIR ISSAC NEWTON')









