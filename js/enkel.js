/* enkel.js — viser en oppgave ett steg om gangen
   Hver .lab-flow med <section class="steg"> faar:
     - en linje oeverst: "Steg 2 av 6" og prikker, pluss "Vis alle steg"
     - en "Neste steg"-knapp nederst i hvert steg som ikke er det siste
   Hvor langt studenten har kommet, lagres per oppgave i nettleseren.
   Ferdige oppgaver viser alle steg. Lastes etter cyberlab.js. */

(function(){
  var KEY = 'enkel_steg';

  function les(){ try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch(e){ return {}; } }
  function lagre(id, n){
    try { var s = les(); if ((s[id] || 0) < n) { s[id] = n; localStorage.setItem(KEY, JSON.stringify(s)); } } catch(e){}
  }

  function settOpp(flow){
    var card = flow.closest('.lab-card');
    var id = card && card.id;
    var steg = [].slice.call(flow.querySelectorAll(':scope > .steg'));
    if (!id || steg.length < 2) return;

    var nav = document.createElement('div');
    nav.className = 'steg-nav';
    var tekst = document.createElement('span');
    var dots = document.createElement('span');
    dots.className = 'steg-dots';
    steg.forEach(function(){ var d = document.createElement('span'); d.className = 'steg-dot'; dots.appendChild(d); });
    var venstre = document.createElement('span');
    venstre.style.cssText = 'display:flex;gap:12px;align-items:center';
    venstre.appendChild(tekst); venstre.appendChild(dots);
    var alle = document.createElement('button');
    alle.type = 'button'; alle.className = 'steg-alle'; alle.textContent = 'Vis alle steg';
    nav.appendChild(venstre); nav.appendChild(alle);
    flow.insertBefore(nav, steg[0]);

    function vis(n){
      steg.forEach(function(s, i){ s.hidden = i >= n; });
      [].forEach.call(dots.children, function(d, i){ d.classList.toggle('on', i < n); });
      tekst.textContent = n >= steg.length ? 'Alle ' + steg.length + ' steg' : 'Steg ' + n + ' av ' + steg.length;
      steg.forEach(function(s, i){ var b = s.querySelector(':scope > .steg-neste'); if (b) b.hidden = i < n - 1; });
      alle.hidden = n >= steg.length;
    }

    steg.forEach(function(s, i){
      if (i === steg.length - 1) return;
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'steg-neste';
      b.textContent = 'Neste steg: ' + ((steg[i + 1].querySelector('.steg-t') || {}).textContent || '').replace(/^\s*\d+\s*/, '') + ' ▶';
      b.addEventListener('click', function(){
        vis(i + 2); lagre(id, i + 2);
        steg[i + 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
        var t = steg[i + 1].querySelector('.steg-t'); if (t) { t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true }); }
      });
      s.appendChild(b);
    });

    alle.addEventListener('click', function(){ vis(steg.length); lagre(id, steg.length); });

    var start = card.classList.contains('done') ? steg.length : Math.max(1, Math.min(les()[id] || 1, steg.length));
    vis(start);
  }

  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.enkel .lab-flow').forEach(settOpp);
  });
})();
