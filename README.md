Twitter'dan belirlediğimiz anahtar kelimelerle ilgili tweetleri çekmek için yazdığımız bir bot aracıdır. 
Selenium ile insan davranışları sergilenerek istenildiği kadar veri çekilmesi sağlanmıştır.
Anahtar kelimeleri aratma nedenimiz belirli sınıflara ait tweetleri hedef göstermek ve bu sayede ihtiyacımız olan corpusa daha kolay ulaşmaktır.

#### Aracın kullanımını anlatan video için <youtube-link>

# Ortam Oluşturma

Lütfen Python sürümünüzü '3.10' olarak ayarlayın.

Python versiyonunuzdan emin olmak için:

```bash
python3 --version
```

`.env` dosyanızı oluşturun.

```bash
    $ cd <project-directory>
    $ touch .env
```
.env dosyasının içerisine twitter hesabınızın e-mail ve parola bilgilerini ekleyip kaydediniz.
```bash
    EMAIL=<your_mail_adress@mail.com>
    PASSWORD=<your_password>
```

## Geliştirme Ortamını Ayarlamak
- Virtual environment oluşturunuz.
```bash
    $ python -m venv <venv-name>
```
- Virtual environmentınızı aktive ediniz.
```bash
    $ source <venv-name>/bin/activate
```
- Kütüphaneleri Yükleyiniz.
```bash
    $ pip install -r requirements.txt
```

## Anahtar Kelime Listesi Oluşturma
- keyword_list.txt oluşturunuz.
```bash
    $ touch keyword_list.txt
```

# Çalıştırma

Uygulamanın çalışması için gerekli adımlar tamamlanmıştır.

```bash
    $ python3 main.py
```
