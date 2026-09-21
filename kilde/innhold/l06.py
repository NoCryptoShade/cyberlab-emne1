# -*- coding: utf-8 -*-
"""L06 - IP-adressering, DNS og DHCP. Modul 2, Nettverk."""

TERM = """{
  help:[
    {t:'info',v:'Tilgjengelige kommandoer:'},
    {t:'out', v:'  ipconfig              adresse, nettmaske, gateway og DNS'},
    {t:'out', v:'  ipconfig /all         ogs\\u00e5 utl\\u00e5nstid fra DHCP'},
    {t:'out', v:'  nslookup [navn]       sl\\u00e5r opp et navn og gir en adresse'},
    {t:'out', v:'  clear                 t\\u00f8mmer skjermen'},
    {t:'info',v:'Navn du kan pr\\u00f8ve: gokstad.local og vg.no'},
  ],
  ipconfig:[
    {t:'info',v:'Ethernet adapter Ethernet:'},
    {t:'out', v:'   IPv4-adresse . . . . . . : 192.168.1.40'},
    {t:'out', v:'   Nettmaske  . . . . . . . : 255.255.255.0'},
    {t:'out', v:'   Standard gateway . . . . : 192.168.1.1'},
    {t:'out', v:'   DNS-server . . . . . . . : 192.168.1.1'},
  ],
  'ipconfig /all':[
    {t:'info',v:'Ethernet adapter Ethernet:'},
    {t:'out', v:'   Fysisk adresse . . . . . : 3C-52-82-A1-04-9F'},
    {t:'out', v:'   DHCP aktivert  . . . . . : Ja'},
    {t:'out', v:'   IPv4-adresse . . . . . . : 192.168.1.40'},
    {t:'out', v:'   Nettmaske  . . . . . . . : 255.255.255.0'},
    {t:'out', v:'   Utl\\u00e5net starter . . . . : 17.09.2026 07:12:44'},
    {t:'out', v:'   Utl\\u00e5net utl\\u00f8per . . . . : 19.09.2026 07:12:44'},
    {t:'out', v:'   Standard gateway . . . . : 192.168.1.1'},
    {t:'out', v:'   DHCP-server  . . . . . . : 192.168.1.1'},
  ],
  'nslookup gokstad.local':[
    {t:'out', v:'Server:   192.168.1.1'},
    {t:'info',v:'Svar:'},
    {t:'out', v:'Navn:     gokstad.local'},
    {t:'out', v:'Adresse:  192.168.1.90'},
  ],
  'nslookup vg.no':[
    {t:'out', v:'Server:   192.168.1.1'},
    {t:'info',v:'Ikke-autoritativt svar:'},
    {t:'out', v:'Navn:     vg.no'},
    {t:'out', v:'Adresse:  195.88.55.16'},
  ],
  nslookup:[
    {t:'info',v:'Bruk: nslookup [navn]'},
    {t:'out', v:'Pr\\u00f8v nslookup gokstad.local eller nslookup vg.no'},
  ],
}"""

