Budowa aplikacji lokalnie : 
Początkowo w bash’u musimy trafić do folderu w którym wcześniej stworzyliśmy wszystkie pliki potrzebne naszej aplikacji do działania, oraz plik dockerfile na podstawie którego możemy stworzyć obraz aplikacji.
Następnie w bash’u wprowadzamy komendę (sudo docker build –t NAZWA_OBRAZU:TAG . ). Komenda ta na podstawie pliku dockerfile znajdującego się w katalogu w którym obecnie się znajdujemy (stąd kropka na końcu polecenia)
stworzy obraz o nazwie oraz tag’u podanym w komendzie. Następnie po zbudowaniu obrazu przechodzimy do uruchomienia go lokalnie. Aby to zrobić do bash’a wprowadzamy polecenie (docker run NAZWA_OBRAZU:TAG). 
Dzięki temu poleceniu nastąpi uruchomienie lokalne obrazu. Aby prześledzić zachowanie naszego obrazu możemy skorzystać z komendy (docker logs ID_OBRAZU). ID_OBRAZU otrzymujemy po uruchomieniu obrazu w bash’u. 


Uruchomienie aplikacji w chmurze (Azure Microsoft): 

1.Początkowo tworzymy Grupę Zasobów 
Grupa Zasobów logicznie organizuje wszystkie składowe naszej aplikacji w chmurze takie jak Rejestr Kontenerów, Serwer Bazy Danych oraz App Serivce. 

2.W następnej kolejności przechodzimy do utworzenia Rejestru Konternerów 
To właśnie do tego miejsca będziemy pushować obrazy, które początkowo testujemy lokalnie. Konfiguracja Rejestru Kontenerów powinna odpowiadać założeniom naszej aplikacji w możliwie najlepszy sposób, 
ponieważ opłaty związane z naszą aplikacją tyczą się zużywanych przez nas zasobów. 

3.Przekazanie obrazu naszej aplikacji do Rejestru Kontenerów 
W tym miejscu nastąpi spushowanie naszego obrazu do Rejestru Kontenerów. Aby tego dokonać początkowo musimy się zalogować się korzystając z polecenia w bash’u (docker login NAZWA_REJESTRU.azurecr.io).  
Tutaj zostaniemy zapytani o klucze dostępu które na przykładzie naszej aplikacji możemy znaleźć w sekcji Klucze dostępu. Gdy uda nam się już zalogować do naszego rejestru możemy przejść do właściwej czynności.  
Tzn. Pushujemy obraz do rejestru. Aby tego dokonać musimy go odpowiednio otagować tak by dotarł do naszego rejestru. Korzystamy z polecenia (docker tag NAZWA_OBRAZU:TAG NAZWA_REJESTRU.azurecr.io/NAZWA_OBRAZU:TAG). 
Gdy już otagujemy obraz w odpowiedni sposób to przystępujemy do pushowania obrazu za pomocą polecenia (docker push NAZWA_REJESTRU.azurecr.io/NAZWA_OBRAZU:TAG). 
Aby sprawdzić czy wszystko dobrze zrobiliśmy możemy przejść do zakładki repozytoria w rejestrze kontenerów, ponieważ to tam będzie widoczny nasz obraz. 

4.Konfiguracja App Services 
Tutaj konfigurujemy naszą aplikację. W naszym przypadku korzystaliśmy z aplikacji internetowej. Istotne jest to aby stworzyć ją na podstawie ówcześnie stworzonej grupy zasobów oraz Rejestru Kontenerów. 
Resztę aplikacji konfigurujemy według naszych potrzeb. 

5.Stworzenie i konfiguracja Serwera Bazy Danych. 
W naszym przypadku korzystaliśmy z Serwerów elastyczne usługi Azure Database for PostgreSQL. Konfiguracja tutaj też jest zależna od nas, lecz najistotniejsze jest tutaj to aby odpowiednio wybrać 
dostępność naszego serwera w zależności od naszych potrzeb, oraz stworzyć odpowiednio chronionego użytkownika bazy danych. Istotna uwaga odnośnie hasła jest taka aby unikać korzystania z znaków specjalnych w 
nazwie oraz haśle o ile nie chcemy ich kodować ponieważ może to spowodować później problemy w połączeniu się z bazą danych. 
Gdy stworzyliśmy już Serwer Bazy Danych istotne jest to aby również ją fizycznie tam stworzyć i nazwać. 

6.Dodanie zmiennych środowiskowych 
W naszym przypadku polegało to na przejściu ponownie do App Services i przejścia do zakładki zmienne środowiskowe. Nasza aplikacja wymagała tego, by skonfigurować port na którym aplikacja nasłuchiwała oraz 
skonfigurowania zmiennej CONNECTION_STRING, która odpowiadała za połącznie z bazą danych. Port który ustawiliśmy to 8000 oraz zmienną odpowiadającą za połączenie z bazą danych tworzyliśmy na podstawie schematu 
(postgresql://NAZWA_UŻYTKOWNIKA_BAZY_DANYCH: HASŁO_UŻYTKOWNIKA_BAZY_DANYCH @NAZWA_SERWERA_BAZY_DANYCH.postgres.database.azure.com:5432/NAZWA_BAZY_DANYCH) 
