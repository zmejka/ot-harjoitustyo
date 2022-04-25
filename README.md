## Ohjelmistotekniikka, harjoitustyö

## Laivanupotuspeli

Sovelluksen toiminta on toteutettu Python-versiolla 3.8. 

Peli on versio perinteisestä laivanupotuspelistä. Pelissä voi pelata joko yksin tai pelata tietokonetta vastaan. Yksinpelissä tavoitteena löytää kenttään piilotettuja laivoja ennen kuin ammukset loppuu. Pelissä tietokonetta vasten tavoittena upottaa tietokoneen laivat ennen kuin tietokone upottaa kaikki pelaajan laivat.


### Dokumentaatio

[Vaatimusmäärittely](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Pelisäännöt](https://github.com/zmejka/ot-harjoitustyo/blob/master/dokumentaatio/battleship.pdf)

### Asennus
1. Asennuskomento:

        poetry install

### Toiminnot

1. Käynnistys:

        poetry run invoke start

2. Testaus

        poetry run invoke test

3. Testikattavuus

        poetry run invoke coverage-report

4. Pylint testaus

        poetry run invoke lint







