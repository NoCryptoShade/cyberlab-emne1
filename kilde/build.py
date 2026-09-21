# -*- coding: utf-8 -*-
"""
Generator for Emne 1-leksjonene i CyberLab.

En side per leksjon, L01 til L26, pluss en oversikt paa modules/leksjoner.html.
Sidene bruker de samme komponentene som resten av CyberLab: samme meny, samme
hero, samme fremdriftslinje, samme filterrad og de samme modulbaandene som
emne1.html. Forskjellen ligger i hvor smaa stegene er, ikke i hvordan det ser ut.

Kjoer:
    python3 build.py            bygger leksjonene som finnes
    python3 build.py --verify   bygger og kjoerer kontrollene

Rediger aldri HTML-filene. All tekst ligger i innhold/lXX.py.
"""

import html
import re
import sys
import unicodedata
from pathlib import Path

from innhold import LEKSJONER, MODULER, PLAN

VERSJON = 1
ROT = Path(__file__).parent

# To maater aa publisere paa.
#   vanlig:     filene legges i modules/ i CyberLab-repoet, og css og js hentes
#               fra ../css og ../js slik alle andre modulsider gjoer
#   standalone: filene legges i rota av sitt eget repo, med egne kopier av css
#               og js, og menyen peker paa den ekte CyberLab-sida
STANDALONE = "--standalone" in sys.argv
UT = ROT / ("standalone" if STANDALONE else "modules")
OVERSIKT = "index.html" if STANDALONE else "leksjoner.html"
OPP = "" if STANDALONE else "../"
CYBERLAB = "https://cybersikkerhet-gokstad.github.io/CyberLab/"
KILDE = Path("/home/claude/site")   # kopi av CyberLab, kilde for css og js


def _les(sti: Path) -> str:
    if not sti.exists():
        raise SystemExit(f"finner ikke {sti}. Pek KILDE mot en kopi av CyberLab.")
    return sti.read_text(encoding="utf-8")


def _ressurser() -> tuple:
    """CSS og JS, enten som lenker eller limt rett inn i sida.

    Standalone-sidene limer alt inn. Da finnes det ingen css- eller js-mappe
    som kan bli glemt ved opplasting, og hver side er en fil som virker alene.
    """
    v = f"?v={VERSJON}"
    if not STANDALONE:
        return (f'<link rel="stylesheet" href="{OPP}css/style.css{v}">\n'
                f'<link rel="stylesheet" href="{OPP}css/lab-shared.css{v}">',
                f'<script src="{OPP}js/cyberlab.js{v}"></script>')
    css = _les(KILDE / "css" / "style.css") + "\n" + _les(KILDE / "css" / "lab-shared.css")
    js = _les(KILDE / "js" / "cyberlab.js")
    return ("<style>\n" + css + "\n</style>", "<script>\n" + js + "\n</script>")


# ------------------------------------------------------------------ hashing
def _i32(n: int) -> int:
    n &= 0xFFFFFFFF
    return n - 0x100000000 if n >= 0x80000000 else n


def cl_hash(s: str) -> int:
    """Identisk med clHash() i js/cyberlab.js."""
    s = re.sub(r"\s+", " ", str(s).strip().lower())
    h = 5381
    for ch in s:
        h = _i32(_i32(h << 5) + h + ord(ch))
    return h


def _selftest() -> None:
    kjent = {"7": 177628, "1": 177622, "header": 30546094,
             "nei": 193500225, "vlan": 2090835094, "2000": 2088324359}
    for tekst, fasit in kjent.items():
        if cl_hash(tekst) != fasit:
            raise SystemExit(f"clHash feiler paa {tekst!r}")


CSS_TAG, JS_TAG = _ressurser()


# ------------------------------------------------------------------ biter
def esc(t: str) -> str:
    return html.escape(str(t), quote=True)


