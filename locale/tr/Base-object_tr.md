_Written for v5.1_(rev.4)

## Genel Bakış

Temel Nesne nesnelerin **en temel özelliklerini** içerir.

- Koordinatlar
- Kapsayıcı(Parent) Nesne
- Alt(Children)
- Biçim
- Klikleme aktif, taşıma aktif gibi özellikler.

Kapsayıcı(parent)'a bağlı olarak **x ve y koordinatları** `lv_obj_set_x(nesne, yeni_x)` ve `lv_obj_set_y(nesne, yeni_y)` fonksiyonları ile veya `lv_obj_set_pos(nesne, yeni_x, yeni_y)` bir fonksiyonu ile ayarlanabilir.

**Nesne boyutu**  `lv_obj_set_width(nesne, yeni_genislik)` ve `lv_obj_set_height(nesne, yeni_yukseklik)` fonksiyonları veya  `lv_obj_set_size(nesne, yeni_genislik, yeni_yukseklik)` fonksiyonu ile modifiye edilebilir. 

Nesneyi `lv_obj_align(nesne1, nesne2, LV_ALIGN_TYPE, x_kaydir, y_kaydir)` fonksiyonu ile başka bir nesneye göre **hizalama**. Son iki argüman (x ve y kaydir) değerleri hizalama yapıldıktan sonra kaydırma değerleridir. İkinci argüman(nesne2) ise ilk argüman(nesne1)'ı hizalamada referans olarak kullanılır ve bu argümana(nesne2)'ye göre hizalama yapar, eğer `NULL` olarak tanımlanmış ise hizalama ekrana göre veya ayarlanmış kapsayıcıya göre uygulanır. Üçüncü eleman ise hizalama türürüdür:
![Hizalama türleri](http://docs.littlevgl.com/img/align.png)

Hizalama türleri `LV_ALIGN_OUT_TOP_MID` bu şekilde oluşturulur. Örneğin bir yazıyı resim dosyasının altına 10 pixel sağa kaydırarak yazdırmak için `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)` şeklinde kullanılır veya yazıy(text)'ı kapsayıcının merkezinde yazdırmak için `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)` şeklinde kullanılır.

Nesne için `lv_obj_set_parent(nesne, yeni_kapsayıcı)` fonksiyonu ile **yeni kapsayıcı** ayarlayabilirsiniz.

Bir nesnenin altlarına sondan başa doğru gitmek için `lv_obj_get_child(nesne, alt_onceki)` fonksiyonu ile, baştan sona doğru gitmek için `lv_obj_get_child_back(obj, child_prev)` fonksiyonu kullanılır. İlk alt birimi geçip bir önceki dönüş değeri için ikinci parametre _NULL_ seçilir. Fonksiyon _NULL_ ile dönüyorsa başka bir alt birim yoktur.

`lv_obj_create(NULL, NULL)` komutu ile **ekran** oluşturduğumuzda, `lv_scr_load(ekran1)` fonksiyonu ile **yükleme** yapabiliriz. `lv_scr_act()` fonksiyonu **geçerli ekran**'na bir işaretçi tanımlar.

Otomatik olarak oluşturulan **iki katman** vardır:

- üst katman
- system katman

Ekranlardan bağımsız olarak oluşturulan nesneler herbir ekranda gösterilecektir. Üst katman(_top layer_) ekrandaki herbir nesnenin üzerindedir ve sistem katmanı(_system layer_) da üst katmanın üzerindedir. Üst katmana pop-up penceresi serbestçe eklenebilir fakat sistem katmanı sistem seviye işleri için sınırlandırılmıştır (örneğin fare imleci buraya taşınmıştır). `lv_layer_top()` ve `lv_layer_sys()` fonksiyonları üst veya sistem katman için bir işaretçi tanımlar.

Nesne için `lv_obj_set_style(obj, &yeni_biçim)` fonksiyonu ile **yeni biçim** tanımlanabilir, eğer biçim `NULL` seçildiyse nesne kapsayıcısının biçim mirasını alır. Eğer nesne için **modifiye bir biçim** kullanılacak ise kesinlikle bunu **nesneye bildirim** yapmamız gerekir. `lv_obj_refresh_style(nesne)` fonksiyonu ile nesnenin biçimini yenileyebilir veya tüm nesnelere `lv_obj_report_style_mod(&biçim)` fonksiyonu ile bildirim yapılabilir. _lv_obj_report_style_mod_'s parametresini `NULL` olarak ayarlayıp tüm nesnelere bildirim yap.

`lv_obj_set_...(obj, true/false)` fonksiyonu ile Aktif/Pasif yapılabilen bazı özellikler:

- **hidden** Nesneyi gizle. Çizilmeyecek ve herhangi bir yer kaplamayacak. Alt elemanlerı da gizlenecek.
- **click** Nesnenin tıklama özelliğini bir girdi cihazı ile aktifleştir (örneğin dokunmatik). Eğer pasif ise, nesne arkasındaki giriş aygıtı tıklama işlemi sırasında kontrol edilir.
- **top** Eger aktifleştirilirse bu nesne veya nesnenin herhangi birine tıklandığında nesne ön tarafa doğru gelir.
- **drag** Sürüklemeyi aktifleştir (bir giriş aracı ile haraket ettirilir)
- **drag_throw** Sürükleme ile bırakmayı aftifleştirildiğinde nesne süskleme ile hızlanma kazanır.
- **drag_parent** Eğer aktifleştirilir ise nesnenin kapsayıcısıda sürüklenir.

Kütüphanede otomatik oluşan bazı özel aksiyonlar vardır, bu bir veya birden çok aksiyondan korunmak için **nesneyi koru** yapılmalı. Mevcut koruma seçenekleri:

- **LV_PROTECT_NONE** Koruma yok
- **LV_PROTECT_POS**  Otomatik pozisyon koruma (örneğin. [lv_cont](/Container_tr))
- **LV_PROTECT_FOLLOW** Takip eden nesnelerin otomatik düzenleme koruma (örneğin. [lv_cont](/Container_tr))
- **LV_PROTECT_PARENT** Otomatik kapsayıcı değişim koruma
- **LV_PROTECT_CHILD_CHG** Alt değişim sinyal pasifleştirme. Kütüphane tarafından kullanılır.

`lv_obj_set/clr_protect(obj, LV_PROTECT_...)` fonksiyonları ile koruma ayarla/temizle yapılır. 'OR' kullanılarak koruma tip değerleri de kullanılabilir.

Nesneler için **gömülü animasyonlar** vardır. Mevcut animasyon türleri:

- **LV_ANIM_FLOAT_TOP** .. dan üst'e kaydır.
- **LV_ANIM_FLOAT_LEFT** .. dan sol'a kaydır.
- **LV_ANIM_FLOAT_BOTTOM** .. dan taban'a kaydır.
- **LV_ANIM_FLOAT_RIGHT** .. dan sağ'a kaydır.
- **LV_ANIM_GROW_H** Yatay Büyült/Küçült 
- **LV_ANIM_GROW_V** Dikey Büyült/Küçült 

`lv_obj_animate(obj, anim_type, time, delay, callback)` fonsiyonu nesneye animasyon uygular. Animasyon yönünü belirlemek için _ANIM_IN_ veya _ANIM_OUT_ animasyon türü seçilir, eğer tür belirtilmemişse varsayılan _ANIM_IN_ dir. Daha fazla bilgi için [animations](/Animations_tr).

## Biçim Kullanımı

Tüm _style.body_ özellirleri kullanır. Normal bir nesne için varsayılan ekranlar _lv_style_plain_  and _lv_style_plain_color_.

## Örnek
![Temel Resim nesnesi](http://docs.littlevgl.com/img/base-obj-lv_obj.png)
```c
/*Basit temel nesne oluştur*/
lv_obj_t * obj1;
obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_size(obj1, 150, 40);
lv_obj_set_style(obj1, &lv_style_plain_color);
lv_obj_align(obj1, NULL, LV_ALIGN_IN_TOP_MID, 0, 40);

/*Bir önceki nesneyi kopyala ve sürüklemeyi aktifleştir.*/
lv_obj_t * obj2;
obj2 = lv_obj_create(lv_scr_act(), obj1);
lv_obj_set_style(obj2, &lv_style_pretty_color);
lv_obj_set_drag(obj2, true);
lv_obj_align(obj2, NULL, LV_ALIGN_CENTER, 0, 0);

static lv_style_t style_shadow;
lv_style_copy(&style_shadow, &lv_style_pretty);
style_shadow.body.shadow.width = 6;
style_shadow.body.radius = LV_RADIUS_CIRCLE;

/*Bir önceki nesneyi kopyala (sürükeleme önceden  aktif edilmiş)*/
lv_obj_t * obj3;
obj3 = lv_obj_create(lv_scr_act(), obj2);
lv_obj_set_style(obj3, &style_shadow);
lv_obj_align(obj3, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -40);
```
