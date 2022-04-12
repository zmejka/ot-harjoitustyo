# Arkkitehtuurikuvaus
----
## Rakenne

Tätä osuutta ei vielä tehty

----
## Käyttöliittymä

Käyttöliittymä ei vielä toteutettu

----
## Sovelluslogiikka

Player luokka ei ole vielä toteutettu. Myös Game luokka ei ole vielä toteutettu. Tämän vuoksi rakenne on vajavaista.

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

Sequence-kaavio on pahasti kesken, koska osa luokista ei vielä toteutettu.
