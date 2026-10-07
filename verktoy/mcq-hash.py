"""Regner ut data-c for flervalg (.mcq): clHash() av teksten i riktig alternativ.
   python3 verktoy/mcq-hash.py "Som mange små pakker"
Samme algoritme som clHash() i js/cyberlab.js."""
import re, sys
def cl_hash(t):
    t = re.sub(r'\s+', ' ', t.strip().lower()); h = 5381
    for i in range(0, len(b := t.encode('utf-16-le')), 2):
        h = ((h << 5) + h + int.from_bytes(b[i:i+2], 'little')) & 0xFFFFFFFF
    return h - (1 << 32) if h >= 1 << 31 else h
for a in sys.argv[1:]: print(cl_hash(a), a)
