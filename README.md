# CALROV'26 Ara Tatil Kampı
Bu kamp, seneye görevlerinizin artacağından dolayı bir eğitim niteliğinde olacaktır. Lütfen ödevleri zamanında ve eksiksiz yetiştirelim. Şimdiden kolay gelsin dostlar.

# Veritabanı ile Banka Yönetim Sistemi
Bu görevin asıl amacı Python’daki sınıf sistemini derinlemesine anlamak, bu sisteme hakim olmak ve bir adım öteye götürerek basit bir veritabanı ile yetkinliği arttırmaktır.
1.	Bu görev sırasında yapılması istenen işlemler şöyledir:
   
    •	Genel olarak bir banka sınıfı yazmak. Bu sınıfta para çekme, para yatırma, sisteme giriş yapma, sistemden çıkış yapma gibi basit işlemler bulunmalıdır. (İkinci olarak oluşturduğunuz sınıfı miras alacak çocuk sınıf)

    •	İkinci banka sınıfı ise veritabanı işlemlerini yönetebilmeli, yeni bir üye kaydı oluşturabilmeli ve sizin önceden tanımladığınız bir admin portalından giriş yapıldığı takdirde bir kullanıcıyı silebilmelidir. Sisteme giriş yaparken verilerin kaydedilmiş veritabanı ile kontrol edilip geriye bir cevap döndürmesi için bir metod yazılmalıdır. Kullanıcılar bankaya giriş, yeni üye kaydı oluşturma gibi işlemleri buradan yapacaktır.

2.	Bu sınıflar yazıldıktan sonra oluşabilecek açıklar olacaktır. Bu açıklar fark edilebildiği takdirde kapatılmış bir şekilde yazılmış olmalıdır.(Bu sınıflar iki farklı kullanıcı tipi için de olabilir)

3.	Üyelerin sahip olacağı 3 temel özellik vardır: 
    1.	İsim
    2.	Soyisim
    3.	Bakiye

4.	Bu kodlar tamamlandıktan sonra test edilecektir.
5.	Veritabanını sqlite3 kütüphanesini kullanarak yapabilirsiniz.
6.	Admin girişinde kullanıcı adı 'admin' şifre 'root123' olmalıdır.

# İletişim Kontrol Ödevi
Bu görevin asıl amacı görev altyapılarını oluştururken veya görev kodlarını yazarken pymavlink kütüphanesi üzerindeki yetkinliğinizi arttırmak ve sizi bu iki konuda bir adım daha öteye taşımaktır.

1.	Udp ile mavlink bağlantısı kurulsun. (Local IP adresi)
  
2.	Mavproxy kurup localhosta bağlanın. (İnternette dokümantasyonu var takılırsanız oradan bakabilirsiniz)
    
3.	İlk başta heartbeat mesajı bekleyip sonrasında mesaj alma yapılacak (wait heartbeat())
   
4.	Mesaj alma işleminde "HEARTBEAT" türünde mesaj alınacak ve herhangi bir txt dosyasına sözlük şeklinde gelen mesaj yazdırılacak. (Bu sonsuz bir döngüde yapılacak)
   
5.	Bir klavye modu yapılacak ve program başladığında otomatik olarak klavye modu da başlayacak. Aşağıda tuşlara atanacak fonksiyonlar verilmiştir:
  o	W, A, S, D: ileri, sol, geri, sağ
  o	Arrow key up, Arrow key down: yukarı, aşağı
  o	Arrow key right, Arrow key left: sağ yaw ekseni, sol yaw ekseni
  o	Q: Arm
  o	E: Disarm
  o	Esc: Klavye modundan çıkış

6.	Klavye modunda hareket komutları mavlink ile verilecek ve verildiğinde x, y, z ve yaw değerleri ekranda gösterilecek. Ekranda gösterirken print() fonksiyonu değil "logging" kütüphanesi kullanılacak. Arm, disarm komutları da yine mavlink ile verilecek ve yine logging kütüphanesi ile ekrana yazdırılacak. Klavye modu çalışırken arka planda aynı anda heartbeat mesajının txt dosyasına yazdırılması da çalışacak. Bu ikisini aynı anda çalıştırmak için threading ve multiprocessing kütüphaneleri kullanılabilir.

# Otonom Görev Algoritması
  Algoritmanın detayları "autonomus mission" branch'indeki pdf dosyasında bulunmaktadır.

# Önemli Not
  Ödevleri atmak için öncelikle GitHub hesabınızda bu repounun bir fork'unu oluşturun ve değişikliklerinizi bu fork üzerinde yapın. Her ödevin son teslim tarihi geldiğinde bu repoya pull request atın. Her ödev için ayrı branch olacak o yüzden pull request atarken ve değişiklik yaparken hangi branch'te olduğunuza dikkat edin. Aynı zamanda ödevleri yaparken yapay zekadan yardım almamaya çalışın. Ancak dökümantasyonlarda aradığınız bilginin tam karşılığını bulup bulmadığınızdan emin değilseniz kullanın. Algoritmalar, yöntemler ve kodlar size ait olsun. (Yapay zekaların yazdığı kodlar fark edilebiliyor dostlar haberiniz olsun 😊).

# Ödev Teslimleri

  •	Veritabanı ile Banka Yönetim Sistemi ödevi son teslim tarihi: 25 Ocak 2026 Pazar
  
  •	İletişim Kontrol ödevi son teslim tarihi: 1 Şubat 2026 Pazar
  
  •	Otonom Görev Algoritması ödevi son teslim tarihi: 8 Şubat 2025 Pazar

