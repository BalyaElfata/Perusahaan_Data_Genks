daftarKaryawan = {
    'star':{'NIP':'DG-001','Nama': 'Star Butterfly','Jenis Kelamin': 'Perempuan','Domisili': 'Jakarta','Divisi':'Operasional','Gaji':'Rp5.000.000'},
    'steve':{'NIP':'DG-002','Nama': 'Steve Harrington','Jenis Kelamin': 'Laki-laki','Domisili': 'Bandung','Divisi':'Marketing','Gaji':'Rp3.500.000'},
    'kobo':{'NIP':'DG-003','Nama': 'Kobo Kanaeru','Jenis Kelamin': 'Perempuan','Domisili': 'Pontianak','Divisi':'Finance','Gaji':'Rp4.500.000'},
    'lemon':{'NIP':'DG-004','Nama': 'Ikhsan Lemon','Jenis Kelamin': 'Laki-laki','Domisili': 'Banda Aceh','Divisi':'Manajerial','Gaji':'Rp10.000.000'},
    'subaru':{'NIP':'DG-005','Nama': 'Natsuki Subaru','Jenis Kelamin': 'Laki-laki','Domisili': 'Jepang','Divisi':'Operasional','Gaji':'Rp6.000.000'},
    'udin':{'NIP':'DG-006','Nama': 'Muhammad Samsudin','Jenis Kelamin': 'Laki-laki','Domisili': 'Bekasi','Divisi':'Kreatif','Gaji':'Rp2.000.000'}
}
n=len(daftarKaryawan)

def menampilkanDataKaryawan():
    while True:
        print('List Menu Menampilkan Data Karyawan:')
        print('1. Menampilkan Semua Data Karyawan')
        print('2. Menampilkan Data Karyawan tertentu')
        print('3. Kembali ke Menu Utama\n')
        opsi = input('Pilih menu : ')
        print()
        if opsi == '1':
            if len(daftarKaryawan) != 0:
                print('Daftar Karyawan')
                print('NIP\t| Nama \t\t\t| Jenis Kelamin\t| Domisili\t| Divisi\t| Gaji')
                for val in daftarKaryawan.values():
                    print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(val['NIP'],val['Nama'],val['Jenis Kelamin'],val['Domisili'],val['Divisi'],val['Gaji']))
                print()
            else:
                print('\nTidak Ada Data\n')
        elif opsi == '2':
            if len(daftarKaryawan) != 0:
                nipKaryawan = input('Masukkan NIP Karyawan: ')
                for val in daftarKaryawan.values():
                    if nipKaryawan == val['NIP']:
                        adaData = True
                        print('NIP\t| Nama \t\t\t| Jenis Kelamin\t| Domisili\t| Divisi\t| Gaji')
                        print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}\n'.format(val['NIP'],val['Nama'],val['Jenis Kelamin'],val['Domisili'],val['Divisi'],val['Gaji']))
                        break
                    adaData = False
                if adaData == False:
                    print('\nTidak Ada Data\n')
            else:
                print('\nTidak Ada Data\n')
        elif opsi == '3':
            break
        else:
            continue


def menambahDataKaryawan() :
    while True:
        print('List Menu Menambah Data Karyawan:')
        print('1. Menambah Data Karyawan')
        print('2. Kembali ke Menu Utama\n')
        opsi = input('Pilih menu : ')
        print()
        if opsi == '1':
            nipKaryawan = input('Masukkan NIP Karyawan : ')
            for val in daftarKaryawan.values():
                if nipKaryawan == val['NIP']:
                    adaData = True
                    print('\nData sudah ada\n')
                    break
                adaData = False
            if adaData == False:
                namaKaryawan = input('Masukkan Nama Karyawan : ')
                jenisKelaminKaryawan = input('Masukkan Jenis Kelamin Karyawan : ')
                domisiliKaryawan = input('Masukkan Domisili Karyawan : ')
                divisiKaryawan = input('Masukkan Divisi Karyawan : ')
                gajiKaryawan = input('Masukkan Gaji Karyawan : ')
                print()
                simpanData = input('Ingin menyimpan data?(Yes/No): ')
                if simpanData == 'Yes':
                    daftarKaryawan[namaKaryawan[:5].lower()] = {'NIP':nipKaryawan,'Nama': namaKaryawan,'Jenis Kelamin': jenisKelaminKaryawan,'Domisili': domisiliKaryawan,'Divisi':divisiKaryawan,'Gaji':gajiKaryawan}
                    global n; n = len(daftarKaryawan)
                    print('\nData Tersimpan\n')
                    continue
                else:
                    print()
                    continue
        elif opsi == '2':
            break
        else:
            continue

