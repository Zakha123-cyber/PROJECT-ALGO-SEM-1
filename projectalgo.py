import csv
import os
import datetime
from datetime import datetime
import time
from tabulate import tabulate

def loginuser():
    os.system('cls')
    print("==========CEK PLAT NOMOR==========")
    platnomor = str(input("Masukkan Plat Nomor : "))
    file = open('user.csv', 'r')
    F = False
    for line in file:
        item = line.split(',')
        if platnomor == item[2]:
            F = True
            break
    if F == True:
        print("Login Anda Berhasil")
    else :
        print("Login Anda Gagal")
        time.sleep(1)
        loginuser()
        

    with open('user.csv', 'r') as file_csv:
        data = []
        nilai_pencarian = platnomor
        reader = csv.reader(file_csv)
        header = next(reader) 
        indeks_kolom = None
        for i, kolom in enumerate(header):
            if kolom == 'NO. PLAT':
                indeks_kolom = i
                break

        for row in reader:
            if row[indeks_kolom] == nilai_pencarian:
                data = row
            
        def tanggal():
            os.system('cls')
            print(f"""
                {"-"*(60)}
                |{"MASUKKAN TANGGAL JATUH TEMPO".center(58)}|
                {"-"*(60)}
                  """)
            
            hari = int(input("Tanggal = "))
            if hari <= 31:
                pass
            else :
                print("Hari yang anda masukkan tidak valid")
                time.sleep(1)
                tanggal()

            bulan = int(input("Bulan = "))
            if bulan <= 12:
                pass
            else:
                print("Bulan yang Anda masukkan ngaworr!!")
                time.sleep(1)
                tanggal()
                
            tahun = input("Tahun = ")
            if len(tahun) >= 4 and (int(tahun)) >= 2000:
                pass
            else:
                print("Tahun yang Anda masukkan tidak benarr!!")
                time.sleep(1)
                tanggal()
            os.system('cls')    
            n = (f"{hari}/{bulan}/{tahun}")
            if len(n) <= 10:
                format_tanggal = "%d/%m/%Y"
                i = datetime.strptime(n, format_tanggal)
                u = datetime.strptime(data[5], format_tanggal)
                z = u - i
                t = i - u
                tahun_sisa = 0
                bulan_sisa = 0
                hari_sisa = 0
               
                if i == u:
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    print("Status \t\t= Anda Telah Memasuki Jatuh Tempo Pembayaran")
                elif i < u:
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    if int(str(z.days)) > 365:
                        tahun_sisa += z.days // 365
                        bulan_sisa += (z.days % 365) // 30
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {tahun_sisa} tahun {bulan_sisa} bulan lagi")
                    elif int(str(z.days)) > 30:
                        bulan_sisa += z.days // 30
                        hari_sisa += z.days % 30
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {bulan_sisa} bulan {hari_sisa} hari lagi")
                    else:
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {z.days} hari lagi")
                elif i > u:
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    if int(str(t.days)) > 365:
                        tahun_sisa += t.days // 365
                        bulan_sisa += (t.days % 365) // 30
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {tahun_sisa} tahun {bulan_sisa} bulan !!!")
                    elif int(str(t.days)) > 30:
                        bulan_sisa += t.days // 30
                        hari_sisa += t.days % 30
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {bulan_sisa} bulan {hari_sisa} hari !!!")
                    else:
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {t.days} hari !!!")
            else:
                print("Tanggal yang Anda masukkan tidak benar!")
                tanggal()
            
            print("\n\n=====TEKAN APA SAJA UNTUK KEMBALI=====")
            e = input("")
            if e == "":
                menu()
            else :
                menu()
                
        def pembayaran():
            os.system('cls')
            motor = 300000
            mobil = 750000
            format_tanggal = "%d/%m/%Y"
            i = datetime.strptime(data[5], format_tanggal)
            u = datetime.now()
            s = str((u-i).days)
            n = (u-i) // 30
            m = str(n.days)
            telat_tahun = 0
            telat_bulan = 0
            telat_hari = 0
            denda = int(0)
            biaya_total = int(0)

            if int(s) <= 0 and int(m) < 1:
                print("="*60)
                print("".center(58))
                print (f"MANTAPPP ANDA DISIPLIN MEMBAYAR PAJAK".center(58))
                print("".center(58))
                print("="*60)
                if data[4] == "Motor":
                    biaya_total += motor
                elif data[4] == "Mobil":
                    biaya_total += mobil
                print (f"\n\t Biaya Total Pajak Anda adalah = Rp. {int(biaya_total)}".center(60))
                print("".center(58))
                print("="*60)
            elif int(s) >= 2 and int(m) <= 1:
                if int(s) > 365:
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                elif int(s) > 30:
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print("="*70)
                    print("".center(68))
                    print(f"==========YAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI==========".center(68))
                    print("".center(68))
                    print("="*70)
                if data[4] == "Motor":
                    denda += motor*(25/100)
                    biaya_total += motor + denda
                elif data[4] == "Mobil":
                    denda += mobil*(25/100)
                    biaya_total += mobil + denda
                print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68))
                print("".center(68))
                print("="*70)
                print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                print("".center(68))
                print("="*70)
            elif int(m) > 1 and int(m) <= 2:
                if int(s) > 365:
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                elif int(s) > 30:
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print("="*70)
                    print("".center(68))
                    print(f"YAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                    
                if data[4] == "Motor":
                    denda += (motor*25/100*2//12)+32000
                    biaya_total += motor + denda
                elif data[4] == "Mobil":
                    denda += (mobil*25/100*2//12)+32000
                    biaya_total += mobil + denda
                    print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68)) 
                    print("".center(68))
                    print("="*70)
                    print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                    print("".center(68))
                    print("="*70)
            else :
                if int(s) > 365:
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                elif int(s) > 30:
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print(f"\nYAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI".center(68))
                    print("".center(68))
                    print("="*70)

                if data[4] == "Motor":
                    denda += (motor*25/100*6//12)+32000
                    biaya_total += motor + denda
                elif data[4] == "Mobil":
                    denda += (mobil*25/100*6//12)+32000
                    biaya_total += mobil + denda
                print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68))
                print("".center(68))
                print("="*70)
                print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                print("".center(68))
                print("="*70)
                
            def bayar():
                i = input("\n\nApakah anda akan membayar? [y/n] : ")
                while i :
                    fuad = ""
                    if i == "y" :
                        os.system('cls')
                        print("\n----------Pilih Metode Pembayaran----------")
                        print("1. Online")
                        print("2. Offline")
                        u = int(input("Online atau Offline : "))
                        if u == 1 :
                            fuad += "Online"
                            print("\n----------Pembayaran Online----------")
                            print("1. Dana")
                            print("2. M-Banking")
                            k = input("Pilih Metode pembayaran = ")
                            if k == "1":
                                os.system('cls')
                                print("\n====================================================")
                                print("========== S T R U K   P E M B A Y A R A N =========")
                                print("====================================================")
                                print ("Nama\t\t\t:", data[3])
                                print ("NIM\t\t\t:", data[1])
                                print ("Plat Nomor\t\t:", data[2])
                                print ("Jenis Kendaraan\t\t:", data[4])
                                print ("Biaya\t\t\t: Rp.", int(biaya_total))
                                print ("Metode Pembayaran\t:", fuad)
                                print("====================================================")
                                print("====================================================")
                                print("\n\n ==========TEKAN APASAJA UNTUK KEMBALI KE MENU==========")
                                j = input("")
                                if j == "":
                                    menu()
                                else:
                                    menu()
                                    break
                            elif k == "2":
                                os.system('cls')
                                print("\n====================================================")
                                print("========== S T R U K   P E M B A Y A R A N =========")
                                print("====================================================")
                                print ("Nama\t\t\t:", data[3])
                                print ("NIM\t\t\t:", data[1])
                                print ("Plat Nomor\t\t:", data[2])
                                print ("Jenis Kendaraan\t\t:", data[4])
                                print ("Biaya\t\t\t: Rp.", int(biaya_total))
                                print ("Metode Pembayaran\t:", fuad)
                                print("====================================================")
                                print("====================================================")
                                print("\n\n ==========TEKAN APASAJA UNTUK KEMBALI KE MENU==========")
                                j = input("")
                                if j == "":
                                    menu()
                                else:
                                    menu()
                                    break
                            else :
                                print("Pilihan Anda Salah")
                                print("\n ==========TEKAN APASAJA UNTUK KEMBALI KE MENU==========")
                                j = input("")
                                if j == "":
                                    menu()
                                else:
                                    menu()
                                    break
                                
                        elif u == 2 :
                            fuad += "Offline"
                            sm = input("Masukkan Kota Anda = ")
                            os.system('cls')
                            print("\n\n\t\t\t\tSILAHKAN MENUJU SAMSAT TERDEKAT\n\n".center(100))
                            with open('samsatbaru.csv', 'r') as f:
                                samsat = []
                                reader = csv.reader(f)
                                header = next(reader)
                                indeks_kolom = None
                                for i, kolom in enumerate(header):
                                    if kolom == 'KOTA':
                                        indeks_kolom = i
                                        break
                                for row in reader:
                                    if row[indeks_kolom] == sm:
                                        samsat = row
                                        tabel_samsat = [header, samsat]
                                        table = tabulate(tabel_samsat, tablefmt='grid')
                                        print(table)
                                g = input("\n\t\t\t=====TEKAN APA SAJA UNTUK KEMBALI KE MENU AWAL=====")
                            if g == "":
                                loginuser()
                            else :
                                loginuser()
                                
                        else :
                            print("input anda salah")
                            time.sleep(0.5)
                            bayar()
                            
                    elif i == "n" :
                        menu()
                        break
                    else :
                        print("input anda salah")
                        time.sleep(0.5)
                        bayar()
                        break
        
            bayar()
                        
    def menu():
        os.system('cls')
        print(f"""
        {"-"*(60)}
        |{"PILIH MENU".center(58)}|   
        |{"-"*(58)}|   
        |{"[1] Jatuh Tempo".ljust(58)}|
        |{"[2] Bayar".ljust(58)}|
        |{"[3] Cek Plat Nomor Ulang".ljust(58)}|
        |{''.center(58)}|   
        {"-"*(60)}
                    """)
        p = int(input("Menu yang diinginkan = "))
        if p == 1:
            tanggal()
        elif p == 2:
            pembayaran()
        elif p == 3:
            loginuser()
        else:
            print("Menu tidak valid")
            time.sleep(0.5)
            menu()
    
    time.sleep(1)
    menu()
    
loginuser()