def svarrad(o: dict) -> str:
    data = ",".join(str(cl_hash(a)) for a in o["a"])
    return (
        f'<div class="ans-row" data-a="{data}">'
        f'<span class="ans-q">{esc(o["q"])}</span>'
        f'<input class="ans-in" placeholder="{esc(o["ph"])}" autocomplete="off">'
        f'<span class="ans-mark"></span>'
        f'<div class="ah">'
        f'<button class="ah-btn" onclick="aTip(this)">&#9654; Hint</button>'
        f'<div class="ah-box tip">{esc(o["hint"])}</div>'
        f'<button class="ah-btn sv" onclick="aTip(this)">&#9654; Svar</button>'
        f'<div class="ah-box sv">{esc(o["sv"])}</div>'
        f'</div></div>'
    )


def flervalg(o: dict) -> str:
    if o["riktig"] not in o["alt"]:
        raise SystemExit(f'flervalg: riktig alternativ mangler i lista: {o["riktig"]!r}')
    alt = "".join(f'<button class="mcq-opt">{esc(a)}</button>' for a in o["alt"])
    return (
        f'<div class="mcq" data-c="{cl_hash(o["riktig"])}"'
        f' data-ok="{esc(o["ok"])}" data-no="{esc(o["nei"])}">'
        f'<div class="mcq-q">{esc(o["mcq"])}</div>{alt}<div class="mcq-fb"></div></div>'
    )


def sporsmal(o: dict) -> str:
    return flervalg(o) if "mcq" in o else svarrad(o)


def terminal(term_id: str, tittel: str) -> str:
    return (
        f'<div class="term-block"><div class="fake-browser" style="flex-direction:column">'
        f'<div class="fake-bar"><div class="fake-dots">'
        f'<div class="fdot fdot-r"></div><div class="fdot fdot-y"></div>'
        f'<div class="fdot fdot-g"></div></div>'
        f'<div class="fake-url">{esc(tittel)}</div></div>'
        f'<div class="lab-term" style="flex:1">'
        f'<div class="lab-term-body" id="{term_id}">'
        f'<div class="lt-info">Skriv help og trykk enter.</div></div>'
        f'<div class="lab-term-input"><span class="lt-ps1">student@storgata12:~$&nbsp;</span>'
        f'<input class="lt-in" id="{term_id}-in" placeholder="skriv en kommando" autocomplete="off">'
        f'</div></div></div></div>'
    )


def _kort(kort_id, nr, tittel, niva, innhold: list) -> str:
    """Ett kort, dimensjonert for aa faa plass i ett skjermbilde.

    Kort uten spoersmaal faar ingen id, slik at de ikke telles i fremdriften.
    Uten det ville et kort som aldri kan fullfoeres gjort 100 prosent
    uoppnaaelig for hele leksjonen.
    """
    har_sporsmal = any('class="ans-row"' in x or 'class="mcq"' in x for x in innhold)
    idattr = f' id="{kort_id}"' if har_sporsmal else ""
    merke = {"easy": "Lett", "medium": "Middels", "hard": "Vanskelig"}[niva]
    p = [f'    <div class="lab-card"{idattr} data-level="{niva}">',
         f'      <div class="lab-header" onclick="toggleTask(this)">',
         f'        <span class="lab-num">{nr:02d}</span>',
         f'        <span class="lab-title">{tittel}</span>',
         f'        <div class="lab-meta"><span class="badge badge-{niva}">{merke}</span>'
         f'<span class="lab-chev">&#9654;</span></div>',
         f'      </div>',
         f'      <div class="lab-body"><div class="lab-flow">']
    p += ["        " + x for x in innhold]
    p += ['      </div></div>', '    </div>']
    return "\n".join(p)


def _blokk_bilde(k) -> str:
    bilde = "".join(f"<p>{x}</p>" for x in k["bilde"])
    return (f'<div class="theory-block"><div class="theory-title">{k["bilde_tittel"]}</div>'
            f'<div class="theory-text">{bilde}</div></div>')


def _blokk_ord(k) -> str:
    ord_ = "".join(f"<p>{x}</p>" for x in k["ord"])
    return (f'<div class="theory-block why">'
            f'<div class="theory-title">Ordet du skal kunne</div>'
            f'<div class="theory-text">{ord_}</div></div>')


