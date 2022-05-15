# Arkkitehtuurikuvaus
----
## Rakenne ja Sovelluslogiikka

Sovelluksen rakenteeseen kuuluvat pakkaukset UI, objects ja sprites. Objects pakkaukseen kuuluvat luokat player, ship ja board. Sovelluksessa on 4 käyttöliittymäluokkaa menu, single, pvc ja scores, sekä 13 sprites-luokkaa. Kansiossa src sijaitsee sovelluslogiikka, kansiossa ui käyttöliittymät, objects kansiossa olio-luokat ja kansiossa sprites sprite-luokat. Kansiossa assets sijaitsevat ui tarvitsemat kuvatiedostot sekä image-luokka.

![Rakenne](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/class_diagram.png)

Luokassa Player on yksi käyttämätön metodi, jolle on tehty oma testi. Metodi on set_name() ja se on luotu käyttäjäkohtaisten tulosten tallentamista varten. Kuitenkin, toiminnallisuutta pelaajan oman nimen/tunniksen syöttämiseksi ei ehditty toteuttamaan ja se jäi jatkokehitykselle. Tämän vuoksi metodi ei poistettu ohjelmasta.

----
## Käyttöliittymä

Käyttöliittymäluokat ovat menu, single, pvc ja scores. Menu luokkaa sisältää aloitusvalikon, josta voi valita haluttu peli, tarkastella tulokset tai lopettaa sovelluksen käyttämistä.

----

##Tietojen pysyväistallennus

Luokka Results tallentaa peleistä syntyvät tulokset txt. tiedostoon. Kun käyttäjä halua tarkastella tuloksia, main luokka hakee tulokset tiedostosta, järjestää ne ja palauttaa kolme parasta tulosta. Nämä tulokset näkyvät Scores käyttöliittymällä.

Sovellus tallentaa tiedot txt- tiedostoon muosossa: 'Pelaajan nimi, score'. Jokainen tulos tallentuu omalle riville.

----
## Päätoiminnallisuudet

### Laivojen alustus

![Laivojen alustus](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/vko_4_sequence.png)

### Menu ja yksinpelin silmukkoiden luonnos. Tämä luonnos ei vielä vastaa kokonaistilannetta.


![Menu silmukka](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sequence_menu_loop.png)

