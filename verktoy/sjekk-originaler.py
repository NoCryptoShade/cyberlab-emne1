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
it = iter(n); mangler = [x for x in g if not any(x == y for y in it)]
gm = [norm(m.group(0)) for m in mcq.finditer(gammel)]; nm = [norm(m.group(0)) for m in mcq.finditer(ny)]
it2 = iter(nm); mmangler = [x for x in gm if not any(x == y for y in it2)]
print(f'{fil}: {len(g)} opprinnelige spørsmål, {len(gm)} flervalg')
for x in mangler: print('  MANGLER/ENDRET:', x[1][:90])
for x in mmangler: print('  FLERVALG ENDRET:', x[:90])
print('OK' if not mangler and not mmangler else 'FEIL'); sys.exit(1 if mangler or mmangler else 0)
