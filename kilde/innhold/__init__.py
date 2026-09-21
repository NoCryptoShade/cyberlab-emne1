# -*- coding: utf-8 -*-
"""
Leksjonsplanen for Emne 1 og registeret over ferdige leksjoner.

PLAN er alle 26 leksjonene. Tittel, beskrivelse og modulinndeling er hentet
ordrett fra emne1.html paa den publiserte sida, saa sidene her sier det samme
om hver leksjon som resten av CyberLab gjoer.

LEKSJONER er de som faktisk er skrevet. Sider bygges bare for disse, og
oversikten viser resten som "Kommer".
"""

MODULER = [
    {"farge": 'green', "tag": 'Modul 1', "navn": 'Grunnlaget', "uker": 'uke 1-2'},
    {"farge": 'blue', "tag": 'Modul 2', "navn": 'Nettverk', "uker": 'uke 3-5'},
    {"farge": 'amber', "tag": 'Modul 3', "navn": 'Linux', "uker": 'uke 6-7'},
    {"farge": 'purple', "tag": 'Modul 4', "navn": 'Skripting, databaser og web', "uker": 'uke 8-13'},
]

PLAN = [
    {"num": 'L01', "fil": "leksjon-01.html", "modul": 0,
     "tittel": 'Å jobbe med cybersikkerhet',
     "beskrivelse": 'Hva cybersikkerhet skal beskytte, fire vanlige jobber i bransjen, og hvem som angriper.'},
    {"num": 'L02', "fil": "leksjon-02.html", "modul": 0,
     "tittel": 'Hvordan digitale systemer virker',
     "beskrivelse": 'Fra bruker til svar: klient, tjener, og de viktigste delene i et digitalt system.'},
    {"num": 'L03', "fil": "leksjon-03.html", "modul": 0,
     "tittel": 'Verdier, trusler, sårbarheter og risiko',
     "beskrivelse": 'Hva en virksomhet må beskytte, og forskjellen på en trussel og en sårbarhet.'},
    {"num": 'L04', "fil": "leksjon-04.html", "modul": 0,
     "tittel": 'Etikk, lov og ansvar',
     "beskrivelse": 'Hvorfor testing krever tillatelse, hvem som kan gi den, og hvordan personopplysninger håndteres.'},
    {"num": 'L05', "fil": "leksjon-05.html", "modul": 1,
     "tittel": 'Hva et nettverk er',
     "beskrivelse": 'Hvorfor data deles i pakker, og hvorfor en enhet trenger både MAC- og IP-adresse.'},
    {"num": 'L06', "fil": "leksjon-06.html", "modul": 1,
     "tittel": 'IP-adressering, DNS og DHCP',
     "beskrivelse": 'Lese en IPv4-adresse med nettverksmaske, og avgjøre om to adresser ligger i samme nett.'},
    {"num": 'L07', "fil": "leksjon-07.html", "modul": 1,
     "tittel": 'Tjenester, porter og eksponering',
     "beskrivelse": 'Portnumre, vanlige tjenester, og skillet mellom lokalt og eksponert.'},
    {"num": 'L08', "fil": "leksjon-08.html", "modul": 1,
     "tittel": 'Switching, VLAN og segmentering',
     "beskrivelse": 'Hvordan en switch lærer hvor enhetene er, og hvorfor flate nett sprer angrep.'},
    {"num": 'L09', "fil": "leksjon-09.html", "modul": 1,
     "tittel": 'Ruting, default gateway og NAT',
     "beskrivelse": 'Hvordan en ruter velger vei, hva standardruten brukes til, og hva NAT gjør.'},
    {"num": 'L10', "fil": "leksjon-10.html", "modul": 1,
     "tittel": 'Trådløse nettverk',
     "beskrivelse": 'Radiosignaler, Wi-Fi-sikkerhet, og hvorfor gamle løsninger ikke bør brukes.'},
    {"num": 'L11', "fil": "leksjon-11.html", "modul": 2,
     "tittel": 'Linux: distribusjoner, terminal, filsystem og pakker',
     "beskrivelse": 'Navigere filsystemet, finne hjelp til en kommando, og installere programvare.'},
    {"num": 'L12', "fil": "leksjon-12.html", "modul": 2,
     "tittel": 'Å finne den ene linja',
     "beskrivelse": 'grep, find, rør og omdirigering. Hva en logg er og hvorfor den er nyttig.'},
    {"num": 'L13', "fil": "leksjon-13.html", "modul": 2,
     "tittel": 'Hvem får gjøre hva',
     "beskrivelse": 'Brukere, grupper, rettigheter og sudo. Lese hvem som får lese, endre og kjøre.'},
    {"num": 'L14', "fil": "leksjon-14.html", "modul": 2,
     "tittel": 'Fire spørsmål til en ukjent maskin',
     "beskrivelse": 'Hvilke tjenester kjører, hvilke porter lyttes det på, hvem er logget inn.'},
    {"num": 'L15', "fil": "leksjon-15.html", "modul": 3,
     "tittel": 'Fra kommando til program',
     "beskrivelse": 'Hva et Python-skript er. Variabler, tekst mot tall, og å hente ut et felt fra en logglinje.'},
    {"num": 'L16', "fil": "leksjon-16.html", "modul": 3,
     "tittel": 'Én regel, mange linjer',
     "beskrivelse": 'La programmet velge mellom handlinger, og gjenta kode for flere linjer.'},
    {"num": 'L17', "fil": "leksjon-17.html", "modul": 3,
     "tittel": 'Hundre funn, én variabel',
     "beskrivelse": 'Lister, mengder og ordbøker. Velge datastruktur ut fra spørsmålet.'},
    {"num": 'L18', "fil": "leksjon-18.html", "modul": 3,
     "tittel": 'Fem linjer med et navn',
     "beskrivelse": 'Funksjoner, parametre og retur. Lese en fil uten å glemme å lukke den.'},
    {"num": 'L19', "fil": "leksjon-19.html", "modul": 3,
     "tittel": 'Fra funn til rapport',
     "beskrivelse": 'Skrive filer uten å overskrive, og lage en enkel tekst- eller CSV-rapport.'},
    {"num": 'L20', "fil": "leksjon-20.html", "modul": 3,
     "tittel": 'Når verden ikke ser ut som du trodde',
     "beskrivelse": 'Lese en Python-feil, håndtere forventede feil, og filstier som virker automatisk.'},
    {"num": 'L21', "fil": "leksjon-21.html", "modul": 3,
     "tittel": 'Tabellen noen andre passer på',
     "beskrivelse": 'Hvordan en database organiserer data, og enkle spørringer med SQL.'},
    {"num": 'L22', "fil": "leksjon-22.html", "modul": 3,
     "tittel": 'Skriptet som spør',
     "beskrivelse": 'Koble Python til en database, og holde brukerens verdier atskilt fra SQL-en.'},
    {"num": 'L23', "fil": "leksjon-23.html", "modul": 3,
     "tittel": 'Kommandolinjen får sitt eget språk',
     "beskrivelse": 'Bash-skript: variabler, valg og løkker. Hvordan Bash behandler mellomrom og hermetegn.'},
    {"num": 'L24', "fil": "leksjon-24.html", "modul": 3,
     "tittel": 'Ett skript, fire spørsmål',
     "beskrivelse": 'Samle maskininfo i én rapport, sammenligne med normalbildet, og kjøre kontroll automatisk.'},
    {"num": 'L25', "fil": "leksjon-25.html", "modul": 3,
     "tittel": 'Under panseret på en nettside',
     "beskrivelse": 'HTML og CSS, elementer og skjemaer, og hva et skjema faktisk sender.'},
    {"num": 'L26', "fil": "leksjon-26.html", "modul": 3,
     "tittel": 'Når navnet blir kode',
     "beskrivelse": 'Hvorfor tjeneren må kontrollere alt den mottar, og hvordan tekst kan bli tolket som kode.'},
]

from .l01 import LEKSJON as L01
from .l05 import LEKSJON as L05
from .l06 import LEKSJON as L06

LEKSJONER = {
    "L01": L01,
    "L05": L05,
    "L06": L06,
}
