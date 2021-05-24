__author__="kvda"

class myClass():

    def myFunc(self):
        offsetRerata = 0
        print("Aplikasi Nilai Mahasiswa")
        print("-----")
        jumlahMahasiswa = input("Masukkan Jumlah Mahasiswa : ")
        offset=0
        while offset<int(jumlahMahasiswa):
            print("Mahasiswa ke-",offset+1)
            print("---")
            nim     =   input("NIM : ")
            nama    =   input("Nama : ")
            nilaiTugas  =   input("Nilai Tugas : ")
            nilaiUTS    =   input("Nilai UTS : ")
            nilaiUAS    =   input("Nilai UAS : ")
            totalNilai = (int(nilaiTugas)+int(nilaiUTS)+int(nilaiUAS))/3
            offsetRerata+=int(totalNilai)
            print("Total Nilai : ",totalNilai)
            offset+=1
        rerata = int(offsetRerata)/int(jumlahMahasiswa)
        print("Rata-rata total nilai : ",rerata)
if __name__ == '__main__':
    myClass().myFunc()