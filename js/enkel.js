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
  function ramme(spill, tittel){
    var topp = el('div', 'sp-topp');
    topp.appendChild(el('span', 'sp-tittel', tittel));
    var merke = el('span', 'sp-merke', '🎮 spill');
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

  var MOTORER = { pakker: pakker, reise: reise, lyn: lyn, chat: chat, rop: rop };
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.enkel .e-spill[data-spill]').forEach(function(sp){
      var f = MOTORER[sp.dataset.spill]; if (f) f(sp);
    });
    jubel();
  });
})();
