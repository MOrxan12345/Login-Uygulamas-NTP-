class KullaniciGirisi():

    def __init__(self,sys_kul_adi,sys_sifre,girisHakki):
        self.sys_kul_adi = sys_kul_adi
        self.sys_sifre = sys_sifre
        self.girisHakki = girisHakki

    def girisHakkiKontrol(self):
        return not self.girisHakki > 0


    def loginKontrol(self,kullanici_adi,sifre):

            if kullanici_adi != self.sys_kul_adi and sifre == self.sys_sifre:
                print("Kullanıcı Adı Yalnış!")
                self.girisHakki -= 1
                print("Giriş hakkınız: ",k.girisHakki)

            elif kullanici_adi == self.sys_kul_adi and sifre != self.sys_sifre:
                self.girisHakki -= 1
                print("Şifreniz Yalnış!")
                print("Giriş hakkınız: ",k.girisHakki)

            elif kullanici_adi != self.sys_kul_adi and sifre != self.sys_sifre:
                print("Şifre ve Parola yalnış!")
                self.girisHakki -= 1
                print("Giriş hakkınız: ",k.girisHakki)
            else:
                return True

if __name__ == '__main__':

    print("""
    ------------------------
        Kullanıcı Girişi
        
    ------------------------
    """)

    k = KullaniciGirisi("Orxan","12345",3)

    while True:
        login = input("Kullanici Adi: ")
        parola = input("Parola: ")


        if k.loginKontrol(login,parola):
            print("Sisteme giriş başarılı!")
            break

        if k.girisHakkiKontrol():
            print("Giriş Hakkınız Bitti!")
            break

