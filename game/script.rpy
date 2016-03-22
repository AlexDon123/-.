# Вы можете расположить сценарий своей игры в этом файле. 


# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"
init:
    $ sl_love = 0
    $ el_happy = 0
    $ un_love = 0
    $ mz_book = 0
    $ dv_happy = 0
    $ us_happy = 0
    $ dv_trust = 0
    $ uv_trust = 0
    
    $ mods["shurick"] = u"Шурик и все все все"
    
    $ treck_op = "music_list/Doctor Who - Doomsday Theme - Doomsday Theme.mp3"
    $ aha_takeonme = "music_list/aha_takeonme.mp3"
    $ pioneer_theme = "music_list/TheCinematics(cover by Pureform).mp3"
    $ alex_theme = "music_list/The Cinematics - Break.mp3"
    $ alex_mind = "music_list/TG Project - Dreaming.mp3"
    $ Freedom = "music_list/TG Project - Solitude.mp3"
    $ Freedom_2 = "music_list/GorthHaur - TG Project - Solitude.mp3"
    $ Memory = "music_list/TG Project - Do you remember .mp3"
    $ semion_theme = "music_list/Кукрыниксы-_skoro_konchitsya_leto_viktor_tsoy_i_gr.kino_(zaycev.net).mp3"
    $ painful_truth = "music_list/TG Project - Blow With The Fires (BAaD cover).mp3"
    $ good_rage = "music_list/Keith Merrow - Put mayones on it.mp3"
  
    $ trio_guitar = "music_list/Ten_Years_After_-_I'D_Love_To_Change_The_World_(-).mp3"
    
    image pioneer normal = "pics/pioneer_1_normal.png"
    image pi normal1 = "pics/pi_1_normal.png"
    image pi smile = "pics/pi_1_pioneer_smile.png"
    image pi rage = "pics/pi_1_pioneer_rage.png"
    image pioneer shadow = "pics/pioneer_shad.png"
    image alex home night = "pics/int_extra_house.jpg"
    image alex home day = "pics/int_extra_house_day.jpg"
    image un home night = "pics/ext_house_of_un_nightF.jpg"
    image ext_square_old = "pics/ext_square_old.jpg"
    image monster = "pics/uv_3_ shade.png"
    image monster_light = "pics/uvshade.png"
    image cs_close = "pics/cs_1_close.png"
    image cs_lust = "pics/cs_1_lst.png"
    image un_night = "pics/un_2_body_cry_night.png"
    image sh_unknown = "pics/sh_unknown.png"
    image mt_young = "pics/mt_young.png"

    
    
    image mz normal nm far = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0),"pics/mz_1_mn.png",(0,0), "images/sprites/far/mz/mz_1_normal.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    image sl smile body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image sl surprise body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image sl angry body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    image dv surprise ex = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "pics/dv_1_ex.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv smile body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv cry2 pioneer = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "pics/dv_1_cry_close.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    image un shy pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "pics/un_1_pl.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un normal pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "pics/un_1_pl.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un angry body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un angry pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "pics/un_1_pl.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un smile pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "pics/un_1_pl.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un cry pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "pics/un_2_pl.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un scared pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "pics/un_2_pl.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un shocked pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "pics/un_2_pl.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un cle pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "pics/un_2_pl.png",(0,0), "pics/un_2_cle.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image un clcr pl = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "pics/un_2_pl.png",(0,0), "pics/un_2_cle_2.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    image mt smile swim = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt grin swim = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "pics/mt_3_swim.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt smile body = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt shy swim = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "pics/mt_1_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt shy pioneer = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "pics/mt_1_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt pl pioneer = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "pics/mt_2_pl.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt pl bra = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "pics/mt_2_bra.png",(0,0), "pics/mt_2_pl.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt angry bra = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "pics/mt_2_bra.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt rage bra = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "pics/mt_2_bra.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt grin bra = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "pics/mt_3_bra.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image mt like swim = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "pics/mt_3_swim.png",(0,0), "pics/mt_3_like.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    
    
    $mod_tags["shurick"] = ["length:days","gameplay:vn","protagonist:male","special:TODO","character:Виола","character:Алиса","character:Электроник","character:Семён","character:Мику","character:Ольга Дмитриевна","character:Женя","character:Шурик","character:Славя","character:Лена","character:Ульяна"]

# Определение персонажей игры.


