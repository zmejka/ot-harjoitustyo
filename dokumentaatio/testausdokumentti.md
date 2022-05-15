# Laivanupotuspelin testausdokumentti
----

Sovellusta on testattu käyttämällä automaattista unittest yksikkötestejä. Lisäksi sovellusta testattu pelaamalla peliä eri koneilla ja eri käyttäjien toimeesta.

## Automaattinen testaus (Unittest)
----

Yksikkötestauksella testattiin olio-luokat sekä sovelluslogikan osia. Näiltä osin testauksen haarautumakattavuudeksi saatiin 79 %.

![Raportti](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage_report.png)

Testauksen ulkopuolelle jätettiin *index.py* -tiedosto, sprite-luokat sekä käyttöliittymaluokat. 

## Käyttöliittymä
----

Käyttöliittymälle ja sprites-luokille ei tehty automaattista testausta. Käyttöliittymä on testattu manuaalisesti käyttämällä sovellusta mahdollisimman monipuolisesti.

## Laatuongelmat
----

Osa ohjelman sovelluslogikasta on jäänyt käyttöliittymän puolelle. 
Ohjelmassa on toisteisuutta.  
