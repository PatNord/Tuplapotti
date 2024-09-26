import random
import time

def main():

    print("Tervetuloa pelaamaan Tuplapottia!\n Ohje: Peliä pelataan syöttämällä numeroita terminaaliin.\n Aloita syöttämällä rahaa.")
    time.sleep(1.5)
    pelaajan_saldo = 0
    panos = 0.20
    

    while True:
        

        valinta = input("| 1. Pelaa | 2. Aseta panos | 3. Lisää rahaa | 4. Voitonmaksu | 5. Voittotaulu | 6. Pelivaraukset | 7. Panos |\n> ")

        if valinta not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("virheellinen syöte")

        if valinta == "1" and pelaajan_saldo == 0:
            print("Pelivaraukset eivät riitä. syötä rahaa jatkaaksesi tai paina voitonmaksu lopettaaksesi.")
                
        
        

        if valinta == "1" and pelaajan_saldo >= 0.20:
            pelaajan_saldo -= panos
            tulos = pelaa(pelaajan_saldo, panos)
            pelaajan_saldo += tulos
            print()
            if pelaajan_saldo < panos:
                panos = tarkista_panos(pelaajan_saldo)
    
            
            
        
        elif valinta == "2":
            panos = aseta_panos(pelaajan_saldo)
        
        elif valinta == "3":
            pelaajan_saldo += syötä_rahaa()
        
        elif valinta == "4":
            print(f"Voitonmaksu {pelaajan_saldo:.2f}€")
            break

        elif valinta == "5":
            näytä_voitonjakotaulu(panos)
        
        elif valinta == "6":
            print("**********************")
            print(f"{pelaajan_saldo:.2f}€")
            print("**********************")
        
        elif valinta == "7":
            if pelaajan_saldo < 0.20:
                print("Pelivaraukset eivät riitä pelaamiseen")
            else:
                print(f"Panos: {panos:.2f}€")
        
        
        
        





def näytä_voitonjakotaulu(panos):
    kertoja = panos
    print("=========================================")
    print(f"🪙🪙🪙   {10.00 * kertoja:.2f}€  " f"🍆🍆🍆 {2.00 * kertoja:.2f}€  " f"🍊🍊⭐ {1.60 * kertoja:.2f}€  ")
    print(f"🍀🍀🍀 {4.00 * kertoja:.2f}€  " f"🍐🍐⭐ {2.00 * kertoja:.2f}€  " f"🍒🍒🍒 {1.60 * kertoja:.2f}€  ")
    print(f"🍀🍀⭐ {3.00 * kertoja:.2f}€  " f"🍉🍉⭐ {2.00 * kertoja:.2f}€  " f"🍒🍒🍓 {1.60 * kertoja:.2f}€  ")
    print(f"🍐🍐🍐 {3.00* kertoja:.2f}€  " f"🍆🍆⭐ {2.00 * kertoja:.2f}€  " f"🍒🍒 - {0.80 * kertoja:.2f}€  ")
    print(f"🍉🍉🍉 {3.00 * kertoja:.2f}€  " f"🍇🍇⭐ {2.00 * kertoja:.2f}€  " f" - -🍓 {0.80 * kertoja:.2f}€  ")
    print(f"🍇🍇🍇 {3.00 * kertoja:.2f}€  " f"🍊🍊🍊 {1.60 * kertoja:.2f}€  " f"🍒 - - {0.40 * kertoja:.2f}€")
    print("=========================================")



#PELIN KULKU