# Игра начинается здесь.
label shurick:
    "Мод на ранней стадии разработки"
    
    $ renpy.pause(5)
    scene prolog_1
    play music treck_op fadein 3
    $ persistent.sprite_time = 'day'
   

    sh "Пионерский лагерь..."
    sh "Сколько я в нём уже провёл?"
    sh "Год? 2? Тысячу...."
    sh "Неважно..."
    sh "Слишком много,{w} чтобы запомнить."
    sh "Вечность с пионерами..."
    sh "Вечность в одиночестве..."
    sh "Они — куклы, марионетки."
    show sl serious pioneer
    sh "Отзывчивая Славя,{w} голубые глаза, да коса-до-пояса."
    sh "Прямо идеал, шаблон."
    sh "Дотошная активистка,{w} красавица и спортсменка.{w} Прямо святая."
    hide sl serious pioneer
    show dv angry pioneer
    sh "Алиса.{w}Вечная бунтарка,{w}не-такая-как-все"
    sh "Пытается выделиться{w} любыми средствами."
    sh "Не хватает только татуировок{w} и кольца в носу."
    hide dv angry pioneer
    show us fear pioneer
    sh "Маленькая Уля."
    sh "Прекрасное беззаботное детство в вакууме.
    {w}Причём вакуум у неё в голове."
    hide us fear pioneer
    show un angry pioneer
    sh "Лена..."
    sh "«Ой, я такая несча-а-астная.»"
    sh "«Такая одино-о-окая.»"
    sh "«Кто же меня уте-е-ешит?»" 
    sh "А сама кого хочешь с ума сведёт."
    hide un angry pioneer
    show mi cry pioneer
    sh "Мику. Необычная внешность,{w} да ещё и певица-актриса."
    sh "Ну просто источает индивидуальность,{w} до тошноты..."
    sh "И от её болтовни голова болит."
    hide mi cry pioneer
    show mz normal glasses  pioneer
    sh "Женя. Вся из себя строгая,{w} серьёзная,{w} спокойная."
    sh "А я-то всё знаю."
    sh "Ох и намучается с тобой Эл, {w}если доживёт."
    hide mz normal pioneer
    show mt normal pioneer
    sh "Ольга Дмитриевна.{w}Вечная мать всея лагеря, {w}хотя не намного от нас и ушла."
    sh "Ещё хватает же ей совести нас отчитывать."
    sh "Лицемерка..."
    hide mt normal pioneer
    show el normal pioneer
    sh "Сыроежкин.{w}Романтик и неудачник."
    sh "Но не всё с тобой потеряно."
    hide el normal pioneer
    sh "И ты..."
    show pioneer normal
    sh "Семён..."
    sh "В тебе нет ровным счётом ничего."
    sh "Обычный,{w} простой,{w} непримечательный.{w} Пожалуй даже слишком."
    sh "Может быть этим ты и заслужил «честь» быть основой этого лагеря?"
    sh "Обычный парень,{w} который ищет себя,{w} и не может найти."
    sh "..."
    sh "Будь ты проклят."
    hide pioneer normal
    "..."
    "Спокойно Сань,{w} не теряй контроль."
    "Твои поиски близки к завершению,{w} осталось совсем немного,{w} ещё чуть-чуть."
    "Ты сможешь найти выход."
    "Ты единственный,{w} кто на это способен.{w} Не в первый раз уже ты прыгаешь в лагерь."
    "Подумаешь, ещё месяц в этих декорациях,{w} 30 одинаковых завтраков и обедов."
    "Ты вытерпишь,{w} ибо на тебя надеются эти люди."
    "Не эти куклы..."
    "А живые..."
    show sl serious pioneer with moveinleft 
    show sl smile pioneer with dissolve
    hide sl smile pioneer with dissolve
    "Реальные..."
    show dv angry pioneer with moveinright 
    show dv smile pioneer with dissolve
    hide dv smile pioneer with dissolve
    "Любящие..."
    show un angry pioneer with moveinleft 
    show un shy pioneer with dissolve
    hide un shy pioneer with dissolve
    "Добрые люди."
    show us fear pioneer with moveinright 
    show us laugh pioneer with dissolve
    hide us laugh pioneer with dissolve
    "Которые заперты и не найдут выход сами."
    show mi cry pioneer with moveinleft 
    show mi happy pioneer with dissolve
    hide mi happy pioneer with dissolve
    "После стольких лет поисков..."
    show mt sad pioneer with moveinright 
    show mt grin pioneer with dissolve
    hide mt grin pioneer with dissolve
    "Отчаяния и пустоты... Я наконец-то вижу финиш."
    show bg ext_camp_entrance_night with dissolve
    show prologue_dream with dissolve
    "«Совёнок», в который приедет Он."
    "Настоящий,{w} но увы, не единственный."
    "И будь Я проклят, если не заставлю тебя освободить нас."
    "Я помогу тебе"
    "Я направлю тебя, иначе и быть не может."
    "Готовься..."
    "Ладно. Посторонние мысли в сторону."
    show blink
    "Закрыть глаза,{w} увидеть цель,{w} сконцентрироваться..."
    hide prologue_dream 
    "..."
    hide blink
    show unblink
    "Провода прямо перед мной."
    "Напряжение в норме,{w} не убьёт."
    "Как говорится"
    "Поехали!!"
    stop music fadeout 3
    play sound sfx_bodyfall_1


    $ backdrop = "3 дня до приезда"
    $ new_chapter(-3, u"3 дня до приезда")
    scene int_clubs_male2_night with dissolve
    play music music_list["my_daily_life"] fadein 3
    
    $ persistent.sprite_time = 'day'
    $ day_time()

    el "Сань, Сань!{w} Ты там уснул чтоли?"
    "Услышал я голос Эла из комнаты."
    el "Ну как так?! Пошёл за припоем,{w} это же минутное дело, и пропал?!"
    sh "Нет, не уснул. Из-за этих мешков не пролезть! Иду."
    "Ну здравствуй недоЭл, {w}век бы тебя не видеть."
    "Хммм, припой в руке."
    "Значит тут они усиленно работают над своим проектом."
    "Это хорошо,{w} даже замечательно."
    "Можно будет запереть двери,{w} и идти по своим делам,"
    "А о нас даже не вспомнят."
    "Но надо будет Эла сбагрить,{w} а то ведь не отстанет."
    "Первым делом надо узнать,{w} как он тут с библиостервой ладит."
    "Я вышел из кладовой и замер."
    scene d5_clubs_robot with fade3
    "На столе стоял почти законченный робот."
    play sound sfx_scary_sting
    "\"Так.{w} Стоп.{w} Какой робот?\""
    "Вдруг остановил я себя."
    "\"Какой робот в начале смены?{w} Этого быть не может.\""
    "Или я ошибся с местом..."
    scene int_clubs_male_day with dissolve
    "Или я оказался тут не просто так."
    "Робот почти готов,{w} а это было под конец 2й недели."
    "Почему сейчас?{w} Я ведь планировал на 2й или 3й день."
    "Неужели...{w} из-за НЕГО?!"
    "Видя мой бледный вид, Эл удивился."
    show el upset pioneer with dissolve
    el "Шур, ну что ты так разволновался! Мы столько трудились!"
    el "Он не может не заработать."
    "Тараторил он."
    show el smile pioneer with dspr
    el "Вот ещё немного осталось, и можем на ВДНХ вести!"
    sh "Да... точно."
    "Пробурчал я."
    "Такая промашка по времени немного выбила меня из себя."
    sh "Вот, держи.{w} Ты подготовил плату контроллера?{w} Проверил?"
    "Передав то,{w} зачем ходил, я осмотрел наш проект."
    el "Да, всё в лучшем виде."
    show el normal pioneer with dspr
    el "Сейчас подпаяем выходы, и можно устанавливать."
    sh "Хорошо. Если всё в порядке, сегодня и запустим."
    show el smile pioneer with dspr
    el "Ого, у тебя хорошее предчувствие?"
    sh "Не, просто уверен."
    "Конечно уверен,{w} в сотый раз запустим, {w}и в сотый раз за огнетушителем побежим."
    show el normal pioneer with dspr
    "Эл доделывал последние штрихи,{w} а я проверил контакты."
    "Целые,{w} хорошо сделаны.{w} Мы столько трудились над этой машиной, что я знаю её просто наизусть. "
    "И когда она загорится, я спокойно определю неисправность по запаху и времени возгорания."
    "Она всегда горит.{w} Без исключений и отсрочек."
    "Видимо, тут ничего нельзя создать,{w} поскольку это место не способно поддерживать что-либо, кроме иллюзий и мыслей."
    "Пока я размышлял, Эл закончил свой сизифов труд,{w} и подошёл к роботу."
    show el serious pioneer with dspr
    "Я взял плату и полез внутрь робота,{w} чтобы завершить обречённый монтаж обречённой  машины."
    "Жаль, таки сколько срэдств и сил зря пропадает."
    "И вот всё готово."
    stop music
    play music music_list["awakening_power"] fadein 2
    "Мы с Элом переглянулись."
    "Он приготовился включать питание,{w} а я осуществлять экстренное пожаротушение и оказание первой помощи."
    "Щелчок..."
    stop music
    play music music_list["doomed_to_be_defeated"] fadein 2
    "Но произошло то,{w} чего я никак не ожидал."
    "Робот заработал."
    show el surprise pioneer with dspr
    stop music
    play music aha_takeonme 
    "Спокойный,{w} приятный гул моторчиков,{w} и показания на приборах говорили о полной исправности."
    show el smile pioneer with dspr
    el "Урааа!! Работает!"
    sh "Фуф, ну наконец-то! ДА!!!"
    "Робот работает, по крайней мере, так как уже сделали.{w} Он работает. Первый раз за всё время."
    "За все эти циклы,{w} за все эти года...{w} эти жизни."
    "Значит, ЭТОТ лагерь не простой."
    "Значит, я прав."
    "Эта мысль так обрадовала меня,{w} что я  просто не находил себе места от счастья."
    "Это был успех,{w} полный и безоговорочный."
    "И тут краем глаза я заметил макушку в окне."
    "Точнее две."
    sh "Кто там?"
    hide el smile pioneer with dissolve
    "Тихо подкравшись к подоконнику,{w} выглянул на улицу."
    "Ну как и ожидал:{w} Уля и Алиска."
    show dv scared pioneer close at center with dspr
    show us fear pioneer close at right with dspr
    sh "А что это вы тут делаете?{w} Кина не будет!"
    show us grin pioneer  at right with dissolve
    us "Ой, а как ты нас увидел?"
    show dv angry pioneer  at center with dissolve
    dv "Четырёхглазый, ты что пугаешь, а?"
    "\"Как много вопросов, как мало патронов,{w} т.е. ответов\""
    sh "Девочки, мы тут немного заняты.{w} Эксперимент по осваиванию робототехники в отдельно взятом пионерлагере."
    "\" Надеюсь, это собьёт их с толку,{w}  и я их спроважу.\""
    sh "Так что не мешайте,{w} а лучше помогите."
    show dv grin pioneer  at center with dspr
    dv "Ой,{w} делать нам больше нечего,{w} чем с вами, электрическими, такой день проводить..."
    dv "Нас Дмитривна за вами послала, что бы вы на обед не опоздали."
    sh "А Славя?{w} Или ты тоже теперь доверенное лицо?"
    show dv rage pioneer  at center with dspr
    "Сань, нарываешься на грубости, не горячись..."
    "Алиса посмотрела на меня, как львица смотрит на добычу,{w} но промолчала."
    "Скорее всего пакость сделает,{w} но меня не проведёшь.{w} Я знаю все твои розыгрыши."
    us "А Славя занята сильно.{w} А мне интересно стало, вы ведь весь день не вылазите из своей каморки."
    sh "И ты вызвалась?"
    us "Ага, интерееесно у вас. То огонь, то искры."
    show dv grin pioneer  at center with dspr
    dv "Так, мы вам передали, и мы пошли.{w}А вы давайте идите до столовой. Или ты хочешь сказать,{w} что я просто так к вам пришла?"
    sh "Хорошо,хорошо. Идём."
    us "И не опаздывайте! Ольга Дмитриевна сказала, чтоб были вовремя."
    "Есть совершенно не хотелось,{w} но во избежание лишнего внимания мы с Элом засобирались в столовую. Верный способ не опоздать -{w} прийти заранее."
    play sound sfx_dinner_horn_processed 
    "В самый раз."
    "Как раз вовремя. Придём первыми, первыми и уйдём."
    "Обычно так и происходит:{w} мы в первых рядах, быстро едим и уходим к себе. {w}Но сейчас я не был так уверен."
    scene ext_dining_hall_away_day with dissolve
    stop music
    play music music_list["everyday_theme"] fadein 2
    "Та же самая надоевшая столовая."
    "Все как обычно."
    "Плетясь как зомби на приём пищи,{w} ставшей уже невмоготу,{w} решил обратить внимание на пионэров, идущих в столовку."
    "Идут неспешно, переговариваются,{w}смеются."
    "Послышался гомон - видать {w} малышня в хорошем настроении."
    "На подходе стали мелькать знакомые лица."
    show sl smile pioneer at cright with dissolve
    "Славя..."
    hide sl smile pioneer at cright with dissolve
    show un normal pioneer at center with dissolve
    "Лена..."
    hide un normal pioneer at center with dissolve
    show mi serious pioneer at cleft with dissolve
    "Мику..."
    hide mi serious pioneer at cleft with dissolve
    show mz bukal glasses pioneer at left with dissolve
    "Женя..."
    hide mz bukal glasses pioneer at left with dissolve
    "Увидев библиотекаршу, {w} Эл густо покраснел. Прям как Лена, ты глянь.{w} И уставился на дорогу."
    "Взглянув на товарища, я спросил:"
    sh "Эл,{w} а тебе кто-нибудь нравится из здешних пионерок?"
    "Бедняга. Таким красным я его ещё не видел. "
    "Я всегда задаю этот вопрос. И реакция всегда одна и та же."
    sh "Ну, не молчи!"
    show el upset pioneer with dissolve
    el "Я бы хотел чтобы это осталось тайной."
    sh "Конечно-конечно. Только между нами."
    "И сейчас ты промямлишь шопотом \"Жееееееняяя.....\" и умолкнешь."
    show el angry pioneer with dspr
    el "Женя.{w}  Такая красивая и умная. {w} Думаю, приглашу её на танцы."
    "Опаньки. {w} Это новенькое. {w} Такой ответ меня удивил.{w} Новое развитие событий.{w} Если уже тут такие различия, то что будет дальше?"
    "Как мне подготовить и подготовиться?{w} Значит ли это, что тут все будут реагировать по-другому?{w} Более активно, живее? {w}Действовать не по шаблону?"
    "Чёрт, значит все мои воспоминания тут не пригодятся.{w} Надо действовать осмотрительнее.{w} А может стоит..."
    "Решив долго не думать, я помахал рукой девочкам. {w} Те переглянулись, зашептались, но помахали нам в ответ,  {w}хотя Лена и Женя явно не горели желанием."
    show un shy pioneer at right with dissolve
    hide un shy pioneer at right with dissolve
    show mz shy glasses pioneer at left with dissolve
    hide mz shy glasses pioneer at left with dissolve
    "Хех, вышло забавно. {w}  Эл смотрит на меня глазами, {w} полными ужаса и восхищения. {w} Дар речи не наблюдается. Надо выводить его из этого состояния."
    show el scared pioneer with dspr
    sh "Что ты смотришь на меня, как Генда на буржуазию? {w} Ты же собираешься с Женей познакомиться поближе? {w} Начнём вместе."
    el "Саня, ты что творишь? Успокойся!"
    scene ext_dining_hall_near_day with dissolve
    show el scared pioneer at right 
    "Эл заметно нервничал, и отчаянно пытался меня заткнуть.{w} Но Остапа понесло."
    sh "Спокойно,{w} сейчас на обеде я тебя к ней подсажу, {w} поговорите."
    "Не унимался я, и не терпящим возражений взглядом уставился на своего попутчика."
    "Тот лишь жалобно хмыкнул, собираясь с силами для - возможно - самого важного действия в своей жизни."
    "На подходе к столовой Ольга Дмитриевна заметила нас и сконцентрировала внимание на томате рядом со мной."
    show mt normal panama pioneer with dissolve
    mt "Саш, что с твоим «оруженосцем»?"
    sh "Перетрудился на благо Родины."
    "Вожатая посмотрела на нас оценивающе-укоризненным взглядом, но ничего не сказала."
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    "Окинув взглядом столовую, я заметил 2 свободных места - у библиотекарши и у Слави. "
    "Думать надо быстро."
    menu:
        "Сесть со Славей":
            jump slavia_dinner1
        "Сесть с Женей":
            jump zhenia_dinner
