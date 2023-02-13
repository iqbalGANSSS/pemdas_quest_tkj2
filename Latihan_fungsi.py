def salam():
    print("Assalamualaikum akhi ukhty")
salam()


#buatlah fungsi versi kalian

def my_function(*kids):
  print("orang paling jelek di dunia" + " " +kids[2])

my_function("iqbal", "Wildan", "Vicky")

def my_function(buah):
  for x in buah:
    print(x)

buah = ["apel", "pisang", "salak"]

my_function(buah)


#Buatlah fungsi dengan 3 parameter
def Orang_Ganteng(orang1, orang2, orang3):
  print("Orang paling ganteng adalah :" + " " + orang3)
  print("Orang Paling Satir adalah :" + " " + orang2)
  print("orang paling sesat adalah :" + " " + orang1)

Orang_Ganteng(orang1 = "Vicky", orang2 = "Masbro", orang3 = "Iqbal")

def biografi(Nama, Domisili, Lahir):
    print("Nama Saya :", Nama)
    print("Domisili Saya :", Domisili)
    print("Saya Lahir Tahun :", Lahir)
biografi(Nama= "Iqbal", Domisili= "Depok", Lahir= 2007)

def segitiga():
    x = 0.5
    alas = input(int("Masukkan Nilai Alas"))
    tinggi = input(int("Masukkan Nilai tinggi"))
    luas = x*alas*tinggi
print("Luas bangun datar segitiga adalah %i")
segitiga()