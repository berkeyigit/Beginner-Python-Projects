
#Functionumuzu olusturuyoruz
def ceaser_cipher(metin,anahtar,islem):

    #Harfleri tanimliyoruz
    buyuk_harfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    kucuk_harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

    sonuc = ""

    #Donguye gore girilen harfleri indexe ekliyoruz.
    for harf in metin:
        if harf in buyuk_harfler:
            alfabe = buyuk_harfler
        elif harf in kucuk_harfler:
            alfabe = kucuk_harfler
        else:
            sonuc += harf
            continue

        index = alfabe.index(harf)

        #Bu harfleri 'anahtar' sayisi kadar ileri veya geriye goturuyoruz. Bu her girilen harf icin tekrar ediliyor hala dongude.
        if islem=="e":
            yeni_harf = (index + anahtar) % len(alfabe)
        elif islem == "d":
            yeni_harf = (index - anahtar) % len(alfabe)
        else:
            print("Lütfen Gecerli bir islem giriniz (E/D): ")
        
        sonuc += alfabe[yeni_harf]

    return sonuc    


metin = input("Lütfen metni giriniz : ")
anahtar = int(input("Lütfen anahtari (0-28) giriniz : "))

# Anahtar 29dan buyuk ise kendisine geri donecegi icin bir anlami yok bu yuzden boyle sınırlıyoruz.
if not (0 <= anahtar <= 28):
    print("Lütfen gecerli bir sayi giriniz (0-28) : ")
else:
    print(f"Anahtar : {anahtar}")

islem = input("Sifrelemek icin 'e',sifre cozmek icin 'd' giriniz : ")
sonuc = ceaser_cipher(metin,anahtar,islem)
print("Sonuc : ", sonuc)

