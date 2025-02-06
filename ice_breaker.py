from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser

from linkedin import scrape_linkedin_profile

information2="""
Elon Reeve Musk (d. 28 Haziran 1971, Pretoria, Güney Afrika), mühendis, endüstriyel tasarımcı, teknoloji girişimcisi ve hayırseverdir.[1][2][3][4][5] Elon Musk, günümüz Amerika Birleşik Devletleri Hükümet Verimliliği Bakanı, SpaceX uzay şirketinin kurucusu, CEO'su ve mühendislik ile tasarım ofislerinin şefi;[6] erken yatırımcı,[7][not 1] Tesla otomotiv şirketinin CEO'su ve ürün mimarı,[10][11] X Corp.'un sahibi, yönetim kurulu başkanı ve CTO'su, The Boring Company ve XAI şirketinin kurucusu,[12] Neuralink, Starlink ile OpenAI'nin kurucu ortağı ve ayrıca ilk eş başkanıdır.[13] Doğduğu yer olan Güney Afrika Cumhuriyeti dışında, Kanada ve ABD vatandaşıdır[14] ve yirmi yaşında göç ettiği ABD'de yaşamaktadır.[15][16]

Musk, Musk ailesi'nin üyeleri Kanadalı bir anne ve Güney Afrikalı bir beyaz babanın çocuğu olarak Pretoria, Güney Afrika'da dünyaya geldi ve orada büyüdü.[17] Queen's Üniversitesine gitmek için Kanada'ya taşınmadan önce, kısa süreliğine Pretoria Üniversitesi [en]'ne katıldı.[14] İki yıl sonra Pennsylvania Üniversitesine geçti ve burada Wharton Schooldan[18] ekonomi alanında lisans, fizik alanında ise B.A. ve B.Sc. derecelerini aldı.[19] Doktora derecesine başlamak için 1995 yılında Kaliforniya'ya taşındı ve Stanford Üniversitesinde, uygulamalı fizik ve malzeme bilimleri alanında yüksek lisans yaptı ancak akademik kariyer üzerinden devam etmek yerine iş kariyeri üzerinden devam etmeye karar verdi.[20] 1999'da Compaq tarafından 340 milyon dolara satın alınan bir web yazılım şirketi olan Zip2'yi, kardeşi Kimbal Musk ile birlikte kurdu. Musk, daha sonra çevrimiçi bir banka olan X.com'u kurdu. 2000 yılında, bir önceki yıl PayPal'ı kuran ve Ekim 2002'de eBay'e 1,5 milyar dolara satan Confinity ile birleşti.[21][22][23]

Mayıs 2002'de Musk, günümüzde hâlen CEO'su ve mühendislik ile tasarım ofisleri şefi olduğu, havacılık teknolojisi üreticisi ve uzay taşımacılığı hizmetleri şirketi olan SpaceX'i kurdu. Elektrikli araç üreticisi Tesla Motors, Inc.'e (günümüzdeki Tesla, Inc.) kuruluşundan bir yıl sonra, 2004'te katıldı ve ürün mimarı oldu; 2008'de de şirketin CEO'su oldu. 2006'da, güneş enerjisi hizmetleri şirketi olan SolarCity'nin (günümüzdeki Tesla'nın bir yan kuruluşu) kurulmasına yardımcı oldu. Musk, 2015'te ise dost canlısı olarak gördüğü yapay zekâyı teşvik etmeyi amaçlayan, kâr amacı gütmeyen bir araştırma şirketi olan OpenAI'yi kurdu. Temmuz 2016'da, beyin-bilgisayar arayüzlerini geliştirmeye odaklanmış bir nöroteknoloji şirketi olan Neuralink'i kurdu. Musk, Aralık 2016'da elektrikli araçlar için optimize edilmiş yollara odaklanmış bir "altyapı ve tünel inşaatı" şirketi olan The Boring Company'yi kurdu. Musk, birincil iş arayışlarına ek olarak Hyperloop ismindeki yüksek hızlı bir ulaşım sistemi de tasarladı. Musk, 2018 yılında Kraliyet Topluluğu Üyesi (FRS) seçildi.[24][25] Ayrıca Forbes dergisinin Aralık 2016'da yayımladığı "Dünyanın En Güçlü İnsanları" listesinde 24. sırada;[26] 2019'da, yine Forbes'un yayımladığı "Dünyanın En Yenilikçi İnsanları" listesinde ise ilk sırada yer aldı.[27] Ocak 2021'in ilk haftasında Elon Musk, Jeff Bezos'u geçerek yaşayan en zengin kişi oldu.[28]

Musk, aynı zamanda alışılmışın dışında duruşlar sergilediği ve çok duyurulan skandallara neden olduğu için de eleştirilere konu oldu. 2018 Tham Luang kurtarma operasyonunda [en] denizaltısı uygun bir seçenek olarak görülmeyip reddedildiğinde Musk, dalgıç takımının liderine "pedo adam" dedi. Dalgıç takımının lideri, Musk'a iftira davası açtı ancak California Hukuk Jürisi, Musk'ın lehine karar verdi. Ayrıca 2018'de Musk, Joe Rogan'ın podcastına kenevir içtiği zamana atıfta bulunarak Tesla'nın özel olarak devralınması için hisse başına 420 dolar fon sağladığını tweetledi. ABD Menkul Kıymetler ve Borsa Komisyonu yorum için kendisine dava açtı, Musk geçici olarak başkanlıktan çekildi ve SEC ile anlaşarak Twitter kullanımındaki sınırlamaları kabul etti. Musk ayrıca yapay zekâ, toplu taşıma ve COVID-19 pandemisi hakkındaki görüşlerinden ötürü de önemli eleştiriler topladı. Musk, Twitter'ı 25 Nisan 2022 tarihinde yaklaşık 44 milyar dolara satın aldı. 9 Temmuz 2022'de ise ihalenin şartlarının delindiğini ifade ederek bu satın alım anlaşmasını feshetti.[29] 2024'te ABD Başkanı Donald Trump tarafından Hükümet Verimliliği bakanı olarak atandı

İlk yılları ve ailesi
28 Haziran 1971'de Pretoria, Güney Afrika'da Elon Reeve Musk ismi ile doğdu.[17][30] Annesi Maye Musk (née Haldeman), Saskatchewan, Kanada'da doğmuş fakat Güney Afrika'da büyümüş bir model ve diyetisyendir.[31][32][33] Babası Errol Musk ise Güney Afrika'da doğmuş elektromekanik mühendisi, pilot, denizci, danışman ve emlak geliştiricisidir.[34] Video izleme sitesi Passionflix'ın CEO'su Kimbal adında (1972 doğumlu) bir erkek kardeşe ve Tosca (1974 doğumlu) adında bir kız kardeşe sahiptir.[35][39][33] Anne tarafından büyükbabası Dr. Joshua Haldeman, Birleşik Devletler doğumlu bir Kanadalıydı.[40] Babasının büyükannesinin ise hem İngiliz hem de Pennsylvania Hollandalılarına [en] dayanan soy ağaçları vardı.[41][42]

Annesi ve babası 1980'de boşandıktan sonra Musk, babasıyla birlikte Pretoria banliyölerinde yaşamaya başladı.[41] Ayrıca Musk'ın baba tarafından bir üvey kız kardeşi[43] ve bir üvey erkek kardeşi vardır.[44]

Elon, kendi kendine yazılım programlayıp kodlamayı öğrendi. On iki yaşındayken kendi yazdığı Blastar adındaki uzay oyununu yaklaşık 500 dolara satarak ilk yazılım satışını yaptı.[45] Bryanston High School'da sekizinci ve dokuzuncu sınıfları geçtikten sonra Musk, Pretoria Boys High School'a geçip oradan mezun oldu. 1988 yılında henüz on yedi yaşındayken Güney Afrika ordusunda askerlik yapmamak için evinden ayrıldı ve “Askerlik yapmakla ilgili bir sorunum yok ancak Güney Afrika ordusunda askerlik yapıp siyahi insanları bastırmaya çalışmak bana vakit geçirmek için iyi bir yol gibi görünmedi.”[45] dedi. ABD’ye taşınmak istiyor ve şöyle diyordu: "Orası muhteşem şeylerin mümkün olduğu yer."[46]

1992 yılında Kingston, Ontario’daki Queen's Üniversitesinde iki yıl geçirdikten sonra Pennsylvania Üniversitesinde işletme ve fizik okumak için Kanada’dan ayrıldı. The Wharton School of the University of Pennsylvania’da ana dalını seçip ekonomi alanında lisans diploması aldı. Ayrıca University of Pennsylvania, School of Arts and Sciences’dan da fizik alanında yan dal diploması aldı.[47] Daha sonra uygulamalı fizik ve malzeme bilimi alanında doktora yapmak için Kaliforniya’nın Silikon Vadisi bölgesine taşındı. Ancak doktorayı tamamlamadı.

Lisans eğitimleri ve Thomas Edison, Nikola Tesla, Bill Gates, Steve Jobs, Walt Disney gibi yenilikçilerden aldığı ilhamla[48] Musk; girmek istediği, “insanlığın geleceğini en çok etkileyecek sorunlardan oluşan” üç alan tespit etti. Bu alanlar internet, temiz enerji ve uzaydı.[45]

Kariyeri
Musk, 1995'te Stanford’da uygulamalı fizik ve malzeme bilimi alanında doktoraya başladı. Ancak iki gün sonra kardeşi Kimbal Musk’la beraber yeni organizasyonlar için bir çevrimiçi içerik yayımlama yazılımı olan Zip2 projesine başlamak için okulu bıraktı.[49] 1999’da, Compaq'ın AltaVista birimi Zip2’yu 307 milyon dolar nakit ve 34 milyon dolarlık hisse senedi vererek satın aldı.[50]

PayPal
Ana madde: PayPal
Musk, 1999 yılının mart ayında bir çevrimiçi finans ve ödeme servisi olan X.com’un ortak kuruculuğunu yaptı. Ertesi yıl X.com bir 50/50 birleşme anlaşmasıyla[51] X.com ile aynı büyüklükte bir açık artırma sistemi olan Confinity’yi bünyesine katarak[52] PayPal’ı oluşturdu. Musk, çevrimiçi aktarım veya "P2P" teknolojisine olan inancından dolayı alımın organize edilmesinde kilit rol oynadı.[52] Musk'a göre Confinity alt markası X.com içerisinde bir kişiden kişiye ödeme platformu kurulup geliştirilmesinde mutlaka gerekli bir araçtı.[52] Birleşen şirketler önceleri şirket adı olarak X.com'u tercih ettiler ancak Şubat 2001'de isim değiştirip PayPal Inc. ismini aldılar. Musk, PayPal'ın küresel ödeme sisteminde ve X.com'un çekirdek finansal tekliflerinden ayrılmasında yine önemli bir rol üstlenmişti.[53]

PayPal'ın çabuk büyümesi büyük ölçüde Musk'ın internette yayılarak büyüme kampanyasının sonucudur.[54] Ekim 2002'de PayPal, eBay tarafından 1,5 milyar dolarlık hisse senedi karşılığında satın alındı.[55] Satıştan önce şirketin en büyük hissedarı olan Musk, PayPal'ın %11,7'lik hissesine sahipti.[56]

SpaceX
Ana madde: SpaceX

Musk, eski ABD başkanı Barack Obama ile Falcon 9 fırlatma tesisinde, 2010
Musk, üçüncü şirketi Space Exploration Technologies'i (SpaceX), Haziran 2002'de kurdu.[57] Şu anda bu şirketin CEO’su ve CTO’sudur. SpaceX roket teknolojisinin durumunu ilerletmeye odaklanmış fırlatma araçları geliştirip üreten bir şirkettir. Şirketin ilk iki fırlatma aracı Falcon 1 ve Falcon 9 roketleri, ilk uzay aracı ise Dragon’dur.[58]

SpaceX, 2011’de kullanımı durdurulan Space Shuttle’ın yerini alan Falcon 9 roketi ve Dragon’un Uluslararası Uzay İstasyonu’na 12 uçuşu için 23 Aralık 2008’de 1,6 milyar dolarlık NASA anlaşmasıyla ödüllendirildi. Başlangıçta Falcon 9/Dragon’un kargo taşıma işlevini üstlenmesi ve astronot taşıma işinin Soyuz tarafından yapılması düşünüldü. Ancak SpaceX Falcon 9/Dragon’u astronot taşıma için tasarlamıştı ve Augustine komisyonu da astronot taşımacılığının SpaceX gibi ticari şirketler tarafından halledilmesini önerdi.[59]


NASA Yöneticisi Charles Bolden, Elon Musk'ı, SpaceX'in 13 Haziran 2012'de Uluslararası Uzay İstasyonu'na malzeme taşımak üzere gerçekleştirdiği ilk başarılı görevin ardından 31 Mayıs'ta Dünya'ya dönen tarihi Dragon kapsülünün önünde tebrik ederken.
Musk’a göre uzayın keşfi; insanlığın bilincini, korumak için değilse de genişletmek için önemli bir adımdır.[60] Onun deyişiyle çok gezegenli hayat, insan ırkının hayatta kalmasını tehdit eden şeylere karşı bir önlem olabilir. "Bir asteroit veya büyük bir volkan bizi yok edebilir, ayrıca dinozorların hiç görmediği risklerle karşı karşıyayız: mühendislik ürünü bir virüs, yanlışlıkla oluşturulmuş bir mikro karadelik, küresel ısınma veya sonumuzu getirecek henüz bulunmamış bir teknoloji. İnsan ırkı milyonlarca yıldır evrimleşmekte fakat son altmış yılda atomik silahlar kendimizi tüketmek için bir potansiyel oluşturdu. Er ya da geç hayatı, mavi-yeşil topun ötesine genişletmek zorunda kalacağız ya da soyumuz tükenecek.”

Musk'ın amacı insanlı uzay uçuşlarının maliyetini onda birine indirmektir.[61] SpaceX'i daha önceden sahip olduğu 100 milyon dolarlık bir servetle kurdu. Şu an hâlâ Kaliforniya merkezli şirketin CEO'su ve CTO'sudur.[62]

Yedi yıl içerisinde SpaceX Falcon fırlatma araçları ailesini ve Dragon çok amaçlı uzay aracını sıfırdan tasarladı. Eylül 2009'da SpaceX'in Falcon 1 roketi özel bir şirket tarafından finanse edilmiş Dünya yörüngesine uydu yerleştiren ilk sıvı yakıtlı fırlatma aracı oldu. NASA, Uluslararası Uzay İstasyonu'na kargo ulaştırılması için özel şirketlerin görevlendirildiği ilk programının bir parçası olmak üzere SpaceX'i seçti. Minimum değeri 1,6 milyar dolar, maksimum değeri 3,1 milyar dolar olan bu anlaşma, Uzay İstasyonu'nun kargo alımı ve gönderimine devam eden erişiminin bir mihenk taşı oldu. Bu hizmetlere ek olarak SpaceX'in hedefleri arasında ilk tamamen yeniden kullanılabilir yörüngesel fırlatma aracını oluştururken aynı anda yörüngesel uzay uçuşu maliyetini on kat azaltıp güvenilirliği on kat artırmak bulunmaktadır. Önümüzdeki yıllarda Musk, Uluslararası Uzay İstasyonu'na astronot göndermeye yoğunlaşacaktır ancak belirtmiştir ki nihai hedefi, Mars'ın keşfedilmesini ve iskânını mümkün kılmaktır. 2011'deki bir röportajında 10-20 yıl içinde Mars'a insan göndermeyi umduğunu söylemiştir.[63] 25 Mayıs 2012'de, SpaceX'in Dragon aracı COTS Demo Uçuşu Uluslararası Uzay İstasyonu'na girmiş ve böylece SpaceX Uluslararası Uzay İstasyonu'na bir araç gönderen ve yanaştıran ilk ticari şirket olarak tarihe geçmiştir.

Tesla Motors
Ana madde: Tesla Motors

Musk, Tesla Motors (Fremont, CA) olan NUMMI tesisinin yeniden açılışında bir montaj demosunu gözlemlerken, 2010
Musk, Tesla Motors'un ortak kurucularından biri ve ürün tasarımı başkanıdır. Musk'ın elektrikli araçlara olan ilgisi Tesla'nın ortaya çıkmasından çok daha öncesine dayanır.

Musk, işe Martin Eberhard'ı CEO olarak işe almakla başladı ve ana paranın neredeyse tamamını Tesla'nın ilk iki yatırım turuna yatırdı. 2008'deki ekonomik krizde Tesla'daki zorunlu işten çıkarmalardan sonra[64] Musk, mecburen CEO'luk görevini de üstlendi.

Tesla Motors ilk olarak elektrikli bir spor araba olan Tesla Roadster'ı üretti ve otuz bir ülkede yaklaşık 2.500 adet sattı. Tesla, ilk dört kapılı sedanı Model S'i 22 Haziran 2012'de teslim etti ve SUV/minivan pazarını hedefleyen üçüncü ürünü Model X 9 Şubat 2012'de duyurdu. Model X'in üretimine 2014'te başlanması planlanıyor.[65] Kendi araçlarına ek olarak Tesla, Daimler'e Smart EV ve Mercedes A serisi ve Toyota'ya gelecekte çıkaracağı RAV4 için elektrik motorları ve güç aktarım organları satmaktadır. Ayrıca Musk, bu iki şirketi de Tesla'ya uzun vadeli yatırımcı olarak kazandırmayı başarmıştır.


Musk Kaliforniya Senatörü Dianne Feinstein ile bir Tesla Model S’in yanında, 2010
Musk, özellikle kitlesel pazar müşterilerine uygun fiyatlı elektrikli araçlar sağlama stratejisinin sorumlusudur. Onun vizyonu öncelikle daha varlıklı müşterileri hedefleyen Tesla Roadster ile para kazanıp daha sonra bu parayı daha düşük fiyatlı elektrikli araçların Ar-Ge'sine yatırmaktı. Tesla'nın başlangıcından beri Musk, temel fiyatı Roadster'ınkinin yarısı kadar olan dört kapılı aile arabası Model S'in destekçisi olmuştur. Musk, ayrıca 30.000 dolarlık küçük araçlar yapılmasının ve diğer üreticilere güç üretim ve aktarım organı yapılıp satılmasının da taraftarıdır. Böylece diğer üreticiler bu ürünleri kendileri geliştirmek zorunda olmadan uygun fiyatlı elektrikli araçlar üretebileceklerdir.[66] Birçok ana yayın organı Musk'ı, gelişmiş güç üretim ve aktarım organları üzerindeki devrimsel çalışmalarından dolayı Henry Ford'la mukayese etti.[67]

Raporlara göre Musk'ın Tesla'da %32 hissesi vardır ve bu hisselerin 29 Mayıs 2013 itibarıyla değeri 12 milyar dolardır.[68][69]

Elektrikli araç piyasasındaki uzun menzil kısıtlamasını aşmak için Musk, Mayıs 2013'te All Things D ile yaptığı bir röportajda Tesla'nın şarj istasyonu ağının genişlemesini önemli ölçüde hızlandırdığını, haziran ayında doğu ve batı yakalarındaki istasyon sayısını üç katına çıkarttığını ve yıl içerisinde Kuzey Amerika ve Kanada'da daha fazla genişleme planladığını söyledi.[70]

SolarCity
Musk, en büyük hissedarı ve yönetim kurulu başkanı olduğu SolarCity’ye başlangıç konseptini verdi. SolarCity, Birleşik Devletler’in en büyük güneş enerjisi sistemi sağlayıcısıdır. Kuzeni Lyndon Rive de şirketin CEO’su ve ortak kurucusudur.[71][72] Hem Tesla’ya hem de SolarCity’ye yatırım yapmanın altındaki motivasyon, küresel ısınma ile savaşmaktır.[73] 2012’de Musk, SolarCity ve Tesla Motors’un çatı üzerindeki güneş panellerinin elektrik şebekesi üzerindeki etkisini yumuşatmak için elektrikli araç bataryalarını kullanmak üzere iş birliği yaptığını duyurdu.[74]

Neuralink

Elon Musk ve Mohammad Al Gergawi Yapay Zeka üzerine konuşurken,Dubai,Birleşik Arap Emirlikleri
Musk, 2016 yılında insan beynini yapay zekâ ile entegre etmek için bir nöroteknoloji şirketi olan Neuralink'i kurdu. Şirket, insanların yazılımla birleşmesine ve yapay zekâ alanındaki gelişmelere ayak uydurmasına yardımcı olmak amacıyla insan beynine yerleştirilebilecek cihazlar yaratmaya odaklanmıştır. Bu geliştirmeler belleği geliştirebilir veya bilgi işlem cihazlarıyla daha doğrudan arayüz oluşturmaya izin verebilir.[75]

Ağustos 2020'de canlı bir gösteride Musk, cihazlarından birini yakında felç, sağırlık, körlük ve diğer engelleri tedavi edebilecek "kafatasında bir Fitbit" olarak tanımladı. Birçok sinir bilimci ve yayın, bu iddiaları eleştirdi. Örneğin MIT Technology Review, onları "oldukça spekülatif" ve "sinir bilimi tiyatrosu" olarak tanımladı.[76]

The Boring Company
Musk, 2016 yılında tüneller inşa etmek için The Boring Company'yi (TBC) kurdu. Düzenleyici kurumlarla görüşmeler Ocak 2017'de başladı.[77]

Şubat 2017'de şirket, Los Angeles'taki Space X ofislerinin tesislerinde 9,1 m genişliğinde, 15 m uzunluğunda ve 4,6 m derinliğinde bir "test çukuru" kazmaya başladı. İnşaat izin gerektirmediğinden Las Vegas Kongre Merkezi'nin altındaki bir tünel 2020'nin başlarında tamamlandı. Yerel yetkililer tünel sisteminin daha fazla genişletilmesini onayladı.

The Boring Company, bir satış ve tanıtım dublörü olarak 2018'de 2.000 "alev makinesi" sattı. Fikrin, Musk'ın favorilerinden biri olan Mel Brooks tarafından yönetilen Spaceballs (1987) filminden ilham aldığı iddia edildi.

Twitter
Musk, 2022 yılında büyük Amerikan sosyal ağ hizmeti Twitter'ı 44 milyar dolara satın almayı kabul etti. ABD Menkul Kıymetler ve Borsa Komisyonuna (SEC) yapılan bildirimde, anlaşma için 46,5 milyar dolarlık finansmanın taahhüt eden Musk, Twitter'dan daha önce de yüzde 9,2 oranında hisse satın almıştı.

Başlangıçta satın almaya karşı mesafeli olan Twitter yönetiminin, Musk'ın finansman için harekete geçmesiyle yumuşadığı ve piyasadan hisseleri toplayarak şirket yönetimini ele alma ihtimali karşısında görüşmelere sıcak baktığı iddia edilmişti.

Musk, 9 Temmuz 2022'de ise ihalenin şartlarının delindiğini ifade ederek bu satın alım anlaşmasını feshetti.

Kişisel hayatı
Elon'un kız kardeşi Tosca Musk, yönetmendir. Musk Entertainment'ın kurucusudur ve çeşitli filmler çekmiştir. Musk, ilk eşi Kanadalı yazar Justine Wilson ile tanışırken her ikisi de Ontario Kraliçe Üniversitesinde öğrenciydi. 2000 yılında evlendiler ve 2008'de ayrıldılar. İlk oğulları Nevada Alexander Musk, on haftalıkken ani bebek ölüm sendromundan (SIDS) öldü. Daha sonra in vitro fertilizasyon yoluyla beş oğlu oldu: 2004'te ikizler, ardından 2006'da üçüzler. Beş oğlun hepsinin velayetini paylaştılar.

2008'de Musk, İngiliz aktris Talulah Riley ile çıkmaya başladı ve çift, 2010'da evlendi. Ocak 2012'de Musk, Riley ile dört yıllık ilişkisini sona erdirdiğini açıkladı. Temmuz 2013'te Musk ve Riley yeniden evlendi. Aralık 2014'te Musk, Riley'den ikinci bir boşanma davası açtı ancak dava geri çekildi. Medya Mart 2016'da boşanma işlemlerinin yeniden başladığını açıkladı. Bu sefer Riley, Musk'a boşanma davası açtı. Boşanma davası 2016 sonlarında sonuçlandırılmıştır.

Musk, 2016 yılında Amerikalı aktris Amber Heard ile çıkmaya başladı ancak ikisi bir yıl sonra ayrıldı.

7 Mayıs 2018'de Musk ve Kanadalı müzisyen Grimes, çıkmaya başladıklarını açıkladı. 8 Ocak 2020'de Grimes ilk çocuğuna hamile olduğunu açıkladı. Grimes, 4 Mayıs 2020'de doğum yaptığını açıkladı.[78][79] Musk, çocuklarına "X Æ A-12" adını verdiğini iddia etti.[80] Eylül 2021'de çeşitli nedenlerden dolayı ilişkileri bitti.[81] 2024 itibarıyla Musk'ın 12 çocuğu vardır[82]

Yardımları
Musk'ın başkanı olduğu Musk Foundation; bilim eğitimi, çocuk sağlığı ve temiz enerji üzerine hayır işlerine yoğunlaşmış durumdadır. Musk aynı zamanda yenilenebilir enerjiyi teşvik eden X Prize Foundation’da da mütevellidir. Diğer kâr amacı gütmeyen kuruluşlardan olan Space Foundation, National Academies Aeronautics and Space Engineering, Planetary Society ve Stanford Engineering Advisory Board yönetim kurullarının da üyesidir. Ayrıca Musk Kaliforniya Teknoloji Enstitüsünün de mütevelli heyetinin üyesidir.

2010 yılında kendi vakfı aracılığıyla afet bölgelerindeki kritik ihtiyaçları karşılamak için güneş enerji sistemlerine bağış yapmak için milyon dolarlık bir program başlattı. Buna örnek olacak ilk güneş enerji sistemi bağışı, devlet ve federal yardımlar tarafından görmezden gelinen Alabama’daki kasırga müdahale merkezine yapıldı. Bu işin Musk’ın ticari amaçlarıyla bir ilgisi olmadığı açıkça göstermek için SolarCity Alabama bölgesiyle ilgili şimdiki veya gelecek zamana dair herhangi bir planlarının bulunmadığını açıkladı.[83]

Musk’ın 2001 yılında Mars’ta küçük bir sera kurup bitki yetiştirmek amaçlı “Mars Vahası” adlı planları vardı.[84][85] Ancak insanlığın uzayda dolaşabilmesini engelleyen sorunun roket teknolojisinin gelişmemesinden kaynaklandığı sonucuna vardığında bu projesini askıya aldı. Bu konuyu ele almak ve gezegenler arası devrimsel roketler yapmak için SpaceX'i kurdu.

Musk'ın uzun vadeli amacı SpaceX vasıtasıyla uzayda gezinen bir medeniyet yaratarak insanlığa yardım etmektir.[86] Musk'ın felsefesi ve problemi çözmek için gerekli olan şey tanımı IEEE yayını olan "Elon Musk: Paypal, Tesla Motors ve SpaceX’in bir kurucusu"[87] yayınında ve "Risky Business" makalesinde verilmiştir.[85]

Musk, Nisan 2012'de The Giving Pledge’e katıldı ve servetinin çoğunu hayır işlerine bağışlayacağını taahhüt etti.[88] Musk, ilk önce Warren Buffett ve Bill Gates sayesinde meşhur olan kampanyaya aralarında Arthur Blank ve Michael Moritz’in de bulunduğu Amerika’nın en zengin ailelerinden ve kişilerinden oluşan on iki kişilik grupla üye olmuş oldu.[88]

Araba blogu Jalopnik’in 16 Ağustos 2012 tarihli haberine göre Musk The Oatmeal'dan Matthew Inman’ın, Nikola Tesla'nın Long Island, New York’taki laboratuvarını koruyup bir müzeye çevirme çabasını destekliyordu.[89]

Musk, diğer bir yüksek profilli girişimci olan Mark Zuckerberg ve göçmen reformunun destekçileri tarafından başlatılan Birleşik Devletler Politik Hareket Komitesi (PAC) FWD.us’ın destekçisiydi. Ancak Mayıs 2013’te PAC’ın Keystone Boru Hattı gibi bir sorunu destekleyen reklamlarını protesto etmek için desteğini açık bir şekilde geri çekti. Kanun koyucuların hoşgörüsünü kazanmak amacıyla PAC’çıların, politik yelpazenin her iki ucuyla ilgili sorunları desteklemeleri; alışılagelmiş bir durumdur. Musk ve grubun David Sacks gibi bazı diğer önemli üyeleri organizasyondan çekildiler ve grubun bu stratejisini “toplumsal değerleri küçümseyen” bir hareket olarak nitelendirdiler.[90]
"""
 

if __name__ == '__main__':
    print("Hello, LangChain!")
    print(os.environ['OPENAI_API_KEY'])

    summary_template="""
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template=PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    #llm=ChatOllama(model="llama3")
    #llm=ChatOllama(model="mistral")
    chain=summary_prompt_template | llm | StrOutputParser()
    linkedin_data= scrape_linkedin_profile("",True)
    res = chain.invoke(input={"information":linkedin_data})
    
    print(res)