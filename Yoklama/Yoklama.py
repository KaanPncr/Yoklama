class Yoklama:
    def __init__(self):
        self.ogrenciler = {}  # Öğrenci numarası ve ismi
        self.dersler = []
        self.yoklama = {}  # Her hafta için yoklama sonuçları

    def ogrenci_ekle(self, numara, isim):
        self.ogrenciler[numara] = isim
        # Her öğrenci için başlangıçta yoklama durumu
        for hafta in range(1, 53):  # 1'den 52'ye kadar haftalar
            if hafta not in self.yoklama:
                self.yoklama[hafta] = {}
            self.yoklama[hafta][numara] = False

    def ders_ekle(self, ders_adi):
        self.dersler.append(ders_adi)

    def yoklama_al(self, ders_adi, hafta):
        if ders_adi not in self.dersler:
            print(f"{ders_adi} dersi bulunmamaktadır.")
            return

        print(f"\n{ders_adi} dersi için {hafta}. hafta yoklama almak üzere öğrencilerin isimlerini girin:")
        for numara, isim in self.ogrenciler.items():
            cevap = input(f"{isim} (Numara: {numara}) yoklamada var mı? (e/h): ").strip().lower()
            if cevap == 'e':
                self.yoklama[hafta][numara] = True
            elif cevap == 'h':
                self.yoklama[hafta][numara] = False

    def yoklama_sonucu(self, hafta):
        if hafta not in self.yoklama:
            print(f"{hafta}. hafta yoklama alınmamıştır.")
            return

        print(f"\n{hafta}. Hafta Yoklama Sonucu:")
        for numara, durum in self.yoklama[hafta].items():
            isim = self.ogrenciler[numara]
            durum_str = "Var" if durum else "Yok"
            print(f"{isim} (Numara: {numara}): {durum_str}")

    def onayla(self, hafta):
        if hafta not in self.yoklama:
            print(f"{hafta}. hafta yoklama alınmamıştır.")
            return

        print(f"\n{hafta}. Hafta Yoklama sonuçlarını onaylayın:")
        for numara, durum in self.yoklama[hafta].items():
            isim = self.ogrenciler[numara]
            durum_str = "Var" if durum else "Yok"
            onay = input(f"{isim} (Numara: {numara}): {durum_str} (onaylamak için 'e', iptal etmek için 'h'): ").strip().lower()
            if onay == 'h':
                self.yoklama[hafta][numara] = not durum  # Durumu tersine çevir

def main():
    yoklama = Yoklama()

    while True:
        print("\n1. Öğrenci Ekle")
        print("2. Ders Ekle")
        print("3. Yoklama Al")
        print("4. Yoklama Sonucunu Göster")
        print("5. Yoklama Sonuçlarını Onayla")
        print("6. Çıkış")
        secim = input("Seçiminizi yapın (1/2/3/4/5/6): ")

        if secim == '1':
            numara = input("Öğrencinin numarasını girin: ")
            isim = input("Öğrencinin ismini girin: ")
            yoklama.ogrenci_ekle(numara, isim)
        elif secim == '2':
            ders_adi = input("Dersin adını girin: ")
            yoklama.ders_ekle(ders_adi)
        elif secim == '3':
            ders_adi = input("Yoklama almak istediğiniz dersin adını girin: ")
            hafta = int(input("Hangi haftanın yoklamasını almak istiyorsunuz? (1-52): "))
            yoklama.yoklama_al(ders_adi, hafta)
        elif secim == '4':
            hafta = int(input("Hangi haftanın yoklama sonucunu görmek istiyorsunuz? (1-52): "))
            yoklama.yoklama_sonucu(hafta)
        elif secim == '5':
            hafta = int(input("Hangi haftanın yoklama sonuçlarını onaylamak istiyorsunuz? (1-52): "))
            yoklama.onayla(hafta)
        elif secim == '6':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()