def mengubahDataKaryawan() :
    while True:
        print('List Menu Mengubah Data Karyawan:')
        print('1. Mengubah Data Karyawan')
        print('2. Kembali ke Menu Utama\n')
        opsi = input('Pilih menu : ')
        print()
        if opsi == '1':
            nipKaryawan = input('Masukkan NIP dari karyawan yang datanya ingin diubah : ')
            for key,val in daftarKaryawan.items():
                if nipKaryawan == val['NIP']:
                    adaData = True
                    print('\nNIP\t| Nama \t\t\t| Jenis Kelamin\t| Domisili\t| Divisi\t| Gaji')
                    print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}\n'.format(val['NIP'],val['Nama'],val['Jenis Kelamin'],val['Domisili'],val['Divisi'],val['Gaji']))
                    lanjutUpdate = input('Apakah anda ingin melanjutkan update?(Yes/No): ')
                    if lanjutUpdate == 'Yes':
                        while True:
                            kolomUpdate = input('Masukkan kolom yang ingin diupdate: ')
                            if kolomUpdate in val:
                                break
                        nilaiUpdate = input('Masukkan nilai baru: ')
                        updateData = input('Update Data?(Yes/No) : ')
                        if updateData == 'Yes':
                            daftarKaryawan[key][kolomUpdate] = nilaiUpdate
                            print('\nData Terupdate\n')
                        else:
                            print()
                    else:
                        print()
                    break
                adaData = False
            if adaData == False:
                print('\nData yang anda cari tidak ada\n')
        elif opsi == '2':
            break
        else:
            continue

def menghapusDataKaryawan() :
    while True:
        print('List Menu Menghapus Data Karyawan:')
        print('1. Menghapus Data Karyawan')
        print('2. Kembali ke Menu Utama\n')
        opsi = input('Pilih menu : ')
        print()
        if opsi == '1':
            nipKaryawan = input('Masukkan NIP dari karyawan yang ingin dihapus : ')
            for key,val in daftarKaryawan.items():
                if nipKaryawan == val['NIP']:
                    adaData = True
                    del daftarKaryawan[key]
                    print('\nData deleted\n')
                    global n; n = len(daftarKaryawan)
                    break
                adaData = False
            if adaData == False:
                print('\nTidak Ada Data\n')
        elif opsi == '2':
            break
        else:
            continue

print('Selamat Datang di Perusahaan Data Genks\n')
while True :
    print('List Menu :')
    print('1. Menampilkan Data Karyawan')
    print('2. Menambah Data Karyawan')
    print('3. Memperbarui Data Karyawan')
    print('4. Menghapus DataKaryawan')
    print('5. Exit Program\n')
    pilihanMenu = input('Pilih menu : ')
    print()

    if(pilihanMenu == '1') :
        menampilkanDataKaryawan()
    elif(pilihanMenu == '2') :
        menambahDataKaryawan()
    elif(pilihanMenu == '3') :
        mengubahDataKaryawan()
    elif(pilihanMenu == '4') :
        menghapusDataKaryawan()
    elif(pilihanMenu != '5') :
        print('Pilihan yang anda masukkan salah')
    elif(pilihanMenu == '5') :
        break