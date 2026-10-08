# CyberLab Emne 1

Startet som en kopi av Emne 1 fra [Cybersikkerhet-Gokstad/CyberLab](https://github.com/Cybersikkerhet-Gokstad/CyberLab)
(commit `7961b8f`), og er nå skrevet om til en tilpasset versjon. Se under.

## Innhold

| Fil | Hva det er |
|-----|------------|
| `emne1.html` | Oversikten over de 26 leksjonene. Alle lenker til en lab |
| `index.html` | Sender rett videre til `emne1.html` |
| `modules/*.html` | Én lab per leksjon (L11–L13 deler én, og det samme gjør L22 og L25) |
| `css/style.css`, `css/lab-shared.css`, `js/cyberlab.js` | Uendret fra CyberLab |
| `css/enkel.css`, `js/enkel.js` | Stilen og spillene i den tilpassede versjonen |
| `verktoy/` | Oppskrift, test og hjelpeskript |

Ingen lenker går til Gokstads CyberLab, så studenten blir alltid på denne sida. Menyen har bare
«Emne 1» (oversikten) og «Self check» (TK1104, åpnes i ny fane). Nederst i hver lab er det en
«Neste»-knapp til neste leksjon.

## Tilpasset versjon

Labbene er skrevet om for en student med ADHD som synes abstrakte begreper er vanskelige.

Alle 26 leksjonene har en lab i den tilpassede stilen:

| Leksjon | Fil | |
|---|---|---|
| L01 Å jobbe med cybersikkerhet | `cybersikkerhet.html` | ny |
| L02 Hvordan digitale systemer virker | `digitale-systemer.html` | ny |
| L03 Verdier, trusler, sårbarheter og risiko | `risiko.html` | ny |
| L04 Etikk, lov og ansvar | `etikk-lov.html` | ny |
| L05 Hva et nettverk er | `nett-grunnlag.html` | tilpasset |
| L06 IP-adressering, DNS og DHCP | `adressering.html` | tilpasset |
| L07 Tjenester, porter og eksponering | `porter.html` | tilpasset |
| L08 Switching, VLAN og segmentering | `vlan.html` | tilpasset |
| L09 Ruting, default gateway og NAT | `ruting-nat.html` | tilpasset |
| L10 Trådløse nettverk | `tradlost.html` | tilpasset |
| L11–L13 Linux | `linux.html` | tilpasset |
| L14 Fire spørsmål til en ukjent maskin | `nettverk.html` | tilpasset |
| L15 Fra kommando til program | `python-start.html` | ny |
| L16 Én regel, mange linjer | `python-valg.html` | ny |
| L17 Hundre funn, én variabel | `python-samlinger.html` | ny |
| L18 Fem linjer med et navn | `python-funksjoner.html` | ny |
| L19 Fra funn til rapport | `python-rapport.html` | ny |
| L20 Når verden ikke ser ut som du trodde | `python-feil.html` | ny |
| L21 Tabellen noen andre passer på | `sql.html` | ny |
| L22 og L25 Web | `web-sarbarheter.html` | tilpasset |
| L23 Kommandolinjen får sitt eget språk | `bash-skript.html` | ny |
| L24 Ett skript, fire spørsmål | `maskinrapport.html` | ny |
| L26 Når navnet blir kode | `injeksjon.html` | tilpasset |

I de tilpassede labbene står alle de opprinnelige spørsmålene uendret. Unntaket er to fasiter
som var «;» og aldri kunne godtas (svarsjekken fjerner tegnsetting). De viser nå «semikolon (;)».

Slik lager eller endrer du en lab: se `verktoy/OPPSKRIFT.md`. Test med
`node verktoy/test-lab.mjs modules/x.html` og `python3 verktoy/sjekk-originaler.py modules/x.html`.

Hver oppgave er bygd slik, og hver idé forklares bare én gang:

1. En kort krok (én–to linjer)
2. Et lite spill, forskjellig fra oppgave til oppgave
3. En blå «Fagord»-boks som gir det du lekte med riktig navn
4. En øve-terminal med oppdrag: skriv kommandoene og se utskriften. Tidlige oppdrag viser kommandoen,
   senere oppdrag gir bare målet og et hint, så studenten må huske selv
5. «Les av øve-terminalen»: spørsmål som besvares fra utskriften, og som teller i fremdriften
6. «Nå på ekte Kali»: de samme kommandoene på egen maskin
7. De opprinnelige spørsmålene

Spilltypene ligger i `js/enkel.js` og styres fra HTML-en:

| `data-spill` | Hva det er | Innhold i HTML |
|---|---|---|
| `pakker` | Send en fil i ett stykke eller som pakker | ingen |
| `reise` | Kjør en pakke hopp for hopp, se hvilken lapp som byttes | ingen |
| `lyn` | Lynrunde med rekke-teller. Feil kort kommer igjen | `.ly-item` med `data-svar` (0-basert) og `data-hvorfor`; knappene i `data-knapper="A\|B"` |
| `chat` | Meldinger som dukker opp én etter én | `.ch-item` med `data-fra` (pc, nabo, ond, sys), `data-navn`, eller `data-stopp` for en pause-knapp |
| `rop` | Et ARP-rop som stopper ved ruteren, og en pakke som hopper | ingen |
| `terminal` | Øve-terminal med oppdrag i rekkefølge | `.tm-o` med `data-cmd`, `data-mal`, `data-alias` (flere skrivemåter, skilt med \|), `data-skjult` og `data-hint`; utskriften i `<template class="ut">`, forklaringen i `<template class="forklar">` |

`css/enkel.css` har stilene, og siden må ha `<body class="page enkel">`. Spillene teller
ikke i fremdriften. Det gjør svarfeltene, som før. Når en oppgave blir ferdig, dukker det opp
en liten feiring nederst på skjermen.