def _korttittel(k) -> str:
    """Tittelen paa det foerste kortet: bildeoverskriften uten emojien.

    Baandet over viser allerede begrepsnavnet, saa kortet gjentar det ikke.
    """
    t = k["bilde_tittel"]
    while t and not (t[0].isalpha() or t[0].isdigit()):
        t = t[1:]
    return t.strip() or k["tittel"]


def tema_html(k: dict, i: int, farge: str, nr):
    """Ett begrep: et modulbaand som overskrift, og stegene som egne kort.

    Delingen foelger hva hvert spoersmaal trenger for aa kunne besvares.
    Sjekken trenger bildet. Regn selv trenger regneeksempelet. Din tur trenger
    hele begrepet. Ingen maa bla ut av kortet for aa finne det hun trenger.
    """
    kort, terminaler = [], []

    if k.get("term"):
        # Terminalen maa staa i samme kort som spoersmaalet den besvarer.
        kort.append(_kort(f'{k["id"]}a', next(nr), _korttittel(k), "easy",
                          [_blokk_bilde(k), _blokk_ord(k)]))
        for n, o in enumerate(k.get("din_tur", []), 1):
            tid = f'{k["term"]["id"]}-{n}'
            terminaler.append((tid, k["term"]["svar"]))
            kort.append(_kort(
                f'{k["id"]}{chr(97 + n)}', next(nr), f"Kjør det selv, {n}", "easy",
                [terminal(tid, k["term"]["tittel"]),
                 '<div class="ans-block"><div class="obj-title">Din tur</div>'
                 + sporsmal(o) + '</div>']))
    else:
        kort.append(_kort(f'{k["id"]}a', next(nr), _korttittel(k), "easy",
                          [_blokk_bilde(k), _blokk_ord(k)]))

        if k.get("sjekk"):
            kort.append(_kort(f'{k["id"]}b', next(nr), "Sjekk", "easy",
                              ['<div class="ans-block">'
                               '<div class="obj-title">Ett sp&oslash;rsm&aring;l f&oslash;r du g&aring;r videre</div>'
                               + svarrad(k["sjekk"]) + '</div>']))

        if k.get("vist"):
            steg = "".join(f"<li>{s}</li>" for s in k["vist"])
            kort.append(_kort(f'{k["id"]}c', next(nr), "Regneeksempel", "easy",
                              [f'<div class="worked"><div class="worked-t">Regneeksempel</div>'
                               f'<div class="worked-b"><p>{k["vist_intro"]}</p>'
                               f'<ol class="wsteps">{steg}</ol></div></div>']))

        if k.get("prov"):
            kort.append(_kort(f'{k["id"]}d', next(nr), "Regn selv", "easy",
                              ['<div class="ans-block">'
                               '<div class="obj-title">Samme regel, nye tall</div>'
                               + "".join(sporsmal(o) for o in k["prov"]) + '</div>']))

        if k.get("din_tur"):
            kort.append(_kort(f'{k["id"]}e', next(nr), "Din tur", "medium",
                              ['<div class="ans-block"><div class="obj-title">Din tur</div>'
                               + "".join(sporsmal(o) for o in k["din_tur"]) + '</div>']))

        if k.get("sikkerhet"):
            kort.append(_kort(f'{k["id"]}f', next(nr), "Sikkerhetsperspektiv", "easy",
                              ['<div class="theory-block">'
                               '<div class="theory-title">\U0001F512 Hvorfor dette betyr noe</div>'
                               f'<div class="theory-text"><p>{k["sikkerhet"]}</p></div></div>']))

    ut = [f'  <div class="mod-band {farge} del-band" onclick="visDel(this)">',
          f'    <div class="mod-band-l"><span class="mod-tag">Del {i}</span>'
          f'<span class="mod-name">{k["tittel"]}</span></div>',
          f'    <span class="mod-weeks del-tell"></span>',
          f'  </div>',
          f'  <div class="del-gruppe">']
    ut += kort
    ut.append('  </div>')
    return "\n".join(ut), terminaler


