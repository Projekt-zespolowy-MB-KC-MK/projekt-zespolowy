# projekt-zespolowy

Biblioteka. Mamy panel administracyjny dla pracownika biblioteki. Wypożyczający fizycznie wybiera książke z półki i przynosi pokazać ją 
pracownikowi. Po kodzie ID książki i zarejestrowanego wypożyczającego tworzymy wpis w bazie o wypożyczeniu wraz z terminem zwrotu. Teraz 
wypożyczający może zabrać książkę. Na razie wypożyczajacy nie ma możliwości dostepu do systemu i np. sprawdzenia swojej historii terminów itp. 
ale można to dodać później. Wypożyczający może również oddawać ksiązki wtedy wpis z tablicy wypożyczeń znika. W panelu administracyjnym można 
dodawać książki i użytkowników. Tak wygląda kształt MINIMALNY projektu. 
Python
SQL
Django/Flask
HTML
CSS
JS

Jak go dowieziemy, to bedziemy stopniowo dodawać nowe ficzery jak np usuwanie ksiązek, wypożyczających. Poszukiwanie ksiązek, wypożyczających. 
Możliwość przeglądania swoich danych przez wypożyczającego. Notyfikacje o terminie upływu itd 



main.py służy do testowania

populate_db.create_test_data(library) 

wypełnia bibliotekę przykładowymi wpisami

#UWAGI DLA TYCH KTÓRZY BEDA ROBIC FRONTEND:

zainicjuj obiekt typu Library

o ile nie wypełnisz biblioteki jakimś testowymi danymi będzie ona pusta: 
populate_db.create_test_data(library)

wszystko co potrzebujesz jest w library.py

metody które się tam znajdują obsługują najczęsciej wymagane czynności jak dodanie nowego wypożyczającego, nowej książki (pamiętaj o unikatowych ID!), także wypożyczenie,
oddanie, listowanie wszystkich ksiązek listowanie wypożyczających znajdz wypozyczajacego czy ksiązkę po id

musisz zbudować jakiś interfejs dla pracowników biblioteki. W backendzie mamy obiekt administrator. W bazie danych jest hasło admina
