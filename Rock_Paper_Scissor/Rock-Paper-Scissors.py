import random as rnd

#Girizgah
print("\n" + "*"*83 + "\n")
print("\t\tTAS - KAGIT - MAKAS OYUNUNA HOS GELDİNİZZ !!!\n")
print("*"*83 + "\n")

#Degiskenleri Tanimliyoruz.
user_score = 0
comp_score = 0
round = 0

#Ana Döngü
while True:

    #Input alıyoruz
    comp_selection = rnd.choice(["TAS","KAGIT","MAKAS"])
    print ("\n" + "1 - TAS \n2 - KAGIT \n3 - MAKAS \n")
    user_selection = {1 : "TAS" , 2 : "KAGIT" , 3: "MAKAS"}
    user_input = int(input("Lütfen Birini Seciniz... \n"))

    
    #Karsilasma Sonucu
    if user_input in user_selection:
        user_choice = user_selection[user_input]

        print("\nKullanici Secimi: {}".format(user_choice))
        print("Bilgisayar Secimi : {}\n".format(comp_selection))

        if user_choice == comp_selection:
            print("Round Berabere")
        elif user_choice == "TAS":
            if comp_selection == "MAKAS":
                print("Roundu Kazandiniz !!")
                user_score += 1
            else:
                print("Roundu Kaybettiniz !!")
                comp_score += 1
        elif user_choice == "KAGIT":
            if comp_selection == "TAS":
                print("Roundu Kazandiniz !!")
                user_score += 1
            else:
                print("Roundu Kaybettiniz !!")
                comp_score += 1
        else:
            if comp_selection == "KAGIT":
                print("Roundu Kazandiniz !!")
                user_score += 1
            else:
                print("Roundu Kaybettiniz !!")
                comp_score += 1

        #Skor Gösterme
        print(f"\nKullanicinin Skoru : {user_score}")
        print(f"Bilgisayarin Skoru : {comp_score}")
        print

        #Kazandi mi sorgusu
        if comp_score == 5:
            print("\n" + "*"*83 + "\n")
            print("Bilgisayar Kazandi. KAYBETTİNİZ!\n")
            print("\n" + "*"*83 + "\n" )
            break
        elif user_score == 5:
            print("\n" + "*"*83 + "\n")
            print("Bilgisayar Kaybetti. KAZANDİNİZ!\n")
            print("\n" + "*"*83 + "\n" )
            break

        round+=1
        print("\n" + "*"*83 + "\n")
        print(f"ROUND : {round}")
        print("\n" + "*"*83 + "\n")

    else:
        print("Gecersiz Secim")
        continue