def syötä_rahaa():
    print("******************")
    print("0.20€ 0.50€ 1€ 2€")
    print("******************")
    syötetyt_rahat = 0
    while True:
        määrä = (input("| 1. 0.20€ | 2. 0.50€ | 3. 1€ | 4. 2€ | 0. Aloitusvalikko |\n> "))

        if määrä not in["0", "1", "2", "3", "4"]:
            print("Virheellinen syöte")
        
        elif määrä == "1":
            syötetyt_rahat += 0.20
            print(f"{syötetyt_rahat:.2f}€")
        elif määrä == "2":
            syötetyt_rahat += 0.50
            print(f"{syötetyt_rahat:.2f}€")
        elif määrä == "3":
            syötetyt_rahat += 1
            print(f"{syötetyt_rahat:.2f}€")
        elif määrä == "4":
            syötetyt_rahat += 2
            print(f"{syötetyt_rahat:.2f}€")
        elif määrä == "0":
            break
        
    print()
    print("************************")        
    print(f"Pelimerkkejä lisätty: {syötetyt_rahat:.2f}€")
    print("************************")   
    print()
    return syötetyt_rahat

def aseta_panos(rahat):
    pelaajan_saldo = rahat
    panostaulu = [0.20, 0.40, 0.60, 0.80, 1]
    korotus = 0
    pelaajan_panos = 0.2
    print("Kirjoita syötteeseen '1' korottaaksesi panosta tai '2' siirry takaisin aloitusvalikkoon.")
    print()
    

    while True:
        panos = input(("| 1. Panos | 2. Aloitusvalikko |\n> ")).strip()
        if panos == "1":
            korotus += 1
            if korotus > 4 or pelaajan_saldo < panostaulu[korotus]:
                korotus = 0
            pelaajan_panos = panostaulu[korotus]
            print(f"Panos {pelaajan_panos:.2f}€")
        elif panos == "2":
            return pelaajan_panos

def pyöräytys():
    index_0_ja_1_merkit = ["🍒", "🍊", "🍇", "🍆", "🍉", "🍐", "🍀", "🪙 "]
    kaikki_pelimerkit = ["🍒", "🍓", "🍊", "🍇", "🍆", "🍉", "🍐", "🍀", "⭐", "🪙 "]

    rivi1 = []
    rivi2 = []
    rivi3 = []
    
    i = 0
    while i < 2:
        hedelmä = random.choice(index_0_ja_1_merkit)
        rivi1.append(hedelmä)
        i += 1
        if i == 2:
            rivi1.append(random.choice(kaikki_pelimerkit))
            i = 0
            break
    
    while i < 2:
        hedelmä = random.choice(index_0_ja_1_merkit)
        rivi2.append(hedelmä)
        i += 1
        if i == 2:
            rivi2.append(random.choice(kaikki_pelimerkit))
            i = 0
            break
    
    while i < 2:
        hedelmä = random.choice(index_0_ja_1_merkit)
        rivi3.append(hedelmä)
        i += 1
        if i == 2:
            rivi3.append(random.choice(kaikki_pelimerkit))
            i = 0
            break

    rivi4 = [rivi1[0], rivi2[1], rivi3[2]]
    rivi5 = [rivi3[0], rivi2[1], rivi1[2]]

    return rivi1, rivi2, rivi3, rivi4, rivi5

def print_pyöräytys(pyöräytys):
    print("Arvonta käynnissä...")
    print()
    time.sleep(1.5)
    for list in pyöräytys[:3]:
        print(" ".join(list))




