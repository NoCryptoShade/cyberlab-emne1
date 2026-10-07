/* cyberlab.js — shared utilities */

/* ── Auto-patch: kun aktiv på modul-sider (modules/) ── */
document.addEventListener('DOMContentLoaded', () => {
  const isModulePage = window.location.pathname.includes('/modules/');

  if (isModulePage) {
    // 1. Tilbake-lenke: alltid til labber.html, alltid teksten "← Tilbake"
    document.querySelectorAll('a.back-link').forEach(el => {
      el.textContent = '← Tilbake';
      if (el.href.includes('index.html')) {
        el.href = el.href.replace('index.html', 'labber.html');
      }
    });

    // 2. Bunn-nav "← Hjem" → "← Labber"
    document.querySelectorAll('a.btn.btn-ghost').forEach(el => {
      if (el.textContent.trim() === '← Hjem') {
        el.textContent = '← Labber';
        el.href = el.href.replace('index.html', 'labber.html');
      }
      if (el.textContent.includes('Tilbake til oversikten')) {
        el.textContent = '← Labber';
        el.href = el.href.replace('index.html', 'labber.html');
      }
    });
    document.querySelectorAll('a.btn.btn-success').forEach(el => {
      if (el.textContent.includes('Tilbake til oversikten')) {
        el.className = 'btn btn-ghost';
        el.textContent = '← Labber';
        el.href = el.href.replace('index.html', 'labber.html');
      }
    });
  }

  // 3. Filter-pill: "Hard" → "Vanskelig" (alle sider)
  document.querySelectorAll('.filter-pill').forEach(el => {
    if (el.textContent.trim() === 'Hard') el.textContent = 'Vanskelig';
  });

  // 4. Badges: "Hard" → "Vanskelig" (alle sider)
  document.querySelectorAll('.badge-hard').forEach(el => {
    el.textContent = el.textContent
      .replace(/: Hard$/, ': Vanskelig')
      .replace(/^Hard$/, 'Vanskelig');
  });

  loadDoneStates();
});

/* ── Task accordion ─────────────────────────────────────── */
function toggleTask(el) {
  const card = el.closest('.lab-card') || el.closest('.task-card');
  if (!card) return;
  card.classList.toggle('open');
}

/* ── Hint / solution toggles ────────────────────────────── */
function toggleHint(btn) {
  const box = btn.nextElementSibling;
  const open = box.classList.toggle('show');
  btn.classList.toggle('on', open);
  btn.textContent = open ? '▼ Skjul hint' : '▶ Hint';
}

function toggleSolution(btn) {
  const box = btn.nextElementSibling;
  const open = box.classList.toggle('show');
  btn.classList.toggle('on', open);
  btn.textContent = open ? '▼ Skjul løsning' : '▶ Vis løsning';
}

/* ── Progress tracking (localStorage) ───────────────────── */
function getProgress() {
  try { return JSON.parse(localStorage.getItem('cl_progress') || '{}'); } catch { return {}; }
}
function saveProgress(data) {
  try { localStorage.setItem('cl_progress', JSON.stringify(data)); } catch {}
}

function markTaskDone(taskId) {
  const p = getProgress();
  p[taskId] = true;
  saveProgress(p);
  const card = document.getElementById(taskId);
  if (card) card.classList.add('done');
  const banner = document.getElementById('done-' + taskId);
  if (banner) banner.classList.add('show');
  updateModuleProgress();
}

function loadDoneStates() {
  const p = getProgress();
  Object.keys(p).forEach(id => {
    const card = document.getElementById(id);
    if (card) card.classList.add('done');
    const banner = document.getElementById('done-' + id);
    if (banner) banner.classList.add('show');
  });
  updateModuleProgress();
}

function updateModuleProgress() {
  const allCards = document.querySelectorAll('.lab-card[id], .task-card[id]');
  const all  = allCards.length;
  const done = document.querySelectorAll('.lab-card[id].done, .task-card[id].done').length;
  const fill  = document.getElementById('progressFill');
  const label = document.getElementById('progressLabel');
  if (fill)  fill.style.width = all ? (done / all * 100) + '%' : '0%';
  if (label) label.textContent = `${done} / ${all} fullført`;
}

/* ── Difficulty filter ───────────────────────────────────── */
function setFilter(level, btn) {
  document.querySelectorAll('.filter-pill').forEach(p => p.className = 'filter-pill');
  btn.classList.add(level === 'all' ? 'active-all' : 'active-' + level);
  document.querySelectorAll('.lab-card, .task-card').forEach(card => {
    card.style.display = (level === 'all' || card.dataset.level === level) ? '' : 'none';
  });
}

