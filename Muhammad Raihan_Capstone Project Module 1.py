#List dictionary untuk menyimpan stok gudang baik yang akan diinput maupun yang sudah exist
stok_gudang = [ 
    {'Kode Barang': 'BB1001',
     'Nama Barang': 'BENG-BENG',
     'Harga Beli': 30000,
     'Harga Jual' : 35000,
     'Stok Akhir' : 45,
     'Jenis Barang' : 'SNACK',
     'Satuan' : 'DUS'
     },
     {'Kode Barang': 'NG1001',
     'Nama Barang': 'NUGGET HURUF',
     'Harga Beli': 35000,
     'Harga Jual' : 42000,
     'Stok Akhir' : 22,
     'Jenis Barang' : 'BAHAN MAKANAN',
     'Satuan' : 'PCS'
     },
    {'Kode Barang': 'SM2001',
     'Nama Barang': 'SPIDOL MERAH',
     'Harga Beli': 48000,
     'Harga Jual' : 60000,
     'Stok Akhir' : 62,
     'Jenis Barang' : 'ATK',
     'Satuan' : 'DUS'
     },
    {'Kode Barang': 'YP1002',
     'Nama Barang': 'YUPI LOVE',
     'Harga Beli': 60000,
     'Harga Jual' : 72000,
     'Stok Akhir' : 42,
     'Jenis Barang' : 'SNACK',
     'Satuan' : 'DUS'
     },
     {'Kode Barang': 'PC1001',
     'Nama Barang': 'POCARI SWEAT',
     'Harga Beli': 72000,
     'Harga Jual' : 96000,
     'Stok Akhir' : 16,
     'Jenis Barang' : 'MINUMAN',
     'Satuan' : 'DUS'
     },
     {'Kode Barang': 'NS4001',
     'Nama Barang': 'NUTRISARI',
     'Harga Beli': 156000,
     'Harga Jual' : 180000,
     'Stok Akhir' : 33,
     'Jenis Barang' : 'MINUMAN',
     'Satuan' : 'DUS'
     },
     {'Kode Barang': 'PP5001',
     'Nama Barang': 'PULPEN HITAM',
     'Harga Beli': 30000,
     'Harga Jual' : 40000,
     'Stok Akhir' : 18,
     'Jenis Barang' : 'ATK',
     'Satuan' : 'DUS'
     },
      {'Kode Barang': 'BR6001',
     'Nama Barang': 'BERAS 1 KG',
     'Harga Beli': 120000,
     'Harga Jual' : 150000,
     'Stok Akhir' : 36,
     'Jenis Barang' : 'BAHAN MAKANAN',
     'Satuan' : 'PCS'
     }
    ] 

#Fungsi untuk print data dalam bentuk tabel
def print_table(data): 
    def create_row(data, column_widths):
        row = "|"
        for col, width in column_widths.items():
            row += f" {data.get(col, ''):{width}} |"
        return row

    columns = data[0].keys()
    col_widths = {col: max(len(col), max(len(str(row[col])) for row in data)) for col in columns}

    header = create_row({col: col for col in columns}, col_widths)

    line = "+".join("-" * (width + 2) for width in col_widths.values())
    print(line)
    print(header)
    print(line)

    for row in data:
        print(create_row(row, col_widths))

    print(line)

#Tampilan Menu Utama
def menu_utama(): 
    start = True
    while start :
        try :    
            intputmenuutama = int(input('''
                SELAMAT DATANG DI PROGRAM MONITORING STOCK
                          CV. MAJU MUNDUR KENA
                        GROSIR NOMOR 1 DI BEKASI
                -------------------------------------------
                        
                Menu Utama :
                1. Daftar Stok Terkini
                2. Tambah Stok Barang
                3. Update Stok Barang
                4. Hapus Stok Barang
                5. Exit Program
                
                Masukan Angka 1-5 untuk memilih menu diatas : '''))
            if intputmenuutama == 1:
                menu1()
            elif intputmenuutama == 2 :
                menu2()
            elif intputmenuutama == 3 :
                menu3()
            elif intputmenuutama == 4 :
                menu4()
            elif intputmenuutama == 5:
                print('Terima kasih, sampai jumpa kembali!')
                start = False
                break
            else :
                print('Input yang anda masukan salah!')
        except ValueError :
            print('Input yang anda masukan salah!')

