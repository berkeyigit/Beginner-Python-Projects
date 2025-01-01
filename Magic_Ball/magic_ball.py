from random import choice
#Cevaplar icin iki farkli dizi olustuyoruz.
default_answer = ["Evet","Hayir","Hiç zannetmiyorum","Kesinlikle Olmaz","Bilemedim","Cevabini biliyorsun","İmkansiz","Kesinlikle","Belkide"]
cruel_answer = ["Basaramayacaksin","Hemde nasil ","Bosuna Umutlanma","'Görüldü'","Gercekten buna mi cevap ariyorsun","Aman ne önemli bir soru"]

#Uygulama girizgahı
print("*"*83 + "\n")
print(" ♥♦♣♠ MAGİC BALL'A HOS GELDİNİZ ♠♣♦♥ \n")
print("*"*83 + "\n")
#Oyun dongusu
while True:

    #Kullanicidan soru ve nasıl bir cevap istedigini aliyoruz
    user_answer = input("Lütfen cevabini aradiginiz soruyu sorun : \n")
    user_choise = input("1 : Normal\n2 : Zalim\nBu soruya nasil bir cevap vermemi istersin.\n").upper()

    #Kosul ifadeleri ile bu girdilere gore programimizi calistiyoruz.
    if user_choise == "NORMAL" or user_choise == "1":
        print("{}".format(choice(default_answer)))
    elif user_choise == "ZALİM" or user_choise =="ZALIM" or user_choise=="2":
        print("{}".format(choice(cruel_answer)))
    else:
        print("Yanlis girdiniz. Daha dikkatli lütfen")
        continue
    break