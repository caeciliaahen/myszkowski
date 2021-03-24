import numpy as np, string, random
from collections import Counter

print("PROGRAM ENKRIPSI-DEKRIPSI MYSZKOWSKI TRANSPOSITION\n")
print("[MENU]")
print(" [1] Enkripsi")
print(" [2] Dekripsi")
na = 0
while na==0:
    pilih = input("Pilih menu: ")

    if pilih == "1":
        na=1
        teks = input("\nMasukkan teks yang ingin dienkripsi: ")
        teks = teks.replace(" ", "")
        teks = teks.upper()
        kunci = input("Masukkan kunci: ")
        kunci = list(kunci.upper())
        sortkunci = []
        sortkunci.append(kunci)
        sortkunci.append([])
        i = 0
        while i<len(kunci):
            sortkunci[1].append(i+1)
            i+=1
        sortkunci = np.array(sortkunci)
        newsortkunci = sortkunci [ :, sortkunci[0].argsort()]
        sortkunci = newsortkunci.tolist()
        sortkunci.append([])
        hitung = Counter(sortkunci[0])
        i = 0
        n = 1
        while i<len(kunci):
            if hitung[sortkunci[0][i]]>1:
                for j in range(hitung[sortkunci[0][i]]):
                    sortkunci[2].append(n)
                i+=(hitung[sortkunci[0][i]]-1)
            else:
                sortkunci[2].append(n)
            n+=1
            i+=1
        sortkunci = np.array(sortkunci)
        newsortkunci = sortkunci [ :, sortkunci[1].argsort()]
        print("\n🔑:"+np.array2string(newsortkunci[2],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        enkripsi = []
        enkripsi.append(kunci)
        for i in range (0, len(teks), len(kunci)):
            x = teks[i:i+len(kunci)]
            x = list(x)
            enkripsi.append(x)
        while len(enkripsi[len(enkripsi)-1])<len(kunci):
            enkripsi[len(enkripsi)-1].append(random.choice(string.ascii_uppercase))
        enkripsi = np.array(enkripsi)
        print(" "+np.array2string(enkripsi[1:len(enkripsi)],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        newenkripsi = enkripsi [ :, enkripsi[0].argsort()]
        hitung = Counter(newenkripsi[0])
        hasil = []
        i = 0
        while i < len(newenkripsi[0]):
            if hitung[newenkripsi[0][i]] == 1:
                for j in range(1, len(newenkripsi)):
                    hasil.append(newenkripsi[j][i])
            else:
                for j in range(1, len(newenkripsi)):
                    for k in range(i, hitung[newenkripsi[0][i]] + i):
                        hasil.append(newenkripsi[j][k])
                i += (hitung[newenkripsi[0][i]] - 1)
            i += 1
        print("\nHasil enkripsi =", end=' ')
        for i in range(len(hasil)):
            print(hasil[i], end='')
            if (i + 1) % (len(newenkripsi) - 1) == 0:
                print(" ", end='')

    elif pilih == "2":
        na=2
        teks = input("\nMasukkan teks yang ingin didekripsi: ")
        teks = teks.replace(" ", "")
        teks = list(teks.upper())
        kunci = input("Masukkan kunci: ")
        kunci = list(kunci.upper())
        sortkunci = []
        sortkunci.append(kunci)
        sortkunci.append([])
        i = 0
        while i<len(kunci):
            sortkunci[1].append(i+1)
            i+=1
        sortkunci = np.array(sortkunci)
        newsortkunci = sortkunci [ :, sortkunci[0].argsort()]
        sortkunci = newsortkunci.tolist()
        sortkunci.append([])
        hitung = Counter(sortkunci[0])
        i = 0
        n = 1
        while i<len(kunci):
            if hitung[sortkunci[0][i]]>1:
                for j in range(hitung[sortkunci[0][i]]):
                    sortkunci[2].append(n)
                i+=(hitung[sortkunci[0][i]]-1)
            else:
                sortkunci[2].append(n)
            n+=1
            i+=1
        sortkunci = np.array(sortkunci)
        newsortkunci = sortkunci [ :, sortkunci[1].argsort()]
        print("\n🔑:"+np.array2string(newsortkunci[2],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        dekripsi = []
        dekripsi.append(kunci)
        dekripsi.append([])
        i = 0
        while i<len(kunci):
            dekripsi[1].append(i+1)
            i+=1
        dekripsi = np.array(dekripsi)
        newdekripsi = dekripsi [ :, dekripsi[0].argsort()]
        dekripsi = newdekripsi.tolist()
        for i in range(int(len(teks)/len(kunci))):
            dekripsi.append([])
        hitung = Counter(dekripsi[0])
        indeks = 0
        i = 0
        while i<len(kunci):
            if hitung[dekripsi[0][i]]>1:
                for k in range(2,int((len(teks)/len(kunci))+2)):
                    for j in range(hitung[dekripsi[0][i]]):
                        dekripsi[k].append(teks[indeks])
                        indeks+=1
                i+=(hitung[dekripsi[0][i]]-1)
            else:
                for k in range(2, int((len(teks) / len(kunci)) + 2)):
                    dekripsi[k].append(teks[indeks])
                    indeks+=1
            i+=1
        dekripsi = np.array(dekripsi)
        hasil = dekripsi [ :, dekripsi[1].argsort()]
        print(" "+np.array2string(hasil[2:len(hasil)],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        print("\nHasil dekripsi =", end=' ')
        for i in range(2,len(hasil)):
            for j in range(len(hasil[0])):
                print(hasil[i][j], end='')
    else:
        print("[!] Silakan masukkan pilihan yang sesuai.")