label slavia_dinner1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    "Зная Эла, его застенчивость и нерешительность, {w}я решил помочь ему и со спокойным лицом подсел к Славе. "
    "Электроник посмотрел на меня обречённым взглядом, и поняв, что ничего не остаётся,{w} сел к своей ненаглядной."
    show sl smile pioneer with dissolve
    sh "Привет Славь, не возражаешь?"
    sl "Нисколько Шур. Даже хорошо, мне с тобой поговорить надо."
    "Ого. Этого раньше не было. Интересно."
    "Я поднял глаза на неё."
    sh "Я весь внимание."
    show sl smile pioneer with dspr
    sl "Шурик, ты ничего не забыл?"
    sh "Эм..."
    "Ну да.{w} Посмотри на себя, от новизны происходящего голова кругом пошла."
    "Зачем люди приходят в столовую?"
    "Дубина, ты забыл взять еду. Во дела.{w} Такого давно не было."
    "Глупо улыбнувшись, и ругая себя, я поплелся к раздаче."
    "Это не заняло много времени, и пища здесь также не изменилась.{w} Не могу сказать, хорошо это или плохо."
    "Однозначно хорошо то, что события здесь начинают разворачиваться иначе,{w} хоть пока и по мелочам."
    "Зная Славю, которая будет ждать до победного,{w} я не беспокоился что она уйдет, так и не поговорив со мной."
    sh "Извини, я задумался."
    sl "Ничего. Ты ешь, а я буду говорить."
    sh "Угу."
    "Итак. Не о радио ли пойдет речь?"
    "Не буду загадывать, лучше уже начинать есть.{w} Хотя и не буду скрывать, что заинтригован, ибо заговорить со мной о радиовещании в лагере она должна после приезда Семёна."
    "Бросив взгляд на Славю, я заметил, что она никак не может начать речь."
    "Женщина, не испытывай моё терпение!"
    "Давай же!"
    "НУ!"
    show sl normal pioneer with dspr
    sl "Шурик... Ульяна с Алисой разболтали, что ты и Сыроежкин делаете робота..."
    sh "Вуву"
    "Пробубнил я с набитым ртом."
    sl "Вооот... Как бы сказать..."
    "По её бегающим глазам было совершенно непонятно, о чем она вещает."
    "Семён, черт тебя дери, как ты это распознавал?"
    "Шустро прожевав еду, я уставился на неё в ожидании ответа."
    "Нет. Ну так разговор не пойдет, надо вставить слово."
    sh "Да, делаем, окончательная компоновка ещё не готова.{w} Но мы близки к цели!"
    "Не нужно говорить, что он уже готов.{w} Судя по тому, что события в этом лагере явно развиваются не по шаблону, не стоит сразу тащить робота всем напоказ."
    "В самый неприятный момент может что-то сломаться, и это будет сокрушительное фиаско."
    "И вообще. Я здесь не за этим."
    sl "Вы молодцы!... Я.. Я..."
    show sl shy pioneer with dspr
    "Славя запнулась, потом густо покраснела."
    "Степень непонимания достигла апогея. "
    "\"Держаться  нету больше сил\"."
    sh "Славь, давай ближе к делу."
    show sl serious pioneer with dspr
    "К моему удивлению она расправила плечи, собралась и продолжила говорить."
    sl "Они сказали, что робот очень похож на меня.{w} Это правда?"
    "О как."
    "Неожиданно."
    "Так вот чего она краснела..."
    "Стоп."
    "Все знают, что внешний вид был на мне. {w}Это означает...{w} Они ей намекнули, что она мне нравится?!"
    "Не-не-не, нет, не краснеть!"
    "Концентрация."
    "Покой."
    "Внутреннее умиротворение."
    "Дыши..."
    "Не помогает..."
    show sl scared pioneer with dspr
    sl "Шурик, все нормально? Ты чего так покраснел?"
    "Ну и ЧТО я должен ответить? Типа - нет, он на тебя не похож совсем. Обидится ведь."
    "Или сказать что похож? Совру, но обрадую."
    "Ох уж эта Алиса, ну я тебе это припомню."
    menu:
        "Нет, он не похож на тебя, они тебя обманули.":
            jump slavia_dinner2_a
        "Есть определенное сходство, я бы так сказал.":
            $ sl_love +=2
            jump slavia_dinner2_b
            
label slavia_dinner2_a:
    $ persistent.sprite_time = 'day'
    $ day_time()
    show sl normal pioneer with dspr
    "Незнаю, что она подумала, но видимо своим ответом я её успокоил."
    sh "Ты слушай Двачу больше, она тебе и не такое расскажет. Про Лену, про Дмитриевну. И про остальных."
    sl "Хах, видимо разыграть решили. {w} Они в последнее время всё активнее и активнее. {w} Наверно в ожидании новичков."
    sh "А ты не волнуешься?"
    sl "Слегка. Главное, чтобы Уля с Алисой им не устроили \"тёплый приём\". Или всяких небылиц и сказок понарассказывают."
    sh "Интересно каких? Ты то в курсе?"
    sl "Глупости разные. Мол Уля видела, как в столовую огромная кошка залазила. А Алиса прЫведений."
    show sl laught pioneer with dspr
    "Я улыбнулся в ответ, но одна вещь не дала мне расслабиться - огромная кошка. Ведь я её тоже видел. Всего пару раз, но я уверен в том что видел."
    "И все те разы эта...кошка...исчезала в лесу."
    "По дороге в старый лагерь. "
    "В те разы я следовал событиям и ходил в старый лагерь.."
    "После первого неудачного похода я стал опытней, скажем так."
    "Теперь меня ничего не удивляет и не пугает."
    "Ни в бомбоубежище, ни в шахтах."
    "Как назло, больше эта \"кошка\" мне не попадалась."
    "Чертовы очки, все время спадают!"
    "Поправляя в сотый раз очки на переносице, я решил, что беседа себя исчерпала."
    show sl normal pioneer with dspr
    sh "Ладно, спасибо тебе за новости, но я пойду. Работа зовет!"
    "Уже тошнит от этой игры в образцового пионера, ей богу."
    "Бросив взгляд на то место, где сидел Эл, я обнаружил что он уже покинул сие заведение."
    "Ну ничего, пойду один, есть о чем подумать. И тишина будет кстати."
    jump air_1
