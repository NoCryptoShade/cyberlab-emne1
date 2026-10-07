/* enkel.js — smaa spill for den tilpassede versjonen av labbene
   Hvert spill er en <div class="e-spill" data-spill="..."> i HTML-en.
     pakker  send en fil i ett stykke eller som pakker
     reise   foelg en pakke hopp for hopp og se hvilken lapp som byttes
     lyn     lynrunde: ett kort om gangen, velg riktig knapp (innhold i .ly-item)
     chat    meldinger som dukker opp en etter en (innhold i .ch-item)
     rop     et rop som stopper ved ruteren, og en pakke som hopper
   Spillene teller ikke i fremdriften. Det gjoer svarfeltene, som foer.
   Lastes etter cyberlab.js. */

(function(){
  'use strict';

  function el(tag, cls, html){ var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function knapp(tekst, cls){ var b = el('button', 'sp-k' + (cls ? ' ' + cls : ''), tekst); b.type = 'button'; return b; }
  function vent(ms){ return new Promise(function(r){ setTimeout(r, ms); }); }
  function animer(node, cls){ node.classList.remove(cls); void node.offsetWidth; node.classList.add(cls); }
  function ramme(spill, tittel, type){
    var topp = el('div', 'sp-topp');
    topp.appendChild(el('span', 'sp-tittel', tittel));
    var merke = el('span', 'sp-merke', type || '🎮 spill');
    topp.appendChild(merke);
    spill.insertBefore(topp, spill.firstChild);
    return function ferdig(){ spill.classList.add('ferdig'); merke.textContent = '✅ klart!'; };
  }

  /* ── 1. Pakker ─────────────────────────────────────────── */
  function pakker(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🎮 Send fila');
    var MANGLER = 7, N = 12;
    var linje = el('div', 'pk-linje');
    linje.appendChild(el('span', 'pk-ende', '💻'));
    var bane = el('div', 'pk-bane'); var stor = el('div', 'pk-stor'); bane.appendChild(stor);
    linje.appendChild(bane); linje.appendChild(el('span', 'pk-ende', '📱'));
    var ko = el('div', 'pk-ko');
    var mottak = el('div', 'pk-mottak'); mottak.hidden = true;
    var tekst = el('p', 'sp-tekst', 'Prøv begge måtene. Start med den store 👇');
    var tell = el('div', 'pk-teller', '<span>Sendt på nytt: <b class="ny">0</b> byte</span>');
    var kn = el('div', 'sp-knapper');
    var a = knapp('📦 Send alt i ett stykke'), b = knapp('🧩 Send som pakker');
    kn.appendChild(a); kn.appendChild(b);
    [linje, ko, mottak, tekst, tell, kn].forEach(function(n){ sp.appendChild(n); });
    var ny = tell.querySelector('.ny');

    a.onclick = async function(){
      a.disabled = b.disabled = true; mottak.hidden = true; linje.hidden = false;
      stor.className = 'pk-stor'; stor.style.transition = 'none'; stor.style.width = '0'; stor.textContent = '';
      tekst.className = 'sp-tekst'; tekst.textContent = 'Sender 3 MB i ett stykke…';
      ko.textContent = '';
      await vent(50);
      stor.style.transition = 'width 2s linear'; stor.style.width = '62%'; stor.textContent = '3 MB';
      for (var i = 0; i < 4; i++) { await vent(450); ko.textContent += '🚗'; }
      stor.classList.add('boom'); stor.textContent = '💥'; animer(bane, 'rist');
      tekst.className = 'sp-tekst nei';
      tekst.innerHTML = 'Au! Et lite hikk på linja, og <b>hele fila</b> må sendes på nytt. Og se køen bak deg 🚗🚗🚗🚗';
      ny.textContent = '3 000 000';
      a.disabled = b.disabled = false;
    };

    b.onclick = async function(){
      a.disabled = b.disabled = true; linje.hidden = true; ko.textContent = ''; mottak.hidden = false; mottak.innerHTML = '';
      tekst.className = 'sp-tekst'; tekst.textContent = 'Fila deles i 12 små pakker. Her kommer de…';
      ny.textContent = '0';
      var ruter = [];
      for (var i = 1; i <= N; i++) { var r = el('div', 'pk-p', String(i)); ruter.push(r); mottak.appendChild(r); }
      for (var j = 0; j < N; j++) {
        await vent(160);
        if (j + 1 === MANGLER) { ruter[j].className = 'pk-p borte'; ruter[j].textContent = '?'; }
        else ruter[j].className = 'pk-p fram';
      }
      var hull = ruter[MANGLER - 1];
      hull.setAttribute('role', 'button'); hull.setAttribute('tabindex', '0');
      hull.setAttribute('aria-label', 'Send pakke ' + MANGLER + ' på nytt');
      tekst.className = 'sp-tekst nei';
      tekst.innerHTML = 'Pakke ' + MANGLER + ' kom aldri fram! <b>Klikk på den</b> for å sende den på nytt.';
      function redd(){
        if (!hull.classList.contains('borte')) return;
        hull.className = 'pk-p reddet'; hull.textContent = String(MANGLER);
        hull.removeAttribute('role'); hull.removeAttribute('tabindex');
        ny.textContent = '1 500';
        tekst.className = 'sp-tekst ok';
        tekst.innerHTML = '🎉 Bare <b>én</b> pakke på nytt: 1 500 byte i stedet for 3 000 000. Og ingen kø!';
        a.disabled = b.disabled = false; ferdig();
      }
      hull.onclick = redd;
      hull.onkeydown = function(e){ if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); redd(); } };
      hull.focus({ preventScroll: true });
    };
  }

  /* ── 2. Reisen ─────────────────────────────────────────── */
  function reise(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🎮 Kjør pakken');
    var st = [['💻','Din PC'],['📦','Ruter 1'],['📦','Ruter 2'],['🌐','Serveren']];
    var vei = el('div', 'rs-vei');
    var noder = st.map(function(s){ var d = el('div', 'rs-st', '<span class="i">' + s[0] + '</span>' + s[1]); vei.appendChild(d); return d; });
    var spor = el('div', 'rs-spor');
    var pakke = el('div', 'rs-pakke');
    var ip = el('div', 'rs-lapp ip', '<span class="laas"></span>🏷️ Til: 93.184.2.10<small>der pakken skal til slutt</small>');
    var mac = el('div', 'rs-lapp mac', '');
    pakke.appendChild(ip); pakke.appendChild(mac); spor.appendChild(pakke);
    var tekst = el('p', 'sp-tekst', 'Pakken har to lapper. Én av dem byttes på veien. Følg med 👀');
    var kn = el('div', 'sp-knapper');
    var kjor = knapp('🚚 Kjør!', 'hoved'); kn.appendChild(kjor);
    [vei, spor, tekst, kn].forEach(function(n){ sp.appendChild(n); });

    var pos = 0;
    function tegn(){
      noder.forEach(function(n, i){ n.classList.toggle('her', i === pos); });
      pakke.style.gridColumn = String(pos + 1);
      mac.innerHTML = pos < 3 ? '🟨 Neste stopp: ' + st[pos + 1][1] + '<small>bare hvor pakken skal nå</small>' : '🟨 Framme! 🎉';
    }
    tegn();

    function gaa(){
      pos++; tegn(); animer(mac, 'byttet');
      ip.querySelector('.laas').textContent = '🔒 samme';
      animer(ip, 'pop');
    }
    function spaa(){
      tekst.className = 'sp-tekst';
      tekst.textContent = 'Tipp før neste hopp: hvilken lapp kommer til å byttes?';
      kn.innerHTML = '';
      var bi = knapp('🏷️ Til-lappen'), bm = knapp('🟨 Neste-stopp-lappen');
      kn.appendChild(bi); kn.appendChild(bm);
      bi.onclick = function(){ bi.classList.add('nei'); animer(bi, 'rist'); tekst.className = 'sp-tekst nei'; tekst.textContent = 'Nope! Se på lappene igjen. Hvilken var lik i stad? 👀'; };
      bm.onclick = function(){
        bi.disabled = bm.disabled = true; bm.classList.add('ok');
        tekst.className = 'sp-tekst ok'; tekst.textContent = '🎯 Yes! Kjører…';
        setTimeout(function(){ gaa(); videre(); }, 600);
      };
    }
    function videre(){
      kn.innerHTML = '';
      if (pos >= 3) {
        tekst.className = 'sp-tekst ok';
        tekst.innerHTML = 'Framme! 🏷️ var lik <b>hele veien</b>. 🟨 ble byttet på <b>hvert stopp</b>.';
        var igjen = knapp('↺ Kjør igjen'); kn.appendChild(igjen);
        igjen.onclick = function(){ pos = 0; ip.querySelector('.laas').textContent = ''; tegn(); videre(); tekst.className = 'sp-tekst'; tekst.textContent = 'En gang til! 🚚'; };
        ferdig(); return;
      }
      var k = knapp('🚚 Kjør til ' + st[pos + 1][1], 'hoved'); kn.appendChild(k);
      k.onclick = function(){
        if (pos === 1 && !sp.classList.contains('ferdig')) return spaa();
        gaa(); tekst.className = 'sp-tekst';
        tekst.textContent = pos === 1 ? 'Så du hva som skjedde med lappene? Kjør videre 👇' : 'Videre!';
        videre();
      };
    }
    kjor.onclick = function(){ gaa(); tekst.textContent = 'Så du hva som skjedde med lappene? Kjør videre 👇'; videre(); };
  }

  /* ── 3 og 5. Lynrunde ──────────────────────────────────── */
  function lyn(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '⚡ Lynrunde');
    var valg = (sp.dataset.knapper || '').split('|');
    var items = [].slice.call(sp.querySelectorAll('.ly-item')).map(function(n){
      n.remove();
      return { html: n.innerHTML, svar: parseInt(n.dataset.svar, 10), hvorfor: n.dataset.hvorfor || '' };
    });
    var fast = sp.querySelector('.ly-fast');
    var status = el('div', 'ly-status');
    var kort = el('div', 'ly-kort');
    var tekst = el('p', 'sp-tekst');
    var kn = el('div', 'ly-knapper');
    var neste = el('div', 'sp-knapper');
    var topp = sp.querySelector('.sp-topp'); topp.insertBefore(status, topp.lastChild);
    [kort, kn, tekst, neste].forEach(function(n){ sp.appendChild(n); });
    if (fast) sp.insertBefore(fast, kort);

    var ko, nr, rette, streak, best, forsteForsok;
    function start(){
      ko = items.slice(); nr = 0; rette = 0; streak = 0; best = 0; forsteForsok = 0;
      vis();
    }
    var naa = 1;
    function oppdater(){
      status.innerHTML = '<span>Kort <b>' + naa + '</b>/' + items.length + '</span>' +
        '<span class="ly-streak' + (streak >= 3 ? ' het' : '') + '">🔥 <b>' + streak + '</b> på rad</span>';
    }
    function vis(){
      naa = rette + 1; oppdater(); neste.innerHTML = ''; tekst.className = 'sp-tekst'; tekst.innerHTML = '';
      var it = ko[0]; kort.className = 'ly-kort pop'; kort.innerHTML = it.html;
      kn.innerHTML = '';
      valg.forEach(function(v, i){
        var b = knapp(v); kn.appendChild(b);
        b.onclick = function(){ svar(it, i, b); };
      });
    }
    function svar(it, i, b){
      [].forEach.call(kn.children, function(x){ x.disabled = true; });
      kort.querySelectorAll('.e-ip').forEach(function(x){ x.classList.add('vis'); });
      ko.shift();
      if (i === it.svar) {
        b.classList.add('ok'); kort.className = 'ly-kort ok';
        rette++; streak++; best = Math.max(best, streak); if (!it.bommet) forsteForsok++;
        var hei = streak === 3 ? ' 🔥 3 på rad!' : streak === 5 ? ' 🔥🔥 5 på rad!' : '';
        tekst.className = 'sp-tekst ok'; tekst.innerHTML = '✅ ' + it.hvorfor + hei;
      } else {
        b.classList.add('nei'); kort.className = 'ly-kort nei'; animer(kort, 'rist');
        kn.children[it.svar].classList.add('ok');
        streak = 0; it.bommet = true; ko.push(it);
        tekst.className = 'sp-tekst nei'; tekst.innerHTML = '❌ ' + it.hvorfor + ' <span style="color:var(--text2)">Dette kortet kommer igjen senere.</span>';
      }
      oppdater();
      var nb = knapp(ko.length ? 'Neste ▶' : 'Se resultatet 🏆', 'hoved'); neste.appendChild(nb);
      nb.onclick = function(){ ko.length ? vis() : slutt(); };
      nb.focus({ preventScroll: true });
    }
    function slutt(){
      kn.innerHTML = ''; neste.innerHTML = ''; tekst.innerHTML = '';
      var alle = forsteForsok === items.length;
      kort.className = 'ly-kort ok';
      kort.innerHTML = '<div class="ly-slutt"><span class="stor">' + (alle ? '🏆' : '⭐') + '</span>' +
        forsteForsok + ' av ' + items.length + ' riktig på første forsøk' + (best >= 3 ? '<br>Lengste rekke: 🔥 ' + best : '') +
        (alle ? '<br>Feilfritt! 👑' : '<br>Alle kortene sitter nå. Bra jobba!') + '</div>';
      var igjen = knapp('↺ Spill igjen'); neste.appendChild(igjen);
      igjen.onclick = function(){ items.forEach(function(x){ x.bommet = false; }); start(); };
      status.innerHTML = '';
      ferdig();
    }
    start();
  }

  /* ── 4. Chat ───────────────────────────────────────────── */
  function chat(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '💬 Lokalnett-chatten');
    var deler = [].slice.call(sp.querySelectorAll('.ch-item')).map(function(n){
      n.remove(); return { fra: n.dataset.fra, navn: n.dataset.navn || '', html: n.innerHTML, stopp: n.dataset.stopp };
    });
    var logg = el('div', 'ch-logg');
    var kn = el('div', 'sp-knapper');
    sp.appendChild(logg); sp.appendChild(kn);
    var i = 0, kjorer = false;

    async function spill(){
      kjorer = true; kn.innerHTML = '';
      while (i < deler.length) {
        var d = deler[i];
        if (d.stopp) {
          i++;
          var b = knapp(d.stopp, 'hoved'); kn.appendChild(b);
          b.onclick = function(){ spill(); }; b.focus({ preventScroll: true });
          kjorer = false; return;
        }
        if (d.fra !== 'sys') {
          var dots = el('div', 'ch-skriver' + (d.fra === 'pc' ? ' pc' : ''), '•••');
          logg.appendChild(dots); await vent(650); dots.remove();
        } else await vent(350);
        var m = el('div', 'ch-m ' + d.fra, (d.navn ? '<span class="fra">' + d.navn + '</span>' : '') + d.html);
        logg.appendChild(m);
        if (m.getBoundingClientRect().bottom > innerHeight) m.scrollIntoView({ behavior: 'smooth', block: 'end' });
        i++;
        await vent(d.fra === 'sys' ? 500 : 900);
      }
      kjorer = false; ferdig();
      var igjen = knapp('↺ Se chatten igjen'); kn.appendChild(igjen);
      igjen.onclick = function(){ logg.innerHTML = ''; i = 0; spill(); };
    }
    var start = knapp('▶ Start chatten', 'hoved'); kn.appendChild(start);
    start.onclick = function(){ if (!kjorer) spill(); };
  }

  /* ── 6. Ropet og hoppene ───────────────────────────────── */
  function rop(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🎮 Hvor langt når du?');
    var kart = el('div', 'rp-kart');
    var hus = el('div', 'rp-hus', '<span class="navn">ditt lokalnett 🏠</span><span class="d">💻</span><span class="d">🖨️</span><span class="d">📱</span><span class="d">🖥️</span>');
    var bolge = el('div', 'rp-bolge'); hus.appendChild(bolge);
    var veg = el('div', 'rp-veg');
    var rutere = [1, 2, 3, 4].map(function(n){
      var r = el('div', 'rp-r', '<span class="nr">' + n + '</span><span class="i">🚪</span>ruter'); veg.appendChild(r); return r;
    });
    veg.appendChild(el('span', 'rp-maal', '🌐'));
    kart.appendChild(hus); kart.appendChild(veg);
    var teller = el('div', 'rp-teller', 'Hopp: <b>0</b>');
    var tekst = el('p', 'sp-tekst', 'To knapper. Prøv begge 👇');
    var kn = el('div', 'sp-knapper');
    var br = knapp('📣 Rop ARP til alle'), bp = knapp('📦 Send pakke til Google');
    kn.appendChild(br); kn.appendChild(bp);
    [kart, teller, tekst, kn].forEach(function(n){ sp.appendChild(n); });
    var gjort = { rop: false, pakke: false };
    function sjekk(){ if (gjort.rop && gjort.pakke) ferdig(); }
    function nullstill(){ rutere.forEach(function(r){ r.className = 'rp-r'; }); teller.innerHTML = 'Hopp: <b>0</b>'; }

    br.onclick = async function(){
      br.disabled = bp.disabled = true; nullstill();
      tekst.className = 'sp-tekst'; tekst.textContent = '📣 «Hvem har 192.168.1.20?»';
      animer(bolge, 'gaar'); await vent(900);
      rutere[0].classList.add('stopp'); animer(rutere[0], 'rist');
      tekst.className = 'sp-tekst';
      tekst.innerHTML = '🛑 Ropet nådde <b>alle i huset</b>, men stoppet ved første ruter. Det slipper aldri ut.';
      gjort.rop = true; sjekk(); br.disabled = bp.disabled = false;
    };
    bp.onclick = async function(){
      br.disabled = bp.disabled = true; nullstill();
      tekst.className = 'sp-tekst'; tekst.textContent = 'Pakken går ut døra…';
      for (var i = 0; i < rutere.length; i++) {
        await vent(550); rutere[i].classList.add('lys'); animer(rutere[i], 'pop');
        teller.innerHTML = 'Hopp: <b>' + (i + 1) + '</b>';
      }
      await vent(400);
      tekst.className = 'sp-tekst ok';
      tekst.innerHTML = '🎉 Framme etter <b>4 hopp</b>. Hver ruter = én grense mellom to nett.';
      gjort.pakke = true; sjekk(); br.disabled = bp.disabled = false;
    };
  }

  /* ── Oeve-terminal ─────────────────────────────────────────
     Ser ut som terminalen i Kali og svarer med faste utskrifter, saa
     spoersmaalene om utskriften kan rettes. Oppdragene tas i rekkefoelge.
       <div class="e-spill" data-spill="terminal">
         <div class="tm-o" data-cmd="ip addr" data-alias="ip a" data-mal="Vis adressene dine" data-skjult>
           <template class="ut">…utskrift…</template>
           <template class="forklar">…forklaring som vises etterpaa…</template>
         </div>
       </div>
     data-skjult: kommandoen vises ikke, bare maalet. Studenten kan be om den.
     Den samme kommandoen kan staa i flere oppdrag med ulik utskrift, for
     eksempel ip neigh foer og etter at tabellen er toemt. */
  function norm(s){ return String(s).trim().toLowerCase().replace(/\s+/g, ' ').replace(/(^| )-([a-z])(\d)/g, '$1-$2 $3'); }
  function avstand(a, b){
    var d = []; for (var i = 0; i <= a.length; i++) { d[i] = [i]; }
    for (var j = 1; j <= b.length; j++) d[0][j] = j;
    for (i = 1; i <= a.length; i++) for (j = 1; j <= b.length; j++)
      d[i][j] = Math.min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (a[i-1] === b[j-1] ? 0 : 1));
    return d[a.length][b.length];
  }
  function lesTerm(){ try { return JSON.parse(localStorage.getItem('enkel_term') || '{}'); } catch(e){ return {}; } }
  function lagreTerm(id, n){ try { var s = lesTerm(); s[id] = n; localStorage.setItem('enkel_term', JSON.stringify(s)); } catch(e){} }

  function terminal(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '💻 Øve-terminal', '💻 øving');
    var card = sp.closest('.lab-card'), id = card ? card.id : 'x';
    var opp = [].slice.call(sp.querySelectorAll('.tm-o')).map(function(n){
      var ut = n.querySelector('template.ut'), fk = n.querySelector('template.forklar');
      var o = { cmd: n.dataset.cmd, alle: [n.dataset.cmd].concat((n.dataset.alias || '').split('|').filter(Boolean)).map(norm),
        mal: n.dataset.mal || '', skjult: n.hasAttribute('data-skjult'), hint: n.dataset.hint || '',
        ut: ut ? ut.innerHTML.replace(/^\n/, '').replace(/\s+$/, '') : '', forklar: fk ? fk.innerHTML : '' };
      n.remove(); return o;
    });
    var kjente = ['clear', 'help'];
    opp.forEach(function(o){ o.alle.forEach(function(c){ var f = c.split(' ')[0]; if (kjente.indexOf(f) === -1) kjente.push(f); }); });

    sp.appendChild(el('p', 'tm-intro', 'Dette er en øve-terminal. Den oppfører seg som den ekte i Kali, men her kan ingenting gå i stykker. Skriv kommandoen og trykk <b>Enter</b>.'));
    var liste = el('ol', 'tm-liste'); sp.appendChild(liste);
    var forklar = el('div', 'tm-forklar'); forklar.hidden = true; sp.appendChild(forklar);
    var vindu = el('div', 'tm-vindu');
    vindu.appendChild(el('div', 'tm-bar', '<i></i><i></i><i></i><span>kali@kali: ~</span>'));
    var ut = el('div', 'tm-ut'); vindu.appendChild(ut);
    var linje = el('label', 'tm-linje', '<span class="tm-ps">kali@kali:~$</span>');
    var inp = el('input', 'tm-in'); inp.setAttribute('autocomplete', 'off'); inp.setAttribute('autocapitalize', 'off');
    inp.setAttribute('spellcheck', 'false'); inp.setAttribute('aria-label', 'Skriv en kommando');
    linje.appendChild(inp); vindu.appendChild(linje); sp.appendChild(vindu);
    vindu.addEventListener('click', function(){ inp.focus(); });

    var naa = Math.min(lesTerm()[id] || 0, opp.length), vist = {}, hist = [], hpos = 0;

    function tegnListe(){
      liste.innerHTML = '';
      opp.forEach(function(o, i){
        var li = el('li', i < naa ? 'gjort' : i === naa ? 'naa' : 'senere');
        var ikon = i < naa ? '✅' : i === naa ? '👉' : '🔒';
        var vis = !o.skjult || i < naa || vist[i];
        li.innerHTML = '<span class="ik">' + ikon + '</span><span class="tx">' + o.mal +
          (vis && i <= naa ? ' <code>' + esc(o.cmd) + '</code>' : '') + '</span>';
        if (i === naa && o.skjult && !vist[i]) {
          var hk = knapp('💡 Vis kommandoen'); hk.classList.add('tm-hint');
          if (o.hint) li.querySelector('.tx').insertAdjacentHTML('beforeend', '<span class="tm-tips">' + o.hint + '</span>');
          hk.onclick = function(){ vist[i] = true; tegnListe(); inp.focus(); };
          li.appendChild(hk);
        }
        liste.appendChild(li);
      });
      if (naa >= opp.length) {
        liste.appendChild(el('li', 'alle', '🎉 Alle oppdrag klare! Svar på spørsmålene under, og prøv det samme på ekte Kali.'));
        ferdig();
      }
    }
    function skriv(html, cls){ var d = el('div', 'tm-l' + (cls ? ' ' + cls : ''), html); ut.appendChild(d); }
    function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function treff(o, c){ return o.alle.indexOf(c) !== -1; }

    function kjor(raa){
      var c = norm(raa);
      skriv('<span class="tm-ps">kali@kali:~$</span> ' + esc(raa));
      if (!c) return;
      if (c === 'clear') { ut.innerHTML = ''; return; }
      if (c === 'help') {
        var lart = opp.slice(0, Math.max(naa, 1)).map(function(o){ return o.cmd; });
        skriv('Kommandoer du har møtt her: ' + lart.map(function(x){ return '<b>' + esc(x) + '</b>'; }).join(', '), 'tm-info');
        return;
      }
      var o = opp[naa];
      if (o && treff(o, c)) {
        if (o.ut) skriv(o.ut);
        if (o.forklar) { forklar.innerHTML = '<span class="t">Hva betyr dette?</span>' + o.forklar; forklar.hidden = false; }
        naa++; lagreTerm(id, naa); tegnListe(); return;
      }
      for (var i = naa - 1; i >= 0; i--) if (treff(opp[i], c)) { if (opp[i].ut) skriv(opp[i].ut); return; }
      for (i = naa + 1; i < opp.length; i++) if (treff(opp[i], c)) { skriv('Riktig kommando, men ta oppdragene i rekkefølge 😉 Se 👉 over.', 'tm-info'); return; }
      var forste = c.split(' ')[0];
      if (o && forste === o.alle[0].split(' ')[0]) {
        skriv(o.skjult && !vist[naa] ? 'Nesten! 👀 Starten er riktig, men noe i resten er feil. Prøv igjen, eller trykk 💡.'
          : 'Nesten! 👀 Sammenlign med <b>' + esc(o.cmd) + '</b>. Mellomrom teller.', 'tm-info');
        return;
      }
      if (kjente.indexOf(forste) !== -1) { skriv('Den kommandoen finnes, men ikke akkurat sånn her. Se 👉 oppdraget over.', 'tm-info'); return; }
      skriv('bash: ' + esc(forste) + ': command not found', 'tm-feil');
      var naer = kjente.filter(function(k){ return avstand(forste, k) <= 2 && k !== forste; })[0];
      skriv(naer ? 'Skrivefeil? Mente du <b>' + esc(naer) + '</b>? 😉' : 'Skriv <b>help</b> for å se kommandoene du har møtt.', 'tm-info');
    }

    inp.addEventListener('keydown', function(e){
      if (e.key === 'Enter') { e.preventDefault(); var v = inp.value; inp.value = ''; if (v.trim()) { hist.push(v); hpos = hist.length; } kjor(v); ut.scrollTop = ut.scrollHeight; }
      else if (e.key === 'ArrowUp' && hist.length) { e.preventDefault(); hpos = Math.max(0, hpos - 1); inp.value = hist[hpos]; }
      else if (e.key === 'ArrowDown' && hist.length) { e.preventDefault(); hpos = Math.min(hist.length, hpos + 1); inp.value = hist[hpos] || ''; }
    });
    tegnListe();
  }

  /* ── Feiring naar en oppgave blir ferdig ───────────────── */
  var JUBEL = ['🎉 Rått! Oppgave ferdig.', '🔥 Den satt!', '⭐ Én ned!', '🚀 Ferdig! Ta en pause hvis du vil ☕', '💪 Sterkt jobba!'];
  function toast(tekst){
    var t = document.querySelector('.e-toast');
    if (!t) { t = el('div', 'e-toast'); t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = tekst; t.classList.add('vis');
    clearTimeout(t._t); t._t = setTimeout(function(){ t.classList.remove('vis'); }, 2800);
  }
  function jubel(){
    var kort = document.querySelectorAll('.enkel .lab-card[id]');
    var obs = new MutationObserver(function(list){
      list.forEach(function(m){
        var c = m.target, var_ = (m.oldValue || '').split(' ').indexOf('done') !== -1;
        if (c.classList.contains('done') && !var_) {
          var alle = [].every.call(kort, function(k){ return k.classList.contains('done'); });
          toast(alle ? '🏆 Hele labben er ferdig! Du er rå.' : JUBEL[Math.floor(Math.random() * JUBEL.length)]);
        }
      });
    });
    kort.forEach(function(k){ obs.observe(k, { attributes: true, attributeFilter: ['class'], attributeOldValue: true }); });
  }

  /* ── Felles: stokk en liste, men aldri tilbake til samme rekkefoelge ── */
  function stokk(a){
    var b = a.slice();
    for (var n = 0; n < 8; n++) {
      for (var i = b.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = b[i]; b[i] = b[j]; b[j] = t; }
      if (b.length < 2 || b.some(function(x, k){ return x !== a[k]; })) break;
    }
    return b;
  }

  /* ── Klikk: finn de riktige bitene i en tekst, logg eller kode ──
       <div class="e-spill" data-spill="klikk" data-oppgave="Klikk på alle IP-adressene">
         <pre>… <span class="kl" data-rett data-forklar="…">10.0.0.1</span> … <span class="kl" data-forklar="…">felle</span></pre>
       </div>
     Ferdig naar alle med data-rett er funnet. data-forklar vises ved klikk. */
  function klikk(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🔎 Finn dem');
    var alle = [].slice.call(sp.querySelectorAll('.kl'));
    var rette = alle.filter(function(k){ return k.hasAttribute('data-rett'); });
    var oppg = el('p', 'kl-oppgave', (sp.dataset.oppgave || 'Klikk på de riktige') + ' <span class="kl-teller"></span>');
    sp.insertBefore(oppg, sp.querySelector('.sp-topp').nextSibling);
    var teller = oppg.querySelector('.kl-teller');
    var tekst = el('p', 'sp-tekst'); sp.appendChild(tekst);
    var funnet = 0;
    function tell(){ teller.textContent = funnet + ' av ' + rette.length + ' funnet'; }
    tell();
    alle.forEach(function(k){
      k.setAttribute('role', 'button'); k.setAttribute('tabindex', '0');
      function trykk(){
        if (k.classList.contains('funnet')) return;
        var f = k.dataset.forklar || '';
        if (k.hasAttribute('data-rett')) {
          k.classList.add('funnet'); animer(k, 'pop'); funnet++; tell();
          tekst.className = 'sp-tekst ok'; tekst.innerHTML = '✅ ' + (f || 'Riktig!');
          if (funnet === rette.length) {
            tekst.innerHTML += '<br>🎉 Alle funnet!'; ferdig();
          }
        } else {
          k.classList.add('feil'); animer(k, 'rist');
          setTimeout(function(){ k.classList.remove('feil'); }, 700);
          tekst.className = 'sp-tekst nei'; tekst.innerHTML = '❌ ' + (f || 'Ikke denne. Prøv en annen.');
        }
      }
      k.addEventListener('click', trykk);
      k.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); trykk(); } });
    });
  }

  /* ── Rekkefoelge: klikk stegene i riktig rekkefoelge ──
       <div class="e-spill" data-spill="rekkefolge" data-oppgave="…">
         <div class="rf-item" data-forklar="…">Første steg</div>   (staar i RIKTIG rekkefoelge i HTML)
         …
       </div> */
  function rekkefolge(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🧩 Sett i riktig rekkefølge');
    var items = [].slice.call(sp.querySelectorAll('.rf-item')).map(function(n, i){
      n.remove(); return { i: i, html: n.innerHTML, forklar: n.dataset.forklar || '' };
    });
    if (sp.dataset.oppgave) sp.appendChild(el('p', 'kl-oppgave', sp.dataset.oppgave));
    var svar = el('ol', 'rf-svar'); sp.appendChild(svar);
    var bunke = el('div', 'rf-bunke'); sp.appendChild(bunke);
    var tekst = el('p', 'sp-tekst', 'Klikk på det som skjer <b>først</b>.'); sp.appendChild(tekst);
    var kn = el('div', 'sp-knapper'); sp.appendChild(kn);
    var neste;
    function start(){
      neste = 0; svar.innerHTML = ''; bunke.innerHTML = ''; kn.innerHTML = '';
      tekst.className = 'sp-tekst'; tekst.innerHTML = 'Klikk på det som skjer <b>først</b>.';
      stokk(items).forEach(function(it){
        var b = knapp(it.html, 'rf-k'); bunke.appendChild(b);
        b.onclick = function(){
          if (it.i === neste) {
            b.remove();
            svar.appendChild(el('li', 'pop', '<span>' + it.html + '</span>' + (it.forklar ? '<small>' + it.forklar + '</small>' : '')));
            neste++;
            if (neste === items.length) {
              tekst.className = 'sp-tekst ok'; tekst.innerHTML = '🎉 Riktig rekkefølge!';
              var ig = knapp('↺ Prøv igjen'); kn.appendChild(ig); ig.onclick = start; ferdig();
            } else { tekst.className = 'sp-tekst ok'; tekst.innerHTML = '✅ Ja! Hva kommer så?'; }
          } else {
            b.classList.add('nei'); animer(b, 'rist'); setTimeout(function(){ b.classList.remove('nei'); }, 700);
            tekst.className = 'sp-tekst nei'; tekst.innerHTML = '❌ Ikke ennå. Hva må skje før dette?';
          }
        };
      });
    }
    start();
  }

  /* ── Par: koble hver ting til riktig partner ──
       <div class="e-spill" data-spill="par" data-oppgave="…">
         <div class="pr-par" data-forklar="…"><span>venstre</span><span>høyre</span></div>
         …
       </div> */
  function par(sp){
    var ferdig = ramme(sp, sp.dataset.tittel || '🔗 Finn parene');
    var parene = [].slice.call(sp.querySelectorAll('.pr-par')).map(function(n, i){
      var s = n.querySelectorAll('span'); n.remove();
      return { i: i, v: s[0].innerHTML, h: s[1].innerHTML, forklar: n.dataset.forklar || '' };
    });
    if (sp.dataset.oppgave) sp.appendChild(el('p', 'kl-oppgave', sp.dataset.oppgave));
    var rad = el('div', 'pr-rad'); sp.appendChild(rad);
    var venstre = el('div', 'pr-kol'), hoyre = el('div', 'pr-kol');
    rad.appendChild(venstre); rad.appendChild(hoyre);
    var tekst = el('p', 'sp-tekst', 'Klikk én til venstre, så partneren til høyre.'); sp.appendChild(tekst);
    var valgt = null, ferdige = 0;
    parene.forEach(function(p){
      var b = knapp(p.v, 'pr-k'); venstre.appendChild(b); p.vk = b;
      b.onclick = function(){
        if (b.disabled) return;
        parene.forEach(function(x){ x.vk.classList.remove('valgt'); });
        b.classList.add('valgt'); valgt = p;
        tekst.className = 'sp-tekst'; tekst.textContent = 'Og partneren er…?';
      };
    });
    stokk(parene).forEach(function(p){
      var b = knapp(p.h, 'pr-k'); hoyre.appendChild(b); p.hk = b;
      b.onclick = function(){
        if (!valgt) { tekst.className = 'sp-tekst'; tekst.textContent = 'Velg en til venstre først 👈'; animer(venstre, 'rist'); return; }
        if (valgt === p) {
          p.vk.classList.remove('valgt'); p.vk.classList.add('ok'); b.classList.add('ok');
          p.vk.disabled = b.disabled = true; ferdige++; valgt = null;
          tekst.className = 'sp-tekst ok'; tekst.innerHTML = '✅ ' + (p.forklar || 'Riktig par!');
          if (ferdige === parene.length) { tekst.innerHTML += '<br>🎉 Alle parene er funnet!'; ferdig(); }
        } else {
          b.classList.add('nei'); animer(b, 'rist'); setTimeout(function(){ b.classList.remove('nei'); }, 700);
          tekst.className = 'sp-tekst nei'; tekst.textContent = '❌ Ikke de to. Prøv en annen.';
        }
      };
    });
  }

  var MOTORER = { pakker: pakker, reise: reise, lyn: lyn, chat: chat, rop: rop, terminal: terminal,
                  klikk: klikk, rekkefolge: rekkefolge, par: par };
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.enkel .e-spill[data-spill]').forEach(function(sp){
      var f = MOTORER[sp.dataset.spill]; if (f) f(sp);
    });
    jubel();
  });
})();
