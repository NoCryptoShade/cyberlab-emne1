# Emne 1-sidene, fire filer som virker alene

## Hva som var galt denne gangen

`index.html` kom opp, men `css/style.css` og `js/cyberlab.js` gjorde det ikke.
De to mappene ble ikke med i opplastingen. Derfor sto sida med hvit bakgrunn og
seriffskrift.

Du så likevel modulbånd og leksjonsrader, fordi de stilene ligger i et
`<style>`-felt inne i sjølve HTML-fila. Alt som lå i de eksterne filene, manglet.

## Hva som er endret

Hele CSS-en og hele JavaScripten er nå limt inn i hver eneste side.

Det finnes ingen `css`-mappe og ingen `js`-mappe lenger. Det er fire filer, og
hver av dem virker alene. Legger du bare én av dem i en tom mappe, fungerer den
fullt ut.

## Slik legger du det ut

Fire filer, rett i rota av repoet:

```
index.html
leksjon-01.html
leksjon-05.html
leksjon-06.html
```

Slett alt annet som ligger der fra før, også `modules`, `css` og `js`.

Adressen blir `https://nocryptoshade.github.io/EasyPeasyEmne1/` uten filnavn.

Filene er større nå, fra 74 til 131 kB. Det er prisen for at ingenting kan mangle.

## Verifisert

En av sidene ble lagt helt alene i en tom mappe og servert derfra. Resultat:

- Mørk bakgrunn og riktig skrift, altså full styling
- Kort, modulbånd og merker stilet som på resten av CyberLab
- Delene åpner på klikk
- Svarfelt godtar riktig svar, og fremdriften teller opp
- Ingen 404 på noen ressurs, ingen JavaScript-feil

Og på alle tre leksjonene samlet:

- Alle 102 svarfelt fylt ut med fasit og godkjent
- Alle 16 flervalg klikket og godkjent
- Fremdriften når 100 prosent på alle tre

Det eneste som fortsatt hentes utenfra, er skrifttypen fra Google Fonts. Skulle
den være utilgjengelig, bytter nettleseren til systemskrift. Farger, layout og
funksjon står uansett.

## Repo-navnet

Repoet heter fortsatt **EasyPeasyEmne1**, og navnet står i adressefeltet hele
tiden hun bruker sida. Selve sidene sier ingenting om at dette er et eget spor.
Adressen gjør det.

Settings, Rename. `emne1`, `gcs101` eller `cyberlab-emne1` gjør samme nytte.
Ingenting i filene trenger å endres.

## Bygge på nytt

Mappa `kilde/` har generatoren.

```
python3 build.py --standalone --verify    fire selvstendige filer
python3 build.py --verify                 modules/ i CyberLab-repoet
```

`--standalone` limer inn CSS og JS. Den henter dem fra stien i `KILDE` øverst i
`build.py`, som må peke på en kopi av CyberLab.

Kontrollen ser bort fra det innlimte når den teller og sjekker, siden `cyberlab.js`
har markup-eksempler i kommentarene sine.

Rediger aldri HTML-filene. All tekst ligger i `innhold/lXX.py`.
