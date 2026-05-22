# Nisan-2026-PDF-Abuse
çoktan patch almis birşey paylaşmak istedim inanılmaz zekice bir payload bunca yıl oturmuş olduğu düşünülen bir sistemde bulunan inanılmaz api açığı ve bunun nereye kadar sömürülebildigini gormenize yarayacak bir rehber. kodlar kullanıma kapalıdır zaten patch almış denemeyin bile 






APRIL 2026 (patched)



Bu Proje Zaten Patchlenmiş bir sistemin sadece yakın dönemde tespit edilmiş büyük bir ntdll api abuse oldugunu ve bu abuse'un nasıl calıstıgını insanlara detaylıca
anlatmak için oluşturulmuş Türkce bir rehberdir. Günlük hayatta tıklayacağımız bir pdf uzantılı dosyanın bile bilgisayarımızdaki bütün verileri baştan aşagı çalabileceği
ve bu tarz risklere karşı dikkatli olunması gerektiğini anlatacak bir örnek yazılımdır
asla kimsenin kullanmasını tavsiye etmiyorum bu bir örnektir ve kullanıma kapalıdır 









Fazla Kapsamlı API İstismarı ZERO DAY 
 Bellek İçi Çok Katmanlı Kod Çözme ve Güvenlik İllüzyonunun Çöküşü //CVE-2026-34621 Mimarisi



Bu laboratuvar, modern siber tehdit dünyasının en karanlık, en sinsi ve en deha işi operasyonlarından birini analiz etmek amacıyla kurulmuştur. Dijital dünyada neredeyse her kullanıcının sorgusuz sualsiz güvendiği, her gün milyarlarca bilgisayarda mutlak bir meşruiyetle çalıştırılan sıradan bir PDF dosyasının (Adobe Reader), aslında işletim sisteminin kalbine sızabilen sessiz bir suikastçıya nasıl dönüştürülebileceğini inceler.

Geleneksel imza tarayıcıları, gelişmiş EDR (Endpoint Detection and Response) sistemleri ve hatta işletim sisteminin en derin katmanlarında çalışan agresif Anti-Cheat yazılımları bile bilgisayarınızda mutlak bir koruma sağladığı illüzyonunu yaratır. Ancak bu laboratuvarda masaya yatırdığımız CVE-2026-34621 mimarisi, bu savunma hatlarının aslında ne kadar kırılgan ve manipülasyona açık olduğunu kanıtlamaktadır. 

Saldırganlar dışarıdan sisteme yabancı, şüpheli veya imzasız bir dosya enjekte etmek yerine; zaten sistemde kurulu olan, kurumsal olarak devasa bir güvenilirliğe sahip platformun kendi iç yeteneklerini kötüye kullanarak (API Abuse) tüm güvenlik mekanizmalarını tamamen körleştirmiştir.

Tekrarlıyorum, bu proje hiçbir şekilde aktif bir exploit (istismar kodu) veya silahlandırılmış zararlı yazılım bileşeni içermez. Projenin amacı; siber güvenlik mühendisliği, tehdit avcılığı ve anti-cheat mimarilerinin zafiyet noktalarını ve kör noktalarını anlamak amacıyla geliştirilmiş kavramsal analizlerden ibarettir.




Siber güvenlik literatüründe en ölümcül saldırı, sistemin canını yakacağını bağıran değil; sistemle aynı dilde konuşarak onu kendi güven zinciriyle vuran saldırıdır. Bu vakayı siber güvenlik tarihinin en zekice kurgulanmış olaylarından biri yapan unsurlar tamamen psikolojik ve mimarisel güven kırılmalarına dayanır.

 Sıradan Bir PDF'in Arkasındaki Deha ve Psikolojik Silahlanma
Bir internet kullanıcısı `.exe`, `.scr` veya `.bat` uzantılı bir dosya açarken doğal bir şüphe duyar, defans mekanizmaları uyanıktır. Ancak `.pdf` uzantısı, evrensel dijital iş akışının, faturaların, resmi sözleşmelerin ve akademik makalelerin dokunulmaz kutsal sığınağıdır. Bir dökümana tıklamak, kullanıcının gözünde sıfır risk taşır. 

