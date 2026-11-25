# Генератор раздела «Статьи»: python3 tools/build_stati.py
import json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://pinkyk.ink"
AV = "https://www.avito.ru/pavlovskaya_sloboda/predlozheniya_uslug/manikyur_pavlovskaya_sloboda_8549696573"
DATE = "2026-11-25"
NB = " "

ARTICLES = [
{
 "slug": "manikyur-s-ukrepleniem-gelem",
 "title": "Маникюр с укреплением гелем: что это, кому подходит и сколько держится",
 "h1": "Маникюр с укреплением гелем",
 "lead": "Почему мастер в Павловской Слободе делает покрытие только на укреплении, чем укрепление отличается от обычного гель-лака и кому оно нужно в первую очередь.",
 "desc": "Что такое укрепление ногтей гелем, чем отличается от гель-лака, кому подходит и сколько держится. Цена в Павловской Слободе — 2 800 ₽.",
 "img": "03",
 "body": """
<p>Укрепление — это тонкий слой геля, который наносится поверх натурального ногтя под цветное покрытие. Он не удлиняет ноготь, а работает как каркас: выравнивает поверхность, распределяет нагрузку и не даёт ногтю гнуться и ломаться.</p>
<h2>Чем укрепление отличается от обычного гель-лака</h2>
<p>Гель-лак — это прежде всего цвет. Он тонкий и гибкий, поэтому на мягких и тонких ногтях со временем начинает «скручиваться» вместе с ногтем: появляются сколы у края и трещины в зоне улыбки.</p>
<p>Гель для укрепления плотнее. Мастер выкладывает им правильную архитектуру — небольшой изгиб в зоне нагрузки, — и ноготь держит форму до самой коррекции. Сверху наносится цвет, поэтому внешне это тот же аккуратный маникюр, только надёжнее.</p>
<h2>Кому особенно подходит</h2>
<ul>
<li>тем, у кого ногти тонкие, мягкие или слоятся;</li>
<li>тем, кто хочет отрастить свою длину без наращивания;</li>
<li>тем, у кого обычный гель-лак не доживает до коррекции;</li>
<li>тем, кто много работает руками и устал от сколов.</li>
</ul>
<h2>Не будет ли «толсто»?</h2>
<p>Нет, если гель распределён правильно. Цель — тонкое покрытие без лишнего объёма: ногти выглядят натурально и изящно, а не «накладными». Толщина набирается только там, где ноготь испытывает нагрузку.</p>
<h2>Сколько держится и когда приходить на коррекцию</h2>
<p>Покрытие аккуратно держится до следующей коррекции. Обычно приходить стоит, когда ноготь отрастает настолько, что у кутикулы становится заметна полоска, — чаще всего это 3–4 недели. Дольше ходить не стоит: центр тяжести смещается к краю, и нагрузка на натуральный ноготь растёт.</p>
<h2>Как проходит процедура</h2>
<ol>
<li>Обработка кутикулы и боковых валиков.</li>
<li>Подготовка ногтевой пластины и выравнивание.</li>
<li>Укрепление гелем с правильной архитектурой.</li>
<li>Цветное покрытие и финиш.</li>
</ol>
<p>В среднем визит занимает около полутора часов: работа идёт без спешки и не на поток.</p>
""",
 "price": [("Укрепление ногтей гелем","2"+NB+"800 ₽"),("Маникюр с покрытием гель-лаком","2"+NB+"500 ₽"),("Снятие гель-лака","500 ₽")],
 "faq": [
  ("Вредно ли укрепление для ногтей?","При правильном снятии — нет. Ноготь не спиливается в ноль: старый материал снимается частично, и новый гель ложится поверх. Это бережнее, чем каждый раз снимать покрытие полностью."),
  ("Можно ли сделать укрепление на коротких ногтях?","Да. Укрепление не меняет длину, его делают и на совсем коротких ногтях — так проще отрастить свою длину."),
  ("Сколько стоит укрепление в Павловской Слободе?","Укрепление ногтей гелем — 2 800 ₽. Новым клиентам — скидка 10% на первый визит."),
 ],
},
{
 "slug": "sterilizaciya-instrumentov-dlya-manikyura",
 "title": "Стерилизация инструментов для маникюра: 3 этапа, о которых стоит спросить мастера",
 "h1": "Как стерилизуют инструменты для маникюра",
 "lead": "Безопасный маникюр начинается не с красивого дизайна, а с обработки инструментов. Рассказываем, из каких этапов она состоит и на что смотреть клиентке.",
 "desc": "Дезинфекция, ультразвуковая очистка и стерилизация: из чего состоит обработка маникюрных инструментов и как понять, что мастер делает это правильно.",
 "img": "05",
 "body": """
<p>Металлические инструменты — кусачки, пушеры, ножницы — контактируют с кожей и могут её травмировать. Поэтому после каждой клиентки они проходят полный цикл обработки. Мастер с медицинским образованием работает по тем же принципам, что и в медицине: обработка состоит из трёх обязательных этапов.</p>
<h2>Этап 1. Дезинфекция</h2>
<p>Сразу после работы инструменты погружают в дезинфицирующий раствор. Он уничтожает большую часть микроорганизмов и делает инструменты безопасными для дальнейшей обработки.</p>
<h2>Этап 2. Ультразвуковая очистка</h2>
<p>В ультразвуковой мойке колебания жидкости выбивают загрязнения из мест, куда не достать щёткой: из шарниров кусачек и мелких насечек. Это предстерилизационная очистка — без неё следующий этап работает хуже.</p>
<h2>Этап 3. Стерилизация</h2>
<p>Чистые сухие инструменты запечатывают в крафт-пакеты и стерилизуют. Стерилизация уничтожает все микроорганизмы, включая споры. Пакет остаётся закрытым до прихода следующей клиентки.</p>
<h2>Что можно проверить самой</h2>
<ul>
<li>Инструменты достают из закрытого крафт-пакета при вас.</li>
<li>Пилки и бафы — новые или одноразовые.</li>
<li>Мастер работает в перчатках и обрабатывает руки перед процедурой.</li>
<li>Рабочее место чистое, без следов предыдущей работы.</li>
</ul>
<p>Если что-то из этого смущает — смело задавайте вопросы. Хороший мастер всегда спокойно расскажет, как обрабатывает инструменты.</p>
""",
 "price": [("Маникюр без покрытия","1"+NB+"300 ₽"),("Аппаратный маникюр","1"+NB+"300 ₽"),("Маникюр с гель-лаком","2"+NB+"500 ₽")],
 "faq": [
  ("Достаточно ли просто протереть инструменты антисептиком?","Нет. Антисептик для кожи не заменяет ни дезинфекцию, ни стерилизацию инструментов."),
  ("Зачем нужен крафт-пакет?","Он сохраняет инструменты стерильными после обработки. Пакет вскрывают непосредственно перед процедурой."),
  ("Как обрабатываются инструменты у мастера в Павловской Слободе?","Полный цикл: дезинфекция, ультразвуковая очистка и стерилизация после каждой клиентки."),
 ],
},
{
 "slug": "naraschivanie-nogtey-formy-i-uhod",
 "title": "Наращивание ногтей: какую форму выбрать, сколько стоит и как ухаживать",
 "h1": "Наращивание ногтей: формы, цена и уход",
 "lead": "Миндаль, квадрат или длинный стилет — разбираемся, какая форма подойдёт под ваш образ, сколько стоит наращивание в Павловской Слободе и как продлить носку.",
 "desc": "Как выбрать форму наращенных ногтей, сколько стоит наращивание и коррекция в Павловской Слободе и как ухаживать за ногтями между визитами.",
 "img": "07",
 "body": """
<p>Наращивание удлиняет ноготь гелем и позволяет сразу получить нужную длину и форму. Это хороший вариант, если свои ногти пока не отросли или хочется длины, которую натуральные ногти не выдерживают.</p>
<h2>Какую форму выбрать</h2>
<ul>
<li><b>Миндаль</b> — визуально вытягивает пальцы и выглядит женственно. Одна из самых универсальных форм.</li>
<li><b>Квадрат и мягкий квадрат</b> — классика под френч, хорошо смотрится на средней длине.</li>
<li><b>Длинный миндаль и стилет</b> — для эффектного образа. Требуют привычки и аккуратности в быту.</li>
</ul>
<p>Если сомневаетесь, начните со средней длины: к ней быстро привыкаешь, а в следующий раз легко сделать длиннее.</p>
<h2>Сколько стоит</h2>
<p>Цена зависит от длины и сложности дизайна. В прайсе мастера наращивание стоит от 3 500 до 7 000 ₽ и занимает около 2,5 часов, коррекция — от 3 000 ₽.</p>
<h2>Как ухаживать между визитами</h2>
<ul>
<li>Используйте масло для кутикулы каждый день — кожа вокруг ногтя остаётся мягкой.</li>
<li>Не используйте ногти как инструмент: не открывайте ими банки и не поддевайте предметы.</li>
<li>Для уборки с бытовой химией надевайте перчатки.</li>
<li>Приходите на коррекцию вовремя — обычно раз в 3–4 недели.</li>
<li>Не снимайте материал самостоятельно: так легко травмировать натуральный ноготь.</li>
</ul>
<h2>Когда лучше выбрать укрепление</h2>
<p>Если длина нужна небольшая, часто хватает укрепления своих ногтей гелем: оно легче и выглядит максимально натурально. На консультации мастер подскажет, что подойдёт именно вам.</p>
""",
 "price": [("Наращивание ногтей","3"+NB+"500–7"+NB+"000 ₽"),("Коррекция наращённых ногтей","от 3"+NB+"000 ₽"),("Снятие наращённых ногтей","600 ₽")],
 "faq": [
  ("Сколько держится наращивание?","До коррекции — обычно 3–4 недели. Дальше ноготь отрастает, и нагрузка смещается к краю."),
  ("Портит ли наращивание ногти?","При аккуратной подготовке и правильном снятии натуральные ногти не страдают. Главное — не снимать материал самой."),
  ("Сколько стоит наращивание в Павловской Слободе?","От 3 500 до 7 000 ₽ в зависимости от длины и дизайна. Коррекция — от 3 000 ₽."),
 ],
},
{
 "slug": "kak-podgotovitsya-k-manikyuru",
 "title": "Как подготовиться к маникюру и продлить носку покрытия: советы мастера",
 "h1": "Как подготовиться к маникюру",
 "lead": "Несколько простых правил до и после визита, которые помогают покрытию держаться дольше, а коже вокруг ногтей — оставаться ухоженной.",
 "desc": "Что сделать до визита к мастеру маникюра и как ухаживать за руками после, чтобы покрытие держалось до коррекции. Советы мастера из Павловской Слободы.",
 "img": "12",
 "body": """
<h2>Перед визитом</h2>
<ul>
<li><b>Не наносите крем на руки</b> в день процедуры: жирная плёнка мешает сцеплению материала с ногтем.</li>
<li><b>Не снимайте старое покрытие сами</b> — мастер снимет его аккуратно и без травм.</li>
<li><b>Подумайте о дизайне заранее.</b> Сохраните пару референсов — так проще договориться о цвете и форме.</li>
<li><b>Скажите мастеру</b>, если ногти недавно ломались, слоятся или есть чувствительность — это поможет подобрать материалы.</li>
</ul>
<h2>После маникюра</h2>
<ul>
<li>Каждый день используйте масло для кутикулы.</li>
<li>Делайте уборку в перчатках: бытовая химия сушит кожу и вредит покрытию.</li>
<li>Не используйте ногти как инструмент.</li>
<li>Если появился скол или трещина — не отрывайте покрытие, лучше напишите мастеру.</li>
</ul>
<h2>Когда приходить снова</h2>
<p>Оптимально — раз в 3–4 недели. Так ноготь не успевает отрасти слишком сильно, а покрытие сохраняет форму и аккуратный вид.</p>
<h2>Сколько длится визит</h2>
<p>Маникюр с укреплением и покрытием занимает в среднем около полутора часов. Запланируйте время с запасом: мастер не работает на поток, и спешить не придётся.</p>
""",
 "price": [("Маникюр с гель-лаком","2"+NB+"500 ₽"),("Укрепление ногтей гелем","2"+NB+"800 ₽"),("Парафинотерапия","300 ₽")],
 "faq": [
  ("Можно ли прийти с покрытием от другого мастера?","Да, снятие гель-лака стоит 500 ₽, а снятие наращённых ногтей — 600 ₽."),
  ("Как записаться?","Напишите мастеру на Авито — она пришлёт свободные окошки и поможет выбрать удобное время."),
 ],
},
]

