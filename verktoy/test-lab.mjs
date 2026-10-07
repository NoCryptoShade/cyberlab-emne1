// Tester en tilpasset lab fra ende til annen.
//   node verktoy/test-lab.mjs modules/nett-grunnlag.html [mappe-for-skjermbilder]
// Starter en lokal server, spiller alle spill, fullfører alle terminaloppdrag,
// svarer på alle spørsmål med fasiten og sjekker at fremdriften blir full.
// Krever Playwright (globalt installert) og Chromium.
import { createRequire } from 'module';
import { execSync, spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
const require = createRequire(import.meta.url);
const pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright'));

const side = process.argv[2];
const bilder = process.argv[3];
if (!side) { console.error('bruk: node verktoy/test-lab.mjs modules/x.html [skjermbildemappe]'); process.exit(2); }
const rot = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const kilde = fs.readFileSync(path.join(rot, side), 'utf8');
const port = 8800 + Math.floor(Math.random() * 150);
const server = spawn('python3', ['-m', 'http.server', String(port)], { cwd: rot, stdio: 'ignore' });
await new Promise(r => setTimeout(r, 700));
const dekod = s => s.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();

const feil = [], rapport = {};
const b = await pw.chromium.launch({ executablePath: fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined });
try {
  const pg = await b.newPage({ viewport: { width: 1280, height: 1000 } });
  pg.on('pageerror', e => feil.push('JS: ' + e.message));
  pg.on('response', r => { if (r.url().includes('localhost:' + port) && r.status() >= 400 && !r.url().includes('favicon')) feil.push(r.status() + ' ' + r.url()); });
  const url = `http://localhost:${port}/${side}`;
  await pg.goto(url); await pg.evaluate(() => localStorage.clear()); await pg.reload(); await pg.waitForTimeout(300);
  const kort = await pg.$$eval('.lab-card[id]', x => x.map(c => c.id));
  const biter = kilde.split('<div class="lab-card"').slice(1);
  for (let ci = 0; ci < kort.length; ci++) {
    const id = kort[ci], blk = biter[ci] || '';
    const r = rapport[id] = { spill: [], rader: 0, mcq: 0 };
    await pg.click(`#${id} .lab-header`);
    const spillKilde = blk.split('data-spill="').slice(1);
    const spill = await pg.$$(`#${id} .e-spill[data-spill]`);
    for (let si = 0; si < spill.length; si++) {
      const sp = spill[si], type = await sp.getAttribute('data-spill'), src = spillKilde[si] || '';
      try {
        if (type === 'lyn') {
          const svar = {};
          for (const m of src.matchAll(/class="ly-item"[^>]*data-svar="(\d+)"[^>]*>([\s\S]*?)<\/div>/g)) svar[dekod(m[2])] = +m[1];
          for (let n = 0; n < 60 && await sp.$('.ly-knapper .sp-k'); n++) {
            const t = dekod(await sp.$eval('.ly-kort', e => e.innerHTML));
            const k = await sp.$$('.ly-knapper .sp-k'); await k[svar[t] ?? 0].click();
            await sp.$eval('.sp-knapper .sp-k', e => e.click());
          }
        } else if (type === 'klikk') {
          for (const k of await sp.$$('.kl[data-rett]')) await k.click();
        } else if (type === 'rekkefolge') {
          const rek = [...src.matchAll(/class="rf-item"[^>]*>([\s\S]*?)<\/div>/g)].map(m => dekod(m[1]));
          for (const t of rek) { for (const k of await sp.$$('.rf-k')) if (dekod(await k.innerHTML()) === t) { await k.click(); break; } }
        } else if (type === 'par') {
          const p = [...src.matchAll(/class="pr-par"[^>]*>\s*<span>([\s\S]*?)<\/span>\s*<span>([\s\S]*?)<\/span>/g)].map(m => [dekod(m[1]), dekod(m[2])]);
          const kol = await sp.$$('.pr-kol');
          for (const [v, h] of p) {
            for (const k of await kol[0].$$('.pr-k')) if (dekod(await k.innerHTML()) === v) { await k.click(); break; }
            for (const k of await kol[1].$$('.pr-k:not([disabled])')) if (dekod(await k.innerHTML()) === h) { await k.click(); break; }
          }
        } else if (type === 'chat') {
          for (let n = 0; n < 12 && !(await sp.evaluate(e => e.classList.contains('ferdig'))); n++) {
            const k = await sp.$('.sp-knapper .sp-k'); if (k) await k.click(); await pg.waitForTimeout(1500);
          }
          for (let n = 0; n < 40 && !(await sp.evaluate(e => e.classList.contains('ferdig'))); n++) await pg.waitForTimeout(500);
        } else if (type === 'terminal') {
          const cmds = [...src.split('data-spill="')[0].matchAll(/class="tm-o" data-cmd="([^"]+)"/g)].map(m => dekod(m[1]));
          const inp = await sp.$('.tm-in');
          for (const c of cmds) { await inp.fill(c); await inp.press('Enter'); }
        } else if (type === 'pakker') {
          await sp.$eval('.sp-knapper .sp-k:nth-child(2)', e => e.click()); await pg.waitForTimeout(2600); await sp.$eval('.pk-p.borte', e => e.click());
        } else if (type === 'reise') {
          for (let n = 0; n < 8 && !(await sp.evaluate(e => e.classList.contains('ferdig'))); n++) {
            const k = await sp.$$('.sp-knapper .sp-k'); await k[k.length - 1].click(); await pg.waitForTimeout(900);
          }
        } else if (type === 'rop') {
          const k = await sp.$$('.sp-knapper .sp-k'); await k[0].click(); await pg.waitForTimeout(1500); await k[1].click(); await pg.waitForTimeout(3000);
        }
      } catch (e) { feil.push(`${id} ${type}: ${e.message.split('\n')[0]}`); }
      const ok = await sp.evaluate(e => e.classList.contains('ferdig'));
      r.spill.push(type + (ok ? ' ✓' : ' ✗'));
      if (!ok) feil.push(`${id}: spillet «${type}» ble ikke ferdig`);
    }
    for (const m of await pg.$$(`#${id} .mcq`)) {
      for (const o of await m.$$('.mcq-opt')) if (await o.evaluate(el => clHash(el.textContent) === parseInt(el.closest('.mcq').dataset.c, 10))) { await o.click(); r.mcq++; break; }
    }
    for (const row of await pg.$$(`#${id} .ans-row`)) {
      const f = await row.$eval('.ah-box.sv', e => e.textContent.trim());
      await (await row.$('.ans-in')).fill(f); await (await row.$('.submit-btn')).click(); r.rader++;
    }
    const ikkeOk = await pg.$$eval(`#${id} .ans-in:not(.ok)`, x => x.map(i => i.closest('.ans-row').querySelector('.ans-q').textContent.slice(0, 70)));
    ikkeOk.forEach(q => feil.push(`${id}: fasiten godtas ikke: «${q}»`));
    if (!(await pg.$eval('#' + id, c => c.classList.contains('done')))) feil.push(`${id}: oppgaven ble ikke markert ferdig`);
    if (bilder) { fs.mkdirSync(bilder, { recursive: true }); await (await pg.$('#' + id)).screenshot({ path: path.join(bilder, id + '.png') }); }
  }
  rapport.fremdrift = await pg.$eval('#progressLabel', e => e.textContent);
  const m = await b.newPage({ viewport: { width: 390, height: 844 } });
  await m.goto(url); await m.waitForTimeout(300);
  for (const id of kort) await m.click(`#${id} .lab-header`);
  const bredde = await m.evaluate(() => document.documentElement.scrollWidth);
  if (bredde > 390) feil.push('mobil: siden er ' + bredde + 'px bred (maks 390)');
} finally { await b.close(); server.kill(); }
console.log(JSON.stringify(rapport, null, 1));
console.log(feil.length ? 'FEIL:\n- ' + feil.join('\n- ') : 'ALT OK');
process.exit(feil.length ? 1 : 0);