/* ── Terminal ── uses lt-* classes ─────────────────────── */
function termRun(bodyId, cmd, responses) {
  const body = document.getElementById(bodyId);
  if (!body) return;
  const add = (text, cls) => {
    const d = document.createElement('div');
    d.className = cls;
    d.textContent = text;
    body.appendChild(d);
  };
  add('$ ' + cmd, 'lt-prompt');
  if (!cmd) { body.scrollTop = body.scrollHeight; return; }
  if (cmd.toLowerCase() === 'clear') { body.innerHTML = ''; return; }

  const key  = cmd.toLowerCase();
  const resp = responses[key] || responses[key.split(' ')[0]];
  if (resp) {
    resp.forEach(l => {
      const cls = l.t === 'info' ? 'lt-info'
                : l.t === 'err'  ? 'lt-err'
                : l.t === 'lt-err' ? 'lt-err'
                : 'lt-out';
      add(l.v, cls);
    });
  } else {
    add(`bash: ${cmd.split(' ')[0]}: command not found  (skriv 'help')`, 'lt-err');
  }
  body.scrollTop = body.scrollHeight;
}

function termInit(bodyId, inputId, responses) {
  const input = document.getElementById(inputId);
  if (!input) return;
  input.addEventListener('keydown', e => {
    if (e.key !== 'Enter') return;
    const cmd = input.value.trim();
    input.value = '';
    termRun(bodyId, cmd, responses);
  });
}

/* ── Quiz ────────────────────────────────────────────────── */
function quiz(el, correct) {
  const group = el.closest('.quiz-group');
  if (!group) return;
  group.querySelectorAll('.quiz-opt').forEach(o => {
    o.style.pointerEvents = 'none';
    if (o.dataset.correct === 'true' && !correct) o.classList.add('reveal');
  });
  el.classList.add(correct ? 'correct' : 'wrong');
}

/* ── SHA-256 hash helper ─────────────────────────────────── */
async function sha256(str) {
  try {
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
  } catch {
    return '(crypto.subtle ikke tilgjengelig — bruk GitHub Pages)';
  }
}

/* ── Answer boxes ── TryHackMe-style typed answers ───────
   Markup:
     <div class="ans-row" data-a="1234567">
       <span class="ans-q">Hvilken statuskode kom tilbake?</span>
       <input class="ans-in" placeholder="tre siffer">
       <span class="ans-mark"></span>
     </div>
   data-a holds one or more accepted answers as hashes, comma
   separated. Generate them with clHash() in the console.
   A task card is marked done when every ans-row inside it is
   correct, so it feeds the existing progress bar for free.
──────────────────────────────────────────────────────── */

function clHash(s){
  let h = 5381;
  s = String(s).trim().toLowerCase().replace(/\s+/g,' ');
  for (let i = 0; i < s.length; i++) { h = ((h << 5) + h) + s.charCodeAt(i); h |= 0; }
  return h;
}

function getAnswers(){
  try { return JSON.parse(localStorage.getItem('cl_answers') || '{}'); } catch { return {}; }
}
function saveAnswers(d){
  try { localStorage.setItem('cl_answers', JSON.stringify(d)); } catch {}
}

function answerKey(row){
  const card = row.closest('.lab-card, .task-card');
  const rows = card ? [...card.querySelectorAll('.ans-row')] : [row];
  return (card && card.id ? card.id : 'x') + ':' + rows.indexOf(row);
}

/* ── Svarsjekk ── romslig, ikke pirkete ────────────────────────
   Tidligere ble svaret hashet og matchet eksakt. Da var «254» riktig
   og «254 adresser» feil, noe som tester skriveform i stedet for
   forstaaelse. Naa ligger svarene i klartekst i data-a, og
   sammenligningen taaler:

     stor/liten bokstav, mellomrom og tegnsetting
     norske varianter: aa/aa, oe/oe, ae/ae
     bindestrek og mellomrom om hverandre: «arp -a» = «arp-a» = «arp a»
     fyllord: «ca», «omtrent», «ca.», «cirka», «rundt», «ish»
     tallsvar: tallet plukkes ut av setningen, «ca 254 stk» = «254»
     delvis treff: svaret staar i det studenten skrev, eller motsatt,
       naar begge er minst fire tegn lange

   Flagg beholder hash og krever eksakt treff. Det er meningen.
──────────────────────────────────────────────────────── */
var CL_FILLER = /\b(ca|cirka|omtrent|rundt|ish|stk|styk|omlag|ca\.|det er|svaret er|er)\b/g;