label slavia_dinner2_b:
    $ persistent.sprite_time = 'day'
    $ day_time()
    "С моим ответом она расцвела."
    sl "Ой, правда? Как мило!"
    show sl smile pioneer with dspr
    "Мой бог. Ну зачем я соврал-то?"
    show sl shy pioneer with dspr
    sl "Ой, Сань, а можно я на него посмотрю? Ну пожааалуйста!"
    "\"Здесь может быть ваше матерное слово\""
    "Нельзя ей показывать."
    "Так мозг, отговорку. Быстро."
    sh "Извини, но пока он недоступен для созерцания.{w} Я повторюсь - он ещё не скомпонован, следовательно собран не весь.{w} А недоделанную вещь показывать нельзя."
    sl "Хорошо.{w} Только скажи, когда ты своего робота ском{w}-по{w}-нуешь, и я обязательно приду посмотреть!"
    "Я не успел ответить, как она схватила свой поднос и упорхнула."
    hide sl shy pioneer with dspr
    "Ну что сказать. Сударь, вы попали."
    "Неспешно поднявшись,{w}я бросив взгляд на то место, где сидел Эл, и обнаружил,{w} что он уже покинул сие заведение."
    "Ну ничего, пойду один, есть о чем подумать.{w} И тишина будет кстати."
    jump air_1
label zhenia_dinner:
    $ persistent.sprite_time = 'day'
    $ day_time()
    "Сесть с Женей это уже достижение, а поговорить - подвиг.{w} Цербер, что ни говори."
    "Но мои глаза видели ТАКОЕ, что её потуги выглядеть неприступной вызывают лишь смех."
    sh "Привет Жень, свободно?"
    show mz bukal glasses pioneer with dissolve
    "Библиотекарша подняла на меня взгляд, полный ненависти в перемешку с жалостью."
    "Мало что способно вывести её.{w} Интересно, что случилось?"
    "Не став дожидаться ответа, я присел и начал трапезу."
    mz "Саш, у меня к тебе дело."
    sh "Сгухаю."
    "С набитым ртом сказал я."
    mz "Твой сотоварищ,{w} Сыроежкин,{w} что с ним?"
    "Я чуть не подавился.{w} Женя и интересуется об Эле. {w} Что происходит с этим миром?"
    sh "Жив-здоров, чего и всем желает. А в чём вопрос?"
    mz "В том, что не долго ему осталось быть таким здоровым."
    sh "Это почему это?"
    mz "Он меня опозорить вздумал."
    "Он?! Тебя?!?!"
    sh "Не понял, объясни."
    mz "Ну...вы робота делаете, так? Всю смену с ним сидите. Так вот."
    show mz rage glasses pioneer with dspr
    mz "Мне сказали, что этот Сыроежкин... Этот гад... Этот!"
    "Женя просто не находила слов, чтобы отобразить все оттенки ненависти к Элу."
    sh "Что этот? Что он сделал?"
    mz "Он...{w}Ну...{w} На меня делает похожим.{w} Чтобы всякую чушь через динамик говорить."
    sh "Дай угадаю - тебе это Алиса сказала?"
    mz "Нет, Ульянка."
    "Хех, мелкая имеет странное чувство юмора.{w}Но Эла надо спасать."
    menu:
        "Всё совсем не так, как кажется":
            jump mz_dinner_2
        "О чём ты? Робот будет похож на Славю!":
            jump mz_dinner_1
        "Я такими глупостями не занимаюсь.{w} НАУКА не шутит!!":
            jump mz_dinner_3
            
    
label mz_dinner_1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    $ sl_love +=1
    "Женя уставилась на меня во все свои 4 глаза.{w} Шок - это по нашему!"
    mz "Ты что,серьёзно?"
    sh "Я серьёзен, и тебе тоже стоит быть собраннее.{w} Нашла чьи сплетни слушать."
    show mz bukal glasses pioneer with dspr
    "Женя посмотрела на меня взглядом палача-инквизитора, в попытке усмотреть ложь." 
    "Но не найдя доказательств своей фобии,{w} еле заметно улыбнулась."
    mz "Эвон как у вас всё завертелось."
    sh "А то. {w}Автоматический помошник вожатой.{w} Мы даже название придумали! \"Единственная Опытная Техразработка\".  Но я тебе не говорил  - секрет. Аббревиатура \"ЕОТ.\""
    mz "Неплохо. Вам так премию дадут."
    show mz laugh glasses pioneer with dspr
    "Смейся-смейся. За этим - будущее."
    mz "Ну конечно не за название."
    hide mz laugh glasses pioneer with dspr
    "Смеясь, Женя встала из-за стола, и я заметил, как на нас покосились окружающие нас пионеры.{w} Не каждый день можно увидеть смеющуюся библиотекаршу."
    "А я неспешно встал, и направился к выходу. Тут делать больше нечего."
    jump air_1
label mz_dinner_2:
    $ persistent.sprite_time = 'day'
    $ day_time()
    $ el_happy +=1
    "Думаю Эл скажет что-нибудь навроде \" И ты, Брут!\" после этого.{w} Но надо же разогреть эту \"вечеринку\"."
    "На лице Жени читалась вся гамма чувств - от страха и ненависти до смущения и удовлетворения."
    show mz shy glasses pioneer with dspr
    mz "Что ты сказал?"
    sh "Сказал то, что Эл хочет, чтобы ты была первой."
    show mz angry glasses pioneer with dspr
    mz "В каком смысле?"
    sh "Ну, для начала, в оценке его труда.{w} Может и дашь ему пару советов."
    mz "Вот делать мне больше нечего! "
    sh "С тебя не убудет, заодно и убедишься."
    show mz normal glasses pioneer with dspr
    "Видимо, мои доводы оказались на её взгляд вполне логичны, и Женя кивком согласилась со мной."
    "Эл, с тебя должок."
    sh "Ладно Жень, приятного тебе аппетита, а у меня дела.{w} Ты заходи, если что."
    jump air_1
label mz_dinner_3:
    $ persistent.sprite_time = 'day'
    $ day_time()
    $ un_love +=1
    "Женя посмотрела мне прямо в глаза испытывающим, изучающим взглядом."
    "А я в свою очередь изобразил ледяное спокойствие и непоколебимость."
    sh "Жень, успокойся. Мало ли что эта мелочь напридумывает?"
    mz "Думаю ты прав."
    show mz shy glasses pioneer with dspr
    "Женя засмущалась и захотела уйти, но я схватил её за руку. "
    sh "Жень, подожди.{w} Теперь мне твоя помощь нужна."
    show mz smile glasses pioneer with dspr
    mz "Тебе?! Ну говори, что надо."
    sh "Книга."
    mz "Какая ИМЕННО книга?"
    "И тут я понял, что забыл название.{w} Какую же книжку читала Лена? Вспоминай...{w}быстрее!"
    sh "Эм....ну такая в фиолетовой обложке."
    "Её лицо отобразило всю печаль и грусть человечества."
    show mz bukal glasses pioneer with dspr
    mz "ОЧЕНЬ информативно. Автора ты, я так поняла, не знаешь?"
    sh "Жень, ты умная и разбираешься, помоги."
    "Видимо этот разговор её утомил."
    mz "Хорошо, приходи в библиотеку, найдём тебе твою фиолэтовую книгу."
    "Фуф, пронесло. Надо выйти подышать воздухом. "
    $ mz_book = True
    jump air_1
    
