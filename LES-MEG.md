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

Labbene skrives om for en student som trenger små steg og konkrete bilder.
Spørsmålene fra originalen beholdes, så læringsmålene er de samme.

| Lab | Status |
|-----|--------|
| `modules/nett-grunnlag.html` (L05) | Tilpasset (pilot) |
| De andre 9 | Som i CyberLab |

Hver oppgave i en tilpasset lab har seks steg, som vises ett om gangen:
Tenk på det slik, Nå med fagord, Oppvarming, Se et eksempel, Prøv på maskinen, Din tur.

- `css/enkel.css` har stilene. Siden må ha `<body class="page enkel">`.
- `js/enkel.js` viser stegene ett om gangen. Lastes etter `cyberlab.js`.
- Flervalg (`.mcq`) bruker `data-c` = `clHash()` av teksten i riktig alternativ, som i resten av CyberLab.
