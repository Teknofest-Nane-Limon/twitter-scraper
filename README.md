Twitter'dan belirlediğimiz anahtar kelimelerle ilgili tweetleri çekmek için yazdığımız bir bot aracıdır. 
Selenium ile insan davranışları sergilenerek istenildiği kadar veri çekilmesi sağlanmıştır.
Anahtar kelimeleri aratma nedenimiz belirli sınıflara ait tweetleri hedef göstermek ve bu sayede ihtiyacımız olan corpusa daha kolay ulaşmaktır.

#### Aracın kullanımını anlatan video için <youtube-link>


# Selenium
    
[Selenium](https://www.selenium.dev/about/) bir web page testing aracıdır. 
Asıl görevi veri çekmek değildir. Fakat aşağıdaki nedenlerden dolayı veri kazıma işlemi bu test aracı ile yapılmıştır.

- Twitter tasarımlarında html taglerinin id, name ve class bilgilerini sürekli değiştiren bir script kullanmaktadır. 
- Ayrıca site içerisindeki gezinme hızına göre botları tespit ederek banlama yoluna gitmiştir. 

Bu engelleri aşabilmek için **twitter-scraper** uygulaması içerisinde insani davranışlar düşünülerek bir algoritma kurgulanmıştır. 
    
## Selenium Gereklilikleri
    
Selenium bir browser oturumu açıp işlemlerini yapmaktadır. Açacağı browser oturumu için bir firefox browser driver ına ihtiyaç duymaktadır.

#### Mac için:

brew install geckodriver

#### Diğerleri için:

link : https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
    
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