label air_1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    stop ambience
    scene ext_houses_day with dissolve
    "Неспешно,{w} дыша свежим воздухом и любуясь небом,{w} я шёл на площадь.{w} В голове было столько мыслей.{w} 
     Всё окружающее меня было таким...{w}новым. {w}Я словно в первый раз тут оказался.{w} Снова появилось то чувство.
     Чувство, что всё хорошо и спокойно. {w}Мне сейчас так хорошо..."
    scene ext_square_day with dissolve
    "Старый добрый Генда. До сих пор не знаю, кто это."
    "Так, хватит отдыхать."
    "Столько дел ещё."
    "Но что это?"
    "Подозрительная мелодия, которой тут не место, донеслась со стороны сцены."
    play music pioneer_theme
    $ renpy.music.set_volume(0.25, .5, channel="music")
    "Может это Алиса играет нечто похожее?"
    "Надо срочно проверить."
    scene ext_stage_normal_day with dissolve
    "Странно, никого нет."
    $ renpy.music.set_volume(0.5, .5, channel="music")
    "А музыка играет."
    "И тут я услышал голос, который век бы не желал слышать."
    "Голос, не суливший ничего хорошего."
    play sound sfx_scary_sting
    show pioneer shadow with dissolve
    pi "Ну здравствуй Александер."
    "Я увидел его тень. Он близко."
    sh "А тебе похворать..."
    "Даже не стоит оборачиваться, и так его лицо я выучил."
    sh "Зачем пожаловал в такую рань?"
    pi "Да вот, решил поговорить с давним знакомым."
    "Тут он увеличил громкость в своём плеере."
    $ renpy.music.set_volume(1.0, .5, channel="music")
    pi "Неужто ты всё пытаешься выбраться?"
    sh "Разумеется! Это не жизнь."
    pi "Ой. Да ладно тебе. Ты даже никого пальцем тут не тронул, или ещё чего такого."
    "Он усмехнулся."
    "Как меня бесит эта его черта."
    sh "Да знаю я о твоих подвигах."
    pi "ТЫ ничего не знаешь."
    sh "Ты пришёл меня передразнивать или что?"
    "Этот диалог начинает меня раздражать."
    pi "Я пришёл повеселиться, посмотреть на твои потуги помочь этому доходяге обрести себя."
    sh "Он ведь ты, разве нет?"
    "В эту игру могут играть двое."
    pi "Не сравнивай нас, это глупо. Ему уже не помочь, как и всем нам. Мы тут навечно."
    sh "Ты ошибаешься, всё можно исправить.{w} Он нас спасёт."
    pi "Да лааадно, не смеши. Что он может?"
    sh "Всё, если захочет."
    pi "А что можешь ты?"
    "Я?! Куда он клонит?"
    pi "Ты наверно возомнил себя эдаким оруженосцем.{w} Похвально.{w} Давай в отсутствие рыцаря справся с драконом."
    stop music
    sh " С кем??"
    hide pioneer shadow with dissolve
    "Нет ответа. Испарился. Ну и чёрт с ним."
    "Обернувшись, я замер."
    "Алиса. Злая. Очень."
    play music music_list["awakening_power"] fadein 3
    show dv rage pioneer with dspr
    dv "Очкастый, ты что тут с моими инструментами делаешь?"
    "Вот вам и огнедышащее чудище."
    "Если я что либо не придумаю прямо сейчас, то мой земной путь тут и закончится."
    "Алиса медленно подходила ко мне, сверкая глазами."
    show dv rage pioneer close with dissolve
    sh "А-а-алиса, п-п-подожди!"
    dv "Ты ещё что-то вякаешь? Сначала пугаешь,{w} издеваешься{w} а теперь и гитару ломаешь?"
    sh "А я, это..."
    dv "Что \"это?\""
    "Сейчас меня будут бить, возможно даже гитарой."
    sh "Я решил играть на гитаре, вот.{w} Я умею."
    "Алиса остановилась и внимательно посмотрела на меня."
    dv "Ты и на гитаре? Не смеши."
    sh "Да."
    dv "И ты хочешь сказать, что это не Мику врубила свои адские песни на полную громкость,{w} а ты тут упражняешься?"
    sh "Ты ещё кроме меня тут кого видишь? Говорю тебе, я умею на гитаре играть."
    show dv laugh pioneer close with dspr
    dv "Ох не смеши меня. Играть он умеет. Взял пару аккордов и возомнил себя музыкантом."
    "Эх, Алиса, Алиса."
    show blink
    $ renpy.pause(3)
    scene int_house_of_dv_night 
    show prologue_dream 
    show dv shy body behind prologue_dream with dissolve
    "Ты ведь меня учила, жаль что не знаешь этого."
    "Сколько времени мы провели вместе, занимаясь музыкой и познавая друг друга."
    "Я знаю всё о тебе.{w} Жаль, что ты лишь кукла..."
    scene ext_stage_normal_day 
    show unblink
    play music music_list["glimmering_coals"] fadein 3
    mi "Ребята, привет.{w} Я услышала мелодию, и решила пойти послушать. Алис,{w} это ты играла?"
    show mi surprise pioneer at right with dissolve
    mi "Красивая мелодия, я заслушалась. Потом решила подыграть и даже придумала как её изменить."
    show dv grin pioneer at left with dissolve
    dv "Не, это вот этот трубадур забавляется"
    show mi shocked pioneer at right with  dspr
    mi "Саш?!? Ты играешь?"
    "Никогда ещё не видел её такой удивленной и немногословной."
    sh "Да, немного."
    mi "Ой-ой-ой, а сыграй ещё! Так красиво было. А я подыграю."
    show mi grin pioneer at right with  dspr
    mi "Нет,{w} подыграет Алиса, а я петь буду."
    mi "Классно получится, мы с этим выступать будем. Саш, давай ко мне в клуб вступай."
    "Тааак, это в мои планы точно не входило. "
    "Что делать? "
    sh "Увы, я занят с роботом. Но я с удовольствием с тобой сыграю в свободное время."
    show mi sad pioneer at right with  dspr
    mi "Ну Саааш. Пожалуйста, давай к нам."
    sh "Ми, ну ты же знаешь."
    mi "Ладно."
    show mi smile pioneer at right with  dspr
    mi "Сегодня или завтра начнём? Тебе какую гитару дать? А может ты не только на гитаре умеешь? Хочешь научу?"
    "Как унять бегущего бизона..."
    sh "Не, гитары - моя тайная страсть."
    show dv shocked pioneer at left with  dspr
    mi "Чудно, чудно!"
    "Алиса всё это время пребывала в лёгком шоке, и на моё счастье, забыла, зачем скандалила."
    "Но просто уйти ей не позволит гордость, так что последнее слово за ней."
    show dv grin pioneer at left with  dspr
    dv "Шур, если ты хотел поиграть, стоило только попросить."
    "Угу, и ты бы мне дала..."
    dv "Брать чужое не хорошо, ты же знаешь.{w} Ладно, играл ты неплохо, так что прощаю. Но смотри у меня."
    dv "Приходи вечером - посмотрим, чего ты стоишь."
    "С этими словами она повернулась и ушла. Мику попрощалась со мной и побежала за ней следом."
    hide dv grin pioneer at left with dissolve
    hide mi smile pioneer at right with dissolve
    "А я остался на едине со своими мыслями."
    play music treck_op fadein 3
    "Зачем он это сделал, устроил этот фарс?"
    "Специально?{w} Всё для того, чтобы у меня был повод для более тесного общения с девушками?"
    "В чём его выгода?{w} Он ведёт свою игру?"
    "Ладно, я подумаю об этом позже. По крайней мере планы на вечер определены."
    "Чтобы что-то было, надо что-то делать."
    stop music fadeout 3
    
    scene ext_library_day with dissolve
    play music music_list["your_bright_side"] fadein 3
    play ambience ambience_library_day
    "С этой мыслью я пошёл в библиотеку, надеясь, что больше неприятностей не будет."
    show int_library_day with dissolve
    show un normal pioneer at left with dissolve
    "Как и ожидалось, в библиотеке была Лена,{w} наверняка любовные романы стопками набирает."
    show un smile pioneer at left with dspr
    "Кивком я дал понять, что рад её видеть, а она,{w} в свою очередь слегка улыбнулась, и вернулась к чтению."
    hide un smile pioneer with dissolve
    "Подойдя к Жене, я нисколечки не удивился{w} — спит как сурок."
    scene d2_micu_lib with dissolve
    sh "Солнце вышло из-за ели!"
    "Выпалил я громко и чётко на ухо этой вахтёрши."
    scene int_library_day with dissolve
    show mz bukal glasses pioneer with dissolve 
    "Та резко подняла голову, и уставилась на меня ничего не понимающим взглядом."
    mz "Ты совсем дурак? Так пугать."
    sh "Ты не спишь в своей постели?"
    "Не унимался я."
    mz "Саш, заканчивай с шуточками."
    show mz angry glasses pioneer with dspr
    mz "По пустякам отвлекаешь."
    if  mz_book == True:
        sh "Мы так не договаривались! Это твоя территория, ты тут обитаешь. Помоги книгу найти!"
        jump lib2
    
    sh "А что ты можешь дать кроме книг?"
    jump lib1
        