LEKSJON = {
 "num": "L06",
 "modul": "Modul 2 · Nettverk",
 "tittel": "IP-adressering, DNS og DHCP",
 "ingress": "Hvordan en maskin vet hvem som er naboen, hvordan navn blir til tall, "
            "og hvem som deler ut adressene i utgangspunktet.",
 "kort": [

{
 "id": "l06-1",
 "tittel": "IP-adressen er leilighetsnummeret",
 "bilde_tittel": "\U0001F6AA Nummeret på døra",
 "bilde": [
   "Alle leilighetene i Storgata 12 har et nummer. Nummeret sier ingenting om hvem som bor "
   "der. Det sier bare hvor i blokka du skal.",
   "To leiligheter kan ikke ha samme nummer. Da vet ikke vaktmesteren hvor posten skal.",
   "Flytter du til en annen blokk, får du et nytt nummer. Nummeret følger leiligheten.",
 ],
 "ord": [
   "Nummeret er en <strong>IP-adresse</strong>. Den sier hvor en maskin er, ikke hvem den er.",
   "Adressen skrives i fire grupper med punktum mellom, for eksempel 192.168.1.40. "
   "Hver gruppe er et tall fra 0 til 255.",
 ],
 "sjekk": {"q": "To naboer bytter leilighet, men tar med seg navneskiltet på døra. Hvilket nummer skal posten til den som nå bor i nummer 7 sendes til?",
           "ph": "et tall", "a": ["7", "nummer 7", "sju", "syv"],
           "hint": "Posten sorteres på nummeret, ikke på hvem som bor der.", "sv": "7"},
 "vist_intro": "Adressen 192.168.1.40 lest fra venstre mot høyre.",
 "vist": [
   "Fire grupper, skilt med punktum",
   "Første gruppe er 192, andre er 168, tredje er 1, fjerde er 40",
   "De første gruppene sier hvilket nett",
   "Den siste sier hvilken maskin i det nettet",
   "Hvor skillet går, bestemmes av nettmasken, som kommer i neste del",
 ],
 "prov": [
   {"q": "Hva er den siste gruppen i adressen 10.20.30.44?",
    "ph": "et tall", "a": ["44"], "hint": "Lengst til høyre.", "sv": "44"},
   {"q": "Hva er den andre gruppen fra venstre i adressen 172.16.5.200?",
    "ph": "et tall", "a": ["16"], "hint": "Tell gruppene fra venstre.", "sv": "16"},
   {"q": "Hvor mange grupper består en IP-adresse av?",
    "ph": "et tall", "a": ["4", "fire"], "hint": "Tell punktumene og legg til en.", "sv": "4"},
 ],
 "din_tur": [
   {"q": "En kollega skriver adressen 192.168.1.300. Den kan ikke stemme. Hva er det høyeste tallet en gruppe kan ha?",
    "ph": "et tall", "a": ["255"],
    "hint": "Se på hvilket intervall hver gruppe kan ligge i.", "sv": "255"},
   {"q": "To maskiner får ved et uhell samme IP-adresse i samme nett. Hvor mange av dem kan være sikre på å få riktig trafikk?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Vaktmesteren står med to dører som har samme nummer.", "sv": "0"},
 ],
 "sikkerhet": "At adressen sier hvor og ikke hvem, er også grunnen til at en IP-adresse "
              "alene er svakt bevis. Den peker på et punkt i nettet på et tidspunkt, ikke "
              "på en person.",
},

{
 "id": "l06-2",
 "tittel": "Nettmasken sier hvor blokka slutter",
 "bilde_tittel": "\U0001F5FA️ Land, by, gate, leilighet",
 "bilde": [
   "Tenk deg at adressen din ble skrevet som fire deler etter hverandre: "
   "Norge.Sandefjord.Storgata.12",
   "Hvor mange av delene som må være like for at dere skal regnes som naboer, er ikke gitt. "
   "Må de tre første være like, er dere i samme gate. Må bare de to første være like, er "
   "hele byen naboer.",
   "Noen må altså si hvor mange av delene som teller.",
 ],
 "ord": [
   "Den som sier det, er <strong>nettmasken</strong>.",
   "255 betyr at denne gruppen må være lik. 0 betyr at den kan være hva som helst. "
   "Nettmasken 255.255.255.0 betyr altså at de tre første gruppene må stemme.",
 ],
 "sjekk": {"q": "Adressen skrives Norge.Sandefjord.Storgata.12. Hvor mange av de fire delene må være like for at to adresser skal ligge i samme gate?",
           "ph": "et tall", "a": ["3", "tre"],
           "hint": "Alt unntatt husnummeret.", "sv": "3"},
 "vist_intro": "Maskinen 192.168.1.40 med nettmaske 255.255.255.0.",
 "vist": [
   "Nettmasken har 255 i de tre første gruppene",
   "Altså er de tre første gruppene nettet",
   "Nettet er 192.168.1",
   "Den siste gruppen, 40, er maskinen",
   "Alle adresser som begynner på 192.168.1, er naboer",
 ],
 "prov": [
   {"q": "Nettmaske 255.255.255.0. Hvor mange av de fire gruppene er nett?",
    "ph": "et tall", "a": ["3", "tre"], "hint": "Tell hvor mange 255 det står.", "sv": "3"},
   {"q": "Nettmaske 255.255.0.0. Hvor mange av de fire gruppene er nett?",
    "ph": "et tall", "a": ["2", "to"], "hint": "Samme telling.", "sv": "2"},
   {"q": "Nettmaske 255.0.0.0. Hvor mange av de fire gruppene er maskin?",
    "ph": "et tall", "a": ["3", "tre"],
    "hint": "Tell nullene denne gangen, ikke 255-erne.", "sv": "3"},
 ],
 "din_tur": [
   {"q": "Nettmasken skrives ofte kort, som /24. Tallet er antall biter, og hver gruppe er 8 biter. Hvor mange grupper er nett når det står /24?",
    "ph": "et tall", "a": ["3", "tre"],
    "hint": "Del antall biter på 8.", "sv": "3"},
   {"q": "Hvor mange grupper er nett når det står /16?",
    "ph": "et tall", "a": ["2", "to"],
    "hint": "Samme regnestykke, mindre tall.", "sv": "2"},
 ],
 "sikkerhet": "Nettmasken avgjør hvor stort område en maskin regner som «hjemme». Settes den "
              "for vidt, snakker maskiner direkte med hverandre som egentlig skulle vært "
              "atskilt, og trafikken passerer aldri noe som kunne stoppet den.",
},

{
 "id": "l06-3",
 "tittel": "Er vi i samme nett eller ikke",
 "bilde_tittel": "⚖️ Sammenligningen maskinen gjør hver gang",
 "bilde": [
   "Før maskinen din sender noe som helst, gjør den en sammenligning.",
   "Den tar sin egen adresse, tar mottakerens adresse og ser på så mange grupper som "
   "nettmasken sier. Stemmer de, sendes det direkte. Stemmer de ikke, sendes det til døra ut.",
   "Dette er den eneste avgjørelsen maskinen tar på egen hånd.",
 ],
 "ord": [
   "Sammenligningen kalles å finne <strong>nettverksadressen</strong> til begge, og "
   "sjekke om de er like.",
   "Du trenger tre ting for å gjøre det: din egen adresse, mottakerens adresse og nettmasken.",
 ],
 "sjekk": {"q": "Du har Norge.Sandefjord.Storgata.12 og naboen har Norge.Sandefjord.Storgata.14. Bare de tre første delene teller. Er dere naboer?",
           "ph": "ja / nei", "a": ["ja"],
           "hint": "Sammenlign de tre første delene og se bort fra den fjerde.", "sv": "ja"},
 "vist_intro": "Maskin A er 192.168.1.40, maskin B er 192.168.1.77, nettmasken er 255.255.255.0.",
 "vist": [
   "Nettmasken sier at tre grupper teller",
   "De tre første gruppene i A er 192.168.1",
   "De tre første gruppene i B er 192.168.1",
   "De er like, altså samme nett",
   "Trafikken går direkte, uten å gå innom ruteren",
 ],
 "prov": [
   {"q": "A er 192.168.1.40 og B er 192.168.1.200, nettmaske 255.255.255.0. Samme nett?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Se bare på de tre første gruppene.", "sv": "ja"},
   {"q": "A er 192.168.1.40 og C er 192.168.4.40, nettmaske 255.255.255.0. Samme nett?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Se på den tredje gruppen, ikke på den siste.", "sv": "nei"},
   {"q": "A er 10.4.1.9 og D er 10.9.9.9, nettmaske 255.0.0.0. Samme nett?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Denne nettmasken sier at bare en gruppe teller.", "sv": "ja"},
 ],
 "din_tur": [
   {"q": "A er 10.4.1.9 og B er 10.4.7.9. Nettmasken er 255.255.0.0. Er de i samme nett?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Hvor mange grupper sier denne nettmasken at du skal sammenligne?", "sv": "ja"},
   {"q": "De samme to maskinene, men nettmasken endres til 255.255.255.0. Er de i samme nett nå?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Adressene er uendret. Det eneste som er endret, er hvor mange grupper som teller.",
    "sv": "nei"},
   {"mcq": "Hva sier de to forrige svarene til sammen?",
    "alt": ["Adressene bestemmer alt", "To maskiner kan være naboer eller ikke, avhengig av nettmasken",
            "Nettmasken har ingen betydning"],
    "riktig": "To maskiner kan være naboer eller ikke, avhengig av nettmasken",
    "ok": "Riktig. Adressene alene forteller ikke om to maskiner når hverandre direkte.",
    "nei": "Ikke helt. Legg merke til at bare en ting ble endret mellom de to spørsmålene."},
 ],
 "sikkerhet": "Feil nettmaske er en klassisk feilkilde, og den er stille. Alt ser ut til å "
              "virke, helt til trafikk som skulle vært innom en brannmur, i stedet går "
              "direkte, eller til at en maskin plutselig ikke når noe som helst.",
},

{
 "id": "l06-4",
 "tittel": "Hvor mange får plass i nettet",
 "bilde_tittel": "🔢 To skilt ingen kan bo bak",
 "bilde": [
   "Blokka har 256 nummerskilt, fra 0 til 255.",
   "To av dem kan ingen bo bak. Det første er navnet på hele blokka. Det siste er "
   "oppslagstavla i inngangen, som når alle beboerne på en gang.",
   "Resten er ekte leiligheter.",
 ],
 "ord": [
   "Det første kalles <strong>nettverksadressen</strong>. Det siste kalles "
   "<strong>kringkastingsadressen</strong>.",
   "Med nettmaske 255.255.255.0 går den siste gruppen fra 0 til 255. Det er 256 tall, "
   "og når du trekker fra de to, står det igjen 254 maskiner.",
 ],
 "sjekk": {"q": "Blokka har 256 nummerskilt, og to av dem kan ingen bo bak. Hvor mange leiligheter er det plass til?",
           "ph": "et tall", "a": ["254"],
           "hint": "Trekk fra de to som er opptatt av noe annet.", "sv": "254"},
 "vist_intro": "Nettet 192.168.1.0 med nettmaske 255.255.255.0.",
 "vist": [
   "Den siste gruppen går fra 0 til 255, altså 256 tall",
   "192.168.1.0 er nettverksadressen",
   "192.168.1.255 er kringkastingsadressen",
   "Igjen står 254 adresser til maskiner",
   "Den første brukbare er 192.168.1.1, og den siste er 192.168.1.254",
 ],
 "prov": [
   {"q": "Nettet 10.0.5.0 med nettmaske 255.255.255.0. Hvor mange maskiner får plass?",
    "ph": "et tall", "a": ["254"],
    "hint": "Samme regnestykke som i eksempelet.", "sv": "254"},
   {"q": "Hva er den første brukbare adressen i det nettet?",
    "ph": "en adresse", "a": ["10.0.5.1"],
    "hint": "Den første er opptatt av navnet på nettet.", "sv": "10.0.5.1"},
   {"q": "Hva er den siste brukbare adressen i det nettet?",
    "ph": "en adresse", "a": ["10.0.5.254"],
    "hint": "Den aller siste er opptatt av oppslagstavla.", "sv": "10.0.5.254"},
 ],
 "din_tur": [
   {"q": "En avdeling trenger adresser til 300 maskiner. Holder ett nett med nettmaske 255.255.255.0?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Sammenlign 300 med hvor mange som faktisk får plass.", "sv": "nei"},
   {"mcq": "Hvorfor kan ingen maskin bruke adressen 192.168.1.255 i et nett med nettmaske 255.255.255.0?",
    "alt": ["Tallet 255 er ikke lov i en adresse",
            "Den adressen når alle maskinene i nettet på en gang",
            "Den er reservert til ruteren"],
    "riktig": "Den adressen når alle maskinene i nettet på en gang",
    "ok": "Riktig. Det er oppslagstavla, ikke en leilighet.",
    "nei": "Ikke helt. Se hvilke to skilt ingen kan bo bak."},
 ],
 "sikkerhet": "En melding til kringkastingsadressen når alle maskinene samtidig. Det kan "
              "brukes til å finne ut hvor mange maskiner som er i live på sekunder, og "
              "derfor er svar på slike kall slått av i de fleste nett i dag.",
},

{
 "id": "l06-5",
 "tittel": "Private og offentlige adresser",
 "bilde_tittel": "\U0001F3D8️ Leilighet 12 finnes i tusenvis av blokker",
 "bilde": [
   "Det finnes en leilighet 12 i tusenvis av blokker i Norge. Det går helt fint, fordi "
   "nummeret bare gjelder inne i den ene blokka.",
   "Gateadressen til selve blokka er derimot unik. Det finnes bare en Storgata 12 i Sandefjord.",
 ],
 "ord": [
   "Adresser som gjentas inne i hvert lokalnett, kalles <strong>private adresser</strong>. "
   "De begynner på 10, på 192.168 eller på 172 fulgt av 16 til 31.",
   "Adresser som er unike på internett, kalles <strong>offentlige adresser</strong>.",
 ],
 "sjekk": {"q": "To ulike blokker har begge en leilighet 12. Er det et problem for posten?",
           "ph": "ja / nei", "a": ["nei"],
           "hint": "Posten finner først blokka, og så leiligheten.", "sv": "nei"},
 "vist_intro": "Tre adresser sortert.",
 "vist": [
   "192.168.1.40 begynner på 192.168, altså privat",
   "10.0.0.7 begynner på 10, altså privat",
   "51.15.44.2 begynner på ingen av dem, altså offentlig",
   "Private adresser kan gjenbrukes i hvert eneste lokalnett",
   "Offentlige adresser må tildeles, og de koster penger",
 ],
 "prov": [
   {"q": "Er 192.168.4.5 privat eller offentlig?",
    "ph": "privat / offentlig", "a": ["privat"], "hint": "Se på de to første gruppene.", "sv": "privat"},
   {"q": "Er 8.8.8.8 privat eller offentlig?",
    "ph": "privat / offentlig", "a": ["offentlig"], "hint": "Begynner den på 10, 192.168 eller 172?", "sv": "offentlig"},
   {"q": "Er 10.44.7.15 privat eller offentlig?",
    "ph": "privat / offentlig", "a": ["privat"], "hint": "Første gruppe avgjør her.", "sv": "privat"},
 ],
 "din_tur": [
   {"q": "Tre ulike bedrifter bruker alle 192.168.1.0 internt. Hvor mange av dem må bytte adresser?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Gjelder nummeret utenfor den enkelte blokka?", "sv": "0"},
   {"mcq": "Hvorfor kan ikke en maskin med privat adresse nås direkte fra internett?",
    "alt": ["Den er slått av", "Adressen finnes mange steder samtidig, så den peker ikke på noe entydig ute",
            "Private adresser er krypterte"],
    "riktig": "Adressen finnes mange steder samtidig, så den peker ikke på noe entydig ute",
    "ok": "Riktig. Du møter løsningen på dette i L09, og den heter NAT.",
    "nei": "Ikke helt. Tenk på leilighet 12 i tusenvis av blokker."},
 ],
 "sikkerhet": "At en maskin har privat adresse, blir ofte lest som at den er beskyttet. "
              "Det stemmer bare så lenge ingen slipper trafikk inn til den med vilje, og "
              "det er nettopp det en videresendt port gjør.",
},

{
 "id": "l06-6",
 "tittel": "Navnet på døra er DNS",
 "bilde_tittel": "\U0001F3F7️ Skiltet og lista",
 "bilde": [
   "På hver dør står et skilt med navnet til den som bor der. Du husker Hansen lettere enn "
   "leilighet 17.",
   "Vaktmesteren har en liste som kobler navn til nummer. Spør du etter Hansen, slår han "
   "opp og finner 17.",
   "Flytter Hansen til nummer 3, endres lista. Navnet er det samme, nummeret er nytt.",
 ],
 "ord": [
   "Lista er <strong>DNS</strong> (Domain Name System). Du oppgir et navn, og DNS gir deg "
   "tilbake en IP-adresse.",
   "Nettsteder bytter IP-adresse ganske ofte. Navnet står stille, og derfor merker du ingenting.",
 ],
 "sjekk": {"q": "Hansen flytter fra nummer 17 til nummer 3, og lista er oppdatert. Hvilket nummer får posten til Hansen nå?",
           "ph": "et tall", "a": ["3", "nummer 3", "tre"],
           "hint": "Navnet er uendret, men oppslaget gir et nytt nummer.", "sv": "3"},
 "vist_intro": "Du skriver inn et nettstedsnavn i nettleseren.",
 "vist": [
   "Nettleseren har bare et navn, ikke en adresse",
   "Den spør DNS om navnet",
   "DNS svarer med en IP-adresse",
   "Nettleseren kobler seg til den adressen",
   "Uten svar fra DNS skjer ingenting, selv om serveren er oppe",
 ],
 "prov": [
   {"q": "Lista sier at gokstad.no er 10.0.0.5. Hvilken adresse kobler nettleseren seg til?",
    "ph": "en adresse", "a": ["10.0.0.5"], "hint": "Den nettleseren fikk tilbake.", "sv": "10.0.0.5"},
   {"q": "Serveren flyttes til 10.0.0.9 og lista oppdateres. Hvilken adresse kobler nettleseren seg til nå?",
    "ph": "en adresse", "a": ["10.0.0.9"], "hint": "Lista er endret.", "sv": "10.0.0.9"},
   {"q": "Serveren flyttes til 10.0.0.9, men lista blir ikke oppdatert. Hvilken adresse blir besøkende sendt til?",
    "ph": "en adresse", "a": ["10.0.0.5"],
    "hint": "Nettleseren stoler på lista, ikke på hvor serveren faktisk står.", "sv": "10.0.0.5"},
 ],
 "din_tur": [
   {"q": "DNS er nede, men du kjenner IP-adressen til serveren fra før. Kan du nå tjenesten likevel?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Du trenger oppslaget bare hvis du mangler nummeret.", "sv": "ja"},
   {"mcq": "En angriper klarer å legge inn feil adresse i lista for et banknavn. Hva skjer med de besøkende?",
    "alt": ["De får feilmelding", "De sendes til angriperens server selv om de skrev riktig navn",
            "Ingenting, navnet er jo riktig"],
    "riktig": "De sendes til angriperens server selv om de skrev riktig navn",
    "ok": "Riktig. Du skrev riktig navn og fikk likevel feil sted. Det kalles DNS-forgiftning.",
    "nei": "Ikke helt. Hvem er det nettleseren stoler på når den skal finne adressen?"},
 ],
 "sikkerhet": "DNS er et tillitsledd som ingen legger merke til før det svikter. Klarer noen "
              "å svare på oppslaget før den ekte serveren, havner du på maskinen deres med "
              "riktig navn i adressefeltet.",
},

{
 "id": "l06-7",
 "tittel": "DHCP deler ut numrene",
 "bilde_tittel": "\U0001F511 Vaktmesteren som deler ut nøkler",
 "bilde": [
   "En ny leieboer flytter inn. Hun velger ikke nummer selv. Vaktmesteren gir henne et ledig "
   "nummer, og noterer at det er opptatt.",
   "Nummeret gjelder for en periode. Flytter hun ut, blir det ledig igjen etter en stund.",
 ],
 "ord": [
   "Vaktmesteren som deler ut numre, er <strong>DHCP</strong> (Dynamic Host Configuration "
   "Protocol). Maskinen din ber om en adresse når den kobler seg til.",
   "Den avtalte tiden kalles <strong>utlånstid</strong>. Først når den er ute, kan adressen "
   "gis til noen andre. Maskinen får også nettmaske, gateway og DNS-server samtidig.",
 ],
 "sjekk": {"q": "Blokka har 24 leiligheter og 24 leieboere. En til flytter inn. Hvor mange ledige numre er igjen til henne?",
           "ph": "et tall", "a": ["0", "null", "ingen"],
           "hint": "Tell hvor mange numre som ikke er i bruk.", "sv": "0"},
 "vist_intro": "Et gjestenett har plass til 50 adresser, og utlånstiden er 2 timer.",
 "vist": [
   "50 gjester kobler seg på, og alle 50 adressene er utdelt",
   "Gjest nummer 51 ber om en adresse",
   "Det finnes ingen ledig, og hun får ingen",
   "En gjest går hjem, men adressen er reservert i 2 timer til",
   "Først etter det kan gjest nummer 51 få plass",
 ],
 "prov": [
   {"q": "Et nett har 20 adresser, og 20 maskiner er på. Hvor mange nye maskiner kan få adresse nå?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Det er ikke plass i rommet som avgjør. Det er antall ledige numre.", "sv": "0"},
   {"q": "Utlånstiden settes ned fra 2 timer til 15 minutter. Blir adressene ledige raskere eller saktere?",
    "ph": "raskere / saktere", "a": ["raskere"],
    "hint": "Kortere reservasjon betyr kortere ventetid.", "sv": "raskere"},
   {"q": "Et nett har 100 adresser, og 60 maskiner er på. Hvor mange nye kan kobles på?",
    "ph": "et tall", "a": ["40", "førti", "forti"],
    "hint": "Trekk de brukte fra de tilgjengelige.", "sv": "40"},
 ],
 "din_tur": [
   {"q": "Maskinen din får adresse, nettmaske, gateway og DNS-server automatisk. Hvor mange av de fire må du selv skrive inn?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Les hva utdeleren sender med.", "sv": "0"},
   {"mcq": "En angriper setter opp sin egen utdeler på nettet og svarer raskere enn den ekte. Hva er det farligste hun kan sette?",
    "alt": ["Utlånstiden", "Gateway og DNS-server, slik at all trafikk går via henne",
            "Antall adresser"],
    "riktig": "Gateway og DNS-server, slik at all trafikk går via henne",
    "ok": "Riktig. Den som deler ut oppsettet, bestemmer hvor trafikken går og hvem som slår opp navn.",
    "nei": "Ikke helt. Se på lista over hva som deles ut, og spør hvilke av dem som styrer trafikken."},
 ],
 "sikkerhet": "En falsk utdeler er et av de enkleste angrepene i et lokalnett, nettopp fordi "
              "maskiner tar imot oppsettet uten å spørre hvem som sendte det. Det er derfor "
              "svitsjer i bedriftsnett ofte settes opp til bare å godta svar fra en kjent port.",
},

{
 "id": "l06-8",
 "tittel": "Se det selv, uten å installere noe",
 "bilde_tittel": "⌨️ Spør maskinen om alt du nettopp leste",
 "bilde": [
   "Terminalen under kjører i nettleseren, og maskinen den viser står i Storgata 12.",
   "Skriv <strong>help</strong> og trykk enter. Spørsmålene under krever at du kombinerer "
   "to deler, ikke bare leser av en linje.",
 ],
 "ord": [
   "Alt du ser her, finnes på en ekte maskin også, med de samme kommandoene.",
 ],
 "term": {"id": "l06term", "tittel": "Terminal · student@storgata12", "svar": TERM},
 "din_tur": [
   {"q": "Kjør ipconfig. Hvilken nettmaske har maskinen?",
    "ph": "en nettmaske", "a": ["255.255.255.0"],
    "hint": "Andre linje i utskriften.", "sv": "255.255.255.0"},
   {"q": "Ut fra den nettmasken, hvor mange av de fire gruppene i adressen din er nett?",
    "ph": "et tall", "a": ["3", "tre"],
    "hint": "Tell hvor mange 255 det står i nettmasken.", "sv": "3"},
   {"q": "Kjør nslookup gokstad.local. Ligger adressen du fikk i ditt eget nett?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Sammenlign de tre første gruppene med din egen adresse.", "sv": "ja"},
   {"q": "Kjør nslookup vg.no. Ligger den adressen i ditt eget nett?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Samme sammenligning, helt annet resultat.", "sv": "nei"},
   {"q": "Kjør ipconfig /all. Hvor mange døgn varer utlånet av adressen?",
    "ph": "et tall", "a": ["2", "to", "2 døgn"],
    "hint": "Se på datoene for når utlånet starter og utløper.", "sv": "2"},
 ],
},

 ],
 "oppsummering": [
   "En <strong>IP-adresse</strong> har fire grupper, og hver gruppe går fra 0 til 255",
   "<strong>Nettmasken</strong> sier hvor mange av gruppene som er nett og hvor mange som er maskin",
   "To maskiner er naboer bare hvis nettdelen er lik, og nettmasken bestemmer hvor den delen slutter",
   "<strong>Private adresser</strong> gjentas i hvert lokalnett, <strong>offentlige</strong> er unike",
   "<strong>DNS</strong> gjør navn om til adresse, og den som svarer på oppslaget styrer hvor du havner",
   "<strong>DHCP</strong> deler ut adresse, nettmaske, gateway og DNS-server, alt sammen automatisk",
 ],
}