def tuplaus(voitto):
    vaihtoehdot = [0, 1, 2, 3]  # 0 häviää, 1 kruuna, 2 klaava, 3 rahat takaisin eli 1/2
    voitonjako = False  #Tarkastetaan, onko pelaaja voittanut vähintään yhden tuplauksen.
    
    while True:
        try:
            #katsotaan onko voitonjako True. Jos on, niin input voitonmaksulla printataan. 
            # Jos ei, niin vain tuplausvaihtoehdot näkyvät. Try - except lisätty nappaamaan mahdolliset virheet.
            if voitonjako:
                    
                    pelaajanvalinta = int(input("| 1. Kruuna | 2. Klaava | 3. Lopeta |\n> "))
            else:
                    pelaajanvalinta = int(input("| 1. Kruuna | 2. Klaava |\n> "))

        except ValueError:
            print("Virheellinen syöte. Valitse 1, 2 tai 3.")
            continue
        
        #katsotaan aluksi voitonjaot. Jos pelaaja valitsee voitonjaon ja voitonjako == True, hänelle palautetaan voitot.
        if pelaajanvalinta == 3 and voitonjako:
            #voitonjako == true, jolloin voitot voidaan nostaa
            print(f"Voitonmaksu: {voitto:.2f}€")
            return voitto
        #Jos voitonjako == False, niin ohjelma jatkaa pyörimistä.
        elif pelaajanvalinta == 3 and not voitonjako:
            #voitonjako == False, voittoja ei voida nostaa.
            print("Tuplaus pitää suorittaa ennen voitonmaksua")
            continue
        
        elif pelaajanvalinta not in [1, 2]:
            #napataan virheellinen syöte.
            print("Virheellinen syöte. Valitse 1 tai 2.")
            continue
        
        #arvotaan koneen tulos ja suoritetaan itse tuplaus
        tietokoneen_valinta = random.choice(vaihtoehdot)
        
        if pelaajanvalinta == 1 and tietokoneen_valinta == 1:
            print("Pelaaja valitsi kruunan.")
            print("Arvonta käynnissä...")
            time.sleep(2)
            print("Kone arpoi kruunan.")
            voitto *= 2
            print(f"Voitit {voitto:.2f}€")
            voitonjako = True  #vaihdetaan voitonjako == True. Seuraavalla kierroksella voi nostaa voitot

        elif pelaajanvalinta == 2 and tietokoneen_valinta == 2:
            print("Pelaaja valitsi klaavan.")
            print("Arvonta käynnissä...")
            time.sleep(2)
            print("Kone arpoi klaavan.")
            voitto *= 2
            print(f"Voitit {voitto:.2f}€")
            voitonjako = True #Sama kuin edellisessä.
        
        elif tietokoneen_valinta == 3:
            print("Arvonta käynnissä...")
            time.sleep(2)
            print(f"Kone arpoi 1/2. Palautus {voitto:.2f}€.")
            return voitto, False
        
        else:
            print("Arvonta käynnissä...")
            time.sleep(2)
            print("Tyhjä! Hävisit tuplauksen.")
            return 0

def voitonjako(panos, pyöräytys):
    
    rivi1, rivi2, rivi3, rivi4, rivi5 = pyöräytys
    voitto = 0

    if rivi1[0] == rivi1[1] == rivi1[2]:
        if rivi1[0] == "🪙":
            voitto += 10.00 * panos
        elif rivi1[0] == "🍀":
            voitto += 4.00 * panos
        elif rivi1[0] == "🍐" or rivi1[0] == "🍉" or rivi1[0] == "🍇":
            voitto += 3.00 * panos
        elif rivi1[0] == "🍆":
            voitto += 2.00 * panos
        elif rivi1[0] == "🍊" or rivi1[0] == "🍒":
            voitto += 1.60 * panos
    
    elif rivi1[0] == rivi1[1] and rivi1[2] == "⭐":
        if rivi1[0] == "🍀":
            voitto += 3.00 * panos
        elif rivi1[0] == "🍐" or rivi1[0] == "🍉" or rivi1[0] == "🍆" or rivi1[0] == "🍇":
            voitto += 2.00 * panos
        elif rivi1[0] == "🍊":
            voitto += 1.60 * panos
    
    elif rivi1[0] == rivi1[1] and rivi1[2] == "🍓":
        if rivi1[0] == "🍒":
            voitto += 1.60 * panos
    elif rivi1[0] == rivi1[1] != rivi1[2]:
        if rivi1[0] == "🍒":
            voitto += 0.80 * panos
    elif rivi1[0] == "🍒" and rivi1[1] != "🍒" and rivi1[2] != "🍒":
        voitto += 0.40 * panos
    
    elif rivi1[0] != "🍒" and rivi1[2] == "🍓":
        voitto += 0.80 * panos

    #===============RIVI 2 =================================

    if rivi2[0] == rivi2[1] == rivi2[2]:
        if rivi2[0] == "🪙":
            voitto += 10.00 * panos
        elif rivi2[0] == "🍀":
            voitto += 4.00 * panos
        elif rivi2[0] == "🍐" or rivi2[0] == "🍉" or rivi2[0] == "🍇":
            voitto += 3.00 * panos
        elif rivi2[0] == "🍆":
            voitto += 2.00 * panos
        elif rivi2[0] == "🍊" or rivi2[0] == "🍒":
            voitto += 1.60 * panos

    elif rivi2[0] == rivi2[1] and rivi2[2] == "⭐":
        if rivi2[0] == "🍀":
            voitto += 3.00 * panos
        elif rivi2[0] == "🍐" or rivi2[0] == "🍉" or rivi2[0] == "🍆" or rivi2[0] == "🍇":
            voitto += 2.00 * panos
        elif rivi2[0] == "🍊":
            voitto += 1.60 * panos

    elif rivi2[0] == rivi2[1] and rivi2[2] == "🍓":
        if rivi2[0] == "🍒":
            voitto += 1.60 * panos
    elif rivi2[0] == rivi2[1] != rivi2[2]:
        if rivi2[0] == "🍒":
            voitto += 0.80 * panos
    elif rivi2[0] == "🍒" and rivi2[1] != "🍒" and rivi2[2] != "🍒":
        voitto += 0.40 * panos

    elif rivi2[0] != "🍒" and rivi2[2] == "🍓":
        voitto += 0.80 * panos