# ------------------------------------------------------------------ sider
STIL = """<style>
/* Hentet ordrett fra emne1.html, slik at modulb&aring;nd og leksjonsrader
   ser ut som p&aring; resten av sida. */
.mod-band{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;
  padding:13px 20px;border-radius:10px;margin:32px 0 14px;border:1px solid var(--border);background:var(--bg2)}
.mod-band.green{border-left:3px solid var(--green)}
.mod-band.amber{border-left:3px solid var(--amber)}
.mod-band.blue{border-left:3px solid var(--blue)}
.mod-band.purple{border-left:3px solid var(--purple)}
.mod-band-l{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.mod-tag{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.08em;color:var(--text3);text-transform:uppercase}
.mod-name{font-size:15px;font-weight:700}
.mod-weeks{font-family:var(--mono);font-size:11px;color:var(--text3)}
.week{display:flex;gap:18px;padding:4px 0 4px 6px}
.week-no{font-family:var(--mono);font-size:11px;color:var(--text3);min-width:56px;padding-top:15px;flex-shrink:0}
.week-body{flex:1;min-width:0}
.lesson{display:flex;align-items:flex-start;gap:14px;padding:13px 16px;background:var(--bg2);
  border:1px solid var(--border);border-radius:9px;margin-bottom:8px;transition:border-color .18s}
.lesson:hover{border-color:var(--border2)}
.l-no{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--green);min-width:26px;padding-top:2px}
.l-main{flex:1;min-width:0}
.l-title{font-size:14px;font-weight:600;margin-bottom:3px}
.l-desc{font-size:12.5px;color:var(--text3);line-height:1.6}
.l-links{display:flex;gap:6px;flex-shrink:0;flex-wrap:wrap}
.lchip{font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.04em;padding:4px 10px;
  border-radius:5px;text-decoration:none;border:1px solid;white-space:nowrap}
.lchip.lab{color:var(--green);border-color:rgba(0,229,160,.35);background:rgba(0,229,160,.08)}
.lchip.lab:hover{background:rgba(0,229,160,.16)}
.lchip.quiz{color:var(--blue);border-color:rgba(75,142,255,.35);background:rgba(75,142,255,.08)}
.lchip.quiz:hover{background:rgba(75,142,255,.16)}
.lchip.soon{color:var(--text3);border-color:var(--border2);background:transparent}
@media(max-width:720px){.week{flex-direction:column;gap:4px}.week-no{padding-top:0}
  .lesson{flex-wrap:wrap}.l-links{width:100%;padding-left:40px}}
.modline{font-size:12.5px;color:var(--text3);margin:-6px 0 12px 6px;max-width:64ch}
.lchip.bok{color:var(--amber);border-color:rgba(255,181,71,.35);background:rgba(255,181,71,.08)}
.lchip.bok:hover{background:rgba(255,181,71,.16)}
.l-no{color:var(--blue)}
/* Begrepene vises som modulb&aring;nd inne i labben. Ett klikk &aring;pner stegene. */
.tasks .mod-band{margin:14px 0 0;cursor:pointer;user-select:none}
.tasks .mod-band:hover{border-color:var(--border2)}
.del-tell:after{content:'▸';display:inline-block;margin-left:10px;transition:transform .2s}
.tasks .mod-band.on .del-tell:after{transform:rotate(90deg)}
.del-gruppe{display:none;padding:8px 0 4px}
.del-gruppe.vis{display:block}
/* Tettere kort, slik at hvert enkelt steg f&aring;r plass i ett skjermbilde. */
.lab-flow .level-badge{display:none}
.tasks .lab-header{padding-top:11px;padding-bottom:11px}
.tasks .lab-card.open .lab-body{padding-top:14px;padding-bottom:14px}
.lab-flow .ans-row{padding-top:7px;padding-bottom:7px}
.lab-flow .theory-block{padding:11px 14px}
.lab-flow .worked{padding:11px 14px}
.term-block .fake-browser{height:auto;min-height:0}
.term-block .lab-term{flex:none}
.term-block .lab-term-body{max-height:170px;min-height:140px;overflow-y:auto}
</style>"""

