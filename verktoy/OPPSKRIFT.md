# Oppskrift: slik lages en tilpasset lab

Fasit for stilen er `modules/nett-grunnlag.html` (L05). Les den før du starter, og kopier
skjelettet derfra: `<head>`, menyen, `e-strip`, ordlista, fremdriftslinja, filterraden og bunnen.

## Hvem det er for

En voksen student med ADHD som synes abstrakte begreper er vanskelige. Hun kjeder seg fort
hvis det samme forklares flere ganger. Hun skal likevel lære terminalen og fagordene ordentlig.

- **Hver idé forklares én gang.** Spillet viser den, fagord-boksen navngir den. Ikke gjenta.
- **Lek først, ord etterpå.** Hverdagsbildet ligger i spillet, ikke i en egen tekst før det.
- **Kort.** Én til to setninger i kroken. Korte setninger overalt. Ingen lange avsnitt.
- **Lekent, men ikke barnslig.** Litt humor og emoji er fint (🎉 🦹 🔥), men ikke på hver linje.
- **Norsk bokmål.** Fagord på engelsk står i parentes første gang, hvis studenten møter dem i verktøyene.
- **Faglig riktig.** En forenkling skal være sann. Ikke finn på tall, porter, flagg eller utskrifter.

## Hver oppgave (`.lab-card`) er bygd slik

1. `level-badge`
2. `<p class="e-hook">`: én–to linjer som vekker nysgjerrighet. Varier formen fra oppgave til oppgave.
3. **Ett spill** (`.e-spill`). Bruk forskjellige typer etter hverandre, ikke samme type to ganger på rad.
4. `<div class="e-fagord">`: navnet på det studenten nettopp lekte med. Kort.
5. Valgfritt: `<p class="e-sikker">` for et sikkerhetspoeng eller en «fun fact».
6. **Øve-terminal** (`data-spill="terminal"`), 2–4 oppdrag. Alltid med, også i teorileksjoner.
7. `<div class="ans-block les">` med tittelen «🔎 Les av øve-terminalen»: 1–2 spørsmål som besvares fra utskriften.
8. `<div class="e-kali">`: «🐉 Nå på ekte Kali». De samme kommandoene på egen maskin, pluss Windows-variant hvis den finnes.
9. `<div class="ans-block">` med tittelen «✍️ Din tur»: oppgavens egne spørsmål.

## Spilltyper i `js/enkel.js`

Bruk bare disse. `pakker`, `reise` og `rop` er laget for L05 og skal ikke brukes andre steder.

| `data-spill` | Brukes til | Markup |
|---|---|---|
| `lyn` | Lynrunde: ett kort om gangen, velg riktig knapp. Feil kort kommer igjen. | `data-knapper="A\|B\|C"`. Kort: `<div class="ly-item" data-svar="0" data-hvorfor="…">tekst</div>` (svar er 0-basert). Valgfritt `<div class="ly-fast">` som står fast over kortet. |
| `klikk` | Finn de riktige bitene i en logg, kode, kommando eller tekst. | `data-oppgave="…"`. I teksten: `<span class="kl" data-rett data-forklar="…">riktig</span>` og feller uten `data-rett`. Bruk gjerne `<pre>`. |
| `rekkefolge` | Sett steg i riktig rekkefølge. | `<div class="rf-item" data-forklar="…">steg</div>` i **riktig** rekkefølge i HTML. Spillet stokker. |
| `par` | Koble ting sammen (begrep ↔ betydning, tjeneste ↔ port). | `<div class="pr-par" data-forklar="…"><span>venstre</span><span>høyre</span></div>` |
| `chat` | En liten historie i chat-form. Bra for angrep, sosial manipulering, protokoller. | `<div class="ch-item" data-fra="pc\|nabo\|ond\|sys" data-navn="…">tekst</div>`. Pause: `<div class="ch-item" data-stopp="Knappetekst"></div>` |
| `terminal` | Øve-terminalen. | Se under. |

Alle spill tar `data-tittel="🎮 …"`. Tekst på kort, steg og par må være **unik** innenfor ett spill.
Attributter skrives med doble anførselstegn, så bruk «» inni teksten.

## Øve-terminalen

```html
<div class="e-spill" data-spill="terminal">
  <div class="tm-o" data-cmd="ip addr" data-alias="ip a|ip address" data-mal="Vis adressene dine:">
    <template class="ut">…utskrift, med <span class="h1">markering</span>…</template>
    <template class="forklar">…forklaring som dukker opp etterpå…</template>
  </div>
  <div class="tm-o" data-cmd="ip neigh" data-mal="Vis naboene dine." data-skjult data-hint="Den starter også med <code>ip</code>.">
    …
  </div>
</div>
```