Saldırganlar tam olarak bu psikolojik güveni silahlandırmıştır. Kullanıcı sadece bir dökümanı görüntülediğini zannederken, arka planda işletim sisteminin tüm bellek haritasını çıkaran, bellek korumalarını (ASLR) hiçe sayan bir süreç tetiklenmektedir.

 Anti-Cheat ve EDR Sistemlerinin Mutlak Çaresizliği
Bugün Ring 0 (Kernel/Çekirdek) seviyesinde çalışan anti-cheat yazılımları (Vanguard, EAC, Faceit yarragı vb.) veya kurumsal EDR ajanları, bilgisayardaki her işlemi, yüklenen her driver'ı milimetrik olarak izler. Ancak bu sistemlerin en büyük yapısal yumuşak karnı Güvenilir Süreç Delege Etme mantığıdır ve bu operasyon tam olarak bu kör noktaya hançer saplamaktadır:

Sonsuz Güven İllüzyonu: Güvenlik ve anti-cheat yazılımları, dijital olarak imzalanmış, Adobe gibi küresel ve meşru süreçlerin (`AcroRd32.exe`) her an bellek sayfalarını tarayamaz. Eğer bu tarz devasa uygulamaların RAM alanları sürekli deşifre edilip taranmaya kalkışılırsa, sistem performansı çöker, oyunlar kilitlenir ve tonlarca "Hatalı Pozitif" (False Positive) alarmı üretilir.
Fileless (Dosyasız) Operasyon: Kod disk uzerinde hiçbir iz bırakmaz. Sabit sürücüye hiçbir şüpheli DLL yazılmadığı, her şey doğrudan meşru uygulamanın kendi hafıza alanında Base64 olarak çözülüp sessizce yürütüldüğü için çekirdek seviyesindeki korumalar tamamen devre dışı kalır.
İmzasız Sürücü/Kod Yoktur: Anti-cheat yazılımları sisteme sızmaya çalışan yabancı driver'ları engellemek üzere programlanmıştır. Ancak burada yabancı bir driver yoktur; saldırgan, sistem korumalarının burnunun ucunda, onların en güvendiği müttefiki (Adobe'un kendi onaylı motorunu) kullanarak operasyonu yürütür.


 ABUSE MANTIĞININ DERİNLEMESİNE ANALİZİ

Bu saldırının özü, bir açığı tetikleyip programı çökertmek değil, programın yasal fonksiyonlarını birer casusluk enstrümanına dönüştürmektir. "Abuse" mantığı üç ana fazda vücut bulur:

Çok Katmanlı Geçici Bellek Gizlemesi (In-Memory Obfuscation)
Tehdit aktörleri, statik tarayıcıların string (metin) eşleştirme algoritmalarını tamamen felç etmek için veriyi iç içe geçmiş katmanlar halinde soyutlar. Dosya ilk açıldığında çalışan ana kod bloğunda (Orkestra Bloğu) hiçbir zararlı komut veya şüpheli API çağrısı bulunmaz. Bu kod sadece dosyanın içine, kod analiz bölgesinin tamamen dışına (örneğin bir form butonunun metadata değerine) saklanmış pasif, yüksek entropili bir metin akışını arar. 

Bu veri diskteyken anlamsız bir gürültüden ibarettir. Ancak orkestra bloğu bu veriyi RAM'e çektiği an maske yavaş yavaş düşmeye başlar. Kod, dinamik değerlendirme döngülerini (uygulamanın iç zamanlayıcılarını) kullanarak bu veriyi çözer ve doğrudan bellek sayfalarında yürütür.

 Ayrıcalıklı API'lerin Silahlandırılması (Privileged API Abuse)