SKRIPT = """<script>
function visDel(el){
  el.classList.toggle('on');
  el.nextElementSibling.classList.toggle('vis');
  tellDel();
}
function tellDel(){
  document.querySelectorAll('.del-gruppe').forEach(function(g){
    var alle = g.querySelectorAll('.lab-card[id]').length;
    var gjort = g.querySelectorAll('.lab-card[id].done').length;
    var t = g.previousElementSibling.querySelector('.del-tell');
    if (t) t.textContent = gjort + ' / ' + alle;
  });
}
document.addEventListener('DOMContentLoaded', tellDel);
document.addEventListener('input', tellDel);
document.addEventListener('click', tellDel);
</script>"""


def hode(tittel: str, aktiv: str = "Labber") -> str:
    v = f"?v={VERSJON}"
    base = CYBERLAB if STANDALONE else "../"
    lenker = [(base + "index.html", "Hjem"), (base + "emne1.html", "Emne 1"),
              (base + "emne3.html", "Emne 3"), (base + "labber.html", "Labber")]
    nav = "\n".join(
        f'    <a href="{h}" class="nav-link{" on" if n == aktiv else ""}">{n}</a>'
        for h, n in lenker)
    return f"""<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{tittel} &middot; CyberLab</title>
{CSS_TAG}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&amp;family=Bricolage+Grotesque:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
{STIL}
</head>
<body class="page">
<nav class="nav">
  <div class="nav-logo"><span class="bracket">[</span>CyberLab<span class="bracket">]</span></div>
  <div class="nav-links">
{nav}
    <a href="https://tk1104.timoamling.com/" target="_blank" rel="noopener" class="nav-link">Self check &nearr;</a>
  </div>
</nav>
"""


FOT = """<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <span>CyberLab &mdash; Fagskole Informasjonssikkerhet</span>
      <span>Gratis &amp; &aring;pen kildekode</span>
    </div>
  </div>
</footer>
"""


def leksjon_html(L: dict, p: dict, forrige, neste) -> str:
    v = f"?v={VERSJON}"
    farge = MODULER[p["modul"]]["farge"]
    nr = iter(range(1, 999))
    biter, terminaler = [], []
    for i, k in enumerate(L["kort"], 1):
        h, t = tema_html(k, i, farge, nr)
        biter.append(h)
        terminaler += t
    oppsum = "".join(f"<li>{x}</li>" for x in L["oppsummering"])

    nav = []
    if forrige:
        nav.append(f'<a href="{forrige["fil"]}" class="btn btn-ghost">'
                   f'&larr; {forrige["num"]} {forrige["tittel"]}</a>')
    nav.append(f'<a href="{OVERSIKT}" class="btn btn-ghost">Alle leksjoner</a>')
    if neste:
        nav.append(f'<a href="{neste["fil"]}" class="btn btn-success">'
                   f'{neste["num"]} {neste["tittel"]} &rarr;</a>')

    term_js = ""
    if terminaler:
        kall = "".join(f"\n  termInit('{t}', '{t}-in', SVAR);" for t, _ in terminaler)
        term_js = (f"<script>\nconst SVAR = {terminaler[0][1]};\n"
                   f"document.addEventListener('DOMContentLoaded', () => {{{kall}\n}});\n"
                   f"</script>\n")

    return f"""{hode(L["tittel"])}
<div class="container-sm page" style="padding-top:40px;padding-bottom:80px">
  <a href="{OVERSIKT}" class="back-link">&larr; Tilbake</a>
  <div class="mod-hero">
    <div class="section-eyebrow">Emne 1 &middot; Leksjon {int(p["num"][1:])}</div>
    <div class="section-title">{L["tittel"]}</div>
    <p class="section-desc">{p["beskrivelse"]}</p>
  </div>

  <div class="info-box"><strong>Krav: ingenting.</strong>
  Alt i denne labben kj&oslash;rer i nettleseren. Ingen virtuell maskin og ingen innlogging.
  Svarene lagres lokalt, s&aring; du kan ta en del av gangen og fortsette n&aring;r du vil.</div>

  <div class="progress-wrap">
    <div class="progress-label"><span>Fremdrift</span>
    <span id="progressLabel">0 / 0 fullf&oslash;rt</span></div>
    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
  </div>

  <div class="filter-row">
    <button class="filter-pill active-all" onclick="setFilter('all',this)">Alle</button>
    <button class="filter-pill" onclick="setFilter('easy',this)">Lett</button>
    <button class="filter-pill" onclick="setFilter('medium',this)">Middels</button>
    <button class="filter-pill" onclick="setFilter('hard',this)">Vanskelig</button>
  </div>

  <div class="tasks">
{chr(10).join(biter)}
  </div>

  <div class="recap-card" style="margin-top:36px">
    <h3>Kort oppsummert</h3>
    <ol>{oppsum}</ol>
  </div>

  <div style="margin-top:36px;display:flex;gap:12px;flex-wrap:wrap">{"".join(nav)}</div>
</div>

{FOT}{JS_TAG}
{SKRIPT}
{term_js}</body>
</html>
"""