function clNorm(s){
  return String(s == null ? '' : s)
    .toLowerCase().trim()
    .replace(/[\u00e6]/g,'ae').replace(/[\u00f8]/g,'oe').replace(/[\u00e5]/g,'aa')
    .replace(/[\u2010-\u2015\u2212]/g,'-')
    .replace(CL_FILLER,' ')
    .replace(/[.,;:!?"'`()\[\]]/g,' ')
    .replace(/\s*-\s*/g,'-')
    .replace(/\s+/g,' ')
    .trim();
}
function clLoose(s){ return clNorm(s).replace(/[-\s]/g,''); }
function clNum(s){ var m = clNorm(s).replace(/\s/g,'').match(/-?\d+(?:[.,]\d+)?/); 
                   return m ? parseFloat(m[0].replace(',','.')) : null; }

function clMatch(input, accepted){
  var g = clNorm(input);
  if (!g) return false;
  for (var i = 0; i < accepted.length; i++){
    var a = accepted[i], n = clNorm(a);
    if (!n) continue;
    if (g === n) return true;                              // eksakt, normalisert
    if (clLoose(g) === clLoose(a)) return true;            // uten bindestrek og mellomrom
    var an = clNum(a), gn = clNum(g);                      // tallsvar
    if (an !== null && gn !== null && an === gn) return true;
    if (an !== null) continue;                             // tall skal ikke delvis-matche
    if (n.length >= 4 && (g.indexOf(n) !== -1 || n.indexOf(g) !== -1)) return true;
    if (n.length < 4 && g.split(' ').indexOf(n) !== -1) return true;  // korte svar som eget ord
  }
  return false;
}

function clSubmit(btn){ var row = btn.closest('.ans-row'); if (row) submitAnswer(row); }
function submitAnswer(row, restoring){
  const input = row.querySelector('.ans-in');
  if (!input) return;
  const val = input.value;
  // tomt felt: nulstill, ikke tell forsoek
  if (!val.trim()){
    input.classList.remove('ok','bad');
    const mk = row.querySelector('.ans-mark'); if (mk) mk.textContent = '';
    saveA(row, ''); saveOk(row, false); syncCardAll(row); return;
  }
  // sjekk svaret (gjenbruker matchelogikken)
  const ok = matchRow(row, val);
  input.classList.toggle('ok', ok); input.classList.toggle('bad', !ok);
  const mk = row.querySelector('.ans-mark'); if (mk) mk.textContent = ok ? '\u2713' : '\u2717';
  saveA(row, val);       // lagre alltid teksten
  saveOk(row, ok);

  // tell forsoek (ikke ved gjenoppretting av lagret svar)
  if (!restoring && !ok){
    const n = (parseInt(row.dataset.tries || '0', 10) || 0) + 1;
    row.dataset.tries = String(n);
    saveTries(row, n);
  }
  revealFasitIfDue(row);
  syncCardAll(row);
}

// vis Fasit-knappen naar feltet har 3+ bomma forsoek
function revealFasitIfDue(row){
  const n = parseInt(row.dataset.tries || getTries(row) || '0', 10) || 0;
  const btn = row.querySelector('.fasit-btn');
  const alreadyOk = row.querySelector('.ans-in').classList.contains('ok');
  if (btn && n >= 3 && !alreadyOk) btn.classList.add('avail');
}

// matchelogikken skilt ut saa baade submit og gjenoppretting bruker den
function matchRow(row, val){
  if (row.dataset.flag === '1'){
    const want = (row.dataset.a||'').split(',').map(Number);
    return want.indexOf(clHash(val)) !== -1;
  }
  return clMatch(val, (row.dataset.a || '').split('|'));
}

function saveTries(row, n){
  try{ var s = JSON.parse(localStorage.getItem('cl_tries')||'{}'); s[answerKey(row)] = n; localStorage.setItem('cl_tries', JSON.stringify(s)); }catch(e){}
}
function getTries(row){
  try{ return (JSON.parse(localStorage.getItem('cl_tries')||'{}'))[answerKey(row)] || 0; }catch(e){ return 0; }
}

function checkAnswerRow(row){
  var inp = row.querySelector('.ans-in'), mark = row.querySelector('.ans-mark');
  var val = inp.value;
  if (!val.trim()){ inp.classList.remove('ok','bad'); if(mark) mark.textContent=''; saveA(row,''); syncCardAll(row); return; }
  var ok;
  if (row.dataset.flag === '1'){                            // flagg: eksakt, via hash
    var want = row.dataset.a.split(',').map(Number);
    ok = want.indexOf(clHash(val)) !== -1;
  } else {
    var list = (row.dataset.a || '').split('|');
    ok = clMatch(val, list);
  }
  inp.classList.toggle('ok', ok); inp.classList.toggle('bad', !ok);
  if (mark) mark.textContent = ok ? '\u2713' : '\u2717';
  saveA(row, val);           // lagre alltid teksten, aldri slett den paa feil svar
  saveOk(row, ok);           // riktig/feil lagres separat, styrer bare fremdrift
  syncCardAll(row);
}
function saveOk(row, ok){
  try{
    var s = JSON.parse(localStorage.getItem('cl_ok') || '{}');
    var k = answerKey(row);
    if (ok) s[k] = 1; else delete s[k];
    localStorage.setItem('cl_ok', JSON.stringify(s));
  }catch(e){}
}
function saveA(row, v){
  var s = getAnswers(); var k = answerKey(row);
  if (v) s[k] = v; else delete s[k];
  saveAnswers(s);
}

function syncCard(row){
  if (row.closest('.lab-card, .task-card, .quiz-card')?.querySelector('.mcq')) return syncCardAll(row);
  const card = row.closest('.lab-card, .task-card');
  if (!card || !card.id) return;
  const rows = [...card.querySelectorAll('.ans-row')];
  const all  = rows.length > 0 && rows.every(r => r.querySelector('.ans-in').classList.contains('ok'));
  if (all) { markTaskDone(card.id); }
  else {
    card.classList.remove('done');
    const p = getProgress(); delete p[card.id]; saveProgress(p);
    const b = document.getElementById('done-' + card.id);
    if (b) b.classList.remove('show');
    updateModuleProgress();
  }
}

function initAnswers(){
  document.querySelectorAll('.ans-row').forEach(row => {
    const input = row.querySelector('.ans-in');
    if (!input || input.dataset.wired) return;
    input.dataset.wired = '1';

    // gjenopprett tidligere svar og vis om det var riktig (uten aa telle nytt forsoek)
    const saved = getAnswers()[answerKey(row)];
    if (saved) { input.value = saved; submitAnswer(row, true); }

    // INGEN live-sjekk lenger. Sjekk skjer ved submit (Svar-knapp) eller Enter.
    input.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); submitAnswer(row); } });
    // hvis feltet endres etter et forsoek, nulstill markering til de sender paa nytt
    input.addEventListener('input', () => {
      input.classList.remove('ok','bad');
      const mk = row.querySelector('.ans-mark'); if (mk) mk.textContent = '';
    });
  });
}

