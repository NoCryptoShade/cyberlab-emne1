# -*- coding: utf-8 -*-
"""L05 - Hva et nettverk er. Modul 2, Nettverk."""

TERM = """{
  help:[
    {t:'info',v:'Tilgjengelige kommandoer:'},
    {t:'out', v:'  ping [adresse]      sjekker om noen svarer'},
    {t:'out', v:'  arp -a              viser naboene i ditt eget lokalnett'},
    {t:'out', v:'  tracert [adresse]   viser hvilke bokser pakken passerte'},
    {t:'out', v:'  clear               t\\u00f8mmer skjermen'},
  ],
  'ping 192.168.1.90':[
    {t:'info',v:'Pinger 192.168.1.90 med 32 byte data:'},
    {t:'out', v:'Svar fra 192.168.1.90: byte=32 tid=1ms'},
    {t:'out', v:'Svar fra 192.168.1.90: byte=32 tid=1ms'},
    {t:'out', v:'Svar fra 192.168.1.90: byte=32 tid=1ms'},
    {t:'out', v:'Svar fra 192.168.1.90: byte=32 tid=1ms'},
    {t:'info',v:'Sendt = 4, mottatt = 4, tapt = 0'},
  ],
  ping:[
    {t:'info',v:'Bruk: ping [adresse]'},
    {t:'out', v:'Pr\\u00f8v ping 192.168.1.90'},
  ],
  'arp -a':[
    {t:'info',v:'Naboer i mitt lokalnett:'},
    {t:'out', v:'  Adresse         Fysisk adresse       Merknad'},
    {t:'out', v:'  192.168.1.1     00-11-22-33-44-55    ytterd\\u00f8ra'},
    {t:'out', v:'  192.168.1.77    aa-bb-cc-dd-ee-ff    en nabo'},
    {t:'out', v:'  192.168.1.90    11-22-33-44-55-66    en nabo'},
  ],
  arp:[{t:'info',v:'Bruk: arp -a'}],
  'tracert 8.8.8.8':[
    {t:'info',v:'Sporer ruten til 8.8.8.8:'},
    {t:'out', v:'  1    <1 ms   192.168.1.1'},
    {t:'out', v:'  2     4 ms   10.0.0.1'},
    {t:'out', v:'  3    11 ms   62.115.2.1'},
    {t:'out', v:'  4    14 ms   8.8.8.8'},
    {t:'info',v:'Sporing fullf\\u00f8rt.'},
  ],
  tracert:[
    {t:'info',v:'Bruk: tracert [adresse]'},
    {t:'out', v:'Pr\\u00f8v tracert 8.8.8.8'},
  ],
}"""

