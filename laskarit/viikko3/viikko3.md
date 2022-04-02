```mermaid
 classDiagram
      Pelilauta -- "2" Noppa
      Pelilauta -- "40" Ruutu
      Pelilauta -- "2..8" Pelaaja
      Pelaaja -- "1" Pelinappula
      class Pelilauta{
      }
      class Pelaaja{
      }
      class Noppa{
      }
      class Ruutu{
          seuraavaRuutu
      }
      class Pelinappula{
          Ruutu
      }
```
