# Käyttöohje
----

Projectin viimeisen version voi ladata Releases osiossa valitsemalla Source code.

## Ohjelman asentaminen ja käynnistäminen
----

Asenna riippuvuudetkomennolla:

    poetry install

Ohjelman voi käynnistä komennolla:

    poetry run invoke start

## Päävalikko:
----

Sovellus käynnistyy päävalikkoon. Päävalikosta voi valita Yksinpelin ja Pelin tietokoneetta vasten valissä. Pelin lopettaminen tapahtii Lopeta peli valikossa. 

### Yksinpeli:
----

Peli käynnistyy välittömästi. Pelissä on yksi kenttä, johon on piilotettu 5 laivaa. Laivojen löytämiseen on tarjolla 40 ammusta. Ampuminen tapahtuu klikkamalla hiiren vasemmalla näppäimella kentän soluja. Solu muuttuu siniseksi, jos paikassa ei ole laivaa, tai punaiseksi, jos laivaan on osuttu. Tässä pelissä jo avatun soluun ampuminen ei kuluta ammiksia. Peli päättyy, kun kaikki laivat ovat upponeet, tai kun ammukset loppuvat. Tämän jälkeen peli palautuu automaattisesti Päävalikkon.

### Kaksinpeli:
----

Pelin alussa pelaaja asettaa oikean puoliselle (omalle) kentälle 5 laiva. Laivat asetetaan seuraavassa järjestyksessä.
Laivat:
Carrier (Lentotukialus) - 5 solua
Battleship (Taistelulaiva) - 4 solua
Cruiser (Risteilija) - 3 solua
Submarine (Sukellusvene) - 3 solua
Destroyer (Hävittäjä) - 2 solua

Laivat asetetaan painamalla haluttuun paikkaan joko hiiren vasenta näppäintä, jolloin laiva asettuu vaakaasentoon, tai hiiren oikeinta näppäintä, jolloin laiva asettuu pystyasentoon. Laivoja ei voi asettaa kenttään ulkopuolelle tai päällekkäin. Kun laivat  on asetettu kentälle, peli alkaa. Pelaaja ampuu vasemman puoliselle (vastustajan) kentälle. Tässä pelissä ei ole rajoitettu ammusten määrä, mutta jo kertalleen ammutun kenttään ampumisellä menettää vuoron tietokoneelle. Peli päätyy, kun pelaaja tai tietokenee onnistuu löytämään kaikki laivat. Tämän jälkeen peli palautuu automaattisesti Päävalikkon.