HEAD_COMMON = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#f4eee8">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://mc.yandex.ru">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/stati/stati.css">
<script>
window.PK_YM_ID=114680630;
(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){if(document.scripts[j].src===r){return;}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})(window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");
ym(114680630,"init",{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/114680630" style="position:absolute;left:-9999px;" alt=""></div></noscript>"""

NAV = f"""<header class="top"><div class="wrap">
  <a href="/" class="brand">Pinky<em>K</em>.ink</a>
  <nav><a href="/#prices">Цены</a><a href="/#works">Работы</a><a href="/stati/">Статьи</a></nav>
  <a class="cta" href="{AV}" data-goal="avito_click" data-place="article_nav" target="_blank" rel="noopener">Записаться</a>
</div></header>"""

FOOT = f"""<footer class="foot"><div class="wrap">
  <div><a href="/" class="brand">Pinky<em>K</em>.ink</a><p>Маникюр и наращивание ногтей в Павловской Слободе · ул. Луначарского, 11, г.о. Истра</p></div>
  <a class="btn" href="{AV}" data-goal="avito_click" data-place="article_footer" target="_blank" rel="noopener">Записаться через Авито →</a>
</div></footer>
<script src="/js/track.js" defer></script>"""

def esc(s): return html.escape(s, quote=True)

def article_page(a, others):
    url = f"{SITE}/stati/{a['slug']}/"
    img = f"{SITE}/img/{a['img']}.jpg"
    ld = {"@context":"https://schema.org","@graph":[
        {"@type":"Article","headline":a["title"],"description":a["desc"],"image":img,
         "datePublished":DATE,"dateModified":DATE,"inLanguage":"ru-RU","mainEntityOfPage":url,
         "author":{"@type":"Person","name":"Катя","jobTitle":"Мастер маникюра"},
         "publisher":{"@type":"Organization","name":"PinkyK.ink","logo":{"@type":"ImageObject","url":SITE+"/icon-512.png"}},
         "about":{"@id":SITE+"/#business"}},
        {"@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Главная","item":SITE+"/"},
            {"@type":"ListItem","position":2,"name":"Статьи","item":SITE+"/stati/"},
            {"@type":"ListItem","position":3,"name":a["h1"],"item":url}]},
        {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":t}} for q,t in a["faq"]]}
    ]}
    price = "".join(f'<div class="pr"><span>{n}</span><b>{p}</b></div>' for n,p in a["price"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(t)}</p></details>" for q,t in a["faq"])
    more = "".join(f'<a class="card" href="/stati/{o["slug"]}/"><img src="/img/{o["img"]}.jpg" alt="" loading="lazy" width="900" height="900"><span>{esc(o["h1"])}</span></a>' for o in others)
    return f"""<!doctype html>
<html lang="ru">
<head>
{HEAD_COMMON}
<title>{esc(a['title'])} | PinkyK.ink</title>
<meta name="description" content="{esc(a['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="ru_RU">
<meta property="og:site_name" content="PinkyK.ink">
<meta property="og:title" content="{esc(a['title'])}">
<meta property="og:description" content="{esc(a['desc'])}">
<meta property="og:image" content="{img}">
<meta property="og:url" content="{url}">
<meta property="article:published_time" content="{DATE}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{NAV}
<main class="wrap art">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a> / <a href="/stati/">Статьи</a></nav>
  <header class="ahead">
    <h1>{esc(a['h1'])}</h1>
    <p class="lead">{esc(a['lead'])}</p>
    <p class="meta">Мастер Катя · медицинское образование, опыт 5+ лет · <time datetime="{DATE}">25 ноября 2026</time></p>
  </header>
  <figure class="cover"><img src="/img/{a['img']}.jpg" alt="{esc(a['h1'])} — работа мастера PinkyK.ink" width="900" height="900"></figure>
  <article class="txt">{a['body']}</article>
  <aside class="box"><h2>Цены в Павловской Слободе</h2>{price}<p class="note">Новым клиентам — скидка 10% на первый визит.</p>
  <a class="btn" href="{AV}" data-goal="avito_click" data-place="article_{a['slug']}" target="_blank" rel="noopener">Записаться через Авито →</a></aside>
  <section class="faq"><h2>Частые вопросы</h2>{faq}</section>
  <section class="more"><h2>Ещё статьи</h2><div class="cards">{more}</div></section>
</main>
{FOOT}
</body>
</html>
"""

def index_page():
    url = SITE + "/stati/"
    ld = {"@context":"https://schema.org","@type":"CollectionPage","name":"Статьи о маникюре","url":url,"inLanguage":"ru-RU",
          "hasPart":[{"@type":"Article","headline":a["title"],"url":f"{SITE}/stati/{a['slug']}/"} for a in ARTICLES]}
    cards = "".join(f'<a class="card big" href="/stati/{a["slug"]}/"><img src="/img/{a["img"]}.jpg" alt="" loading="lazy" width="900" height="900"><span>{esc(a["h1"])}</span><small>{esc(a["lead"])}</small></a>' for a in ARTICLES)
    return f"""<!doctype html>
<html lang="ru">
<head>
{HEAD_COMMON}
<title>Статьи о маникюре и наращивании ногтей | PinkyK.ink</title>
<meta name="description" content="Полезные статьи мастера маникюра из Павловской Слободы: укрепление гелем, стерилизация инструментов, наращивание и уход за ногтями.">
<link rel="canonical" href="{url}">
<meta property="og:title" content="Статьи о маникюре — PinkyK.ink">
<meta property="og:image" content="{SITE}/img/og.jpg">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{NAV}
<main class="wrap art">
  <nav class="crumbs"><a href="/">Главная</a> / Статьи</nav>
  <header class="ahead"><h1>Статьи о маникюре</h1><p class="lead">Отвечаю на вопросы, которые чаще всего задают клиентки: как работает укрепление, как обрабатываются инструменты, какую форму выбрать и как продлить носку.</p></header>
  <div class="cards grid">{cards}</div>
</main>
{FOOT}
</body>
</html>
"""

os.makedirs(os.path.join(ROOT,"stati"), exist_ok=True)
open(os.path.join(ROOT,"stati","index.html"),"w",encoding="utf-8").write(index_page())
for a in ARTICLES:
    d = os.path.join(ROOT,"stati",a["slug"]); os.makedirs(d, exist_ok=True)
    others = [o for o in ARTICLES if o is not a][:3]
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(article_page(a, others))

# sitemap
imgs = [f"{n:02d}" for n in range(1,13)]
urls = [("/", "1.0", imgs), ("/stati/", "0.8", [])] + [(f"/stati/{a['slug']}/", "0.7", [a["img"]]) for a in ARTICLES]
sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
for u,pr,im in urls:
    sm.append(f"<url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod><priority>{pr}</priority>" + "".join(f"<image:image><image:loc>{SITE}/img/{i}.jpg</image:loc></image:image>" for i in im) + "</url>")
sm.append("</urlset>")
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write("\n".join(sm)+"\n")
print("ok", len(ARTICLES))
