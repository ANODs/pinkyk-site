/* PinkyK.ink — motion */
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var intro = document.getElementById('intro');
  function done() { root.classList.add('ready'); root.classList.remove('js'); }

  if (!window.gsap || !window.ScrollTrigger || !window.SplitText || reduce) {
    if (intro) intro.remove();
    done();
    return;
  }

  gsap.registerPlugin(ScrollTrigger, SplitText, CustomEase);
  CustomEase.create('out', '0.16,1,0.3,1');
  CustomEase.create('io', '0.77,0,0.18,1');
  gsap.defaults({ ease: 'out', duration: 1.2 });

  var fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var PK = (window.PK = {});

  /* native scroll; anchors glide with the browser's own smooth scroll */
  document.documentElement.style.scrollBehavior = 'smooth';

  var fontsReady = document.fonts && document.fonts.ready
    ? Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 1500); })])
    : Promise.resolve();

  fontsReady.then(init);

  function lines(el, opts) {
    return SplitText.create(el, Object.assign({ type: 'lines', mask: 'lines', linesClass: 'sl', autoSplit: true }, opts || {}));
  }

  function init() {
    /* ---------- HERO ---------- */
    var hero = document.querySelector('.hero');
    var h1Lines = hero.querySelectorAll('h1 .ln > span');
    var sub = hero.querySelector('.h1sub');
    var lead = hero.querySelector('.hero-mid p');
    var ctas = hero.querySelectorAll('.hero-cta .btn');
    var figs = hero.querySelectorAll('.stack figure');

    var subSplit = lines(sub);
    var leadSplit = lines(lead);

    var heroTl = gsap.timeline({ paused: true });
    heroTl
      .fromTo(h1Lines, { yPercent: 115, rotate: 3 }, { yPercent: 0, rotate: 0, duration: 1.5, stagger: 0.11 }, 0)
      .fromTo(subSplit.lines, { yPercent: 110 }, { yPercent: 0, duration: 1.1, stagger: 0.06 }, 0.15)
      .fromTo(figs, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.5, ease: 'io', stagger: 0.14 }, 0.25)
      .fromTo(hero.querySelectorAll('.stack img'), { scale: 1.4 }, { scale: 1, duration: 2, stagger: 0.14 }, 0.25)
      .fromTo(leadSplit.lines, { yPercent: 110 }, { yPercent: 0, duration: 1.1, stagger: 0.07 }, 0.5)
      .fromTo(ctas, { y: 28, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.1, stagger: 0.08 }, 0.7)
      .fromTo('.nav', { y: -30, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.2, clearProps: 'transform' }, 0.6);

    /* hero parallax */
    if (window.innerWidth > 900) {
      [['.f1', -6], ['.f2', -26], ['.f3', -48]].forEach(function (p) {
        gsap.to(hero.querySelector('.stack ' + p[0]), { yPercent: p[1], ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
      });
      gsap.to(hero.querySelector('h1'), { yPercent: -12, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
    }

    /* ---------- generic reveals ---------- */
    document.querySelectorAll('[data-split]').forEach(function (el) {
      SplitText.create(el, {
        type: 'lines', mask: 'lines', linesClass: 'sl', autoSplit: true,
        onSplit: function (self) {
          return gsap.fromTo(self.lines, { yPercent: 110, rotate: 2.5 }, { yPercent: 0, rotate: 0, duration: 1.4, stagger: 0.09, scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
        }
      });
    });

    function up(targets, trigger, opts) {
      var t = gsap.utils.toArray(targets);
      if (!t.length) return;
      gsap.fromTo(t, { y: 40, autoAlpha: 0 }, Object.assign({ y: 0, autoAlpha: 1, duration: 1.1, stagger: 0.08, scrollTrigger: { trigger: trigger || t[0], start: 'top 88%', once: true } }, opts || {}));
    }
    function draw(targets, trigger, opts) {
      var t = gsap.utils.toArray(targets);
      if (!t.length) return;
      gsap.fromTo(t, { '--w': '0%' }, Object.assign({ '--w': '100%', duration: 1.4, ease: 'io', stagger: 0.06, scrollTrigger: { trigger: trigger || t[0], start: 'top 90%', once: true } }, opts || {}));
    }

    gsap.utils.toArray('.kicker').forEach(function (k) { up(k, k, { y: 16 }); });

    /* ---------- MANIFESTO: words light up on scroll ---------- */
    var big = document.querySelector('.mani .big');
    if (big) {
      SplitText.create(big, {
        type: 'words', wordsClass: 'w', autoSplit: true,
        onSplit: function (self) {
          var tl = gsap.timeline({ scrollTrigger: { trigger: big, start: 'top 80%', end: 'bottom 45%', scrub: 0.6 } });
          tl.fromTo(self.words, { opacity: 0.12 }, { opacity: 1, stagger: 0.1, ease: 'none', duration: 0.4 }, 0);
          tl.fromTo(big.querySelectorAll('.ph'), { scale: 0, rotate: -12 }, { scale: 1, rotate: 0, ease: 'back.out(2)', duration: 0.8, stagger: 1.4 }, 0.2);
          return tl;
        }
      });
    }

    /* stats: count up */
    var stats = document.querySelectorAll('.stats > div');
    up(stats, '.stats', { stagger: 0.1 });
    stats.forEach(function (d, i) {
      var b = d.querySelector('b');
      var node = b && b.firstChild;
      if (!node || node.nodeType !== 3) return;
      var raw = node.nodeValue.trim();
      var dec = raw.indexOf(',') > -1 ? raw.split(',')[1].length : 0;
      var target = parseFloat(raw.replace(',', '.'));
      var o = { v: 0 };
      node.nodeValue = (0).toFixed(dec).replace('.', ',');
      gsap.to(o, {
        v: target, duration: 2, delay: i * 0.1, ease: 'power3.out',
        scrollTrigger: { trigger: '.stats', start: 'top 88%', once: true },
        onUpdate: function () { node.nodeValue = o.v.toFixed(dec).replace('.', ','); }
      });
    });

    /* ---------- WHY: panel opens, rows draw ---------- */
    var why = document.querySelector('.why');
    gsap.fromTo(why, { clipPath: 'inset(0% 4% 0% 4% round 48px)' }, { clipPath: 'inset(0% 0% 0% 0% round 28px)', ease: 'none', scrollTrigger: { trigger: why, start: 'top bottom', end: 'top 25%', scrub: true } });
    gsap.utils.toArray('.acc .it').forEach(function (it) {
      draw(it, it, { duration: 1.6 });
      gsap.fromTo(it.children, { y: 34, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.1, stagger: 0.08, scrollTrigger: { trigger: it, start: 'top 90%', once: true } });
    });

    /* ---------- WORKS: tiles wipe in ---------- */
    up('#filters button', '#filters', { y: 16, stagger: 0.05 });
    var tiles = gsap.utils.toArray('.bento .c');
    gsap.set(tiles, { clipPath: 'inset(100% 0% 0% 0% round 22px)' });
    ScrollTrigger.batch(tiles, {
      start: 'top 92%', once: true,
      onEnter: function (batch) {
        gsap.to(batch, { clipPath: 'inset(0% 0% 0% 0% round 22px)', duration: 1.4, ease: 'io', stagger: 0.09 });
        gsap.fromTo(batch.map(function (c) { return c.querySelector('img,video'); }), { scale: 1.35 }, { scale: 1, duration: 1.9, stagger: 0.09, clearProps: 'transform' });
      }
    });
    up('.works .foot > *', '.works .foot');
    PK.filtered = function (visible) {
      gsap.fromTo(visible, { autoAlpha: 0, y: 24, scale: 0.97 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.8, stagger: 0.04, clipPath: 'inset(0% 0% 0% 0% round 22px)', overwrite: true });
      ScrollTrigger.refresh();
    };

    /* ---------- PRICES ---------- */
    gsap.utils.toArray('.prices .side p').forEach(function (p) {
      var sp = lines(p);
      gsap.fromTo(sp.lines, { yPercent: 110 }, { yPercent: 0, duration: 1.1, stagger: 0.07, scrollTrigger: { trigger: p, start: 'top 90%', once: true } });
    });
    up(['.prices .sale', '.prices .side .btn'], '.prices .sale');
    gsap.utils.toArray('.grp').forEach(function (g) {
      draw(g.querySelector('h3'), g);
      up(g.querySelector('h3'), g, { y: 12 });
      var rows = g.querySelectorAll('.pr');
      draw(rows, g, { stagger: 0.07 });
      gsap.fromTo(rows, { y: 22, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1, stagger: 0.07, scrollTrigger: { trigger: g, start: 'top 85%', once: true } });
    });

    /* ---------- REVIEW ---------- */
    var card = document.querySelector('.rev .card');
    gsap.fromTo(card, { scale: 0.86, borderRadius: 80 }, { scale: 1, borderRadius: 28, ease: 'none', scrollTrigger: { trigger: card, start: 'top bottom', end: 'top 35%', scrub: true } });
    var bq = lines(card.querySelector('blockquote'));
    gsap.fromTo(bq.lines, { yPercent: 110 }, { yPercent: 0, duration: 1.3, stagger: 0.09, scrollTrigger: { trigger: card, start: 'top 70%', once: true } });
    gsap.fromTo(card.querySelector('.q'), { yPercent: 40, rotate: -20, autoAlpha: 0 }, { yPercent: 0, rotate: 0, autoAlpha: 1, duration: 1.4, scrollTrigger: { trigger: card, start: 'top 70%', once: true } });
    up(card.querySelectorAll('cite > *'), card, { delay: 0.5, scrollTrigger: { trigger: card, start: 'top 70%', once: true } });

    /* ---------- FAQ ---------- */
    var qs = gsap.utils.toArray('.faq details');
    draw(qs, '.faq .qs', { stagger: 0.08 });
    gsap.fromTo(qs, { y: 26, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1, stagger: 0.07, scrollTrigger: { trigger: '.faq .qs', start: 'top 85%', once: true } });
    qs.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (d.open) gsap.fromTo(d.querySelector('p'), { y: -8, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.7 });
        ScrollTrigger.refresh();
      });
    });

    /* ---------- CONTACT ---------- */
    up('.contact .ways > *', '.contact .ways', { y: 50, stagger: 0.1 });
    var map = document.querySelector('.contact .map');
    gsap.fromTo(map, { clipPath: 'inset(0% 0% 100% 0% round 24px)' }, { clipPath: 'inset(0% 0% 0% 0% round 24px)', duration: 1.6, ease: 'io', scrollTrigger: { trigger: map, start: 'top 88%', once: true } });
    var sign = document.querySelector('#sign svg');
    if (sign) {
      var vb = sign.viewBox.baseVal;
      gsap.fromTo(sign.querySelectorAll('.ch'), { y: vb.height }, {
        y: 0, ease: 'none', stagger: 0.06,
        scrollTrigger: { trigger: sign, start: 'top bottom', end: 'bottom bottom', scrub: 0.8 }
      });
    }

    /* ---------- nav hide/show ---------- */
    var nav = document.querySelector('.nav');
    ScrollTrigger.create({
      start: 'top -120',
      onUpdate: function (self) { nav.classList.toggle('hid', self.direction === 1 && self.scroll() > 400); }
    });

    /* ---------- desktop niceties ---------- */
    if (fine) {
      document.querySelectorAll('.btn, .nav .cta, .way .go').forEach(function (el) {
        var xTo = gsap.quickTo(el, 'x', { duration: 0.6, ease: 'power3.out' });
        var yTo = gsap.quickTo(el, 'y', { duration: 0.6, ease: 'power3.out' });
        el.addEventListener('mousemove', function (e) {
          var r = el.getBoundingClientRect();
          xTo((e.clientX - r.left - r.width / 2) * 0.22);
          yTo((e.clientY - r.top - r.height / 2) * 0.32);
        });
        el.addEventListener('mouseleave', function () {
          gsap.to(el, { x: 0, y: 0, duration: 1, ease: 'elastic.out(1,0.4)' });
        });
      });

      /* "Смотреть" cursor: state is derived from what is under the pointer,
         so it can never get stuck when tiles move, hide or the lightbox opens */
      var cur = document.getElementById('cur');
      var cx = gsap.quickTo(cur, 'x', { duration: 0.45, ease: 'power3.out' });
      var cy = gsap.quickTo(cur, 'y', { duration: 0.45, ease: 'power3.out' });
      var px = -1, py = -1, shown = false;
      function setCur(on) {
        if (on === shown) return;
        shown = on;
        gsap.to(cur, on ? { scale: 1, duration: 0.5, ease: 'back.out(1.8)', overwrite: true }
                        : { scale: 0, duration: 0.3, ease: 'power2.in', overwrite: true });
      }
      function check() {
        if (px < 0 || document.getElementById('lb').classList.contains('open')) return setCur(false);
        var el = document.elementFromPoint(px, py);
        var tile = el && el.closest('.bento .c');
        setCur(!!(tile && !tile.classList.contains('vid') && !tile.classList.contains('hide')));
      }
      window.addEventListener('mousemove', function (e) { px = e.clientX; py = e.clientY; cx(px); cy(py); check(); }, { passive: true });
      window.addEventListener('scroll', check, { passive: true });
      document.addEventListener('click', function () { setTimeout(check, 0); });
      document.documentElement.addEventListener('mouseleave', function () { px = -1; setCur(false); });
      window.addEventListener('blur', function () { setCur(false); });
    }

    /* ---------- start ---------- */
    done();
    var seen = false;
    try { seen = sessionStorage.getItem('pk-intro') === '1'; sessionStorage.setItem('pk-intro', '1'); } catch (e) {}

    if (!intro || seen || window.scrollY > 50) {
      if (intro) intro.remove();
      heroTl.play(0);
    } else {
      document.documentElement.style.overflow = 'hidden';
      var w = intro.querySelector('.intro-w span');
      gsap.timeline({ onComplete: function () { intro.remove(); document.documentElement.style.overflow = ''; } })
        .fromTo(w, { yPercent: 110 }, { yPercent: 0, duration: 1.1 }, 0.1)
        .to(intro.querySelector('.intro-bar i'), { scaleX: 1, duration: 1.1, ease: 'io' }, 0.1)
        .to(w, { yPercent: -110, duration: 0.8, ease: 'io' }, 1.25)
        .to(intro, { yPercent: -100, duration: 1.1, ease: 'io' }, 1.4)
        .add(function () { heroTl.play(0); }, 1.75);
    }
    ScrollTrigger.refresh();
  }
})();