#Tampilan Menu untuk read data
def menu1() :
    try :    
        inputmenu1 = int(input('''
                    Selamat Datang di Menu daftar stok CV. MAJU MUNDUR KENA
                        
                    1. Tampilkan semua data stok yang ada
                    2. Cari barang
                    3. Filter barang berdasarkan jenis barang
                    4. Kembali ke menu utama
                                
                    Masukan angka 1-4 : '''))
        if inputmenu1 == 1 :
            if not stok_gudang :
                print('Stok gudang saat ini kosong')
            else :
                print_table(stok_gudang)
        elif inputmenu1 == 2 :
            hasil_cari = None
            cari_stok = input('Masukan nama barang/kode barang yang ingin dicari :').upper()
            for stok in stok_gudang :
                if cari_stok == stok['Nama Barang'] or cari_stok == stok['Kode Barang'] :
                    print ('\tBERIKUT STOK BARANG YANG ANDA CARI :')
                    print_table([stok])
                    hasil_cari == stok
                    break
            else :
                print('Barang yang anda cari tidak ada di data stok gudang!')
        elif inputmenu1 == 3 :
            try:
                jenis_barang =  {
                    1: 'SNACK',
                    2: 'MINUMAN',
                    3: 'ATK',
                    4: 'BAHAN MAKANAN',
                    5: 'ELEKTRONIK',
                    6: 'BUMBU DAPUR',
                    7: 'OTHERS'
                }
                filter_stok = int(input('''Jenis barang apa yang ingin anda filter :
                                
                                1. SNACK
                                2. MINUMAN
                                3. ATK
                                4. BAHAN MAKANAN
                                5. ELEKTRONIK
                                6. BUMBU DAPUR
                                7. OTHERS
                                
                                Masukan angka 1-7 : '''))
                if filter_stok in range(1, 8):
                    filtered_items = [item for item in stok_gudang if item['Jenis Barang'] == jenis_barang[filter_stok]]
                    if not filtered_items:
                        print('Tidak ada barang di dalam kategori tersebut!')
                    else:
                        print("Berikut tabel untuk jenis barang tersebut :")
                        print_table(filtered_items)
            except ValueError :
                print('Input yang anda masukan tidak valid!')
            
        elif inputmenu1 == 4 :
            menu_utama()
        else : 
            print('Input yang anda masukan salah!')
    except ValueError :
        print('Input yang anda masukan salah!')
            
#Tampilan menu untuk create/menambahkan data ke dalam stok gudang         
def menu2() :
    try :
        inputmenu2 = int(input('''
                    Selamat Datang di Menu Tambah Stok CV. MAJU MUNDUR KENA
                            
                    1. Menambahkan barang ke data stok
                    2. Kembali ke menu utama
                            
                    Masukan angka 1-2 : '''))
        if inputmenu2 == 1 :
            print('Selamat datang di Menu Menambahkan Barang CV. MAJU MUNDUR KENA')
            while True :
                tam_kode = input('Masukan Kode Barang yang anda ingin tambahkan ke daftar stok (6 DIGIT) :').upper()
                if len(tam_kode) != 6 :
                    print('Kode Barang harus 6 digit')
                else :
                    break
            tam_nama = input('Masukan Nama Barang yang anda ingin tambahkan ke daftar stok :').upper()

            for stok in stok_gudang :
                if tam_kode == stok['Kode Barang'] or tam_nama == stok ['Nama Barang'] :
                    print('Barang sudah ada di daftar stok, silahkan ke menu Update Stok jika ingin menambah stok barang')
                    continue
                elif tam_kode != stok['Kode Barang'] or tam_nama != stok ['Nama Barang'] :
                    try :
                        tam_hargabeli = int(input('Masukan Harga Beli barang yang anda ingin tambahkan ke daftar stok :'))
                        tam_hargajual = int(input('Masukan Harga Jual barang yang anda ingin tambahkan ke daftar stok :'))
                        tam_stok = int(input('Masukan Jumlah Stok barang yang anda ingin tambahkan ke daftar stok :')) 
                        tam_jenis = int(input('''Jenis barang yang ingin diinput :
                                            1. SNACK
                                            2. MINUMAN
                                            3. ATK
                                            4. BAHAN MAKANAN
                                            5. ELEKTRONIK
                                            6. BUMBU DAPUR
                                            7. OTHERS
                                            
                                            Masukan angka 1-7 : '''))
                        if tam_jenis == 1 :
                            tam_jenis = 'SNACK'
                        elif tam_jenis == 2 :
                            tam_jenis = 'MINUMAN'
                        elif tam_jenis == 3 :
                            tam_jenis = 'ATK'
                        elif tam_jenis == 4 :
                            tam_jenis = 'BAHAN MAKANAN'
                        elif tam_jenis == 5 :
                            tam_jenis = 'ELEKTRONIK'
                        elif tam_jenis == 6 :
                            tam_jenis = 'BUMBU DAPUR'
                        elif tam_jenis == 7 :
                            tam_jenis = 'OTHERS' 
                        else :
                            print('Input yang anda masukan tidak valid')
                        tam_satuan = input('Masukan Satuan Stok barang yang anda ingin tambahkan ke daftar stok :').upper()

                        print(' Kode Barang : {}\n Nama Barang : {}\n Harga Beli : {}\n Harga Jual : {}\n Stok Akhir : {}\n Jenis Barang : {}\n Satuan : {}'
                              .format(tam_kode,tam_nama,tam_hargabeli,tam_hargajual,tam_stok,tam_jenis,tam_satuan))
                        save_stok = input('Apakah anda sudah yakin dengan inputan diatas (Yes or No) : ').upper()
                        if save_stok == 'YES' :
                            stok_gudang.append(
                                {'Kode Barang' : tam_kode,
                                'Nama Barang' : tam_nama,
                                'Harga Beli' : tam_hargabeli,
                                'Harga Jual' : tam_hargajual,
                                'Stok Akhir' : tam_stok,
                                'Jenis Barang' : tam_jenis,
                                'Satuan' : tam_satuan
                                })
                            print('Barang berhasil ditambahkan!')
                            print('Berikut stok terupdate gudang anda!')
                            print_table(stok_gudang)
                            menu_utama()
                        elif save_stok =='NO' :
                            print('Barang anda belum disimpan, silahkan input ulang')
                            menu2()
                        else :
                            print('Input anda salah, masukan ulang!')
                            menu2()
                    except ValueError :
                        print('Input yang anda masukan salah!')
        if inputmenu2 == 2 :
            menu_utama()
    except ValueError :
        print('Input yang anda masukan salah!')