document.addEventListener('DOMContentLoaded', initAnswers);

/* ── Flervalg ── MC-spørsmål som lagrer og teller med i fremdriften ──
   Markup:
     <div class="mcq" data-c="123456">
       <div class="mcq-q">Hva betyr LISTENING?</div>
       <button class="mcq-opt">En tjeneste venter på tilkoblinger</button>
       <button class="mcq-opt">To maskiner snakker sammen nå</button>
       <button class="mcq-opt">Porten er stengt</button>
       <div class="mcq-fb"></div>
     </div>
   data-c er clHash() av teksten i det riktige alternativet, ikke en
   indeks, slik at rekkefølgen kan endres og svaret ikke ligger synlig
   som "riktig = nummer to". Feilsvar låser ikke, studenten kan prøve
   igjen, men riktig svar låser valget.
──────────────────────────────────────────────────────── */

function mcqKey(box){
  const card = box.closest('.lab-card, .task-card, .quiz-card');
  const boxes = card ? [...card.querySelectorAll('.mcq')] : [box];
  return 'mcq:' + (card && card.id ? card.id : 'x') + ':' + boxes.indexOf(box);
}

function markMcq(box, btn, silent){
  const want = parseInt(box.dataset.c, 10);
  const fb   = box.querySelector('.mcq-fb');
  const ok   = clHash(btn.textContent) === want;
  box.querySelectorAll('.mcq-opt').forEach(b => b.classList.remove('sel'));
  btn.classList.add('sel', ok ? 'ok' : 'bad');
  if (!ok) btn.classList.remove('ok'); else btn.classList.remove('bad');
  if (fb) {
    fb.textContent = ok ? (box.dataset.ok || 'Riktig.') : (box.dataset.no || 'Ikke helt. Prøv igjen.');
    fb.className = 'mcq-fb show ' + (ok ? 'ok' : 'bad');
  }
  const store = getAnswers();
  if (ok) {
    store[mcqKey(box)] = btn.textContent.trim();
    box.querySelectorAll('.mcq-opt').forEach(b => { if (b !== btn) b.disabled = true; });
  } else {
    delete store[mcqKey(box)];
  }
  saveAnswers(store);
  syncCardAll(box);
}