label lib2:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_library_day with dissolve
    show mz bukal glasses pioneer with dissolve 
    "Видя, что от меня так просто не отстать,{w} Женя с явным нежеланием встала из-за стола и пошла к книжным полкам."
    mz "Какую тебе?"
    sh "Мне б по части электроники, справочник или пособие."
    "Женя что-то невнятное пробурчала в ответ, и полезла копаться в стойках,{w} а я подошёл к Лене."
    hide mz bukal glasses pioneer with dissolve
    show un normal pioneer with dissolve 
    play music music_list["lets_be_friends"] fadein 3
    "Та была полностью поглощена книгой, и внешний мир для неё не существовал."
    "Рыцари,{w} принцессы,{w} любовь до гроба,{w} «и жили они недолго и несчастливо, но умерли в один день.»"
    "Жаль, но я разрушу её уединение, её уютный Лена-мирок."
    sh "Лен, привет.{w} Что читаешь?"
    show un surprise pioneer with dspr 
    "Я навис над ней,{w} и она в страхе отринула от меня, стукнувшись головой об книжную стойку и села на пол."
    play sound sfx_bodyfall_1 
    with hpunch
    play music music_list["revenga"]
    "Наверно пребольно ударилась, ведь потом она посмотрела на меня очень даже злым взглядом.{w} Интересно, у неё нож при себе?" 
    "Мои опасения не подтвердились, и я,{w} чувствуя некоторую вину за случившееся внеплановое понижение её умственной деятельности,{w} решил извиниться."
    sh "Ой Лен, прости, не хотел тебя пугать. Больно ударилась?"
    show un normal pioneer with dspr
    play music music_list["lets_be_friends"] fadein 3
    un "Нет, всё нормально, но больше не надо так делать."
    "Главное запереть сегодня всё и вся, а не то прирежет ночью {w}- пронеслось в голове."
    sh "Ты не злись, я не специально"
    "Решил я умилостивить её поскорее."
    un "Ладно, прощаю."
    show un smile pioneer with dspr
    "Она слабо улыбнулась и встала с пола." 
    "Однако вставая, она задела эту самую злосчастную стойку, и книга с верхней полки{w}, в фиолетовом переплёте, полетела вниз."
    "Прямо на её больную голову."
    stop music
    menu:
        "Поймать":
            $ un_love +=1
            jump lib2_1
        "Пускай страдает":
            $ un_love -=1
            jump lib2_2
        
label lib2_1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    "Резким движением я хватаю это \"горе\"{w}, и прижимаю к себе, попутно схватив злополучную книгу."
    play music music_list["lets_be_friends"] fadein 3
    show un shocked pioneer with dspr 
    "Лена посмотрела на меня удивлённым взглядом,{w} медленно переходящим в благодарственный. Я же, повертев книгу в руках, улыбнулся."
    sh "Осторожнее надо быть. Нам не нужны лишние травмы."
    un "Спасибо, Сань."
    show un shy pioneer with dspr
    "Она густо покраснела." 
    "Прямо романтика. Но внезапно вылезшая из дебрей Женя с книгами в руках, эффектно и картинно разрушила этот момент."
    show mz angry glasses pioneer at right with dissolve 
    mz "Значит, пока я тебе книги ищу{w}, ты девок соблазняешь?"
    "Только сейчас я осознал, что прижимаю к себе Лену.{w} Мдааа, теперь поползут слухи.{w} А Женя не унималась."
    mz "Значит пока я трачу своё время..."
    sh "И свои лучшие годы..."
    "Вставил я."
    mz "Я смотрю, у тебя юмора поприбавилось."
    "Она начинает злиться."
    show mz rage glasses pioneer at right with dspr 
    sh "Ты всё не так поняла." 
    "Этот спор мог длиться очень долго, если бы нас не отвлёк голос Слави и Ольги Дмитриевны."
    mt "Ну и где она?" 
    sl "Тут была полчаса назад."
    "Женя, бормоча что-то явно не хорошее, пошла к ним."
    hide mz rage glasses pioneer at right with dissolve 
    "Я не стал вслушиваться в их разговор, но Женя сказала, чтобы мы выходили, так как она запирает библиотеку."
    "Лена набрала своей литературы и пошла к выходу.{w} Я взял всё то, что библиотекарша для меня накопала, плюс «трофей» , от которого я спас нашу «тихоню»." 
    hide un shy pioneer with dissolve
    show ext_library_day
    "Книга оказалась «Унесённые ветром». Хорошее произведение, пригодится.{w} Ну а мне тут делать больше нечего - своих дел навалом."
    jump muzhome
    
label lib2_2:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_library_day with dissolve
    play music alex_theme
    $ renpy.music.set_volume(0.5, .5, channel="music")
    "С плохо скрываемым удовольствием смотрел на то, как книга приземляется на макушку этой бесноватой." 
    with hpunch
    show un sad pioneer close  with dissolve
    "Не думаю что ей больно,{w} но что неловко это точно." 
    "Её изумрудные глаза недобро сверкнули в немом укоре «А поймать нельзя было?!».{w} Нет, нельзя." 
    scene d7_un_suicide with dissolve
    show prologue_dream with dissolve
    "Как ты заставляла меня переживать и страдать,{w} так получи же заслуженное."
    "Жаль что ты фальшивка, мне бы хотелось, чтобы эту боль почувствовали все вы.{w} Куклы."
    scene int_library_day with dissolve
    show un sad pioneer close  with dissolve
    sh "Дааааа, сплошное несчастье с тобой." 
    "Проворчал я. Поднимая книгу «Унесённые ветром»."
    "«Вежливость не мешает даже и в горе.»"
    sh "Слушай,может тебя в медпункт сводить?{w} Там тебя подлечат."
    "Сказал я с максимально доступной для меня дружелюбностью."
    show un angry2 pioneer with dspr
    un "Спасибо, обойдусь сама."
    "Думаю не стоит мне ей надоедать, но напряжение надо снять.{w} Я негромко засмеялся, скорее на показ, чем от радости."
    sh "Горе ты наше, Лен. За тобой глаз да глаз."
    hide un angry2 pioneer with dissolve
    "На это она ничего не ответила, и пошла к Жене. {w}Та, к моему удивлению, была занята разговором со Славей и Ольгой Дмитриевной."
    show sl normal pioneer at right with dissolve 
    show mt normal panama pioneer with dissolve 
    "Видимо те от неё чтото хотели, так как Женя мрачнела на глазах.{w} Я взял книги, которые для меня подобрала эта вахтёрша, и добавил \"Унесённых\"." 
    "Я вышел из библиотеки и направился по своим делам."
    jump muzhome

label lib1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_library_day with dissolve
    sh "А что ты можешь дать кроме книг?" 
    "Спросиля я с сарказмом."
    "Нет, видимо я точно нарываюсь." 
    show mz rage glasses pioneer with dissolve 
    mz "Так, пошёл отсюда."
    sh "Лааадно, не кипятись. Возьму пару справочников, и уйду отсель.{w} И надоедать тебе не буду. Честно-честно."
    show mz angry glasses pioneer  with dspr 
    mz "Ну пошли."
    "Мы двинулись к полкам. Чего тут только не было: Дюма, Конан Дойль, и много других замечательных писателей.{w} А ещё море справочников, пособий и учебников."
    "Подойдя к одной из таких стопок Женя начала беглым взглядом изучать содержимое."
    sh "Мне бы по материаловедению чего-нибудь."
    show mz bukal glasses pioneer  with dspr
    mz "Поняла." 
    "Буркнула она." 
    "На нижних полках нужного не обнаружилась, и она пошла за стремянкой."
    hide mz bukal glasses pioneer  with dissolve  
    "Когда же она её принесла, меня обуял дикий ужас."
    sh "Я на ЭТО никогда не полезу." 
    show mz normal glasses pioneer  with dissolve 
    mz "Эх ты, а ещё мужик."
    sh "Мужик-то я мужик, но высоты боюсь и качества этой шухерки.{w} Да и к тому же ты легче."
    "С логикой не поспоришь."
    mz "Хорошо, только держи крепче."
    "Она начала эпохальное вскарабкивание по этому деревянному Эвересту, а я приложил все силы, чтобы эта конструкция из плоти и дерева не рухнула."
    show mz bukal pioneer glasses far with dissolve 
    "Вроде всё идёт хорошо, хоть и необычно.{w} Между делом я оценил фигурку нашего библиотекаря."
    "Да, немного физкультуры конечно не помешает, но ножки у неё заглядение." 
    "Та, тем временем лезла всё выше и выше, стараясь не смотреть вниз. Хорошо что она лёгкая. Я, волей-неволей, был ей благодарен за это. {w}Всёж не такая она и стерва.{w} Интересно, настоящая Женя какая?" 
    "Тем временем она вскарабкалась достаточно высоко, и её таз был на уровне моих глаз.{w} Аппетитные формы проступали через помятую юбку."
    "Соблазн велик, очень велик..."
    menu:
        "Заглянуть под юбку":
            $ el_happy -= 1
            jump lib1_1
        "Отогнать пошлые мысли":
            $ el_happy += 1
            jump lib1_2
