### Viikko 3: 
- uusi ohjelma
- luotu Ship- ja Board- luokat.

### Viikko 4: 
- Board-luokaan lisätty yksinpelin alussa alustettavat laivat. Laivojen sijainti arvotaan kentälle. Laivojen lisäämisen yhteydessä tarkistetaan, että laivat eivät ylitä kentän rajoja, eivätkä mene päällekkäin. 
- Käyttöliittymään ei ole tehty muutoksia ja se on otettu pois käytöstä tässä vaiheessa. 
- Tällä hetkellä ohjelmassa ei ole testattavissa olevia toimintoja. Laivoja alustettaessa tulostuu konsolille kentän matriisirakenne, jossa 0-solut ovat tyhjiä ruutuja ja 1-solut laivojen ruudut. Toteutuksessa on käytetty Hasbron pelisääntöjä (linkkiä ei ole vielä lisätty dokumentaatioon).
- Testaus: luotu testit luokille Ship ja Board. Testien kattavuus kokonaisuudessa on 46%, luokan Ship kattavuus on 100% ja luokan Board kattavuus on 69%.

### Viikko 5: 
- Luotu aloitusmenun käyttöliittymä. Näkymässä toimivat tässä vaiheessa yksinpeli- ja pelin lopetus- toiminnot. 
- Luotu yksinpelin käyttöliittymä. Pelissä on 40 ammusta. Peli päätyy, kun kaikki laivat on ammuttu tai ammukset loppuvat. Toiminnallisuudesta puuttuu ilmoitukset kuten laiva (nimi) on uppunut tai kuinka monta ammusta on jäljellä.
- Peli tietokonetta vasten on aloitettu. Tässä vaiheessa pelissä tulostuu kentät sekä kentälle arvotut laivat. Laivoja pystyy ampumaan samalla tavoin kuin yksinpelissä. Seuraavaksi laivojen arpominen korvataan laivojen asettamisella pelaajan toimeesta sekä tietokoneen luomaan kenttään ampumiset.
- Testaus: testauksesta on poistettu käyttöliittymien testaus. Ship luokan testauksessa puuttuu random-koordinattien testaus. Testauksen kattavuus on vasta 44%.

### Viikko 6:
- Aloitettu pelaaja vs tietokone pelin toteutus. Tietokonetta vastaava kenttän toiminnallisuudet kuten laivojen sijoitus ja pelaajan ammunta toimivat samalla tavoin kuin yksinpelissä. Pelissä on 100 ammusta, eli ammusten määrä ei ole rajoitettu. Seuraavaksi toteutetaan pelaajan laivojen alustus ja tietokoneen ammunta. 
- Lisätty toiminnallisuus yksittäisten laivojen uppoamista seuraava toiminnallisuus
- Testaus: päivitetty/lisätty testit. Testauksen kattavuus 64%

### Viikko 7:
- Toteutettu pelaaja vs tietokone osa.
- Toteutettu pelajaan laivojen asettaminen kentälle.
- Päivitetty molempien pelien käyttöliittymät.
- Lisätty tulosten tallentaminen tiedostoon. Toteutettu kolmeen parhaan tuloksen näkymä.
- Päivitetty dokumentaatio. Lisätty käyttöohje.
- Testaus: poistettu turhat testit (muuttujat ja metodit, jotka eivät olleet enää käytössä). Testauksen kattavuus 79%.