#===================RIVI3============================

    if rivi3[0] == rivi3[1] == rivi3[2]:
        if rivi3[0] == "🪙":
            voitto += 10.00 * panos
        elif rivi3[0] == "🍀":
            voitto += 4.00 * panos
        elif rivi3[0] == "🍐" or rivi3[0] == "🍉" or rivi3[0] == "🍇":
            voitto += 3.00 * panos
        elif rivi3[0] == "🍆":
            voitto += 2.00 * panos
        elif rivi3[0] == "🍊" or rivi3[0] == "🍒":
            voitto += 1.60 * panos

    elif rivi3[0] == rivi3[1] and rivi3[2] == "⭐":
        if rivi3[0] == "🍀":
            voitto += 3.00 * panos
        elif rivi3[0] == "🍐" or rivi3[0] == "🍉" or rivi3[0] == "🍆" or rivi3[0] == "🍇":
            voitto += 2.00 * panos
        elif rivi3[0] == "🍊":
            voitto += 1.60 * panos

    elif rivi3[0] == rivi3[1] and rivi3[2] == "🍓":
        if rivi3[0] == "🍒":
            voitto += 1.60 * panos
    elif rivi3[0] == rivi3[1] != rivi3[2]:
        if rivi3[0] == "🍒":
            voitto += 0.80 * panos
    elif rivi3[0] == "🍒" and rivi3[1] != "🍒" and rivi3[2] != "🍒":
        voitto += 0.40 * panos

    elif rivi3[0] != "🍒" and rivi3[2] == "🍓":
        voitto += 0.80 * panos