def oversikt_html(bygd: dict) -> str:
    v = f"?v={VERSJON}"
    rader, forrige_modul = [], None
    for p in PLAN:
        if p["modul"] != forrige_modul:
            forrige_modul = p["modul"]
            m = MODULER[forrige_modul]
            rader.append(
                f'  <div class="mod-band {m["farge"]}">\n'
                f'    <div class="mod-band-l"><span class="mod-tag">{m["tag"]}</span>'
                f'<span class="mod-name">{m["navn"]}</span></div>\n'
                f'    <span class="mod-weeks">{m["uker"]}</span>\n  </div>')
        if p["num"] in bygd:
            chip = f'<a class="lchip lab" href="{p["fil"]}">Lab</a>'
        else:
            chip = '<span class="lchip soon">Kommer</span>'
        rader.append(
            f'  <div class="lesson">\n'
            f'    <span class="l-no">{p["num"]}</span>\n'
            f'    <div class="l-main"><div class="l-title">{p["tittel"]}</div>'
            f'<div class="l-desc">{p["beskrivelse"]}</div></div>\n'
            f'    <div class="l-links">{chip}</div>\n  </div>')

    return f"""{hode("Emne 1", aktiv="Emne 1")}
<div class="container-sm page" style="padding-top:40px;padding-bottom:80px">
  <div class="mod-hero">
    <div class="section-eyebrow">Emne 1</div>
    <div class="section-title">Grunnleggende cybersikkerhet</div>
    <p class="section-desc">26 leksjoner over 13 uker, to i uka. Grunnlaget, nettverk, Linux og
    skripting. Du trenger ingen forkunnskaper.</p>
  </div>

  <div class="intro-card">
    <div class="lect">Slik bruker du denne siden</div>
    <h3>Finn uka di</h3>
    <p>Hver leksjon st&aring;r med nummer og en linje om hva den handler om. St&aring;r det
    <strong>Lab</strong>, finnes det en praktisk &oslash;ving du kan gj&oslash;re n&aring;r som helst, ogs&aring;
    etter timen. St&aring;r det <strong>Kommer</strong>, er labben ikke bygget enn&aring;.</p>
    <p>Inne i en lab er stoffet delt i deler. Klikk p&aring; en del for &aring; &aring;pne den, og ta en
    boks av gangen. Alt kj&oslash;rer i nettleseren, og svarene lagres lokalt.</p>
  </div>

{chr(10).join(rader)}

  <div class="recap-card" style="margin-top:36px">
    <h3>Fire sp&oslash;rsm&aring;l som g&aring;r igjen hele emnet</h3>
    <ol>
      <li><strong>Hva skal beskyttes?</strong> Verdier f&oslash;r tiltak. Du kan ikke sikre noe du ikke har funnet.</li>
      <li><strong>Hvem f&aring;r gj&oslash;re hva?</strong> Rettigheter i Linux, tilgang i nettverket, tillatelse i en test.</li>
      <li><strong>Hvor kommer dataene fra?</strong> Alt som kommer utenfra m&aring; kontrolleres f&oslash;r det brukes.</li>
      <li><strong>Kan du svare med en kommando?</strong> Fra uke 6 skal sp&oslash;rsm&aring;l ende i noe du faktisk kj&oslash;rer.</li>
    </ol>
  </div>
</div>

{FOT}{JS_TAG}
</body>
</html>
"""


# ------------------------------------------------------------------ kontroll
KJENTE_FUNKS = {"toggleTask", "aTip", "toggleHint", "toggleSolution",
                "setFilter", "markTaskDone", "termInit", "quiz", "visDel"}


