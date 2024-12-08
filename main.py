
def main():
    print("\n")
    print("     HESAP MAKİNESİ")
    print("\n")
    ilk = int(input("İlk sayınızı giriniz: "))
    print("\b")
    ikinci = int(input("İkinci sayınızı giriniz: "))
    print("\b")
    islem = input("Yapmak istediğiniz işlemi(+, -, /, *) seçiniz: ")
    print("\b")
    islemler(ilk, ikinci, islem)

def islemler(ilkSayi, ikinciSayi, islem):
    if islem == "+":
        print("Sonucunuz: ", ilkSayi + ikinciSayi)
    elif islem == "-":
        print("Sonucunuz: ", ilkSayi - ikinciSayi)
    elif islem == "/":
        print("Sonucunuz: ", ilkSayi / ikinciSayi)
    elif islem == "*":
        print("Sonucunuz: ", ilkSayi * ikinciSayi)
    else:
        print("lütfen toplama(+), çıkarma(-), bölme(/) veya çarpma(*) sembollerinden birini yazınız.")



main()

