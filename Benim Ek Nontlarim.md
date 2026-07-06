

# Veri tipleri

>[!INFO] Python da Obje ve Ram Mantigi
> Pythonda tum veriler heapte tutulur bunu da cok ozel bir mekanizma ile yapar
> aslinda bir struct icinde veriyi tutan degiskenler ReferenceCounter - Garpage collector icin, verinin tipi, adresi gibi bir degisken olusturur ve esas veri heapte tutulur sadece bu yapi stackte yer alir

```python
#ornek vericek olusak asagidaki yapiya bakalim ve ne oldugunu inceleyelim

a = 5
b = a
a = 10

# Burada arka planda heapten 4 baytlik bir alan alinir ve ve icine 5 yazilir
# Daha sonrasinda b=a ile b yapisi da a ile ayni yeri gosterir
# a = 10 yapildiginda heapten yine 4 baytlik bir alan alinir ve icine 10 yazilir a burayi gostermeye baslar
# b hala 5 in oldugu alani gosterdiginden 5 kismi serbest birakilmaz
# yani python da aslinda tum veriler heap bellek bolgesinde tutulur
 

```


> Pythondaki veri yapilari su sekilde java ya benzetilebilir
> Dictionary = Hashmap
>  Set = HashSet
>  List = ArrayList
>  Tuple = Immutable List
>  String = Char Array

> Listelerde slicing mantigi
> [Start Index : Last Index : Hopping Value]
> seklinde listenin istenen bolumu alinabilir

---
# Python da Class yapilari

> Pythonda sinif yapilari class anahtar kelimesi ile olusturulur
> kurucu fonksiyonu __init__(self) fonkisoyu ile olustulur
> ek kurucular tanimlanmak istenirse @classmethod anatasyonu ile tanimlanabilir
> Siniflardaki private fonksiyonlar tanimlanirken basina __ eklemesi yapilabilir

```Python
    class MyNewClass
    
    def __init__(self, name, age, no):
        # Buradaki self this anahtar kelimesi gibidir sinifin kendini gosteren pointerdir
        # Bu sinif altina yazilan fieldlar ayni zamanda class in propertyleri olur
        self.name = name
        self.age = age
        self.no = no

    def __isNoValid(self):
        if no % 2 == 0:
            return True;
        return False


```


---
# Modules

```Python

import module # Tum modulu getirir

from module import function # module icindeki sadece istenen fonksiyonu ve fonksiyonun bagimliliklarini projye dahil eder 

```


> modullerde __init__.py dosyasi olmasi gerekir python yorumlayicisi bu sekilde bu dosyanin bir package oldugunu anlar
> gereken sub modullerde de bu init dosyasinin bulunmasi gerekir. Sub modulleri dahil etme syntaxi asagisaki gibidir

```Python
    import modul.submodule
```

