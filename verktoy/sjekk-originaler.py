"""Sjekker at alle opprinnelige spørsmål i en tilpasset lab står uendret.
   python3 verktoy/sjekk-originaler.py modules/x.html [git-ref]
Sammenligner (spørsmålstekst, data-a, fasit) og flervalg (data-c + alternativer)
med versjonen i git-ref (standard: 49cf27d, før tilpasningene), i samme rekkefølge."""
import re, subprocess, sys
fil = sys.argv[1]; ref = sys.argv[2] if len(sys.argv) > 2 else '49cf27d'
gammel = subprocess.run(['git', 'show', f'{ref}:{fil}'], capture_output=True, text=True, check=True).stdout
ny = open(fil, encoding='utf-8').read()
rad = re.compile(r'data-a="([^"]*)"[^>]*>\s*<span class="ans-q">(.*?)</span>.*?<div class="ah-box sv">(.*?)</div>', re.S)
mcq = re.compile(r'<div class="mcq" data-c="(-?\d+)".*?<div class="mcq-fb">', re.S)
def norm(t): return re.sub(r'\s+', ' ', t).strip()
g = [tuple(map(norm, m)) for m in rad.findall(gammel)]; n = [tuple(map(norm, m)) for m in rad.findall(ny)]
def i_rekkefolge(gamle, nye):
    mangler, pos = [], 0
    for x in gamle:
        if x in nye[pos:]: pos = nye.index(x, pos) + 1
        else: mangler.append(x)
    return mangler
mangler = i_rekkefolge(g, n)
gm = [norm(m.group(0)) for m in mcq.finditer(gammel)]; nm = [norm(m.group(0)) for m in mcq.finditer(ny)]
mmangler = i_rekkefolge(gm, nm)
print(f'{fil}: {len(g)} opprinnelige spørsmål, {len(gm)} flervalg')
for x in mangler: print('  MANGLER/ENDRET:', x[1][:90])
for x in mmangler: print('  FLERVALG ENDRET:', x[:90])
print('OK' if not mangler and not mmangler else 'FEIL'); sys.exit(1 if mangler or mmangler else 0)