- Første oppdrag viser kommandoen. Senere oppdrag bruker `data-skjult` + `data-hint`, så studenten må huske selv.
  Hint kan peke tilbake: «Samme kommando som i oppgave 2».
- `data-alias`: andre skrivemåter som også skal godtas, skilt med `|`. `-c4` og `-c 4` godtas automatisk.
- `&&`, `<` og `>` skrives som `&amp;&amp;`, `&lt;` og `&gt;`, også i `data-cmd`.
- **Utskriftene skal være ekte.** Kjør kommandoen i containeren når det går (`python3`, `bash`, `sqlite3`,
  `ls`, `grep`, `sha256sum` …) og lim inn det som faktisk kommer ut. Når det ikke går (nettverk, `sudo`),
  lag en realistisk utskrift i riktig format.
- Hold labnettet likt overalt: din PC `192.168.1.10/24`, MAC `08:00:27:3c:7a:10`, gateway `192.168.1.1`
  (MAC `3c:22:fb:7a:10:05`), brukeren heter `kali`, maskinen heter `kali`.
- Markering i utskrift: `h1` gul, `h2` blå, `h3` grønn, `h4` lilla, `dim` grå. Forklar fargene i `forklar` med
  `<ul class="e-forklar"><li><span class="m h1"></span><span>…</span></li></ul>`.
- Python, SQL og Bash: vis koden med `cat fil.py` først, så kjør den med `python3 fil.py`. Utskriften må
  komme fra en ekte kjøring av akkurat den koden.

## Spørsmål

```html
<div class="ans-row" data-p="1" data-a="svar|annet godkjent svar"><span class="ans-q">Spørsmål?</span><input class="ans-in" placeholder="et tall"><span class="ans-mark"></span><button class="submit-btn" onclick="clSubmit(this)">Svar</button><div class="ah"><button class="ah-btn" onclick="aTip(this)">&#9654; Hint</button><div class="ah-box tip">Hint</div><button class="ah-btn sv fasit-btn" onclick="aTip(this)">&#9654; Fasit</button><div class="ah-box sv">fasit</div></div></div>
```

- Svarsjekken er romslig (store/små bokstaver, «ca.», tall i setninger). List likevel vanlige varianter i `data-a`.
- Svarsjekken fjerner tegnsetting (`. , ; : ! ? " ' ` ( ) [ ]`). Er svaret selve tegnene (`!=`, `:`, `>>`, `()`),
  bruk flervalg (`.mcq`) i stedet, ellers godtas feil svar. Flervalg sammenligner teksten nøyaktig.
- Teksten i `.ah-box.sv` (fasiten) **må** godtas av `data-a`. Testen sjekker det.
- Hint skal peke på noe studenten har gjort: «Hvor mange pakker klikket du på i spillet?»

### Når en eksisterende lab tilpasses

- Behold **alle** oppgavene med samme `id`, `data-level`, nummer og tittel.
- Behold **alle** spørsmålene i «Din tur» med nøyaktig samme spørsmålstekst, `data-a` og fasit, i samme rekkefølge.
  Bare hintene kan skrives om. Flervalg (`.mcq`) beholdes uendret, med samme `data-c`.
- Alt det andre (teori, regneeksempel, «Kjør dette») erstattes av krok, spill, fagord, terminal og Kali-boks.
- Les originalen i `/home/user/cyberlab/modules/` hvis du trenger å sammenligne.

### Når en ny lab lages

- Filnavn og prefiks for `id` står i oppdraget. 4–6 oppgaver, med `id` `<prefiks>-1`, `<prefiks>-2` osv.
- 3 spørsmål i «Din tur» per oppgave. Bland lette og litt vanskeligere. Første oppgave(r) `data-level="easy"`, resten `medium`.
- Overskrift: `<div class="section-eyebrow">Emne 1 &middot; Leksjon N</div>`. Følg beskrivelsen av leksjonen i `emne1.html`.

## Ikke rør

`js/enkel.js`, `css/enkel.css`, `css/style.css`, `css/lab-shared.css`, `js/cyberlab.js`, `emne1.html` og
andre labber enn din. Trenger siden egen stil, legg den i en `<style>` i `<head>` med klasser som starter på `x-`.
Ikke commit og ikke push.

## Test før du sier deg ferdig

```
node verktoy/test-lab.mjs modules/din-lab.html /tmp/skjermbilder-din-lab
```

Den må skrive `ALT OK`. Se så på skjermbildene (ett per oppgave) og sjekk at alt ser ryddig ut:
ingen tekst som overlapper, ingen tomme bokser, riktige farger.

Flervalg: `python3 verktoy/mcq-hash.py "teksten i riktig alternativ"` gir verdien til `data-c`.