label lib1_1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_library_day with dissolve
    sh "Жень, ну как?"
    show mz normal pioneer glasses far with dissolve 
    mz "Никак, нет тут ничего." 
    "Она собралась спускаться."
    sh "Жень, а вон там, чуть повыше?"
    mz "Вот ты... приставучий."
    "Женя полезла ёще выше, и эта идея ей самой резко переставала нравиться.{w} Видимо она нашла нечто интересное, поскольку сняла очки."
    "А я коварно воспользовался моментом, чтобы заглянуть в святая святых.{w} От увиденного я потерял дар речи - на ней не было нижнего белья!"
    show mz normal nm  far with dspr 
    sh "Ёёёёё" 
    "Я так удивился, что ослабил хватку лестницы, и Женя закономерно полетела вниз, успев схватить очки и пару книжек."
    mz "Аааайй"
    show mz bukal pioneer glasses close with dissolve
    with hpunch
    "Она упала прямо мне на лицо.{w} Ой и больно же было. Ещё больнее было осознавать то, что произосшедшее было из-за моего плохого зрения." 
    "Её трусы были телесного цвета. Придумают же."
    "И да, ошибся я на счёт веса.{w} На диету, сегодня же."
    "Хорошо хоть очки не пострадали,{w} подумал я." 
    "Женя же пулей вскочила с меня, и вид её был тот ещё - стыд в перемешку с гневом." 
    show mz rage pioneer glasses  with dissolve
    mz "Ну ничего тебе доверить нельзя. Руки не оттуда у вас растут! Что у тебя, что у Сыроежкина."
    "Ох и злая фурия."
    sh "Это всё от того, что кто-то слишком много ест."
    mz "Чего?!"
    "От жестокой расправы меня спас легкий смешок Лены, которая тихо наблюдала за нашей сценой."
    show un smile pioneer at left with dissolve 
    "Женя в момент переключилась на неё."
    mz "А ты чего смеёшься?"
    "Та тихо смеялась в кулачок."
    hide un smile pioneer at left with dissolve 
    "Наверно всё закончилось бы плохо, если бы не Славя с Ольгой Дмитриевной, появившиеся в дверном проёме."
    show sl normal pioneer at right with dissolve 
    show mt normal panama  pioneer at left with dissolve 
    mt "Как у вас, однако, оживлённо." 
    mz "А мы это... тут... книги ищем."
    mt "Понятно. Жень, у нас к тебе дело, и надолго. Новая партия литературы пришла, надо бы тебе разобраться."
    "Женя выглядела совсем подавленной. Да, не видать ей спокойного сна аж до конца дня. Чтож, терпи."
    mt "И вы, ребята, без дела не сидите."
    sh "А мы уже уходим - сказал я и Лена кивком подтвердила."
    "Подобрав справочники,{w} которые нашла для меня библиотекарша, я собрался уходить, но взгляд мой зацепился за одну книгу."
    "\"Унесённые ветром\". Хммм, пригодится."
    "Схватив её, я вышел на улицу - дел ещё очень много."
    jump muzhome
    
label lib1_2:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_library_day with dissolve
    "О чём я думаю?!"
    "Конечно, эту куклу сделали красивой, но я не могу отвлекаться. {w}Несмотря на её приятный запах и ухоженный вид."
    "Чтобы противостоять нахлынувшим соблазнам, я отвернулся и увидел Лену,{w} выглядывающей из-за угла." 
    show un normal pioneer at cright  with dissolve
    "Я закатил глаза, давая понять, как долго Женя делает примитивные действия, и как мне надоело ждать." 
    "Лена слабо улыбнулась и кивнула - она со мной согласна."
    show un smile pioneer at cright  with dspr
    "Раздался голос сверху."
    mz "Эй, чего вы там переглядываетесь?"
    show mz bukal pioneer glasses  with dissolve
    "Жене явно не нравилось происходящее внизу{w}, и она всеми силами пыталась понять, что нас веселит."
    "Её ёрзания на стремянке явно не шли на пользу последней, и ступенька, на которой стояла \"стесняша\", сломалась ровно пополам."
    "Женя полетела вниз со страшным визгом, Лена в ужасе закрыла лицо руками{w}, а я... А что я? Делать было нечего, пришлось ловить."
    show un scared pioneer at cright  with dspr
    "Библиотекарша приземлилась прямо мне в руки, хотя я сам чуть не сломался под её весом. {w}Жень, хорош отъедать пятую точку."
    "Пришлось напрячь все силы, чтобы не уронить космонавтку и самому устоять."
    "Руки налились свинцом от напряжения, выступили вены, а на лице отобразились великие муки."
    sh "Хххнннгх..."
    un "Ой..."
    "Выдохнула Лена. Её изумрудные глаза были полны восхищением и бладодарностью."
    show un surprise pioneer at cright  with dspr
    "Её взгляд обладал какой-то мистической силой, что ему сложно противостоять."
    un "Жень, ты как?"
    show mz smile glasses pioneer  with dissolve 
    mz "Всё хорошо."
    "Я поставил её на землю, и её щеки загорелись румянцем."
    show mz shy glasses pioneer  with dspr 
    mz "С-с-спасибо Саш."
    show un normal pioneer at cright  with dspr
    sh "Ничего, сочтёмся. Ты книги то достала?"
    mz "Да. Вот держи."
    "И она отдала мои трофеи."
    sh "Хорошо то, что хорошо кончается."
    "Сказал я, а Лена подтвердила."
    show un smile pioneer at cright  with dspr
    mz "А ты как?"
    mz "Это то, что ты искал?"
    sh "Да, то что нужно. Спасибо."
    show mz normal glasses pioneer  with dspr
    "Не знаю, сколько бы продолжился этот обмен любезностями, но появившиеся Славя и Ольга Дмитриевна внесли свои коррективы."
    show sl normal pioneer at right with dspr 
    show mt normal panama  pioneer at left with dspr
    sl "Женя, ты где?"
    "Та, услышав своё имя, пошла выяснять, в чём вопрос.{w} Видимо появились неотложные дела, т.к. Женя стала мрачнеть на глазах."
    "Переглянувшись с Леной, мы решили не задерживаться, чтобы новоявленные проблемы обошли нас стороной."
    "Обычно прошмыгнуть мимо Дмитриевны довольно-таки сложно{w}, но нам удалось проскользнуть на улицу.{w} На прощанье я подмигнул Жене, а та покаснела больше варёного рака."
    scene ext_library_day
    show un normal pioneer with dissolve
    sh "Ну, вот и очередное приключение подошло к концу."
    un "Да."
    sh "Я по своим делам, давай, ещё свидимся.{w} Не пропадай."
    show un smile pioneer with dspr 
    un "И тебе удачи."
    "И каждый пошёл по своим делам."
    jump muzhome