def kontroller(navn: str, doc: str, L=None) -> list:
    feil = []
    if doc.count("<div") != doc.count("</div>"):
        feil.append(f"{navn}: div-ubalanse {doc.count('<div')}/{doc.count('</div>')}")
    for fn in set(re.findall(r'onclick="(\w+)\(', doc)):
        if fn not in KJENTE_FUNKS:
            feil.append(f"{navn}: ukjent funksjon i onclick, {fn}")
    ids = re.findall(r'\sid="([^"]+)"', doc)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        feil.append(f"{navn}: dupliserte id-er {sorted(dup)}")
    for q in re.findall(r'<span class="ans-q">(.*?)</span>', doc):
        if "<" in q or ">" in q:
            feil.append(f"{navn}: raa tagg i spoersmaal, {q[:50]}")
    for d in re.findall(r'data-a="([^"]*)"', doc):
        for del_ in d.split(","):
            if not re.fullmatch(r"-?\d+", del_):
                feil.append(f"{navn}: ugyldig data-a, {d}")
    for ch in ("–", "—"):
        if ch in doc:
            feil.append(f"{navn}: {unicodedata.name(ch)} i teksten")
    if not navn.isascii():
        feil.append(f"{navn}: filnavnet er ikke ASCII")

    if L:
        for k in L["kort"]:
            prosa = " ".join(k["bilde"] + k["ord"] + k.get("vist", []) +
                             [k.get("vist_intro", ""), k.get("sikkerhet", "")]).lower()
            for o in k.get("din_tur", []):
                if "mcq" in o or "/" in o.get("ph", ""):
                    continue
                sv = str(o["sv"]).lower()
                if len(sv) > 1 and re.search(r"(?<![\w.])" + re.escape(sv) + r"(?![\w.])", prosa):
                    feil.append(f'MERK {k["id"]}: "{o["sv"]}" staar ordrett i teksten over')
    return feil


def uten_ressurser(doc: str) -> str:
    """Sida uten den innlimte CSS-en og JS-en.

    Kontrollene og tellingene skal bare gjelde det generatoren selv skriver.
    cyberlab.js har markup-eksempler i kommentarene sine, og bade css og js
    inneholder tankestrek. Uten dette fratrekket ville kontrollen telt dem med.
    """
    return doc.replace(CSS_TAG, "").replace(JS_TAG, "")


def main() -> int:
    _selftest()
    UT.mkdir(parents=True, exist_ok=True)
    ferdig = [p for p in PLAN if p["num"] in LEKSJONER]

    alle_feil, bygd, felt = [], {}, 0
    for i, p in enumerate(ferdig):
        L = LEKSJONER[p["num"]]
        doc = leksjon_html(L, p, ferdig[i - 1] if i else None,
                           ferdig[i + 1] if i + 1 < len(ferdig) else None)
        (UT / p["fil"]).write_text(doc, encoding="utf-8")
        egen = uten_ressurser(doc)
        n = egen.count('class="ans-row"') + egen.count('class="mcq"')
        felt += n
        bygd[p["num"]] = n
        alle_feil += kontroller(p["fil"], egen, L)
        n_kort = egen.count('class="lab-card"')
        print("  %-18s %s %s   %d deler, %d kort, %d sp."
              % (p["fil"], p["num"], p["tittel"], len(L["kort"]), n_kort, n))

    idx = oversikt_html(bygd)
    (UT / OVERSIKT).write_text(idx, encoding="utf-8")
    alle_feil += kontroller(OVERSIKT, uten_ressurser(idx))

    print(f"Bygget {len(ferdig)} av {len(PLAN)} leksjoner, {felt} spoersmaal totalt")
    if "--verify" in sys.argv:
        merk = [f for f in alle_feil if f.startswith("MERK")]
        feil = [f for f in alle_feil if not f.startswith("MERK")]
        for m in merk:
            print(f"  {m}")
        for f in feil:
            print(f"  FEIL  {f}")
        if not feil:
            print("Strukturkontroll: ingen feil.")
        return 1 if feil else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