/* et kort er ferdig når BÅDE alle ans-row og alle mcq er riktige */
function syncCardAll(node){
  const card = node.closest('.lab-card, .task-card, .quiz-card');
  if (!card || !card.id) return;
  const rows = [...card.querySelectorAll('.ans-row')];
  const mcqs = [...card.querySelectorAll('.mcq')];
  const store = getAnswers();
  const rowsOk = rows.every(r => r.querySelector('.ans-in').classList.contains('ok'));
  const mcqsOk = mcqs.every(m => store[mcqKey(m)]);
  if ((rows.length + mcqs.length) > 0 && rowsOk && mcqsOk) { markTaskDone(card.id); }
  else {
    card.classList.remove('done');
    const p = getProgress(); delete p[card.id]; saveProgress(p);
    const b = document.getElementById('done-' + card.id);
    if (b) b.classList.remove('show');
    updateModuleProgress();
  }
}

function initMcq(){
  document.querySelectorAll('.mcq').forEach(box => {
    const saved = getAnswers()[mcqKey(box)];
    box.querySelectorAll('.mcq-opt').forEach(btn => {
      if (btn.dataset.wired) return;
      btn.dataset.wired = '1';
      btn.addEventListener('click', () => markMcq(box, btn, false));
      if (saved && btn.textContent.trim() === saved) markMcq(box, btn, true);
    });
  });
}

document.addEventListener('DOMContentLoaded', initMcq);

/* hint og svar per sp&oslash;rsm&aring;l */
function aTip(b){
  b.classList.toggle('on');
  var box = b.nextElementSibling;
  if (box && box.classList.contains('ah-box')) box.classList.toggle('show');
}

/* ── Tastaturtilgang ── klikkbare headere maa kunne naas uten mus ──
   lab-header, faq-q og route-kort er <div> med onclick. Uten tabindex
   og en tastaturhandler kan de ikke aapnes med tastatur, og en
   skjermleser annonserer dem ikke som kontroller. Her gjoeres de om
   til ekte knapper ved innlasting, saa alle moduler faar det uten aa
   redigere hver fil.
──────────────────────────────────────────────────────────── */
function clA11y(){
  document.querySelectorAll('.lab-header, .faq-q, .task-card-header')
    .forEach(function(el){
      if (el.dataset.a11y) return;
      el.dataset.a11y = '1';
      if (!el.hasAttribute('role')) el.setAttribute('role', 'button');
      if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '0');
      el.addEventListener('keydown', function(e){
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          el.click();
        }
      });
    });
}
document.addEventListener('DOMContentLoaded', clA11y);

/* ── Ta labben paa nytt ── nullstill KUN denne modulen ──────────
   Fjerner lagrede svar, riktig-markering og fremdrift for kortene
   som finnes paa DENNE siden, og lar alle andre moduler staa.
──────────────────────────────────────────────────────────── */
function clResetModule(){
  const cards = [...document.querySelectorAll('.lab-card, .task-card, .quiz-card')]
    .map(c => c.id).filter(Boolean);
  if (!cards.length) return;
  if (!confirm('Nullstille denne labben? Svarene dine her slettes, men andre labber beroeres ikke.')) return;
  const prune = (storeKey) => {
    let s; try { s = JSON.parse(localStorage.getItem(storeKey) || '{}'); } catch(e){ return; }
    Object.keys(s).forEach(k => {
      const card = k.split(':')[0];
      if (cards.indexOf(card) !== -1 || cards.indexOf(k) !== -1) delete s[k];
    });
    localStorage.setItem(storeKey, JSON.stringify(s));
  };
  prune('cl_answers'); prune('cl_ok'); prune('cl_progress'); prune('cl_tries');
  location.reload();
}
function clAddResetButton(){
  if (!document.querySelector('.lab-card, .task-card')) return;
  if (document.getElementById('cl-reset-btn')) return;
  if (typeof bReset === 'function') return;                       // The Board har sin egen
  const host = document.querySelector('.container-sm, .container') || document.body;
  const wrap = document.createElement('div');
  wrap.style.cssText = 'margin:34px 0 0;text-align:center';
  const b = document.createElement('button');
  b.id = 'cl-reset-btn';
  b.className = 'btn btn-ghost';
  b.textContent = 'Ta denne labben paa nytt';
  b.onclick = clResetModule;
  wrap.appendChild(b);
  host.appendChild(wrap);
}
document.addEventListener('DOMContentLoaded', clAddResetButton);
