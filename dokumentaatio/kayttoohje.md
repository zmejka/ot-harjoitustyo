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

Sovellus käynnistyy päävalikkoon. Päävalikosta voi valita Yksinpelin tai Pelin tietokoneetta vasten valissä. Lisäksi päävalikosta pääse tarkastelemaan 3 parhaan tuloksen tekijät. Pelin lopettaminen tapahtuu Lopeta peli- valikossa. Pelin pesussäännöt voi lukea [ohjeesta](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/battleship.pdf). 

## Yksinpeli:
----

Peli käynnistyy välittömästi. Pelissä on yksi kenttä, johon on piilotettu 5 laivaa. Laivojen löytämiseen on tarjolla 40 ammusta. Ampuminen tapahtuu klikkamalla hiiren vasemmalla näppäimella kentän soluja. Solu muuttuu siniseksi, jos paikassa ei ole laivaa, tai punaiseksi, jos laivaan on osuttu. Kun koko laiva on uppunut, tulostuu ruudulle ilmoitus mikä laiva on upotettu. Tässä pelissä jo avatun soluun ampuminen ei kuluta ammiksia. Peli päättyy, kun kaikki laivat ovat upponeet, tai kun ammukset loppuvat. Tämän jälkeen peli palautuu automaattisesti Päävalikkon. Jos pelin halua keskeyttää, pääsee takausiin Päävalikkoon Paluu-näppäintä painamalla.

Yksinpelin näkymä.

![Yksinpeli](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/single_layout.png)

## Kaksinpeli:
----

Pelin alussa pelaaja asettaa oikean puoliselle (omalle) kentälle 5 laiva. Laivat asetetaan seuraavassa järjestyksessä.
Laivat:

- Carrier (Lentotukialus) - 5 solua
- Battleship (Taistelulaiva) - 4 solua
- Cruiser (Risteilija) - 3 solua
- Submarine (Sukellusvene) - 3 solua
- Destroyer (Hävittäjä) - 2 solua

Laivat asetetaan painamalla haluttuun paikkaan joko hiiren vasenta näppäintä, jolloin laiva asettuu vaakaasentoon, tai hiiren oikeinta näppäintä, jolloin laiva asettuu pystyasentoon. Laivoja ei voi asettaa kenttään ulkopuolelle tai päällekkäin. 

![Laivat](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pvc_ships.png)

Kun laivat  on asetettu kentälle, peli alkaa. Pelaaja ampuu vasemman puoliselle (vastustajan) kentälle. Tässä pelissä ei ole rajoitettu ammusten määrä, mutta jo kertalleen ammutun kenttään ampumisellä menettää vuoron tietokoneelle. Peli päätyy, kun pelaaja tai tietokene onnistuu löytämään ja upottamaan kaikki laivat. Tämän jälkeen peli palautuu automaattisesti Päävalikkon. Jos pelin halua keskeyttää, pääsee takausiin Päävalikkoon Paluu-näppäintä painamalla.

![PvC](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pvc_layout.png)


