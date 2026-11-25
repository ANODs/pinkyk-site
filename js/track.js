/* Цели Яндекс Метрики: клики по кнопкам записи и соцсетям, просмотр работ, вопросы */
(function () {
  var ID = window.PK_YM_ID;
  function goal(name, params) {
    if (ID && typeof window.ym === 'function') window.ym(ID, 'reachGoal', name, params || {});
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-goal]');
    if (a) goal(a.getAttribute('data-goal'), { place: a.getAttribute('data-place') || '' });
    var f = e.target.closest('#filters button');
    if (f) goal('works_filter', { filter: f.getAttribute('data-f') });
    var tile = e.target.closest('.bento .c:not(.vid)');
    if (tile) goal('photo_open', { photo: (tile.querySelector('img') || {}).alt || '' });
  });
  document.querySelectorAll('.faq details').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) goal('faq_open', { q: d.querySelector('summary').textContent.trim() });
    });
  });
  var map = document.querySelector('.contact .map');
  if (map && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { goal('map_view'); io.disconnect(); }
    }, { threshold: 0.6 });
    io.observe(map);
  }
})();
