

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


>[!INFO] Pythondaki veri yapilari su sekilde java ya benzetilebilir
> Dictionary = Hashmap
>  Set = HashSet
>  List = ArrayList
>  Tuple = Immutable List
>  String = Char Array

>[!INFO] Listelerde slicing mantigi
> [Start Index : Last Index : Hopping Value]
> seklinde listenin istenen bolumu alinabilir