LEKSJON = {
 "num": "L05",
 "modul": "Modul 2 · Nettverk",
 "tittel": "Hva et nettverk er",
 "ingress": "Pakker, to slags adresser, og tre bokser som gjør hver sin jobb. "
            "Dette er grunnlaget alt senere i emnet hviler på.",
 "kort": [

{
 "id": "l05-1",
 "tittel": "Et nettverk er to maskiner og en vei mellom dem",
 "bilde_tittel": "\U0001F3E2 Blokka i Storgata 12",
 "bilde": [
   "Storgata 12 er en helt vanlig blokk. 24 leiligheter, en vaktmester som sorterer posten "
   "i kjelleren, og en ytterdør ut mot gata.",
   "Skal du sende en lapp til naboen i samme blokk, går den aldri ut på gata. Vaktmesteren "
   "tar den rett til riktig dør.",
   "Skal du sende en lapp til noen i en annen by, må den ut ytterdøra først.",
 ],
 "ord": [
   "Blokka er et <strong>lokalnett</strong>. Alt som skjer inne i blokka, er lokal trafikk.",
   "Denne blokka følger deg gjennom hele emnet. Hvert nytt faguttrykk får sin plass i den, "
   "så du slipper å bygge et nytt bilde for hvert tema.",
 ],
 "sjekk": {"q": "Du skal levere en pakke til leilighet 14 i samme blokk. Må pakken innom postsystemet ute i byen?",
           "ph": "ja / nei", "a": ["nei"],
           "hint": "Vaktmesteren når begge dørene uten å gå ut.", "sv": "nei"},
 "vist_intro": "Maskinen din stiller seg ett spørsmål hver gang den skal sende noe.",
 "vist": [
   "Du oppgir adressen til mottakeren",
   "Maskinen sammenligner den med sin egen adresse",
   "Er de i samme blokk, sendes det direkte",
   "Er de ikke det, sendes det til ytterdøra",
   "Ytterdøra tar seg av resten, og maskinen din vet ikke mer",
 ],
 "prov": [
   {"q": "To maskiner står i samme lokalnett og sender data til hverandre. Hvor mange ganger må trafikken ut av nettet?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Tenk på lappen til naboen i samme oppgang.", "sv": "0"},
   {"q": "En maskin sender data til en maskin i en annen by. Hvor mange ganger må trafikken ut av nettet?",
    "ph": "et tall", "a": ["1", "en", "én"],
    "hint": "Det finnes bare en vei ut av blokka.", "sv": "1"},
   {"q": "Kabelen ut av blokka blir kuttet. Kan leilighet 3 fortsatt sende en lapp til leilighet 14?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Den lappen skulle aldri ut på gata.", "sv": "ja"},
 ],
 "din_tur": [
   {"q": "En bedrift mister internettforbindelsen helt. De har en filserver som står i samme lokalnett som de ansatte. Kan de fortsatt åpne filene sine?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Hvor står serveren i forhold til dem?", "sv": "ja"},
   {"mcq": "Hvorfor virker en skriver på kontoret ofte selv når internett er nede?",
    "alt": ["Skriveren har sitt eget internett", "Skriveren står i det samme lokalnettet som maskinene",
            "Skriveren bruker ikke nettverk"],
    "riktig": "Skriveren står i det samme lokalnettet som maskinene",
    "ok": "Riktig. Trafikken til skriveren skal aldri ut ytterdøra.",
    "nei": "Ikke helt. Spør hvor skriveren står, ikke hva den er."},
 ],
 "sikkerhet": "Dette er også grunnen til at en angriper som først er kommet inn i lokalnettet, "
              "står mye friere enn en som står utenfor. Inne i blokka slipper han forbi "
              "ytterdøra på alt han gjør videre.",
},

{
 "id": "l05-2",
 "tittel": "Meldinger deles opp i pakker",
 "bilde_tittel": "\U0001F4E6 Esker, ikke ett stort lass",
 "bilde": [
   "Du skal flytte 300 bøker til naboen. Du kan bruke ett stort lass, eller du kan bruke esker.",
   "Med ett stort lass sperrer du hele oppgangen til du er ferdig. Mister du lasset, mister du alt.",
   "Med esker kan andre gå forbi mellom hver tur. Mister du en eske, bærer du den ene om igjen.",
 ],
 "ord": [
   "En eske er en <strong>pakke</strong>. All data på nettet sendes som pakker, ikke som en "
   "sammenhengende strøm.",
   "En vanlig pakke er på omtrent 1500 byte. Alt større enn det deles opp.",
 ],
 "sjekk": {"q": "Du bærer 12 esker og setter fra deg nummer 5 i feil etasje. Hvor mange esker må du hente på nytt?",
           "ph": "et tall", "a": ["1", "en", "én", "ett"],
           "hint": "Bare den ene esken gikk feil vei.", "sv": "1"},
 "vist_intro": "En fil på 1 MB sendes over nettet.",
 "vist": [
   "1 MB er omtrent 1 000 000 byte",
   "En pakke tar omtrent 1500 byte",
   "1 000 000 delt på 1500 blir omtrent 667 pakker",
   "Pakke nummer 300 forsvinner underveis",
   "Mottakeren ber om pakke 300 på nytt, ikke om hele fila",
 ],
 "prov": [
   {"q": "En fil på 3 MB deles i pakker på 1500 byte. Omtrent hvor mange pakker blir det?",
    "ph": "et tall", "a": ["2000", "2 000", "ca 2000", "omtrent 2000"],
    "hint": "3 MB er omtrent 3 000 000 byte. Del på størrelsen per pakke.", "sv": "omtrent 2000"},
   {"q": "En fil på 6 MB deles i pakker på 1500 byte. Omtrent hvor mange pakker blir det?",
    "ph": "et tall", "a": ["4000", "4 000", "ca 4000", "omtrent 4000"],
    "hint": "Samme regnestykke, dobbelt så stor fil.", "sv": "omtrent 4000"},
   {"q": "Tre av de pakkene forsvinner underveis. Hvor mange byte må sendes på nytt?",
    "ph": "et tall", "a": ["4500", "4 500", "4500 byte"],
    "hint": "Tre pakker, og hver pakke er 1500 byte.", "sv": "4500"},
 ],
 "din_tur": [
   {"q": "En forbindelse mister omtrent 1 av 1000 pakker. Du laster ned en fil på 3 MB. Omtrent hvor mange pakker må sendes på nytt?",
    "ph": "et tall", "a": ["2", "to", "ca 2", "omtrent 2"],
    "hint": "Regn først ut hvor mange pakker fila blir, og ta så en av tusen av det.",
    "sv": "2"},
   {"mcq": "En kollega sier at nettet er «tregt fordi fila er stor». Hva er en bedre forklaring når akkurat den ene fila er treg?",
    "alt": ["Store filer er alltid trege", "Mange pakker må sendes på nytt fordi noe faller bort underveis",
            "Maskinen har for lite minne"],
    "riktig": "Mange pakker må sendes på nytt fordi noe faller bort underveis",
    "ok": "Riktig. Pakketap koster tid, ikke bare størrelse.",
    "nei": "Ikke helt. Tenk på hva som skjer med en eske som ikke kommer fram."},
 ],
 "sikkerhet": "At trafikk er delt i pakker, er også det som gjør den mulig å se på. En brannmur "
              "leser pakker en for en og bestemmer seg for hver av dem. Uten oppdeling ville "
              "det ikke finnes noe sted å ta den avgjørelsen.",
},

{
 "id": "l05-3",
 "tittel": "Header og nyttelast",
 "bilde_tittel": "✉️ Utenpå konvolutten og inni den",
 "bilde": [
   "Utenpå en konvolutt står avsender og mottaker. Inni ligger brevet.",
   "Posten trenger bare det som står utenpå, for å gjøre jobben sin. Innholdet kan være "
   "hva som helst, og posten trenger ikke åpne det.",
 ],
 "ord": [
   "Det som står utenpå pakken, kalles <strong>header</strong>. Det som ligger inni, kalles "
   "<strong>nyttelast</strong>.",
   "Headeren er den delen nettverket leser. Nyttelasten er den delen mottakeren bryr seg om.",
 ],
 "sjekk": {"q": "Posten sorterer et brev uten å åpne det. Leste de konvolutten eller brevet?",
           "ph": "konvolutten / brevet", "a": ["konvolutten", "konvolutt"],
           "hint": "Hva trengte de for å vite hvor det skulle?", "sv": "konvolutten"},
 "vist_intro": "En pakke på 1500 byte, sett fra utsiden.",
 "vist": [
   "Omtrent 40 byte går med til header",
   "Der står avsenderadresse, mottakeradresse og litt til",
   "Resten er nyttelast, altså omtrent 1460 byte",
   "Rutere underveis leser bare headeren",
   "Bare mottakeren åpner nyttelasten",
 ],
 "prov": [
   {"q": "En pakke er på 1500 byte og headeren tar 40. Hvor mange byte er nyttelast?",
    "ph": "et tall", "a": ["1460", "1 460"],
    "hint": "Trekk fra det som står utenpå.", "sv": "1460"},
   {"q": "En pakke er på 600 byte og headeren tar 40. Hvor mange byte er nyttelast?",
    "ph": "et tall", "a": ["560", "560 byte"],
    "hint": "Samme regnestykke, mindre pakke.", "sv": "560"},
   {"q": "Du sender 100 pakker, hver med 40 byte header. Hvor mange byte gikk med til header til sammen?",
    "ph": "et tall", "a": ["4000", "4 000"],
    "hint": "Hundre konvolutter koster hundre konvolutter.", "sv": "4000"},
 ],
 "din_tur": [
   {"q": "Du fanger opp en pakke der selve innholdet er kryptert, men adressene er lesbare. Hva heter delen som fortsatt er lesbar?",
    "ph": "ett ord", "a": ["header", "headeren", "hode", "hodet"],
    "hint": "Krypteringen traff det som lå inni konvolutten, ikke det som sto utenpå.",
    "sv": "header"},
   {"mcq": "Noen som overvåker trafikken din, klarer ikke å lese innholdet, men ser likevel hvem du snakker med. Hvordan?",
    "alt": ["Han gjetter", "Headeren er ikke kryptert, og den kan leses",
            "Kryptering virker ikke"],
    "riktig": "Headeren er ikke kryptert, og den kan leses",
    "ok": "Riktig. Kryptering skjuler hva du sier, ikke hvem du sier det til.",
    "nei": "Ikke helt. Hvilken del av pakken må være lesbar for at den skal komme fram i det hele tatt?"},
 ],
 "sikkerhet": "Dette skillet er hele grunnen til at metadata er verdt å beskytte. Hvem som "
              "snakket med hvem, når og hvor ofte, ligger i headeren og er lesbart selv når "
              "innholdet ikke er det.",
},

{
 "id": "l05-4",
 "tittel": "To slags adresser",
 "bilde_tittel": "\U0001F516 Nummeret på døra og serienummeret på postkassa",
 "bilde": [
   "På døra står leilighetsnummeret. Det hører til leiligheten. Flytter du, får du et nytt.",
   "På selve postkassa står et lite serienummer fra fabrikken. Det hører til kassa. "
   "Flyttes kassa til en annen blokk, følger serienummeret med.",
   "De to endrer seg altså på helt ulike tidspunkt.",
 ],
 "ord": [
   "Leilighetsnummeret er <strong>IP-adressen</strong>. Den sier hvor maskinen er akkurat nå.",
   "Serienummeret er <strong>MAC-adressen</strong> (Media Access Control). Den ligger i "
   "nettkortet og følger maskinen uansett hvilket nett den kobles til.",
 ],
 "sjekk": {"q": "Postkassa fra leilighet 7 flyttes til en annen blokk. Hvilket av de to numrene følger med kassa?",
           "ph": "leilighetsnummeret / serienummeret", "a": ["serienummeret", "serienummer", "serienr"],
           "hint": "Det ene står på selve kassa.", "sv": "serienummeret"},
 "vist_intro": "En bærbar maskin flyttes fra jobb til hjemmenettet.",
 "vist": [
   "På jobb har den IP-adressen 10.20.30.44",
   "Hjemme får den 192.168.1.40",
   "MAC-adressen er den samme begge steder",
   "Altså endret IP-adressen seg, men MAC-adressen gjorde det ikke",
   "Det er derfor MAC brukes lokalt og IP brukes på tvers av nett",
 ],
 "prov": [
   {"q": "En maskin flyttes fra et nett til et annet. Hvilken av de to adressene endrer seg?",
    "ph": "IP / MAC", "a": ["ip", "ip-adressen", "ip adressen", "ipen"],
    "hint": "Den ene sier hvor du er.", "sv": "IP"},
   {"q": "Den samme maskinen kobles på et tredje nett. Hvilken adresse er fortsatt den samme som første gang?",
    "ph": "IP / MAC", "a": ["mac", "mac-adressen", "mac adressen", "macen"],
    "hint": "Den ene ligger i selve nettkortet.", "sv": "MAC"},
   {"q": "En bedrift bytter ut nettkortet i en maskin, men beholder den samme IP-adressen. Hvilken adresse er ny nå?",
    "ph": "IP / MAC", "a": ["mac", "mac-adressen", "mac adressen", "macen"],
    "hint": "Hva ble fysisk byttet ut?", "sv": "MAC"},
 ],
 "din_tur": [
   {"q": "Et gjestenett logger hvilke enheter som har vært innom over tid. Enhetene får ny IP-adresse hver gang. Hvilken adresse må loggen bruke for å kjenne igjen den samme enheten?",
    "ph": "IP / MAC", "a": ["mac", "mac-adressen", "mac adressen", "macen"],
    "hint": "Hvilken av de to er lik fra gang til gang?", "sv": "MAC"},
   {"mcq": "Hvorfor lar mange telefoner deg slå på «tilfeldig MAC-adresse» på trådløse nett?",
    "alt": ["For å gjøre forbindelsen raskere", "For å spare batteri",
            "For at nettet ikke skal kunne kjenne deg igjen fra gang til gang"],
    "riktig": "For at nettet ikke skal kunne kjenne deg igjen fra gang til gang",
    "ok": "Riktig. Det er nettopp fordi MAC-adressen ellers er den samme hver gang.",
    "nei": "Ikke helt. Tenk på hva en fast MAC-adresse forteller om deg over tid."},
 ],
 "sikkerhet": "En fast MAC-adresse er et sporingsmerke. Butikker og flyplasser har brukt "
              "trådløse nett til å telle og følge besøkende på nettopp dette grunnlaget, "
              "og det er derfor tilfeldig MAC-adresse er blitt standard på nye telefoner.",
},

{
 "id": "l05-5",
 "tittel": "Tre bokser med hver sin jobb",
 "bilde_tittel": "\U0001F9F0 Vaktmesteren, ytterdøra og dørvakten",
 "bilde": [
   "Vaktmesteren sorterer post inne i blokka. Han vet hvilken dør hvert nummer hører til, "
   "og han går aldri ut.",
   "Ytterdøra er veien mellom blokka og resten av byen. Alt som skal ut eller inn, må gjennom den.",
   "Dørvakten står ved ytterdøra og bestemmer hvem som får passere. Han flytter ingenting selv.",
 ],
 "ord": [
   "Vaktmesteren er en <strong>svitsj</strong> (switch). Den sender trafikk til riktig maskin "
   "inne i lokalnettet.",
   "Ytterdøra er en <strong>ruter</strong>. Den sender trafikk mellom ulike nett.",
   "Dørvakten er en <strong>brannmur</strong>. Den slipper trafikk gjennom eller stopper den, etter faste regler.",
 ],
 "sjekk": {"q": "En lapp skal fra leilighet 3 til leilighet 14. Hvem av de tre håndterer den?",
           "ph": "vaktmesteren / ytterdøra / dørvakten", "a": ["vaktmesteren", "vaktmester"],
           "hint": "Skal lappen ut av blokka i det hele tatt?", "sv": "vaktmesteren"},
 "vist_intro": "Du åpner en nettside fra maskinen din.",
 "vist": [
   "Trafikken går først til svitsjen, som er nærmest deg",
   "Svitsjen ser at adressen ikke hører hjemme i lokalnettet",
   "Den sender trafikken videre til ruteren",
   "Brannmuren vurderer om den får passere",
   "Først da går den ut på internett",
 ],
 "prov": [
   {"q": "Trafikk mellom to maskiner i samme lokalnett. Hvilken boks gjør jobben?",
    "ph": "svitsj / ruter / brannmur", "a": ["svitsj", "switch", "svitsjen", "switchen"],
    "hint": "Trafikken skal ikke ut av nettet.", "sv": "svitsj"},
   {"q": "Trafikk fra lokalnettet ut til internett. Hvilken boks sender den videre?",
    "ph": "svitsj / ruter / brannmur", "a": ["ruter", "ruteren", "router"],
    "hint": "Den som binder to ulike nett sammen.", "sv": "ruter"},
   {"q": "En regel sier at trafikk til port 23 skal stoppes. Hvilken boks håndhever den?",
    "ph": "svitsj / ruter / brannmur", "a": ["brannmur", "brannmuren", "firewall"],
    "hint": "Hvem av de tre tar stilling til om noe får lov?", "sv": "brannmur"},
 ],
 "din_tur": [
   {"q": "En bedrift har brannmur mot internett, men ingen kontroll på trafikk mellom maskiner i samme lokalnett. En angriper står allerede inne i lokalnettet. Hvor mange ganger møter han brannmuren når han beveger seg til nabomaskinen?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Hvor står dørvakten, og hvor beveger angriperen seg?", "sv": "0"},
   {"mcq": "Hva er den praktiske konsekvensen av svaret over?",
    "alt": ["Brannmuren er unødvendig", "En angriper som først er innenfor, kan bevege seg fritt sidelengs",
            "Lokalnettet er alltid trygt"],
    "riktig": "En angriper som først er innenfor, kan bevege seg fritt sidelengs",
    "ok": "Riktig. Det kalles lateral movement, og det er derfor segmentering finnes. Du møter det i L08.",
    "nei": "Ikke helt. Brannmuren gjør jobben sin, men bare der den står."},
 ],
 "sikkerhet": "En brannmur som bare står i ytterkanten, beskytter mot dem som er utenfor. "
              "Den gjør ingenting med en angriper som allerede er kommet inn, og det er "
              "utgangspunktet for alt som handler om segmentering.",
},

{
 "id": "l05-6",
 "tittel": "Følg pakken inne i nettet",
 "bilde_tittel": "📣 Ropet i oppgangen",
 "bilde": [
   "Vaktmesteren vet hvilket leilighetsnummer posten skal til, men han vet ikke hvilken "
   "postkasse som hører til nummeret.",
   "Så roper han ut i oppgangen: «Hvem har leilighet 90?» Den det gjelder, svarer.",
   "Han noterer svaret på en lapp, slik at han slipper å rope neste gang.",
 ],
 "ord": [
   "Ropet heter <strong>ARP</strong> (Address Resolution Protocol). Maskinen kjenner "
   "IP-adressen, men trenger MAC-adressen for å kunne sende noe i lokalnettet.",
   "Lappen heter <strong>ARP-tabellen</strong>. Svaret blir liggende der en stund, så "
   "spørsmålet stilles bare den første gangen.",
 ],
 "sjekk": {"q": "Vaktmesteren har ropt en gang og skrevet svaret på lappen. Må han rope igjen neste gang han har post til det samme nummeret?",
           "ph": "ja / nei", "a": ["nei"],
           "hint": "Hva var lappen til?", "sv": "nei"},
 "vist_intro": "Første gang maskinen din skal sende noe til 192.168.1.90.",
 "vist": [
   "Du kjenner IP-adressen, altså leilighetsnummeret",
   "Du mangler MAC-adressen, altså hvilken postkasse det er",
   "Maskinen sender spørsmålet til alle i lokalnettet samtidig",
   "Bare den ene maskinen svarer",
   "Svaret lagres i ARP-tabellen og brukes videre",
 ],
 "prov": [
   {"q": "Du sender til en maskin du aldri har snakket med før. Må maskinen din spørre etter MAC-adressen først?",
    "ph": "ja / nei", "a": ["ja"],
    "hint": "Står det noe om den på lappen fra før?", "sv": "ja"},
   {"q": "Du sender til den samme maskinen ett sekund senere. Må den spørre på nytt?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Svaret ble jo notert.", "sv": "nei"},
   {"q": "Nettet har 20 maskiner. Hvor mange av dem hører spørsmålet når det sendes ut?",
    "ph": "et tall", "a": ["20", "alle", "tjue"],
    "hint": "Ropet går ut i hele oppgangen, ikke til en bestemt dør.", "sv": "20"},
 ],
 "din_tur": [
   {"q": "Kan en maskin i et annet lokalnett høre ARP-spørsmålet ditt?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Hvor langt rekker et rop i oppgangen?", "sv": "nei"},
   {"mcq": "En angriper i det samme nettet svarer på ARP-spørsmålet ditt og oppgir sin egen MAC-adresse. Hva oppnår hun?",
    "alt": ["Ingenting, hun har feil adresse",
            "Trafikken din går til henne i stedet for til riktig maskin",
            "Hun får IP-adressen din"],
    "riktig": "Trafikken din går til henne i stedet for til riktig maskin",
    "ok": "Riktig. Du skrev feil postkasse på lappen, og du merker ingenting.",
    "nei": "Ikke helt. Hva er det svaret på ropet avgjør?"},
 ],
 "sikkerhet": "Ingen kontrollerer hvem som svarer på ropet. Den som svarer først, får "
              "trafikken. Det kalles ARP-forfalskning, og det er grunnen til at et lokalnett "
              "ikke er et trygt sted bare fordi det er lokalt.",
},

{
 "id": "l05-7",
 "tittel": "Se det selv, uten å installere noe",
 "bilde_tittel": "⌨️ Terminalen under er ekte nok til å øve på",
 "bilde": [
   "Maskinen kan spørres direkte om alt du nettopp har lest. Terminalen under kjører i "
   "nettleseren, og maskinen den viser står i Storgata 12.",
   "Skriv <strong>help</strong> og trykk enter for å se hvilke kommandoer som finnes. "
   "Skriver du feil, skjer det ingenting galt.",
 ],
 "ord": [
   "Dette er de samme kommandoene du bruker i en ekte maskin senere i emnet. Forskjellen "
   "er at her kan ingenting gå i stykker, og ingenting skal installeres først.",
 ],
 "term": {"id": "l05term", "tittel": "Terminal · student@storgata12", "svar": TERM},
 "din_tur": [
   {"q": "Kjør arp -a. Hvor mange naboer står i lista?",
    "ph": "et tall", "a": ["3", "tre"],
    "hint": "Tell linjene med adresser, ikke overskriften.", "sv": "3"},
   {"q": "I den samme lista, hvilken adresse er merket som ytterdøra?",
    "ph": "en adresse", "a": ["192.168.1.1"],
    "hint": "Se på merknaden helt til høyre.", "sv": "192.168.1.1"},
   {"q": "Kjør ping 192.168.1.90. Hvor mange pakker gikk tapt?",
    "ph": "et tall", "a": ["0", "null", "ingen"],
    "hint": "Siste linje oppsummerer.", "sv": "0"},
   {"q": "Kjør tracert 8.8.8.8. Hvor mange bokser sto mellom deg og målet, uten å telle målet selv?",
    "ph": "et tall", "a": ["3", "tre"],
    "hint": "Tell linjene i sporingen, og trekk fra den siste.", "sv": "3"},
 ],
},

 ],
 "oppsummering": [
   "Et <strong>lokalnett</strong> er alt som når hverandre uten å gå ut av nettet",
   "Data sendes som <strong>pakker</strong>, og en tapt pakke koster en pakke",
   "Hver pakke har en <strong>header</strong> utenpå og en <strong>nyttelast</strong> inni",
   "<strong>IP-adressen</strong> sier hvor maskinen er, <strong>MAC-adressen</strong> følger nettkortet",
   "<strong>Svitsj</strong> flytter trafikk inne i nettet, <strong>ruter</strong> mellom nett, <strong>brannmur</strong> bestemmer hvem som får passere",
   "En <strong>klient</strong> spør, en <strong>tjener</strong> venter og svarer",
 ],
}
