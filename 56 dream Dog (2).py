#joce
#02/26/2025
#dream dog


#int
dog_breeds =["Affenpinscher", "AfghanHound", "AiredaleTerrier", "AkbashDog", "Akita", "AlapahaBlueBloodBulldog", "AlaskanHusky", "AlaskanMalamute", "AmericanEskimoDog", "AmericanFoxhound", "AmericanPitBullTerrier", "AmericanWaterSpaniel", "AnatolianShepherdDog", "AustralianKelpie", "AustralianShepherd", "Azawakh", "Basenji", "BassetBleudeGascogne", "Beagle", "Beauceron", "BedlingtonTerrier", "BelgianMalinois", "BelgianTervuren", "BerneseMountainDog", "BlackandTanCoonhound", "Bloodhound", "BluetickCoonhound", "Boerboel", "BorderTerrier", "BostonTerrier", "BouvierdesFlandres", "Boxer", "BoykinSpaniel", "BraccoItaliano", "Briard", "Brittany", "Bullmastiff", "CairnTerrier", "CaneCorso", "CardiganWelshCorgi", "CatahoulaLeopardDog", "CaucasianShepherd(Ovcharka)", "CavalierKingCharlesSpaniel", "ChineseCrested", "Chinook", "ChowChow", "ClumberSpaniel", "CockerSpaniel(American)", "CotondeTulear", "Dalmatian", "DogoArgentino", "EnglishShepherd", "EnglishSpringerSpaniel", "Eurasier", "FieldSpaniel", "FinnishLapphund", "GermanPinscher", "GermanShepherdDog", "GermanShorthairedPointer", "GiantSchnauzer", "GlenofImaalTerrier", "GoldenRetriever", "GordonSetter", "GreatDane", "GreatPyrenees", "Greyhound", "Harrier", "Havanese", "IrishSetter", "IrishWolfhound", "ItalianGreyhound", "JapaneseChin", "Keeshond", "Komondor", "Kuvasz", "LabradorRetriever", "LagottoRomagnolo", "Leonberger", "LhasaApso", "Maltese", "MiniatureSchnauzer", "Newfoundland", "NorfolkTerrier", "Papillon", "PembrokeWelshCorgi", "PharaohHound", "Plott", "Pug", "RedboneCoonhound", "RhodesianRidgeback", "Rottweiler", "Samoyed", "Schipperke", "ScottishDeerhound", "ShihTzu", "SilkyTerrier", "SoftCoatedWheatenTerrier", "SpanishWaterDog", "Vizsla", "Weimaraner"]
dog_weight = [6, 50, 40, 90, 65, 55, 38, 65, 20, 65, 30, 25, 80, 31, 35, 33, 22, 35, 20, 80, 17, 40, 40, 65, 65, 80, 45, 110, 12, 10, 70, 50, 25, 55, 70, 30, 100, 13, 88, 25, 50, 80, 13, 10, 50, 40, 55, 20, 9, 50, 80, 44, 35, 40, 35, 33, 25, 50, 45, 65, 32, 55, 45, 110, 85, 50, 40, 7, 35, 105, 7, 4, 35, 80, 70, 55, 24, 120, 12, 4, 11, 100, 11, 3, 25, 40, 40, 14, 45, 75, 75, 50, 10, 70, 9, 8, 30, 30, 50, 55]
filtered_list = []


#functiom
#main
#ask the user for what size dog they are looking for
#tiny = <11
#small 11-25
#medium 26-60
#large = >60


# loop through weight list finding tiny dogs
#for i in range (len(dog_weight)): #good becuase we want the number
 #   if dog_weight[i]<= 10: # little dog
  #      filtered_list.append(dog_breeds[i])
        #append dog bread to the same index to the filtered list
#print(filtered_list)

# for weight in dog_weights:#not good
#         #wehn you find one, add tiny dog name to filtered list

def dog_size(size): #step 1
    #x = input("What dog ssize do you want (tiny, small, medium, large):")
    if size == "tiny":
        for i in range(len(dog_weight)):
            if dog_weight[i]<=10:
                filtered_list.append(dog_breeds[i])

    if size == "small":
        for i in range(len(dog_weight)):
            if dog_weight[i]<=25:
                filtered_list.append(dog_breeds[i])

    if size == "medium":
        for i in range(len(dog_weight)):
            if dog_weight[i]<=60:
                filtered_list.append(dog_breeds[i])

    if size == "large":
        for i in range(len(dog_weight)):
            if dog_weight[i]>60:
                filtered_list.append(dog_breeds[i])
    print(filtered_list)
#main
dog_size(input("Enter size:")) # step 2
