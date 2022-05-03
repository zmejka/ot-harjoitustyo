# Arkkitehtuurikuvaus
----
## Rakenne

Sovelluksen rakenne koostuu luokista main, ship ja board. Lisäksi sovelluksessa on 3 käyttöliittymäluokkaa menu, single ja pvc  sekä 13 sprites-luokkaa. Luokat on jaettu kansioihin ui, objects ja sprites. Kansiossa src sijaitsee sovelluslogiikka, kansiossa ui käyttöliittymät, objects kansiossa luokat ship ja board ja kansiossa sprites sprite-luokat. Kansiossa assets sijaitsevat ui tarvitsemat kuvatiedostot sekä image-luokka.

![Rakenne](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/rakenne_kuva.png)
----
## Käyttöliittymä

Käyttöliittymäluokat ovat menu, single ja pvc. Menu luokkaa sisältää aloitusvalikon, josta voi valita haluttu peli tai lopettaa sovelluksen käyttämistä.

----
## Sovelluslogiikka

Player luokka ei ole vielä toteutettu. Tämän vuoksi rakenne on vajavaista.

```mermaid
 classDiagram
      Board "1" --> "*" Ship
      Player "1-2" --> "1" Board
      class Board{
          board
          visible
          ships
          game_status
          ammo
      }
      class Ship{
          name
          length
          orientation
          status
          position
          hits
      }

```

----
## Päätoiminnallisuudet

### Laivojen alustus

![Laivojen alustus](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/vko_4_sequence.png)

### Menu silmukan luonnos. Tämä luonnos ei vielä vastaa kokonaistilannetta.


![Menu silmukka](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sequence_menu_loop.png)

### Yksinpelin silmukka
