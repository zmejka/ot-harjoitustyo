# Ohjelmistotekniikka, harjoitustyö
----
## Laivanupotuspeli
----
Sovelus on toteutettu Python-versiolla 3.8. 

Peli on versio perinteisestä laivanupotuspelistä. Pelissä voi pelata joko yksin tai pelata tietokonetta vastaan. Yksinpelissä tavoitteena löytää kenttään piilotettuja laivoja ennen kuin ammukset loppuvat. 
Pelissä tietokonetta vastaan tavoitteena on upottaa tietokoneen laivat ennen kuin tietokone upottaa kaikki pelaajan laivat.


### Dokumentaatio
----

[Vaatimusmäärittely](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testaus](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[Changelog](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Työaikakirjanpito](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)


### Julkaisu

[Release 1](https://github.com/zmejka/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/zmejka/ot-harjoitustyo/releases/tag/viikko6)

[Release 3](https://github.com/zmejka/ot-harjoitustyo/releases/tag/viikko6)

### Asennus
----

1. Asennuskomento:

        poetry install

### Toiminnot
----

1. Käynnistys:

        poetry run invoke start

2. Testaus

        poetry run invoke test

3. Testikattavuus

        poetry run invoke coverage-report

4. Pylint testaus

        poetry run invoke lint
