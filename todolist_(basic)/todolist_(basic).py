def menu_goster(liste):
    print("TO DO LİST MENU}\n")
    print("1-Gorev Ekle")
    print("2-Gorev Sil")
    print("3-Liste Goster")
    print("4- Cikis")

def gorev_ekle(liste):
    print("\nCikis yapmak icin 'Q' giriniz.")
    while True:
        yeni_gorev = input("Lütfen eklemek istediginiz gorevi giriniz : ").lower()
        if yeni_gorev == "q":
            break
        else:
            liste.append(yeni_gorev)
            print("Gorev basari ile eklendi \n")

def gorev_sil(liste):
    if not liste:
        print("Liste bos")
        return
    
    liste_goster(liste)
    try:
        sil_index = int(input("\nSilmek istediginiz gorev dizinini seciniz"))
        silinen_gorev = liste.pop(sil_index)
        print(f"'{silinen_gorev}' basariyla silindi.")
    except(IndexError,ValueError):
        print("Gecersiz numara girildi")

def liste_goster(liste):
    print("\nAktif Liste : \n")
    for i,gorev in enumerate(liste,1):
        print(f"{i} - {gorev}")

yapilacaklar = []

while True:
    menu_goster(yapilacaklar)
    islem = int(input("Lütfen yapmak istediginiz islemin numarasini giriniz: "))
    if islem == 1:
        gorev_ekle(yapilacaklar)
    elif islem == 2:
        gorev_sil(yapilacaklar)
    elif islem == 3:
        liste_goster(yapilacaklar)
    elif islem == 4:
        print("Cikis yapiliyor.")
        break
    else:
        print("Gecersiz numara girisi.")