#Tampilan menu untuk update data yang ada di stok gudang
def menu3() :
    try :
        inputmenu3 = int(input('''
                    Selamat Datang di Menu Update Stok CV. MAJU MUNDUR KENA
                            
                    1. Update data stok
                    2. Kembali ke menu utama
                            
                    Masukan angka 1-2 : '''))
        if inputmenu3 == 1 :
            if not stok_gudang :
                print('Saat ini tidak ada barang apapun di stok gudang anda!')
            else :
                print_table(stok_gudang)
                hasil_cari = None
                stok_update = input('\nMasukan Kode Barang atau Nama Barang yang ingin anda Update :').upper()
                for stok in stok_gudang :
                    if stok_update == stok['Kode Barang'] or stok_update == stok['Nama Barang'] :
                        stokawal = stok.copy()
                        print_table([stok])
                        hasil_cari == stok
                        
                        save_update1 = input(f'Apakah anda yakin ingin melakukan update {stok_update} (Yes/No)?').upper()
                        if save_update1 == 'YES' :
                            option_update = input('''
                                            Menu Update Stok :
                                            1. Update Kode Barang
                                            2. Update Nama Barang
                                            3. Update Harga Beli
                                            4. Update Harga Jual
                                            5. Update Stok Barang
                                            6. Update Jenis Barang
                                            7. Update Satuan Barang
                                                    
                                            Pilih angka 1-7 :''')
                            if option_update == '1':
                                while True :
                                    update_kode = input('Masukan Kode Barang terbaru (6 DIGIT):').upper()
                                    if len(update_kode) != 6 :
                                        print('Kode Barang harus 6 digit')
                                    else :
                                        break
                                stok['Kode Barang'] = update_kode
                            elif option_update == '2':
                                update_nama = input('Masukan Nama Barang terbaru :').upper()
                                stok['Nama Barang'] = update_nama
                            elif option_update == '3':
                                try :
                                    update_hargabeli = int(input('Masukan Harga Beli terbaru :'))
                                    stok['Harga Beli'] = update_hargabeli
                                except ValueError :
                                    print('Input yang anda masukan salah, harus numerik!')
                            elif option_update == '4':
                                try :
                                    update_hargajual = int(input('Masukan Harga Jual terbaru :'))
                                    stok['Harga Jual'] = update_hargajual
                                except ValueError :
                                    print('Input yang anda masukan salah, harus numerik!')
                            elif option_update == '5':
                                try :
                                    update_stok = int(input('Masukan Stok Barang terbaru :'))
                                    stok['Stok Akhir'] = update_stok
                                except ValueError :
                                    print('Input yang anda masukan salah, harus numerik!')
                            elif option_update == '6':
                                try : 
                                    update_jenis = int(input('''Masukan jenis barang anda yang terbaru :
                                              1. SNACK
                                              2. MINUMAN
                                              3. ATK
                                              4. BAHAN MAKANAN
                                              5. ELEKTRONIK
                                              6. BUMBU DAPUR
                                              7. OTHERS
                                              
                                              Masukan angka 1-7 : '''))
                                    if update_jenis == 1 :
                                        update_jenis = 'SNACK'
                                    elif update_jenis == 2 :
                                        update_jenis = 'MINUMAN'
                                    elif update_jenis == 3 :
                                        update_jenis = 'ATK'
                                    elif update_jenis == 4 :
                                        update_jenis = 'BAHAN MAKANAN'
                                    elif update_jenis == 5 :
                                        update_jenis = 'ELEKTRONIK'
                                    elif update_jenis == 6 :
                                        update_jenis = 'BUMBU DAPUR'
                                    elif update_jenis == 7 :
                                        update_jenis = 'OTHERS'
                                    else :
                                        print('Input yang anda masukan tidak valid!')
                                        menu3()
                                    stok['Jenis Barang'] = update_jenis
                                except ValueError :
                                    print('Input yang anda masukan salah, harus numerik!')
                            elif option_update == '7':
                                update_satuan = input('Masukan Satuan Barang terbaru :')
                                stok['Satuan'] = update_satuan
                            else :
                                print('Input tidak valid')
                            save_update2 = input('Apakah anda yakin ingin menyimpan update ini (Yes/No) :').upper()
                            if save_update2 == 'NO':
                                for item in stok_gudang :
                                        item['Kode Barang'] = stokawal['Kode Barang']
                                        item['Nama Barang'] = stokawal['Nama Barang']
                                        item['Harga Beli'] = stokawal['Harga Beli']
                                        item['Harga Jual'] = stokawal['Harga Jual']
                                        item['Stok Akhir'] = stokawal['Stok Akhir']
                                        item['Jenis Barang'] = stokawal['Jenis Barang']
                                        item['Satuan'] = stokawal['Satuan']
                                print('Update dibatalkan!')
                                menu3()
                            elif save_update2 == 'YES' :
                                print('Update berhasil disimpan! Berikut stok gudang anda\n')
                                print_table(stok_gudang)
                                menu3()
                        elif save_update1 == 'NO' :
                            print('Update stok gudang dibatalkan!')
                            menu3()
                else :
                    print('Barang tidak ditemukan di Stok Gudang Anda!')
                    menu3()
        elif inputmenu3 == 2 :
            menu_utama()
        else :
            print('Input yang anda masukan tidak valid!')
    except ValueError :
        print('Input yang anda masukan salah!')

