# Meili matkasuunnittelusovellus

Tämä on kevään 2021 ohjelmistotekniikan harjoitustyö. Sovelluksen avulla käyttäjien on mahdollista etsiä tietoa maailman maista ja laatia matkasuunnitelmia alustavine aika- ja bujettiarvioineen.


## Dokumentaatio
 * [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
 * [Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)

## Asennus
```shell
poetry install
```

## Käynnistys
```shell
poetry run invoke start
```

## Testaus
```shell
poetry run invoke test
```

Testikattavuuden tarkistamiseksi aja
```shell
poetry run invoke coverage_report
```