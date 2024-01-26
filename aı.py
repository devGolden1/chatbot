import json
from difflib import get_close_matches as yakin_sonuclari_getir
art =''' 
WELLCOME TO 
  _____  ____  _      _____  ______ _   _    _____ _    _       _______   ____   ____ _______ 
  / ____|/ __ \| |    |  __ \|  ____| \ | |  / ____| |  | |   /\|__   __| |  _ \ / __ \__   __|
 | |  __| |  | | |    | |  | | |__  |  \| | | |    | |__| |  /  \  | |    | |_) | |  | | | |   
 | | |_ | |  | | |    | |  | |  __| | . ` | | |    |  __  | / /\ \ | |    |  _ <| |  | | | |   
 | |__| | |__| | |____| |__| | |____| |\  | | |____| |  | |/ ____ \| |    | |_) | |__| | | |   
  \_____|\____/|______|_____/|______|_| \_|  \_____|_|  |_/_/    \_\_|    |____/ \____/  |_|   
                                                                                               
                                                                                               '''
print(art)

def veritabanini_yukle():
    with open('C:\\Users\\golden\\OneDrive\\Masaüstü\\pyaı\\veritabani.json', 'r') as dosya:
        return json.load(dosya)

def veritabanina_yaz(veriler):
    with open('C:\\Users\\golden\\OneDrive\\Masaüstü\\pyaı\\veritabani.json', 'w') as dosya:
        json.dump(veriler, dosya, indent=2)

def yakin_sonuc_bul(soru, sorular):
    eslesen = yakin_sonuclari_getir(soru, sorular, n=1, cutoff=0.7)
    return eslesen[0] if eslesen else None

def cevabini_bul(soru, veritabani):
    for soru_cevaplar in veritabani["sorular"]:
        if soru_cevaplar["soru"] == soru:
            return soru_cevaplar["cevap"]
    return None

def Golden_Aİ():
    veritabani = veritabanini_yukle()

    while True:
        soru = input("User: ")
        if soru == 'çık':
            break
        
        gelen_sonuc = yakin_sonuc_bul(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
        if gelen_sonuc:
            verilecek_cevap = cevabini_bul(gelen_sonuc, veritabani)
            print(f"Golden AI: {verilecek_cevap}")
        else:
            print("Golden AI: Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misiniz?")
            yeni_cevap = input("Öğretmek için yazabilir veya 'geç' diyebilirsiniz. ")

            if yeni_cevap != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veritabanina_yaz(veritabani)
                print("Golden AI: Yeni birşey daha!!")

if __name__ == '__main__':
    Golden_Aİ()