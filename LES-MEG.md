# CyberLab Emne 1

Kopi av Emne 1 fra [Cybersikkerhet-Gokstad/CyberLab](https://github.com/Cybersikkerhet-Gokstad/CyberLab),
hentet fra commit `7961b8f`. Dette repoet er stedet der endringene til Emne 1 gjøres.

## Innhold

| Fil | Fra CyberLab |
|-----|--------------|
| `emne1.html` | `emne1.html`, oversikten over de 26 leksjonene |
| `index.html` | Ny. Sender rett videre til `emne1.html` |
| `modules/*.html` | De 10 labbene som `emne1.html` lenker til |
| `css/`, `js/` | Uendret |

## Det eneste som er endret

Lenker til sider som ikke er en del av Emne 1, peker nå på den ekte CyberLab-sida:
`index.html`, `emne3.html`, `labber.html` og `modules/kryptografi.html`.
Ellers er alt likt med originalen, tegn for tegn.

## Tilpasset versjon

Labbene skrives om for en student med ADHD som synes abstrakte begreper er vanskelige.
Spørsmålene fra originalen beholdes, så læringsmålene er de samme.

| Lab | Status |
|-----|--------|
| `modules/nett-grunnlag.html` (L05) | Tilpasset (pilot) |
| De andre 9 | Som i CyberLab |

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