Normal şartlarda bir bellek havuzunda (Sandbox) izole edilen bir dökümanın, işletim sisteminin kritik bileşenlerine dokunamaması gerekir. Ancak bu deha işi mantıksal zafiyet, uygulamanın kendi iç sınırlarını aşmasını sağlar:
util.readFileIntoStream() İstismarı: Bu fonksiyon, normalde sadece döküman içi stream operasyonları için tasarlanmışken, mantıksal bir sınır hatasıyla manipüle edilerek işletim sisteminin kalbi olan `ntdll.dll` dosyasını ham byte dizisi olarak okumak için kullanılır. Amaç, sistemin canlı bellek offsetlerini haritalandırmak ve ASLR korumasını dinamik olarak alt etmektir.
RSS.addFeed() İstismarı: Toplanan sistem parmak izlerini (Fingerprint) dışarı sızdırmak için hiçbir şüpheli socket veya network bağlantısı açılmaz. Uygulamanın meşru haber kaynağı ekleme fonksiyonu kötüye kullanılarak, veri bir HTTP parametresi olarak dışarı fırlatılır. Network firewall ve EDR sistemleri, meşru bir Adobe süreci dış dünyaya standart bir web isteği attığı için bu trafiği tamamen zararsız kabul eder.

Asenkron Kurban Filtreleme ve Nihai Karar
Saldırganlar bu sıfırıncı gün açığını alelade harcamamak adına inanılmaz bir soğukkanlılıkla hareket eder. Sistem bilgileri dışarı sızdırıldıktan sonra, Komuta Kontrol (C2) sunucusu gelen profili analiz eder. Eğer kurban bir siber güvenlik araştırmacısı, bir analiz laboratuvarı veya otomatik bir sandbox ise, sistem kendini tamamen kapatır ve hiçbir zararlı faaliyet göstermez; böylece açık "yanmamış" (unburnt) olur. 

Ancak hedef yüksek profilli bir devlet kurumu, kritik bir endüstri veya hedef alınan spesifik bir sistem ise, sunucu onay verir ve asıl yıkıcı Uzaktan Kod Çalıştırma (RCE) emrini geri göndererek bilgisayarı tamamen teslim alır.


 BÜYÜK PLATFORMLARDAKİ BU TARZ AÇIKLARIN KÜRESEL ETKİSİ

Adobe veya benzeri küresel ölçekteki platformlarda meydana gelen bu tarz mantıksal koruma kırılmaları, siber dünyada zincirleme bir reaksiyon başlatır:

Güven Zincirinin Mutlak Çöküşü: Kullanıcılar en temel dijital element olan bir dökümanı açarken bile sistemlerinin ele geçirilebileceğini görür. Güven illüzyonu yok olur.
Whitelist Silahlanması: Koruma yazılımlarının performansı korumak için tasarladığı "güvenilir uygulamalar" listesi, saldırganların en büyük sığınma mekanizması haline gelir.
Tek Tıklamayla Gelen Teslimiyet: Kullanıcı ruhu bile duymadan, hiçbir ek yetki yükseltme (UAC) uyarısı almadan, sadece meşru bir uygulamayı başlattığı için tüm dijital varlığı (tokenlar, şifreler, cüzdanlar) saniyeler içinde buharlaşır.



PROJE DİZİN YAPISI VE SONRAKİ ADIMLAR

Bu analiz laboratuvarı, teoriyi kod mimarisinden ayırarak her bir bileşenin saf, karmaşık ve derinlemesine incelenmesini kolaylaştırmak adına çoklu dosya yapısına bölünmüştür. 

Analiz etmek istediğiniz dinamik katmanlara göre aşağıdaki harici dosyalara odaklanabilirsiniz:

1.  loader.js: Tamamen karartılmış, diske temas etmeyen, statik tarayıcıları felç eden yüksek entropili Bellek İçi Çözücü ve Orkestra Motoru kod bloğu.
2.  exploit.js: Uygulamanın korumalı alanını (Sandbox) delerek `ntdll.dll` modülünü okuyan ve meşru network fonksiyonlarını casusluk aracına dönüştüren Ayrıcalıklı API İstismarı (Abuse) kod bloğu.
3.  telemetry.py: Bu gizli bellek operasyonlarını ve sinsi network isteklerini dinamik olarak yakalamak, Shannon Entropi değişimlerini hesaplamak için geliştirilmiş Defansif Teşhis ve Analiz Motoru.