label muzhome:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene alex home day with dissolve
    stop ambience 
    play music music_list["my_daily_life"] fadein 3 
    "Придя в свой домик, я сложил добытые книги. Да уж, улов не слабый. Куда бы деть всю эту макулатуру?{w} Ведь мне нужны были только «Унесённые ветром»."
    "Ладно, подумаю над этим позже{w}, а сейчас меня уже ждут в храме музыки и творчества.{w} А этих музыканток расстраивать я не хочу, ибо проблемы не нужны."
    "Хорошо, в путь!"
    scene ext_houses_day with dissolve
    "На подходе к клубу меня перехватила Мику."
    show mi normal pioneer with dissolve
    mi "Ой Санечка, привет тебе ещё раз. Я пошла к вашему домику, хотела тебя поймать, вдруг ты передумаешь. Ты ведь не передумал?"
    sh "Нет, я..."
    mi "Вот и славно! Пойдём, пойдём, Алиса уже подготовила инструменты, а я песни новые разучила. Тебе точно понравится. Честно-честно." 
    show mi smile pioneer with dspr
    mi "Я тебе свою гитару дам, она такая хорошая." 
    "Господи женщина, да дай ты мне слово вставить"
    mi"...а завтра-послезавтра я тебя на флейте и фортепьяно играть научу..."
    show mi happy pioneer with dspr
    sh "Мику"
    mi "...а потом поедем ко мне на Родину, выступать будем. Наше трио будет..."
    sh "МИКУ!!"
    "Ми удивлённо посмотрела на меня{w}, а потом как-то резко погрустнела."
    show mi sad pioneer with dspr
    mi "Извини Саш, я увлеклась..."
    sh "Всё нормально, но не стоит строить такие далеко идущие планы. {w}Всё будет, но не сразу."
    "Я знаю, что у этой марионетки настроение меняется очень быстро, так что у меня она грустить не будет."
    sh "Давай, покажу тебе на что я способен, а ты решишь, что делать дальше."
    show mi smile pioneer with dspr
    mi "Саш, я уверена, что ты способен на очень многое. Ты можешь."
    "Таких слов от неё я никак не ожидал.{w} Странное чувство, когда столь тёплые вещи, наполненные чувствами, тебе говорит бездушный предмет." 
    "Если так пойдёт и дальше, то не передумаю ли я?{w} Не захочу ли провести тут вечность?{w} Вечность в счастье?{w} Стоит напрячься, попытаться забыть...{w}Как смог ОН.{w} Стоит ли?"
    "Пока разговаривали, мы дошли до клуба, где на пороге нас уже ждала Алиса."
    scene ext_musclub_day with dissolve
    show dv smile pioneer at left with dissolve
    dv "Пришёл таки, не запылился."
    show mi normal pioneer at right with dissolve
    mi "Перестань, Алис. Саня сам шёл к нам, я составила ему компанию. Он на всё согласен."
    "Ээээ, в каком смысле?? - промелькнуло в голове."
    show dv normal pioneer at left with dspr
    dv "Всё готово, заходите."
    "Алиса сделала жест рукой, приглашая внутрь."
    scene int_musclub_day 
    show dv normal pioneer at left 
    show mi normal pioneer at right 
    with dissolve
    "Да, Алисе действительно можно поручить важное задание — инструменты расставлены, протёрты и готовы к игре. Интересно, Ми её долго уламывала?"
    play music trio_guitar 
    dv "Очкастый, ну что ты стоишь как бедный родственник? Заходи, гостем будешь. Держи инструмент, нажми на клавиши, продай талант."
    "Я осторожно взял гитару из её рук и  поудобнее устроился на стуле. Девушки с нескрываемым любопытством посмотрели на меня."
    "Нехорошо заставлять женщин ждать. На ум приходит мелодия, и хотя я плохо её помню и ещё хуже играю, пальцы начинают перебирать струны." 
    "Алиса слегка поморщилась:{w} оно и ясно — исполнение хуже некуда, но Мику слушала очень внимательно, пытаясь уловить суть сквозь завесу фальши." 
    "Мне кажется, или она заслушалась?  Отстукивает каблучком ритм, глаза закрыты. По всей видимости ей нравится." 
    "Алиска, смотря на этот перфоманс, пошла за 2-й гитарой, и вступила второй партией."
    "Да, играть наша бунтарка умеет - сразу взляла ритм и с довольным лицом смотрела на Мику. Та просто находилась в нирване от этого галаконцерта."
    stop music
    show mi shocked pioneer at right with dspr
    play music music_list["everyday_theme"]
    mi "Ой ребят, это так... так.. так.. КЛАССНО!!{w} Саш, ты просто должен приходить к нам почаще."
    sh "Ну, я занят..."
    "Но Алиса была более категорична."
    show dv angry pioneer at left with dspr
    dv "Сань, всё очень плохо.{w} Никуда не годится. {w}Играй больше, иначе ничего не добьёшься! Не одну-две песенки, а полноценные упражнения."
    "ДваЧе странная - поливает грязью с ног до головы, но в то же время даёт действительно хорошие советы и поддерживает.{w} Втроём мы играли до самого ужина." 
    play sound sfx_dinner_horn_processed
    sh "Всё, девушки, концерт окончен. Скрипку в печку. Пойдёмте есть."
    show dv smile pioneer at left with dspr
    dv "Ишь, раскомандовался."
    show mi grin pioneer at right with dspr
    mi "Да ладно тебе Алис, дай ему почувствовать силу, ведь ты его вымотала."
    "Все соки высосала просто."
    "Та прыснула и мы вместе вышли на крыльцо..."
    stop music
    
    scene ext_musclub_day with dissolve
    play music music_list["my_daily_life"] fadein 3
    "Где тут же столкнулись с Улей и Леной. Вид у них был заинтересованный."
    show un surprise pioneer at left with dissolve
    show us surp1 pioneer at right with dissolve
    un "А вы тут репетируете?"
    show mi grin pioneer  with dissolve
    mi "Да-да, а вам понравилось?"
    show un shy pioneer at left with dspr
    un "Ты нас заметила? Мы вам мешали?"
    show mi happy pioneer with dspr
    mi "Нисколечки. Зрители всегда приветствуются, и их критика тоже."
    show us grin pioneer at right with dspr
    us "Тогда вам нужны ещё музыканты."
    show un normal pioneer at left with dspr
    "С умным видом начала Уля."
    us "У каждого современного ансамбля больше народу, чем у вас."
    hide mi happy pioneer at cleft with dissolve
    show dv smile pioneer  with dissolve
    dv "Учтём."
    "Видимо её веселит эта идея с группой."
    dv "Вот только кого ещё брать? Тебя?"
    show us laugh2 pioneer at right with dspr
    us "А я согласная! Я молодая, красивая."
    dv "Там таких хватает и без тебя."
    show dv grin pioneer  with dspr
    "Покачала головой её старшая подруга."
    show us laugh pioneer at right with dspr
    us "Так я ещё и талантливая..."
    sh "Нет, ты будешь заводилой в толпах фанатов. Это очень важная работа."
    "Вставил я своё слово."
    "Малая посмотрела на меня такими глазами, будто я открыл законы перемещения в пространстве и времени." 
    show us surp3 pioneer at right with dspr
    us "Тоооооочно! Шурик, ты гений!"
    hide dv grin pioneer with dissolve
    "Уле так понравилась эта идея, что она запрыгала на месте и, наверно, уже представляла себя ведущей за собой толпы людей, а на нас просто перестала обращать внимание.{w} Да, просто живая батарейка.{w} Счастливое детство.{w} Жаль, что фальшивое..."
    show mi smile pioneer  with dissolve
    mi "Дааа....группа это хорошо."
    "Мечтательно выдала Мику."
    mi "Это так хорошо, когда друзья вместе занимаются любимым делом. Уля права — надо больше людей. "
    mi "Может, Лена согласится? Играть так играть."
    show un surprise pioneer at left with dspr
    "Лена покраснела, но робко сказала."
    un "Я не против."
    sh "А ведь скоро новенькие приедут, вдруг среди них есть музыканты, и тоже захотят присоединиться?"
    hide un surprise pioneer at left with dissolve
    show mi happy pioneer  with dissolve
    mi "Это будет просто замечательно! Бэк-вокал, бас-ритм-партии, а ещё и фортепьяно!"
    "Мику просто летала в облаках от таких мечтаний."
    show dv normal pioneer at left with dissolve
    dv "Спустись с небес на землю, звезда ты наша."
    "Остудила её Алиса."
    dv "Нам до выступлений, как Сане до его щетины."
    sh "Эй!"
    "Но на меня уже не обращают внимания. Ну да и хорошо — пора в столовую."
    show mi dontlike pioneer with dspr
    "Мику заметила лишь несколько мгновений спустя, когда я уже скрылся за поворотом." 
    scene ext_houses_sunset with dissolve
    "Послышалось только."
    scene ext_dining_hall_away_sunset with dissolve
    mi "...Стой... куда?"
    scene int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_full
    "Ужин прошёл спокойно, без лишних приключений."
    show el normal pioneer with dissolve
    "Я ужинал вместе с Элом, неспешно переговариваясь на счёт дальнейших планов в нашем кружке.{w} Хотя как переговаривались — говорил в основном я, а Эл поддакивал, да украдкой на Женю посматривал. "
    show mz normal glasses pioneer at right with dissolve
    "Та всеми силами делала вид, что не замечает и не интересуется. Забавно за ними следить — такая качественная постановка."
    show dv normal pioneer at left with dissolve
    "Я бы так и наслаждался бы зрелищем, если бы не подошедшая Алиса и её подзатыльник со словами «За то, что убежал от нас»."
    with hpunch
    stop music
    stop ambience
    show blink
    "..."
    scene ext_beach_night 
    $ persistent.sprite_time = 'night'
    play music treck_op 
    show prologue_dream 
    "Никакой боли.{w}Мир погас на мгновенье.{w} Но за эти доли секунды я увидел странную картину, даже по меркам той ситуации, в которой оказался"
    show el normal pioneer at right behind prologue_dream with dissolve
    show mz normal glasses pioneer at left behind prologue_dream with dissolve
    "Пляж, Эл и Женя."
    "Они о чём-то говорят."
    el "..."
    show el grin pioneer at right behind prologue_dream with dissolve
    mz "...!"
    show mz normal glasses pioneer at left behind prologue_dream with dissolve
    el "..."
    show el smile pioneer at right behind prologue_dream with dissolve
    mz "...?"
    "Но слов не слышно."
    show mz angry glasses pioneer at left behind prologue_dream with dissolve
    el "...!"
    show el shocked pioneer at right behind prologue_dream with dissolve
    mz "...!"
    show mz rage glasses pioneer at left behind prologue_dream with dissolve
    el "..."
    show el sad pioneer at right behind prologue_dream with dissolve
    mz "..."
    "Он выглядит раздавленным."
    hide el sad pioneer at right behind prologue_dream with dissolve
    mz "..."
    "А она чуть не плачет."
    show mz shy glasses pioneer at left behind prologue_dream with dissolve
    "Что это такое?"
    show mz rage glasses pioneer at left behind prologue_dream with dissolve
    hide blink
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_dining_hall_sunset
    show unblink
    play ambience ambience_dining_hall_full
    el "Саш?"
    show el shocked pioneer at right with dissolve
    dv "Совсем дохлый."
    show dv shocked pioneer at left with dissolve
    sh "Всё нормально... "
    "Видимо отключился я не на пару мгновений."
    show sl scared pioneer with dissolve
    sl "Может тебе к медсестре?"
    sh "Успокойтесь, всё хорошо."
    stop ambience
    "Встав я пошёл к выходу, а Славя стала отчитывать растерявшуюся Алису."
    show sl angry pioneer  with dspr
    show dv scared pioneer at left with dspr
    sl "...!"
    scene alex home night 
    "Дойдя до кровати, я рухнул без сил.{w} Странное дело — все сегодняшние приключения ни чуть не вымотали меня{w}, а один лёгкий тычок просто раздавил. "
    "Но что это было?{w} Я будто бы увидел будущее. {w}Нет, я знаю что есть множество «Совят», но я думал, что время в них движется одинаково. Значит нет...{w} Мысли стали путаться у меня в голове. Сложно сконцентрироваться."
    "Словно кто-то не хочет, чтобы я загружал себя этими размышлениями..."
    "И я уснул."
    stop music
    jump day_2
    
            
    return