#====================RIVI4 =================================
    if rivi4[0] == rivi4[1] == rivi4[2]:
        if rivi4[0] == "🪙":
            voitto += 10.00 * panos
        elif rivi4[0] == "🍀":
            voitto += 4.00 * panos
        elif rivi4[0] == "🍐" or rivi4[0] == "🍉" or rivi4[0] == "🍇":
            voitto += 3.00 * panos
        elif rivi4[0] == "🍆":
            voitto += 2.00 * panos
        elif rivi4[0] == "🍊" or rivi4[0] == "🍒":
            voitto += 1.60 * panos

    elif rivi4[0] == rivi4[1] and rivi4[2] == "⭐":
        if rivi4[0] == "🍀":
            voitto += 3.00 * panos
        elif rivi4[0] == "🍐" or rivi4[0] == "🍉" or rivi4[0] == "🍆" or rivi4[0] == "🍇":
            voitto += 2.00 * panos
        elif rivi4[0] == "🍊":
            voitto += 1.60 * panos

    elif rivi4[0] == rivi4[1] and rivi4[2] == "🍓":
        if rivi4[0] == "🍒":
            voitto += 1.60 * panos
    elif rivi4[0] == rivi4[1] != rivi4[2]:
        if rivi4[0] == "🍒":
            voitto += 0.80 * panos
    elif rivi4[0] == "🍒" and rivi4[1] != "🍒" and rivi4[2] != "🍒":
        voitto += 0.40 * panos

    elif rivi4[0] != "🍒" and rivi4[2] == "🍓":
        voitto += 0.80 * panos
    
    #===================RIVI5==============================

    if rivi5[0] == rivi5[1] == rivi5[2]:
        if rivi5[0] == "🪙":
            voitto += 10.00 * panos
        elif rivi5[0] == "🍀":
            voitto += 4.00 * panos
        elif rivi5[0] == "🍐" or rivi5[0] == "🍉" or rivi5[0] == "🍇":
            voitto += 3.00 * panos
        elif rivi5[0] == "🍆":
            voitto += 2.00 * panos
        elif rivi5[0] == "🍊" or rivi5[0] == "🍒":
            voitto += 1.60 * panos

    elif rivi5[0] == rivi5[1] and rivi5[2] == "⭐":
        if rivi5[0] == "🍀":
            voitto += 3.00 * panos
        elif rivi5[0] == "🍐" or rivi5[0] == "🍉" or rivi5[0] == "🍆" or rivi5[0] == "🍇":
            voitto += 2.00 * panos
        elif rivi5[0] == "🍊":
            voitto += 1.60 * panos

    elif rivi5[0] == rivi5[1] and rivi5[2] == "🍓":
        if rivi5[0] == "🍒":
            voitto += 1.60 * panos
    elif rivi5[0] == rivi5[1] != rivi5[2]:
        if rivi5[0] == "🍒":
            voitto += 0.80 * panos
    elif rivi5[0] == "🍒" and rivi5[1] != "🍒" and rivi5[2] != "🍒":
        voitto += 0.40 * panos

    elif rivi5[0] != "🍒" and rivi5[2] == "🍓":
        voitto += 0.80 * panos
    
    if voitto == 0:
        return 0
    else:
        return voitto

def pelaa(pelaajan_saldo, panos):
    print("************************")        
    print(f"Pelivaraukset: {pelaajan_saldo:.2f}€")
    print("************************")  
    p = pyöräytys()
    print_pyöräytys(p)
    lopputulos = voitonjako(panos, p)
    if lopputulos == 0:
        print()
        print("Ei voittoa.")
        return 0
    else:
        print()
        print(f"Voitit {lopputulos:.2f}€")
        while True:
            valinta = input("| 1. Tuplaa | 2. Voitonmaksu |\n> ")
            if valinta not in ["1", "2"]:
                print("virheellinen syöte")
            elif valinta == "1":
                tuplattu = tuplaus(lopputulos)
                if tuplattu == 0:
                    return 0
                elif tuplattu[1] == False:
                    break
                    
            elif valinta == "2":
                print(f"Voitit {lopputulos:.2f}€")
                return lopputulos
    return lopputulos


def tarkista_panos(pelaajan_saldo):
    if pelaajan_saldo > 0.80 and pelaajan_saldo < 1:
        return 0.80
    elif pelaajan_saldo > 0.60 and pelaajan_saldo < 0.80:
        return 0.60
    elif pelaajan_saldo > 0.40 and pelaajan_saldo < 0.60:
        return 0.40
    elif pelaajan_saldo > 0.20 and pelaajan_saldo < 0.40:
        return 0.20
    elif pelaajan_saldo < 0.20:
        print("Pelivaraukset eivät riitä. syötä rahaa jatkaaksesi tai paina voitonmaksu lopettaaksesi.")

if __name__=="__main__":
    main()