# Käyttöohje
----

Projektin viimeisin versio on ladattavissa Releases osiosta valitsemalla Source code.

## Ohjelman asentaminen ja käynnistäminen
----

Asenna riippuvuudet komennolla:

    poetry install

Ohjelman voi käynnistä komennolla:

    poetry run invoke start

## Päävalikko:
----

Sovellus käynnistyy päävalikkoon. Päävalikosta voit valita Yksinpelin tai Pelin tietokonetta vastaan. Tulokset-valinta näyttää kolme parasta tulosta. Sovelluksen sulkeminen tapahtuu valitsemall "Lopeta peli". Laivaupotuspelin perussäännöt ovat luettavissa [ohjeesta](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/battleship.pdf). 

## Yksinpeli:
----

Peli käynnistyy välittömästi. Pelissä on yksi kenttä, jossa on piilotettu 5 sotalaivaa. Laivojen ampumiseen on käytettävissä 45 ammusta. Ampuminen tapahtuu klikkaamalla hiiren vasemmalla näppäimella kentän ruutuja. Ruutu muuttuu siniseksi, jos paikassa ei ole laivaa, tai punaiseksi, jos laivaan on osuttu. Kun jokin laiva on uponnut, näyttölle tulee ilmoitus, joka kertoo, mikä alus on upotettu. Tässä pelissä jo ammuttuun ruutuun ampuminen ei kuluta ammuksia. Peli päättyy, kun kaikki alukset ovat uponneet tai kun ammukset loppuvat. Tämän jälkeen peli palautuu automaattisesti Päävalikkoon. Jos haluaa keskeyttää pelin, niin pääsee takaisin Päävalikkoon Paluu-nappia painamalla.

Yksinpelin näkymä.

![Yksinpeli](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/single_layout.png)

## Kaksinpeli:
----

Pelin alussa pelaaja asettaa oikeanpuoleiselle (omalle) kentälle 5 laivaa. Laivat asetetaan seuraavassa järjestyksessä:

- Lentotukialus - 5 ruutua
- Taistelulaiva - 4 ruutua
- Risteilija - 3 ruutua
- Sukellusvene - 3 ruutua
- Hävittäjä - 2 ruutua

Hiiren vasemmalla painikeella laiva asettuu vaaka-asentoon ja hiiren oikealla painikkeella pystyasentoon. Laivoja ei voi asettaa kentän ulkopuolelle tai päällekkäin. Laivat voi olla vierekkäisissä ruuduissa. 

![Laivat](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pvc_ships.png)

Kun laivat  ovat asetettu kentälle, peli alkaa. Pelaaja ja tietokone ampuvat vuorotellen. Pelaaja aloittaa. Pelaaja ampuu vasemmanpuoleiselle (vastustajan) kentälle. Tässä pelissä ei ole rajoitettu ammusten määrää, mutta jo kertalleen ammuttuun ruutuun ampumisella menettää vuoron tietokoneelle. Peli päättyy, kun pelaaja tai tietokone onnistuu löytämään ja upottamaan kaikki vastustajan laivat. Tämän jälkeen peli palautuu automaattisesti Päävalikkoon. Jos pelin haluaa keskeyttää, niin pääsee takaisin Päävalikkoon Paluu-nappia painamalla.

![PvC](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pvc_layout.png)


