# Arkkitehtuurikuvaus
----
## Rakenne ja Sovelluslogiikka

Sovelluksen rakenteeseen kuuluvat pakkaukset UI, objects ja sprites. Objects pakkaukseen kuuluvat luokat player, ship ja board. Sovelluksessa on 4 käyttöliittymäluokkaa menu, single, pvc ja scores, sekä 13 sprites-luokkaa. Kansiossa src sijaitsee sovelluslogiikka, kansiossa ui käyttöliittymät, objects kansiossa olio-luokat ja kansiossa sprites sprite-luokat. Kansiossa assets sijaitsevat ui tarvitsemat kuvatiedostot sekä image-luokka.

![Rakenne](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/class_diagram.png)

Luokassa Player on yksi käyttämätön metodi, jolle on tehty oma testi. Metodi on set_name() ja se on luotu käyttäjäkohtaisten tulosten tallentamista varten. Kuitenkin, toiminnallisuutta pelaajan oman nimen/tunniksen syöttämiseksi ei ehditty toteuttamaan ja se jäi jatkokehitykselle. Tämän vuoksi metodia ei ole poistettu ohjelmasta.

----
## Käyttöliittymä

Käyttöliittymäluokat ovat menu, single, pvc ja scores. Menu luokkaa sisältävät aloitusvalikon, josta voidaan valita haluttu peli, tarkastella tuloksia tai lopettaa sovelluksen käyttäminen.

----

##Tietojen pysyväistallennus

Luokka Results tallentaa peleistä syntyvät tulokset txt. tiedostoon. Kun käyttäjä halua tarkastella tuloksia, Main luokka hakee tulokset tiedostosta, järjestää ne ja palauttaa kolme parasta tulosta. Nämä tulokset näkyvät Scores käyttöliittymäosassa.

Sovellus tallentaa tiedot txt- tiedostoon muosossa: 'Pelaajan nimi, score'. Jokainen tulos tallentuu omalle riville.

----
## Päätoiminnallisuudet

### Päävalikon alueiden toiminta

Sovelluksen käynnistyessä ohjelma avaa ohjelman Päävalikon. Käyttäjä valitse toiminnon. 

Jos käyttäjä valitsee Lopeta Peli toiminnon, palauttaa Menu arvon Quit ja ohjelma sulkeutuu. 

Jos käyttäjä valitsee Yksinpelin, palauttaa Menu arvon Single. Main alustaa yksinpelin luomalla pelikentän (Board). Board luokka luo 5 laiva-oliota (Ship), sekä arpoo laivoille paikat kentällä. Koordinaattien arvonnan jälkeen board luokka tarkistaa, että laiva on kentällä ja laiva ei ole päällekkäin muiden laivojen kanssa. Metodi palauttaa True, jos laivan sijoittaminen kentälle onnistuu. Muutoin arvotaan uusi koordinaattipari. Tämän jälkeen luodaan ja alustetaan Single käyttäliittymä ja aloitetaan pelisilmukka. Silmukassa hiirenklikkauksella saadaan koordinaattipari ja kutsutaan board luokan metodia shot(). Jos tulos on 'ohi', peli jatkuu. Jos tulos on 'osuma', tarkistaa board luokka laivan tilanteen. Jos laivan kaikkiin ruutuihin on osuttu, niin board luokka tarkistaa pelin tilanteen. Jos kaikki laivat ovat uponneet, peli päättyy, muutoin peli jatkuu uudella klikkauksella.
PvC peli on toteutettu samalla tavoin. PvC pelissa on kaksi board oliota kummassakin on 5 laivaa. Peli jatkuu vuorotellen pelaajan ja tietokoneen välillä. 

### Ohjelman sulkeminen ja yksinpeli 

![Yksinpeli](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sequence_menu_loop_single.png)

### PvC peli

![PvC](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sequence_menu_loop_pvc.png)

### Tulosten tarkastelu

![PvC](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sequence_menu_loop_scores.png)

