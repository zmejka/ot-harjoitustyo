# Arkkitehtuurikuvaus
----
## Rakenne

Tässä vaiheessa sovelluksen rakenne koostuu luokista main, ship ja board. Lisäksi sovelluksessa on 2 käyttöliittymäluokkaa sekä 13 sprites luokkaa.

![Rakenne](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/rakenne_kuva.png)
----
## Käyttöliittymä

Käyttöliittymäluokat ovat menu ja single. Menu luokkaa sisältää aloitusvalikon, josta voi valita haluttu peli tai lopettaa sovelluksen käyttämistä. 

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
          initialize_ships()
          game_over()
      }
      class Ship{
          name
          length
          orientation
          status
          is_sunk()
      }

```

----
## Päätoiminnallisuudet

Sequence-kaavio on tämän hetken tilannetta kuvaava kaavio. 

### Laivojen alustus

![Sequence](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/vko_4_sequence.png)
