# projekt-zespolowy

#OPROGRAMOWANIE BIBLIOTEKI

Przedmiotem niniejszego projektu jest stworzenie aplikacji dla pracowników biblioteki która zautomatyzowałaby proces przechowywania danych o książkach, wypożyczających i wypożyczeniach. Zastępując tradycyjne karty biblioteczne.

Mamy panel administracyjny dla pracownika biblioteki. Wypożyczający fizycznie wybiera książke z półki i przynosi pokazać ją 
pracownikowi. Po kodzie ID książki i zarejestrowanego wypożyczającego tworzymy wpis w bazie o wypożyczeniu wraz z terminem zwrotu. Teraz 
wypożyczający może zabrać książkę. Wypożyczający może również oddawać ksiązki wtedy wpis z tablicy wypożyczeń znika. W panelu administracyjnym można 
dodawać książki i użytkowników.

Wykorzystujemy następujące technologie:

Python

SQLite

Django

#jak z niego korzystać?

użytkownik loguje się do aplikacji swoim loginem i hasłem. Użytkownik ma do wyboru nastepujące zakładki:

1. Books:

w tej zakładce można wyszukiwać książki po gatunkach po autorze tytule czy ID. Kiedy wypożyczający wysunie prośbę o zaporponowanie jakiejś ksiązki lub znalezieni konkretnej.

2. Edit Book:

użytkownik może edytować wpis dotyczący książki. Jeżeli poda istniejący ID książki wówczas nadpisze stary rekord w bazie danych. Jeżeli poda nowy ID nowa książka pojawi się w bazie. Pamiętajmy że możę być wiele egzemplarzy tej samej książki w bibliotece ale każda ma swój indywidualny ID.

3. Edit Borrower:

użytkownik może edytować wpis dotyczący wypożyczającego. Jeżeli poda istniejący ID wówczas nadpisze stary rekord w bazie danych. Jeżeli poda nowy ID nowy wypożyczający pojawi się w bazie. 

4. Borrower:

Tutaj wpisując ID wypożyczającego otrzymamy jego kartę z jego danymi osobowymi oraz z listą wypożyczonych książek. Książki których termin oddania został przekroczony zostaną wizualnie wyróżnione. Znajduje się również tam przycisk wypożycz który przekieruje do formularza wypożyczenia. Należy uzupełnić dane wypożyczenia aby zdarzenie wypożyczenia zostało zapisane do bazy danych


#Notatki developera:

w repozytorium nie ma gotowej bazy danych. Użyj create_test_data() z modułu populate_db aby zasiedlić bazę danych przykładowymi wpisami

baza danych składa się z 4ch tablic:

1.Borrowers: przechowuje rekordy wypożyczających

2.Books: przechowuje rekordy książk

3.Administrators: przechowuje rekordy z danymi pracowników biblioteki łącznie z hasłami

4.Borrows: przechowuje informacje o tym kto wypożyczył jaką książkę
