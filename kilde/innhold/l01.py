# -*- coding: utf-8 -*-
"""L01 - Aa jobbe med cybersikkerhet. Modul 1, Grunnlaget.

Innholdet foelger beskrivelsen emne1.html gir leksjonen: hva cybersikkerhet
skal beskytte, fire vanlige jobber i bransjen, og hvem som angriper.
Angrepsflate og risiko hoerer til L03 og staar derfor ikke her.
"""

LEKSJON = {
 "num": "L01",
 "modul": "Modul 1 · Grunnlaget",
 "tittel": "Å jobbe med cybersikkerhet",
 "kort": [

{
 "id": "l01-1",
 "tittel": "De tre tingene vi beskytter",
 "bilde_tittel": "\U0001F4D2 Permen med leieboerlista",
 "bilde": [
   "Vaktmesteren i Storgata 12 har en perm med lista over hvem som bor i hvilken leilighet.",
   "Tre forskjellige ting kan gå galt med den permen. Noen uvedkommende leser den. "
   "Noen endrer et navn i den. Eller den er borte når han trenger den.",
   "De tre henger ikke sammen. Permen kan være lest uten å være endret, og endret uten "
   "å være borte.",
 ],
 "ord": [
   "De tre heter <strong>konfidensialitet</strong>, <strong>integritet</strong> og "
   "<strong>tilgjengelighet</strong>. På engelsk confidentiality, integrity og "
   "availability (CIA).",
   "Konfidensialitet betyr at ingen uvedkommende får se det. Integritet betyr at ingen "
   "har endret på det uten lov. Tilgjengelighet betyr at det er der når du trenger det.",
   "Alt du gjør i faget handler om å verne en eller flere av disse tre.",
 ],
 "sjekk": {"q": "Permen ligger framme i en ulåst kjeller. Ingenting er endret, og den er på plass. Hvilken av de tre er brutt?",
           "ph": "konfidensialitet / integritet / tilgjengelighet",
           "a": ["konfidensialitet", "konfidensialiteten"],
           "hint": "To av de tre er i orden. Hvilken er det ikke?", "sv": "konfidensialitet"},
 "vist_intro": "En e-post blir lest av feil person.",
 "vist": [
   "Innholdet i e-posten er uendret",
   "Du får den fortsatt selv",
   "Men noen andre har lest den",
   "Altså er bare en av de tre brutt",
   "Hvilken som er brutt, bestemmer hva du må gjøre etterpå",
 ],
 "prov": [
   {"q": "Noen endrer beløpet i en faktura fra 5000 til 50000. Hvilken av de tre er brutt?",
    "ph": "konfidensialitet / integritet / tilgjengelighet", "a": ["integritet", "integriteten"],
    "hint": "Alle kan fortsatt se fakturaen, og den er ikke borte.", "sv": "integritet"},
   {"q": "En nettbutikk er nede i seks timer. Hvilken av de tre er brutt?",
    "ph": "konfidensialitet / integritet / tilgjengelighet",
    "a": ["tilgjengelighet", "tilgjengeligheten"],
    "hint": "Ingenting er lest, og ingenting er endret.", "sv": "tilgjengelighet"},
   {"q": "Et passordregister blir lastet ned av en utenforstående. Ingenting endres, og tjenesten går som før. Hvilken er brutt?",
    "ph": "konfidensialitet / integritet / tilgjengelighet",
    "a": ["konfidensialitet", "konfidensialiteten"],
    "hint": "Noen har sett noe de ikke skulle ha sett.", "sv": "konfidensialitet"},
 ],
 "din_tur": [
   {"q": "Et løsepengevirus krypterer alle filene så ingen får åpnet dem, men kopierer ingenting ut. Hvilken av de tre er brutt?",
    "ph": "konfidensialitet / integritet / tilgjengelighet",
    "a": ["tilgjengelighet", "tilgjengeligheten"],
    "hint": "Filene ligger der fortsatt. Hjelper det?", "sv": "tilgjengelighet"},
   {"mcq": "En kollega får ved en feil lesetilgang til lønnsmappa. Hun endrer ingenting, og alle andre har tilgang som før. Hva er brutt?",
    "alt": ["Konfidensialitet", "Integritet", "Tilgjengelighet", "Ingen av dem"],
    "riktig": "Konfidensialitet",
    "ok": "Riktig. At det var et uhell, endrer ikke at noen har sett noe de ikke skulle ha sett.",
    "nei": "Ikke helt. Gå gjennom de tre etter tur og spør om hver enkelt er i orden."},
 ],
 "sikkerhet": "Hvilken av de tre som er brutt, avgjør hva du gjør. Brutt tilgjengelighet "
              "løses med gjenoppretting. Brutt konfidensialitet kan ikke gjenopprettes, for "
              "det som er lest, er lest. Da handler jobben om varsling og skadebegrensning.",
},

{
 "id": "l01-2",
 "tittel": "Sikkerhetsarbeid er tre jobber, ikke en",
 "bilde_tittel": "\U0001F3E2 Vaktmesteren i Storgata 12",
 "bilde": [
   "I kjelleren står det sykler. I gangen henger postkassene. På veggen hos vaktmesteren "
   "henger lista over hvem som bor hvor.",
   "Vaktmesteren kan ikke gjøre tyveri umulig. Det han kan, er å gjøre det vanskelig nok, "
   "merke seg når noe skjer, og sørge for at blokka kommer seg på beina etterpå.",
 ],
 "ord": [
   "Cybersikkerhet er det samme arbeidet, bare at verdiene er data.",
   "Det er alltid tre jobber, og de er forskjellige. <strong>Hindre</strong> at noe skjer. "
   "<strong>Oppdage</strong> at det likevel skjedde. <strong>Komme tilbake</strong> etterpå.",
 ],
 "sjekk": {"q": "Vaktmesteren setter opp en lås ingen klarer å bryte opp. Er blokka dermed helt sikker?",
           "ph": "ja / nei", "a": ["nei"],
           "hint": "Må alle som kommer inn, gå gjennom akkurat den døra?", "sv": "nei"},
 "vist_intro": "Slik tenker vaktmesteren når han ser på sykkelboden.",
 "vist": [
   "Hva er verdt å ta her",
   "Hvem kan tenkes å ville ha det",
   "Hvordan kommer de eventuelt inn",
   "Hva kan gjøre det vanskeligere for dem",
   "Og hvordan får vi vite at det faktisk skjedde",
 ],
 "prov": [
   {"q": "Vaktmesteren setter opp et kamera ved sykkelboden. Er det å hindre, oppdage eller komme tilbake?",
    "ph": "hindre / oppdage / komme tilbake", "a": ["oppdage", "å oppdage", "oppdage det"],
    "hint": "Et kamera stopper ingen. Det forteller deg noe.", "sv": "oppdage"},
   {"q": "Døra til sykkelboden får en kodelås. Hindre, oppdage eller komme tilbake?",
    "ph": "hindre / oppdage / komme tilbake", "a": ["hindre", "å hindre"],
    "hint": "En lås gjør det vanskeligere å komme inn i utgangspunktet.", "sv": "hindre"},
   {"q": "Blokka har en lånesykkel i kjelleren til den som mister sin. Hindre, oppdage eller komme tilbake?",
    "ph": "hindre / oppdage / komme tilbake",
    "a": ["komme tilbake", "å komme tilbake", "komme seg tilbake"],
    "hint": "Den gjør ingenting med tyveriet. Den gjør noe med etterpå.", "sv": "komme tilbake"},
 ],
 "din_tur": [
   {"q": "En bedrift tar sikkerhetskopi av alle filene hver natt. Hvilken av de tre jobbene er det?",
    "ph": "hindre / oppdage / komme tilbake",
    "a": ["komme tilbake", "å komme tilbake", "komme seg tilbake"],
    "hint": "En kopi stopper ingen, og den varsler ingen.", "sv": "komme tilbake"},
   {"mcq": "Et selskap har brannmur og sikkerhetskopi, men ingen ser på loggene. Hvilken av de tre jobbene mangler?",
    "alt": ["Hindre", "Oppdage", "Komme tilbake"],
    "riktig": "Oppdage",
    "ok": "Riktig. De kan stoppe, og de kan gjenopprette, men de vet ikke når noe skjer.",
    "nei": "Ikke helt. Se hvilke to de allerede har, og hva som da står igjen."},
 ],
 "sikkerhet": "De fleste virksomheter bruker mest penger på å hindre og minst på å oppdage. "
              "Derfor er den vanligste alvorlige hendelsen ikke et innbrudd ingen kunne stoppet, "
              "men et innbrudd ingen la merke til på flere måneder.",
},

{
 "id": "l01-3",
 "tittel": "Fire vanlige jobber i bransjen",
 "bilde_tittel": "\U0001F465 Fire personer rundt den samme blokka",
 "bilde": [
   "Vaktmesteren går runden hver dag og ser etter noe uvanlig.",
   "Kontrolløren kommer en gang i året, går gjennom alle låsene og skriver en rapport.",
   "Skadeservice rykker ut når noe allerede har skjedd, og rydder opp.",
   "Og hun som styret har leid inn, prøver alle dørene for å se hvilke som står ulåste.",
 ],
 "ord": [
   "De fire rollene finnes i faget også. En <strong>SOC-analytiker</strong> (Security Operations "
   "Centre) følger med til daglig. En <strong>sikkerhetsrådgiver</strong> vurderer og "
   "anbefaler. En <strong>hendelseshåndterer</strong> rykker ut. En "
   "<strong>penetrasjonstester</strong> bryter seg inn på oppdrag.",
   "De som forsvarer, kalles <strong>blått lag</strong>. De som angriper på oppdrag, "
   "kalles <strong>rødt lag</strong>. Begge jobber for den samme virksomheten.",
 ],
 "sjekk": {"q": "Hun som prøver alle dørene i blokka, gjør det på oppdrag fra styret. Jobber hun for blokka eller mot den?",
           "ph": "for / mot", "a": ["for", "for blokka"],
           "hint": "Hvem har bedt henne om å gjøre det?", "sv": "for"},
 "vist_intro": "En vanlig dag i et SOC.",
 "vist": [
   "Varsler kommer inn hele døgnet",
   "De aller fleste er falske alarmer",
   "Analytikeren vurderer hvert enkelt varsel",
   "Ett av dem viser seg å være ekte",
   "Da eskaleres det til dem som håndterer hendelser",
 ],
 "prov": [
   {"q": "En som overvåker logger og svarer på varsler. Blått eller rødt lag?",
    "ph": "blått / rødt", "a": ["blått", "blatt", "blaatt", "blått lag", "blå"],
    "hint": "Forsvar eller angrep?", "sv": "blått"},
   {"q": "En som forsøker å bryte seg inn på oppdrag for å finne hull. Blått eller rødt lag?",
    "ph": "blått / rødt", "a": ["rødt", "rodt", "roedt", "rødt lag", "rød"],
    "hint": "Hun gjør det samme som en angriper, bare med tillatelse.", "sv": "rødt"},
   {"q": "En som setter opp regler i brannmuren. Blått eller rødt lag?",
    "ph": "blått / rødt", "a": ["blått", "blatt", "blaatt", "blått lag", "blå"],
    "hint": "Bygger hun en vei inn, eller stenger hun en?", "sv": "blått"},
 ],
 "din_tur": [
   {"q": "Et SOC får 500 varsler på en dag, og 499 av dem er falske alarmer. Hvor mange ekte hendelser er det?",
    "ph": "et tall", "a": ["1", "en", "én"],
    "hint": "Trekk de falske fra antallet.", "sv": "1"},
   {"mcq": "Hvorfor er mange falske alarmer et sikkerhetsproblem, og ikke bare et irritasjonsmoment?",
    "alt": ["De bruker strøm", "Den ekte hendelsen drukner i mengden",
            "De fyller opp harddisken"],
    "riktig": "Den ekte hendelsen drukner i mengden",
    "ok": "Riktig. Det koster ikke maskinen noe. Det koster oppmerksomheten til den som ser.",
    "nei": "Ikke helt. Tenk på mennesket som skal vurdere 500 varsler på en dag."},
 ],
 "sikkerhet": "Varslingstretthet er en reell svakhet. Et system som varsler om alt, varsler "
              "i praksis om ingenting, og en angriper som vet det, legger seg innenfor "
              "støyen i stedet for utenfor den.",
},

{
 "id": "l01-4",
 "tittel": "Hvem som angriper",
 "bilde_tittel": "\U0001F575️ Fire som kan tenkes å ville inn",
 "bilde": [
   "Han som går gjennom sykkelboden og tar den som ikke er låst. Han bryr seg ikke om "
   "hvilken sykkel det er.",
   "Hun som har planlagt i ukevis fordi hun vet at det står noe bestemt i bod 14.",
   "Den tidligere beboeren som fortsatt har nøkkel og aldri leverte den inn.",
   "Og han som henger opp en plakat i oppgangen fordi han vil bli sett.",
 ],
 "ord": [
   "De fire kalles <strong>trusselaktører</strong>, og de skilles på motiv.",
   "<strong>Kriminelle</strong> vil ha penger. <strong>Statlige aktører</strong> vil ha "
   "informasjon, og de har tålmodighet. <strong>Innsidere</strong> har allerede tilgang. "
   "<strong>Hacktivister</strong> vil ha oppmerksomhet om en sak.",
   "Motivet bestemmer hvem de går etter, og hvor lenge de holder på.",
 ],
 "sjekk": {"q": "Han i sykkelboden prøver alle låsene og går videre når de holder. Leter han etter en bestemt sykkel, eller etter hvilken som helst ulåst sykkel?",
           "ph": "bestemt / ulåst", "a": ["ulåst", "en ulåst", "ulast", "ulaast", "ulåst en"],
           "hint": "Hvorfor gikk han videre fra de låste?", "sv": "ulåst"},
 "vist_intro": "Motivet bestemmer hvem som rammes.",
 "vist": [
   "Den som vil ha penger, går etter den som betaler raskest",
   "Den som vil ha informasjon, går etter den som har den",
   "Den som vil ha oppmerksomhet, går etter den som er mest synlig",
   "Ingen av dem leter først etter en bestemt virksomhet",
   "De fleste angrep treffer den som var lettest å komme inn hos",
 ],
 "prov": [
   {"q": "Et løsepengeangrep mot et sykehjem. Er motivet penger, informasjon eller oppmerksomhet?",
    "ph": "penger / informasjon / oppmerksomhet", "a": ["penger"],
    "hint": "Hva er det de ber om for å gi filene tilbake?", "sv": "penger"},
   {"q": "Noen kopierer forskningsdata fra et universitet over to år uten å ødelegge noe. Penger, informasjon eller oppmerksomhet?",
    "ph": "penger / informasjon / oppmerksomhet", "a": ["informasjon"],
    "hint": "De ville ikke bli oppdaget, og de krevde ingenting.", "sv": "informasjon"},
   {"q": "Forsida på nettstedet til en kommune byttes ut med et politisk budskap. Penger, informasjon eller oppmerksomhet?",
    "ph": "penger / informasjon / oppmerksomhet", "a": ["oppmerksomhet"],
    "hint": "Hva oppnår de ved at alle ser det?", "sv": "oppmerksomhet"},
 ],
 "din_tur": [
   {"q": "En ansatt slutter, men brukerkontoen hennes er fortsatt gyldig tre måneder etter. Regnes hun som utenforstående eller innsider?",
    "ph": "utenforstående / innsider", "a": ["innsider", "innsiden"],
    "hint": "Hva er det som skiller de to gruppene? Ikke hvor de sitter.", "sv": "innsider"},
   {"mcq": "En liten bedrift sier «vi er for små til at noen bryr seg». Hva er svakheten i resonnementet?",
    "alt": ["De har rett, små virksomheter blir ikke angrepet",
            "De fleste angrep leter etter det som står åpent, ikke etter en bestemt virksomhet",
            "Små virksomheter har ingen data"],
    "riktig": "De fleste angrep leter etter det som står åpent, ikke etter en bestemt virksomhet",
    "ok": "Riktig. Du blir ikke valgt ut. Du blir funnet.",
    "nei": "Ikke helt. Tenk på ham som gikk gjennom hele sykkelboden."},
 ],
 "sikkerhet": "Angrepet som rammer en liten norsk virksomhet, starter sjelden med at noen "
              "valgte akkurat den. Det starter med at en maskin lette etter en bestemt "
              "åpen tjeneste på hele internett og fant den.",
},

{
 "id": "l01-5",
 "tittel": "Den korteste veien inn går ofte gjennom et menneske",
 "bilde_tittel": "\U0001F4E6 Han som bærer en pakke og ser travel ut",
 "bilde": [
   "Blokka får ny kodelås på ytterdøra. Ingen klarer å bryte den opp.",
   "Så kommer det en mann med en pakke i armene. Han ser sliten og travel ut, og en "
   "beboer holder døra for ham.",
   "Låsen var aldri problemet.",
 ],
 "ord": [
   "Når noen blir lurt til å slippe en inn, eller til å gi fra seg noe de ikke burde, "
   "kalles det <strong>sosial manipulering</strong>.",
   "Det er ikke et hull i teknikken. Det er et hull i tilliten, og teknikk alene lukker "
   "det ikke.",
 ],
 "sjekk": {"q": "Blokka får ny kodelås, og beboerne skriver koden på en lapp ved døra. Er blokka sikrere enn før?",
           "ph": "ja / nei", "a": ["nei"],
           "hint": "Hvem kan lese lappen?", "sv": "nei"},
 "vist_intro": "En helt vanlig hendelse, steg for steg.",
 "vist": [
   "En e-post ser ut til å komme fra sjefen",
   "Den sier at det haster",
   "Mottakeren logger inn på en side som ligner på den ekte",
   "Passordet havner hos avsenderen av e-posten",
   "Og angriperen logger inn som en helt vanlig ansatt",
 ],
 "prov": [
   {"q": "En ansatt gir passordet sitt på telefon til en som sier han er fra IT. Er svakheten teknisk eller menneskelig?",
    "ph": "teknisk / menneskelig", "a": ["menneskelig", "menneske"],
    "hint": "Ble det utnyttet et hull i et program her?", "sv": "menneskelig"},
   {"q": "En gammel versjon av et program har et kjent hull som blir utnyttet. Teknisk eller menneskelig?",
    "ph": "teknisk / menneskelig", "a": ["teknisk"],
    "hint": "Her ble ingen snakket med.", "sv": "teknisk"},
   {"q": "En minnepinne som lå på parkeringsplassen, blir plugget inn av nysgjerrighet. Teknisk eller menneskelig?",
    "ph": "teknisk / menneskelig", "a": ["menneskelig", "menneske"],
    "hint": "Noen tok et valg her.", "sv": "menneskelig"},
 ],
 "din_tur": [
   {"q": "En bedrift kjøper en dyrere brannmur etter at en ansatt ble lurt av en falsk e-post. Løser det problemet som faktisk oppsto?",
    "ph": "ja / nei", "a": ["nei"],
    "hint": "Hvor sto døra åpen, og hvor satte de inn tiltaket?", "sv": "nei"},
   {"mcq": "En ansatt blir lurt til å oppgi passordet sitt på en falsk side. Hva begrenser skaden mest?",
    "alt": ["En raskere server", "En større harddisk",
            "Tofaktor, slik at passordet alene ikke er nok"],
    "riktig": "Tofaktor, slik at passordet alene ikke er nok",
    "ok": "Riktig. Teknikken hindret ikke feilen, men den gjorde feilen mindre verdt.",
    "nei": "Ikke helt. Feilen er allerede gjort. Spørsmålet er hva som stopper neste steg."},
 ],
 "sikkerhet": "Tofaktor er et av få tiltak som virker etter at et menneske allerede har "
              "gjort en feil. Teknikk kan ikke hindre at noen blir lurt, men den kan "
              "sørge for at det ikke holder å bli lurt.",
},

 ],
 "oppsummering": [
   "Vi beskytter <strong>konfidensialitet</strong>, <strong>integritet</strong> og <strong>tilgjengelighet</strong>",
   "Sikkerhetsarbeid er tre jobber: <strong>hindre</strong>, <strong>oppdage</strong> og <strong>komme tilbake</strong>",
   "Fire vanlige roller: SOC-analytiker, sikkerhetsrådgiver, hendelseshåndterer og penetrasjonstester",
   "<strong>Blått lag</strong> forsvarer, <strong>rødt lag</strong> angriper på oppdrag, begge for samme virksomhet",
   "<strong>Trusselaktører</strong> skilles på motiv: penger, informasjon, tilgang innenfra eller oppmerksomhet",
   "De fleste angrep leter etter det som står åpent, ikke etter en bestemt virksomhet",
   "Mange hendelser starter med <strong>sosial manipulering</strong>, ikke med et teknisk hull",
 ],
}