#Tampilan menu untuk delete data yang ada di stok gudang
def menu4() :
    try :
        inputmenu4 = int(input('''
                    Selamat Datang di Menu Delete Stok CV. MAJU MUNDUR KENA
                            
                    1. Delete 1 Barang di Stok Gudang
                    2. Delete semua barang yang ada di Stok Gudang
                    3. Kembali ke menu utama
                            
                    Masukan angka 1-3 : '''))
        if inputmenu4 == 1:
            if not stok_gudang :
                print('Saat ini tidak ada barang apapun di stok gudang anda!')
            else :
                print_table(stok_gudang)
                stok_delete = input('\nMasukan Kode Barang atau Nama Barang yang ingin anda Delete :').upper()
                for stok in stok_gudang :
                    if stok_delete == stok['Kode Barang'] or stok_delete == stok['Nama Barang'] :
                        print('Stok barang yang ingin anda hapus :')
                        print_table([stok])

                        save_delete1 = input(f'Apakah anda yakin ingin melakukan delete stok {stok_delete} (Yes/No)?').upper()
                        if save_delete1 == 'YES' :
                            stok_gudang.remove(stok)
                            print('Stok telah dihapus dari daftar stok gudang!')
                            menu4()
                        elif save_delete1 == 'NO' :
                            print(f'Stok barang {stok_delete} tidak dihapus dari gudang!')
                            break
                        else :
                            print('Input yang anda masukan salah!')
                else :
                    print('Barang tidak ditemukan di stok gudang!')
                    menu4()
        elif inputmenu4 == 2:
            if not stok_gudang:
                print('Saat ini tidak ada barang apapun di stok gudang anda!')
            else : 
                print_table(stok_gudang)
                clear_stok = input('Apakah anda yakin ingin menghapus semua daftar stok gudang? (Yes/No)').upper()
                if clear_stok == 'YES' :
                    stok_gudang.clear()
                    print('Semua stok gudang berhasil dihapus!')
                elif clear_stok == 'NO' :
                    print('Stok gudang tidak jadi dihapus semua!')
                else :
                    print('Input yang anda masukan salah!')
        elif inputmenu4 == 3:
            menu_utama()
    except ValueError :
        print('Input yang anda masukan salah!')

menu_utama()
