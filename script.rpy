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
    
label day_2:
    $ backdrop = "2 дня до приезда"
    $ new_chapter(-2, u"2 дня до приезда")
    scene alex home day with dissolve
    play music alex_mind 
    
    $ persistent.sprite_time = 'day'
    $ day_time()

    "Проснулся я ещё до побудки. Чувствовал себя сильно разбитым и вымотанным.{w}Да и голова болела после такого сна. А снились мне странные вещи: "
    show prologue_dream with dissolve
    show dv cry pioneer behind prologue_dream with dissolve
    "Плачущая Алиса"
    hide dv cry pioneer behind prologue_dream with dissolve
    show us sad pioneer behind prologue_dream with dissolve
    "Грустящая Уля"
    hide us sad pioneer behind prologue_dream with dissolve
    show sl sad pioneer behind prologue_dream with dissolve
    stop music fadeout 5
    "Одинокая Славя."
    hide sl sad pioneer behind prologue_dream with dissolve
    hide prologue_dream with dissolve
    "Что это?{w} Я должен выяснить это?{w} Скорее всего это настоящие люди, и они страдают.{w} А может я просто вчера переел..."
    play sound sfx_dinner_horn_processed 
    "А вот и подъём, пора мыться-купаться и на зарядку."
    scene ext_washstand_day with dissolve
    "Новый день ласково приветствовал меня солнечным утром, так что моё настроение сразу улучшилось{w}, и я со спокойной душой пошёл умываться."
    stop music
    play music music_list["so_good_to_be_careless"] 
    show ext_washstand2_day with dissolve
    "Бррррр, ледяная."
    show ext_houses_day
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    "На обратной дороге вижу вереницу «выспавшихся и счастливых» пионеров.{w} Забежав в домик, я схватил форму и побежал на площадь, где уже начиналась зарядка."
    scene ext_square_day
    "Дмитриевна любит вести зарядку сама, подавая пример и заодно выдавать «наряды» лентяям и опозданцам."
    "И раз, и два, отдышались, повторили."
    sl "Саш, ты не напрягался бы"
    "Подошла ко мне Славя"
    show sl normal sport  at right with dissolve
    sl "После вчерашнего-то"
    "И покосилась на проходящую мимо Алиску."
    show dv normal pioneer2 at left with dissolve
    "Та делала вид что «я не я» и продолжала идти по своим делам."
    sh "Славь, всё хорошо."
    hide dv normal pioneer2 at left with dissolve
    "Девушка посмотрела на меня очень внимательно, но ничего не сказала.{w} Я продолжил упражнения, краем глаза замечая, что Славя с меня глаз не сводит. {w}Видимо боится, что опять отключусь или нечто подобное.{w} Странно видеть это."
    "Конечно, она запрограммирована быть доброй и отзывчивой{w}, но тут по другому.{w} Она словно живая, настоящая.{w} Она такая... хорошая."
    "Если бы я не знал, что она просто кукла, я бы влюбился.{w} А собственно, с чего я взял, что она фальшивка?{w} Может она действительно настоящая? И Семён с ней спасёт нас всех?{w} А может, с Леной или Алисой? Да вообще без разницы." 
    "Что если тут все настоящие, но не помнят ничего из прошлых посещений?{w} Тогда почему я был в другом «Совёнке»?{w} И этот «Пионер» тоже?"
    "От моих размышлений меня оторвала Славя."
    sl "Саш, мы закончили вообще-то. Скоро завтрак. Я с тобой пойду, попрошу чтоб увеличенную порцию дали.{w} Вон ты как взмок. Да и побледнел."
    show sl scared sport at right with dspr
    "Я улыбнулся"
    sh "Славь, честно, всё в полном порядке."
    scene ext_dining_hall_away_sunset with dissolve
    "Мы разошлись по домикам переодеться, и встретились у столовой. "
    "Как Славя и обещала, в столовой уже всё было обговорено{w}, и увеличенную порцию я получил с большим удовольствием."
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full 
    show sl normal pioneer with dissolve
    "Славя, удостоверившись, что я не упаду с этой грудой еды, пошла по своим делам. А я остался думать, куда податься."
    hide sl pioneer normal with dissolve
    menu:
        "Сесть с Леной":
            $ un_love += 1
            jump d2_un_br
        "Сесть с Алисой":
            jump d2_dv_br
label d2_un_br:
    $ persistent.sprite_time = 'day'
    $ day_time()
    play music music_list["memories"] 
    "Присесть к Лене было самым разумным решением{w}, да и поговорить мне с ней нужно."
    "Тихая спокойная кампания{w} — самое то, что нужно."
    "Она, как обычно, сидела несколько поодаль от шумных пионеров.{w} Казалось, что она хочет спрятаться за саму себя."
    sh "Лен, привет, свободно?"
    show un normal pioneer with dissolve
    "Она оторвалась от тарелки и посмотрела на меня.{w} Неужто мой обморок так всех напугал?"
    un "Да, садись конечно."
    "Я сел и принялся за еду.{w} Мне кажется, или она вкуснее обычного?{w} Но эта гнетущая тишина между нами...{w}Чёрт, как же это трудно — просто начать разговор."
    "Иногда мне кажется, что это дар.{w} Он им обладает, {w}а я нет...{w}Справедливостью тут не пахнет. Придётся идти напролом."
    sh "Лен, давно хотел спросить — а какие книги ты читаешь? Часто вижу тебя у Жени."
    "Ну не молчи!! Ответь...{w}пожалуйста."
    show un shy pioneer with dspr
    "Она посмотрела на меня изучающим взглядом и тихо ответила"
    un "Разные. Про природу, про отношения."
    "Чёрт, не могу вспомнить ни одного автора или текста.{w} Да и когда в последний раз я что-либо читал?"
    sh "И как тебе местная библиотека?"
    show un sad pioneer with dspr
    un "Многое я прочла, а того что хочу, там нет."
    sh "Например?"
    un "«Унесённые ветром»"
    "Ого, знакомое название. Я вроде её и нашёл."
    sh "Я точно видел её в библиотеке."
    show un normal pioneer with dspr
    un "А мы не нашли."
    sh "Может лежит у кого-нибудь, взяли и забыли?"
    un "Не буду я ходить, людей донимать.{w} Обойдусь пока."
    "Женщина, не вгоняй в тоску."
    sh "Знаю я несколько мест, где можно поискать."
    show un smile pioneer with dspr
    "Она мило улыбнулась"
    un "Хорошо."
    "Я закончил завтрак и пошёл к выходу — там меня уже ждала Славя."
    jump d2_ban



label d2_dv_br:
    $ persistent.sprite_time = 'day'
    $ day_time()
    play music music_list["i_want_to_play"] 
    "Мы не ищем лёгких путей.{w} Как мотылька тянет к огню, так и меня к Алисе.{w} Она обладает странным шармом, который манит и не отпускает.{w} Она сидела как раз одна, Ули видно не было, и я решил воспользоваться шансом."
    sh "Привет Алис, свободно?"
    show dv surprise pioneer2  with dissolve
    "Она посмотрела на меня удивлённым взглядом"
    dv "А ты не трус, хоть и дохлый.{w} Неужто за добавкой пришёл?"
    sh "Я, если что, с тобой поделюсь."
    show dv grin pioneer2  with dspr
    "Ей, видимо, понравилось такое поведение."
    dv "Ну говори очкастый, зачем пожаловал?"
    sh "Да поговорить на счёт..."
    "Действительно, а зачем?"
    sh "Насчёт группы."
    "Она удивилась"
    show dv surprise pioneer2  with dspr
    dv "Ты серьёзно?"
    sh "Да.{w} То есть нет.{w} В смысле, как бы Мику отговорить, а не то она действительно соберётся..."
    show dv pioneer2 laugh with dspr
    dv "А ты прям такой сразу испугался и прятаться"
    sh "Я не трус, позориться не хочу. Да и времени на репетиции нет."
    show dv guilty pioneer2  with dspr
    dv "А ты приложи больше стараний и усилий, может поможет."
    sh "Если долго мучиться..."
    "Вдруг я заметил одну странность в Алисе.{w} Она при любой возможности складывает руки на груди,{w} словно обхватывает её.{w} Обычно такая открытая, всё на показ, а тут такая скромность."
    "Я внимательно посмотрел на неё, что это не могло остаться незамеченным."
    show dv shy pioneer2 with dspr
    "Алиса густо покраснела, а до меня дошла причина её поведения {w}— на ней не было лифчика." 
    sh "А..."
    show dv rage pioneer2  with dspr
    dv "Слово вякнешь — закопаю"
    "Леденящим голосом сказала она."
    sh "Ты в эксгибиционистки записалась?"
    show dv shy pioneer2  with dspr
    dv "Нет, просто мелкая спёрла мой лифак для чего-то."
    "Ха-ха-ха-ха.{w} Но внешне я был невозмутим."
    sh "Мда, и где она сейчас?"
    dv "Незнаю.{w} Найду — на век отучу моё брать."
    sh "Хех. А тебе идёт."
    show dv guilty pioneer2  with dspr
    dv "Саш, помолчи а?"
    hide dv guilty pioneer2  with dissolve
    "Она встала из-за стола и пошла к выходу.{w} Я быстро проглотил последний кусочек и пошёл за ней следом.{w} Эхххх, надо было не торопиться, поскольку в столовую просто ворвались младшие, несмотря на вожатых."
    "Среди них была Уля."
    show us normal pioneer at right with dissolve
    "Алиса заметила её, и направилась прямиком к ней, с явно не дружескими намерениями."
    show dv angry pioneer2 at left with dissolve
    "Уля, учуяв неладное, действовала на удивление чётко и быстро." 
    "Прошмыгнув вплотную к своей возможной мучительнице она...{w} развязала узелок на рубашке и стала раскрывать её." 
    play sound sfx_scary_sting
    show dv surprise ex at left with dspr
    "Вау, вот это было бы зрелище{w}, но тогда Дмитревна запрёт её чёрт знает где{w}, подальше от глаз, и на одну опцию по спасению у меня станет меньше.{w} Придётся действовать быстро."
    menu:
        "Отвлечь":
            $ dv_happy += 1
            jump d2_dv_br1
        
        "Прикрыть её":
            $ dv_happy += 3
            jump d2_dv_br2
label d2_dv_br1:
    $ persistent.sprite_time = 'day'
    $ day_time()
    play music music_list["always_ready"] 
    "Я подскочил к Алисе и Уле.{w} Считанные секунды оставались до скандала.{w} Придётся импровизировать, и быстро." 
    sh "Ах вот ты!! Попалась!"
    show us fear pioneer at right with dissolve
    us "А что я?!"
    "Время на исходе." 
    sh "Стоять-бояться!!"
    "Но ни того, ни второго делать эта мелкая катастрофа не собиралась.{w} Я пронёсся сквозь столовую привлекая внимание всего и вся.{w} Возможно мне потом выскажут за поведение, но это неважно."
    "Выигранного времени достаточно, чтобы Алиса привела себя в порядок." 
    scene ext_dining_hall_near_day with dissolve
    "Уля уже скрылась из вида, когда я выскочил на крыльцо.{w} Да, резво бегает, нечего сказать.{w} Спортсменкой будет."
    "Размышлять о возможном конечно приятно{w}, но меня отвлекла вожатая"
    show mt angry pioneer panama with dissolve
    mt "Саша, что это было?{w} Как ты ведёшь себя?{w} Ты же такой прилежный и хороший мальчик."
    sh "А она у нас провода взяла"
    "Сказал я заранее продуманную ложь."
    show mt sad pioneer panama with dspr
    mt "И стоит ради этого устраивать истерики?{w} Эх Саша, Саша, я думала, что хоть на тебя и Славю можно положиться, а у тебя тоже ветер в голове.{w} Ладно, иди ищи свои провода."
    hide mt sad pioneer panama with dissolve
    "Дмитриевна ушла внутрь{w}, а я остался наслаждаться своим актёрским мастерством.{w} Хех, а я хорош."
    show dv normal pioneer2 at left with dissolve
    "По немногу из столовой стали выходить пионеры, и одной из первых была Алиса."
    show dv normal pioneer2 close with dspr
    "Она подошла ко мне, и тихо шепнула"
    dv "Спасибо тебе."
    sh "Без проблем"
    "Так же тихо ответил я ей."
    show dv smile pioneer2 close with dspr
    "Она еле заметно улыбнулась, и пошла по своим делам.{w} Я посмотрел ей в след.{w} Чёрт, а она такая красивая.{w} Таких просто не может существовать. {w}Однако я вижу это чудо предо мной, говорю с ней.{w} Сон наяву."
    hide dv smile pioneer2 close with dissolve
    show sl smile pioneer at right with dissolve
    "В это время ко мне подошла Славя." 
    sl "Ну и цирк ты устроил."
    sh "Да пожалуй."
    sl "Не надо так больше."
    sh "Постараюсь."
    sl "Ладно, пошли за мной — отрабатывать будешь"
    sh "Э, а с чего это?"
    sl "Ольга Дмитриевна сказала."
    "Вот стерва."
    jump d2_ban
    
label d2_dv_br2:
    $ persistent.sprite_time = 'day'
    $ day_time()
    play music music_list["glimmering_coals"]
    "Такой конфуз окончательно уничтожит её репутацию."
    "С этой мыслью я бросился к Алисе, которая бледнела на глазах.{w} В пару шагов я оказался у неё и заслонил своим телом, попутно откинув Улю."
    hide us normal pioneer at right with dissolve
    "Вроде я не привлёк большого внимания. Это хорошо."
    show dv shy pioneer2 close with dissolve
    "Вдруг я ощутил тепло на спине.{w} Хотя не тепло — пламя голого тела.{w} Алиса прижалась ко мне, спешно поправляя свой внешний вид.{w} Наверно и видок у меня, потому-что Уля стала неудержимо хохотать."
    "А за спиной было слышно только шебуршание блузки {w}, а чувствовалось только тепло Алисы.{w} Я начинаю понемногу по нему скучать.{w} Наконец закончив приводить себя в порядок, Алиса накинулась душить свою подругу"
    show us angry pioneer at right with dissolve
    show dv rage pioneer2 at left with dissolve
    dv "Ах ты маленькая..."
    "Но делала она это скорее напоказ, чем реально на неё злилась." 
    sh "Цирк, да и только."
    show us grin pioneer at right with dspr
    us "Ой Сань, а что ты так покраснел?"
    show dv grin pioneer2 at left with dspr
    dv "Это он почувствовал то, чего ему никогда не приходилось и не придётся"
    show dv laugh pioneer2 at left with dspr
    "Хоть несмотря на подколку, она смотрела на меня с благодарностью{w}, и в знак благодарности еле заметно чмокнула воздух."
    "Видимо это ещё больше вогнало меня в краску, т.к. девушки засмеялись."
    sh "Да ну вас"
    "И с этими словами я пошёл на выход"
    scene ext_dining_hall_near_day with dissolve
    show dv laugh pioneer2 at left with dissolve
    dv "Обиделся что ли?"
    "Раздался из-за спины голос Алисы"
    sh "Не, на обиженных воду возят."
    dv "Вот и правильно."
    show dv smile pioneer2 at left with dspr
    "Она чмокнула меня в щёку и упорхнула."
    hide dv smile pioneer2 at left with dissolve
    "Я огляделся — никого.{w} Так значит вот ты какая, вот как тебя запрограммировали.{w} Это сильно отличается от ожидаемого. {w}Ты глянь — почти настоящая. "
    show sl smile pioneer  with dissolve
    sl "Опять они над тобой издеваются?"
    sh "Есть немного" 
    sl "Не обращай внимания.{w} Столько лет, а до сих пор не могут нормально привлечь к себе внимание.{w} Ладно Уля - Она ещё ребёнок, но эта дылда!"
    "Хмм, Славя делает выводы и рассуждает об этих оторвах. {w}И в её словах не одной злой мысли."
    "Интересно, а ты то тут какая? Думаю, сейчас я это и выясню"
    sl "Мне тут Дмитриевна одно дело поручила, не поможешь?"
    sh "Почту за честь"
    "Картинно раскланялся я."
    "Славя засмеялась"
    show sl laugh pioneer  with dspr
    sl "Пошли, джентельмен."
    jump d2_ban



label d2_ban:
    $ persistent.sprite_time = 'day'
    stop ambience
    scene ext_houses_day with dissolve
    play music music_list["forest_maiden"]
    "Не торопясь, мы вышли из лагеря.{w} По всей видимости, наш путь лежал к бане.{w} Уж не дрова колоть меня зовут?"
    show sl normal pioneer  with dissolve
    sl "Не волнуйся Саш, они уже наколоты. Нам только сложить их."
    sh "Неужто у меня всё на лице написано?"
    sl "Да, читаешся невооружённым глазом"
    "Улыбнулась она."
    show sl smile pioneer  with dspr
    "И мы продолжили путь в тишине."
    "Утро было в самом разгаре, и я наслаждася прекрасной погодой.{w} Абсолютно чистое небо действует успокаивающее, отгоняя тоску и ненужные мысли." 
    scene ext_path_day with dissolve
    show sl normal pioneer  with dissolve
    "Ну и что, что я тут единственный живой человек?{w} Эти...{w}пионеры вполне похожи на людей.{w} В общем - мне тут пока комфортно. {w}Всё же в 1-й раз в таких декорациях."
    sl "О чём думаешь, Саш?"
    sh "Небо такое красивое... и зелень кругом."
    show sl smile pioneer  with dspr
    "Славя понимающе посмотрела на меня"
    sl "Да, мне тоже нравится.{w} Чувствуешь себя такой спокойной{w}, такой живой." 
    sh "Хотелось бы, чтобы это длилось вечно."
    show sl serious pioneer  with dspr
    sl "Что ты, Саш?{w} В этом и есть красота - в том, что она конечна.{w} Наслаждаться моментом, а потом ждать нового."
    sh "Бррр, не люблю я осень и зиму."
    "Мы углубились в лес, и мне показалось, что солнце уж слишком слабо пробивалось сквозь кроны деревьев.{w} Кажется, что уже не то вечер, не то ночь."
    scene ext_bathhouse_night with dissolve
    $ persistent.sprite_time = 'night'
    $ night_time()
    "Вот уже и баня показалась на виду"
    show sl normal pioneer  with dissolve
    sl "А я везде красоту нахожу.{w} У нас так красиво."
    sh "Ты, наверно, краеведом или зоологом станешь..."
    show sl surprise pioneer  with dspr
    sl "Точно, а как ты догадался?"
    sh "Тебе это явно пойдёт."
    show sl shy pioneer  with dspr
    sl "Спасибо. Хорошо, что ты заметил."
    hide sl shy pioneer  with dissolve
    "Вот мы и на месте.{w} Чтож, работы не так уж и много, а со Славей  вместе тем более быстрее справимся. Ну что, поехали."
    "Работка не пыльная, неспешная, и я решил развлечь себя разговором{w}, а может и узнаю что-либо важное."
    sh "Славь, всё хотел спросить — тебе нравится в лагере?"
    show sl normal pioneer  with dissolve
    sl "Да, очень."
    sh "Но ты вся в работе?{w} Какой отдых?"
    sl "Перемена работы - лучший отдых.{w} Да и работа тут одно название. Можешь считать это активным отдыхом."
    sh "И ты бы не хотела ничего \"эдакого\"?"
    sl "Думаю нет. Я довольна тем, что имею."
    "А я нет.{w} Просто смириться я отказываюсь."
    show sl smile pioneer  with dspr
    sl "А ты, Саш?"
    sh "Тут тихо и умиротворённо.{w} Это да.{w} Но мне кажется, что тут жизнь как бы \"замерла\"."
    stop music fadeout 3
    sl "Тебе кажется.{w} Я слышала, что ты с Мику и Алисой музыкой занимался, да и в библиотеке я тебя нашла в окружении девушек.{w} Так что тут жизнь бьёт ключом, что бы ты ни говорил."
    sh "Хм, я понял тебя. А как же остальные?"
    play music treck_op
    sl "А что они? Отдыхают, расслабляются.{w} У них всё хорошо.{w} Каждый нашёл тут себе развлечение."
    "Мда, толку от тебя немного.{w} Всё у всех прекрасно и удивительно.{w} С чего это я вообще затеял с тобой разговаривать?{w} Мда, с кукол толку не будет."
    "Стоп.{w} Почему я раньше не додумался?{w} Зачем сводить Его и этих чучел?{w} Если я нашёл способ пройти, то и настоящие пионерки смогут!" 
    "Но как привести их сюда?{w} Ведь мне такой фокус удался далеко не с первого раза{w}, и потребовалось очень много сил."
    "Да и как мне это поможет...{w} Хотя, если каждой из них рассказать о \"Совёнке\"{w}, Семёне{w}, то они тоже захотят вырваться.{w} Они должны захотеть,{w} обязанны."
    "Мне \"просто\" надо помочь им вспомнить."
    "И если удасться вытащить хоть одну сюда,{w} то шансы на спасение резко возрастут."
    "Так и поступлю."
    stop music fadeout 3
    show sl happy pioneer  with dspr
    play music music_list["reminiscences"]
    "Закончив работу, Славя удовлетворённо улыбнулась"
    sl "Фуф, вот и справились."
    sh "Ага, быстро"
    show sl shy pioneer  with dspr
    sl "Спасибо тебе за помощь"
    sh "Нет проблем."
    sl "Саш, не в службу а в дружбу - не поможешь баньку натопить?{w} Помоемся и на обед пойдём."
    sh "Да без вопросов, Славь"
    "Под её руководством я быстро растопил баню. Это оказалось не так уж и сложно, мне даже понравилось."
    show sl serious pioneer  with dspr
    sl "Саш, ты первым пойдёшь или я?"
    sh "Славь, ну ты же знаешь ответ уже. Могла бы не спрашивать."
    sl "Ты уверен? Ты ведь больше работал, тебе и отдыхать первому."
    sh "Потом отдохну. Давай иди. И не боись - подсматривать не буду."
    show sl smile pioneer  with dspr
    sl "А я в тебя верю - ты не такой"
    hide sl smile pioneer  with dissolve
    "Улыбнулась она и пошла в предбанник."
    play music music_list["take_me_beautifully"] fadein 3
    "Спустя пару минут я уже слышал плеск воды.{w} Пусть попарит свои косточки, а я пока со своими мыслями разберусь.{w} Но придаться размышлением мне не получилось, ибо я услышал пение"
    "Вот чего не ожидал, так этого.{w} У Слави красивый голос, и петь она явно умеет.{w} Но петь в бане? {w}Странная она порой."
    scene d3_sl_bathhouse with dissolve
    "Тихонько загянув в окно, я увидел, как Славя проверяет воду и веники.{w} Она в одном полотенце, {w}и пока не запотели окна, я любовался её телом.{w} Эти изгибы тела, ноги, волосы."
    "Я отвернулся {w}- хороша, чертовка.{w} И почему ЕМУ достаются такие?"
    stop music
    scene ext_path2_night with dissolve
    "Внезапно я услышал шуршание в ближайших кустах."
    play sound sfx_mystery_movement
    play music music_list["sunny_day"] fadein 3
    "Слишком близко и слишком шумно.{w} Мне стало не по себе{w}- мало ли что тут водится.{w} Взяв небольшое полено в руки, я приготовился защищаться."
    "Секунды тянулись мучительно долго. {w}Я чувствовал, что тут кроме меня и Слави есть ещё что-то или кто-то{w}, чьи замыслы мне не известны.{w} Страх начал сковывать мой разум, и большими усилиями воли я поддерживал сосредоточение."
    sh "Эй, кто там?"
    "Нет ответа."
    "Может моё воображение разыгралось?{w} Но я точно слышал хруст веток и шебуршание. {w}Я напряг все чувства, чтобы удостовериться в нашей безопасности."
    "И смог мельком увидеть едва заметную тень{w}, которая быстро скрылась в чаще."
    show monster with moveinright 
    hide monster with dissolve
    menu:
        "Не уйдешь":
            $ uv_trust += 1
            $ sl_love += 1
            $ el_happy += 1
            $ un_love += 1
            $ dv_happy += 1
            jump d2_ban_1
        "Слишком быстро":
            jump d2_ban_2
label d2_ban_1:
    play music music_list["revenga"] fadein 3
    play sound sfx_run_forest
    "Я помчался за тенью, в надежде хотя бы рассмотреть то, что бежит.{w} Всякого можно ожидать, так что «оружие» (обычное полено) я прихватил с собой. {w}Моя цель явно была в хорошей форме, и не давала мне и шанса достичь её. "
    "Вскоре я понял, что скоро выдохнусь, и приложил все силы.{w} На последнем рывке я увидел то, за чем гнался, точнее хвост этого. "
    show monster with dissolve
    "Странно всё это. Ладно, пора обратно."
    hide monster with dissolve
    play music music_list["forest_maiden"] fadein 3
    scene ext_bathhouse_night with dissolve
    "У бани меня уже ждала Славя.{w} Вид её был сильно обеспокоенный."
    stop sound 
    show sl serious pioneer  with dissolve
    sl "Саш, ты где был?"
    sh "Бегал"
    sl "Куда? Зачем?"
    sh "Да так, показалось. Не бери в голову."
    sl "А мыться?"
    sh "Потом."
    "Девушка сильно удивилась, но ничего не сказала."
    show sl surprise pioneer  with dspr
    sl "А бревно  зачем?"
    sh "Вот ты любопытная.{w} Понадобилась оно мне. Зачем, не скажу."
    sl "Саш, если ты думаешь, то тут в округе хищный зверь, то успокойся — таких тут нет."
    show sl serious pioneer  with dspr
    sh "А какие есть?"
    sl "Мелкие грызуны, зайцы, может лисы. В общем ничего такого, что может навредить.{w} Уж я-то знаю — не первый год сюда езжу."
    "Ты даже не представляешь на сколько «не первый» я сюда езжу."
    sh "Ладно, пошли отсюда, обед скоро. Есть охота."
    show sl normal pioneer  with dspr
    sl "Хорошо Саш, я тоже так думаю."
    "Обратная дорога показалась мне легче и приятнее, но меня не покидало ощущение, что за мной наблюдают."
    jump d2_dinn
    
label d2_ban_2:
    play music music_list["no_tresspassing"] fadein 3
    "Гнаться смысла не было абсолютно, и желания тоже.{w} Мало ли что ТУТ по лесам бегает?{w} Но на всякий случай я подошёл ко входу бани, чтобы пресечь возможные неприятности"
    "Пару минут спустя на улицу вышла Славя.{w} Она удивлённо посмотрела на меня, эдакий почётный караул."
    show sl serious pioneer  with dissolve
    sl "Саш?"
    sh "Прежде чем ты подумаешь всякое -  тут бегает что-то. Вот я и решил у входа постоять."
    sl "Какой ты, Саш, ответственный."
    show sl smile pioneer  with dspr
    sl "Но зря ты волновался - хищников тут нет."
    "Только \"хищницы\",да?"
    sh "Но я же видел..."
    show sl normal pioneer  with dspr
    sl "Зайца или лису. Успокойся Саш, и пойдём обратно "
    sh "Ну раз ты так уверена, тогда пошли."
    "На обратной дороге я шёл позади Cлави, с опаской оглядываясь по сторонам.{w} Нет, мне точно не показалось, и оно вполне себе может быть рядом."
    show sl smile2 pioneer  with dspr
    sl "Саш, да не волнуйся ты так ."
    "Вправду, её голос вселял спокойствие и уверенность.{w} Я посмотрел на идущую впереди девушку.{w} Она улыбнулась, поправила косы, и пошла дальше.{w} Идя за ней, я поймал себя на мысле, что не спускаю с неё глаз{w} - она просто пленила мой разум."
    "Все мысли только о ней.{w} Славя, почему ты не настоящая? {w}Почему должна достаться ЕМУ? "
    "Ненавижу.{w} Просто ненавижу."
    jump d2_dinn
    
label d2_dinn:
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene ext_dining_hall_near_day with dissolve
    play music music_list["she_is_kind"] fadein 3
    "У столовой нас ждала Ольга Дмитриевна." 
    show mt normal pioneer panama with dissolve
    mt "Ну, как всё прошло?"
    sh "Всё прошло в лучшем виде.{w} Ваше задание выполнено"
    show mt smile pioneer panama with dspr
    mt "Вот и молодцы, а теперь идите обедать, не то ничего не останется "
    sh "Я руки мыть"
    "И с этими словами я пошёл до умывальников."
    scene ext_washstand2_day with dissolve
    "По быстрому освежившись, я вернулся в столовую."
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    "Там во всю щёл приём пищи{w} - пионеры весело галдели, наслаждаясь простыми, но вкусными блюдами."
    "Взяв свою порцию и окинув зал взглядом я прищёл к неутешительному выводу - место есть только рядом с Мику. Делать нечего, ведь нет в мире совершенства."
    sh "Мику, привет. {w}К тебе можно?"
    show mi smile pioneer at left with dissolve
    mi "Конечно Сань, садись пожалуйста. Нам есть о чём поговорить..."
    "Вот это страшно."
    mi "Ты не бери в голову, что Алиса наговорила тебе о твоей игре. Для новичка ты играл очень хорошо, намного лучше, чем остальные. "
    mi "И мне очень понравилось с тобой играть, и поэтому я настаиваю на твоём вступлении ко мне в клуб для дальнейших репетиций."
    sh "А Алиску что не зовёшь?"
    show mi dontlike pioneer at left with dspr
    mi "Будто ты её не знаешь? Делает вид, что сама по себе, и никто ей не нужен. Красивая, гордая... И одинокая."
    show mi sad pioneer at left with dspr
    "Мику на этих словах несколько приуныла.{w} Браво, хорошая постановка{w}, но меня не разжалобить."
    sh "Она сама решила поставить себя так."
    mi "Но мы-то можем постараться её исправить. Такое поведение не пойдёт на пользу ни ей, ни нам. Она ведь хорошая."
    "\"Нам\"?! С каких это пор?"
    show mi normal pioneer at left with dspr
    sh "А с его это такая о ней забота? {w}Ты что-то скрываешь"
    mi "Нет Саш. Я музыкант, а музыкант чует музыканта издалека. У Алисы есть дар, но из-за её характера она может всё... упустить. Мы, как пионеры и её друзья, не можем допустить такого.  Мы обязаны ей помочь, даже если она этого не просит."
    sh "Не умеешь — научим. Не хочешь — заставим …"
    show mi surprise pioneer at left with dspr
    mi "Что? О чём ты?"
    sh "Да так, пошутил."
    "Мику зло посмотрела на меня" 
    show mi angry pioneer at left with dspr
    mi "Саш, это очень серьёзно. Будь серьёзнее, это важное дело."
    sh "Да знаю я.{w} И согласен с тобой. {w}Только как мы это делать будем?"
    show mi smile pioneer at left with dspr
    "Она улыбнулась"
    mi "Я всё продумала. Нам надо научить её выражать свои чувства более мягкими средствами. "
    sh "Ну ты и замахнулась!"
    mi "Для начала ты поговоришь с ней о..."
    dv "О чём он со мной поговорит?"
    "Раздался голос Алисы из-за  спины."
    "Я обернулся"
    play music music_list["that_s_our_madhouse"] fadein 3
    show dv angry pioneer with dissolve
    "Вид у неё был не очень дружелюбным. {w} Ответ надо искать быстро, но как назло ничего толкового в голову не идёт"
    sh "Поговорить о новеньких."
    "И тут Остапа понесло"
    sh "Надо их хорошо встретить, и заинтересовать." 
    show dv surprise pioneer with dspr
    dv "С каких это пор ты, Саш, такую деятельность развил?"
    "Так, я её заинтересовал.{w} Что дальше?"
    sh "Ну знаешь, остаётся мало времени."
    show dv angry pioneer with dspr
    sh "Славя  попросила нас... Э... Организовать им насыщенный отдых.{w} Мы пока ничего умнее клубов не придумали."
    show dv angry pioneer with dspr
    dv "А я тут при чём?"
    sh "А при том, что это касается всех.{w} Ты весьма...{w} активная девушка, так что поможешь?"
    dv "Быть клоуном и развлекать залётных мажоров?"
    sh "Быть другом и помочь отдохнуть."
    "Алиса удивлённо посмотрела на нас."
    show mi normal pioneer at left with dspr
    show dv surprise pioneer with dspr
    dv "Ну вы даёте.{w} Никогда бы не подумала, что вы мне такое предложите."
    "Видимо, её не проняло."
    sh "По крайней мере не доставай новеньких сильно.{w} Будь ласковой, что ли "
    show dv grin pioneer with dspr
    dv "Сань, а не пойти тебе сам знаешь куда?"
    "Мику,{w} всё это время сидевшая тихо, поняла,{w} что я сдаю позиции, и нужна помощь"
    show mi smile pioneer at left with dspr
    mi "Алис, ну будет тебе. Может ты новых друзей найдёшь. Их много не бывает. А ты то одна, то с Улькой носишся. Чем больше — тем веселее."
    dv "Скажите честно{w}, это вас Дмитревна подписала на агитацию?"
    mi "Нет, это добровольное начало." 
    "Подобных разговоров я никогда не слышал от этих двоих.{w} Столько жизни{w}, столько заботы."
    show dv grin pioneer with dspr
    dv "Хорошо, я поняла вас. Сменим тему.{w} Какие у тебя планы Мику? "
    show mi happy pioneer at left with dspr
    mi "Я в клуб пойду. Надо приводить всё в порядок, чтобы произвести правильное впечатление."
    show dv smile pioneer with dspr
    stop ambience
    dv "Хорошо.{w} Потом зайду — помогу тебе."
    "Про меня не спросила.{w} Видимо программа не позволяет отойти от намеченных установок на Семёна."
    sh "Ладно девушки. Приятно было с вами поболтать, но работа зовёт."
    "И с этими словами я пошёл относить поднос на мойку."
    
    scene ext_dining_hall_away_day
    play music music_list["your_bright_side"] fadein 3
    "Выйдя на улицу, я быстрым шагом пошёл до радиоклуба{w}, а не то Дмитревна найдёт для меня очередное гениальное задание."
    "Сейчас прекрасное время предаться раздумьям о дальнейших планах.{w}Славя,{w} Лена, {w}Алиса,{w} Мику,{w} Уля,{w} Женя {w}- с какой начать?{w} Как мне обьяснить им цель прибытия? Поймут ли? Согласятся ли?"
    "Чёрт{w}, это так сложно продумать.{w} И почему Ему удаётся так легко говорить с ними?{w} Они всегда его выслушают и поймут.{w} А мой путь тернист, даже слишком."
    "Справедливо ли это?{w} Скорее всего да, ведь не всем дано наслаждаться жизнью и иметь возможность исправлять свои мелкие ошибки{w}, а кому-то предписано идти к цели сквозь боль и страдания, трудиться на благо других,{w} затем погрузиться в забвение."
    "Да уж{w}, хорошая перспектива, нечего сказать." 
    "Я не придавал этому значение{w}, но один вопрос всё время мучает меня {w}- почему я?{w} Жил бы в беспамятстве в своём \"Совёнке\",{w} делал робота,{w} лазил по подвалам. {w}Но нет, великое провидение выбрало меня для мытарств и злоключений."
    "Интересно,{w} хочу ли я всё забыть?{w} Наверно..."
    "Но дать ответ самому себе я попросту не успел, ведь мой верный оруженосец появляется в самый нужный момент."
    show el smile pioneer with dissolve
    el "Cаш, а вот и ты! {w}Так быстро выскочил из столовой, что я еле догнал.{w} Куда летишь?"
    sh "Подальше о начальства.{w} Чувствую, что у неё на меня большие планы."
    el "Не, врятли - она с девчёнками по делам пошла."
    sh "Да?{w} Хорошая новость.{w} Можно не ожидать внезапных вторжений. Пошли до клуба."
    "По дороге Эл не обронил ни слова, хотя это на него уж точно не похоже.{w} Такая гнетущая тишина действует мне на нервы, и я решил первым начать разговор"
    scene ext_clubs_day with dspr
    sh "Эл, ну а как твои дела с Женей?{w} На тебе просто лица нет, опять она тебя отшила?"
    show el normal pioneer with dspr
    el "Не совсем так.{w} Я не понимаю, что она от меня хочет.{w} Вроде она и не против общения, но внезапно может охладеть и начать ругаться.{w}Я не знаю что делать."
    sh "Не расстраивайся. Если она с тобой общается, значит ты ей не безразличен. {w}Да и кто поймёт этих женщин?"
    "Я улыбнулся "
    sh "Если поймём,то на нобелевка обеспечена,{w} а может и вечная благодарность человечества."
    show el sad pioneer with dspr
    el "Угу, а может наши имена предадут забвению"
    "Горько пошутил он."
    sh "Хорошо, что чувство юмора у тебя на месте."
    el "Да уж.{w} Саш, что мне делать?{w} я запутался"
    show el upset pioneer with dspr
    menu:
        "Никто тебе в этом деле не советчик. Я могу только всё испортить":
            $ el_happy += 1
            jump d2_el_1
            
        "Эл, возможно здесь и сейчас решается наше будующее. Не упусти своё счастье":
            jump d2_el_2
        
        "Эл, а ты в ней уверен? Если бы ты ей нравился, она бы так не вела себя":
            $ el_happy -= 1
            jump d2_el_3
label d2_el_1:
    "Наверно я разочаровал его своим ответом,{w} ведь нужного совета он так и не получил"
    sh "Эл, я тебе тут не советчик {w}- у самого опыта мало в таких вещах.{w} Но могу сказать одно - будь честен с собой и с ней, а там разберётесь. Одним словом — дерзай."
    show el normal pioneer with dspr
    el "Хм, спасибо и на этом, что ли."
    "Эл задумался и приободрился"
    show el smile pioneer with dspr
    el "Наверное, ты прав. Это моё дело — я с ним и разберусь."
    "Самовнушение — интересная штука. Появляется надежда, которая порождает стремление."
    sh "Рад слышать это." 
    el "Спасибо."
    sh "Да не за что, вроде как."
    show el normal pioneer with dspr
    el "Нет, ты подсказал мне верную мысль. {w}Я сам решу свои проблемы."
    jump d2_uv
    
label d2_el_2:
    show el surprise pioneer with dspr
    el "Ты уверен?"
    sh "Да.{w} Всё что с нами происходит имеет значение и важные последствия. {w}Не теряйся и подойди к ней."
    show el scared pioneer with dspr
    el "Что, прямо сейчас? Я... стесняюсь"
    sh "Может, боишся отказа?{w} А может, она согласится? Не попробуешь - не узнаешь.{w}А так будешь сидеть и ждать, а ожидание сводит с ума, уж поверь."
    "Создаётся впечатление, что Эл хочет спрятать себя за себя."
    sh "Можешь не сегодня.{w} Подготовься морально{w}, соберись с силами.{w} Но в долгий ящик не откладывай, а не то уедет твоя принцесса на тыкве, и останется у тебя лишь её туфелька 40го размера." 
    show el normal pioneer with dspr
    el "Спасибо Саш. Так и сделаю."
    jump d2_uv
    
label d2_el_3:
    show el shocked pioneer with dspr
    el "Но..."
    sh "Что «НО?»{w} Нет, девушка может поломаться для приличия,{w} но в разумных пределах.{w} Хорошо, что она хоть разговаривает с тобой, а не игноритрует."
    "Мои слова вгоняли Эла в ступор{w}, но ты просил совет — так получи."
    sh "Ты, конечно, можешь пытаться привлечь её внимание{w}, хотя мне кажется, проще танк консервным ножом вскрыть."
    show el serious pioneer with dspr
    el "Уверен? Мне казалось, я ей...{w} приятен."
    sh "Увы, ты не различаешь сути.{w} Влюбился ты друг, по самые уши.{w} Ведь ты меня сейчас даже не слушаешь, верно?"
    el "Я тебя понять не могу.{w} Ты меня отговариваешь что-ли? "
    show el upset pioneer with dspr
    sh "Предостерегаю. Ты можешь обжечься очень больно." 
    "Эл задумался.{w} Мне хотелось высказать ему всё об этих «пионерках», но это не принесёт никакой пользы."
    sh "Ты ведь не передумаешь, я уверен в этом.{w} Тогда не тяни резину — иди и поговори с ней."
    show el normal pioneer with dspr
    el "Да, точно. Когда на пляж пойдём, {w}я с Женей все расставлю на свои места."
    "Пляж?"
    jump d2_uv

label d2_uv:
    scene int_clubs_male_day with dissolve
    play music music_list["drown"] 
    play sound sfx_open_door_clubs
    "Войдя в клуб, Эл подошёл к роботу и начал возиться с ним{w}, полностью погрузившись в работу.{w} Я же начал дорабатывать плату управления.{w} Работа несложная, даже медитативная."
    show el normal pioneer with dissolve
    "Но ожидание приезда это «героя» не даёт мне покоя.{w} Так мало времени, и так мало сделанно."
    el "Саш, что задумался?{w} Всё получается?"
    sh "Да, просто хандра напала."
    show el sad pioneer with dspr
    el "Тебе скучно?"
    sh "Нет, скорее грусть. Столько планов - а не успеваю."
    show el smile pioneer with dspr
    el"Пффф, не бери в голову. Мы всё доделаем, а ЕСЛИ"
    "Он сделал акцент" 
    el "ЕСЛИ не успеем, то мы же не в разные концы планеты разъедемся.{w} Ты же говорил, что рядом живём, считай соседи.{w} Надо будет — я к тебе домой приеду и привезу всё необходимое."
    "Дом.{w} Я уже и не помню то это значит.{w} Что он из себя представляет?{w} Кто ждёт меня? {w}Да и кто я? {w}В памяти остались лишь бессчётные смены, да этот клуб, {w}чтоб ему провалиться, {w}и пустота. "
    "Как можно забыть такую важную вещь,{w} как дом и родных?"
    "Вдруг страшная мысль пронзила мой разум {w}— а есть ли это у меня?{w} Существую ли я вообще? "
    "Но я есть я{w}, сижу тут, паяю и думаю.{w} Я есть! {w}Меня не может не быть! {w}Так почему же я забыл своё прошлое?{w} Что заставило сесть в тот проклятый автобус?"
    "Странно.{w} Такие мысли не посещали меня раньше.{w} Всё было для меня словно задачей, которую надо решить подручными средствами. "
    "Эл встал и пощёл в кладовку. «Я за винтами»"
    hide el smile pioneer with dissolve
    sh "Хорошо."
    "Буркнул я и вернулся к своим мыслям. {w}Так{w}, на чём я остановился в самокопании?"
    "Но продолжить не удалось{w} — раздался стук в дверь."
    play sound sfx_knock_door3_dull
    sh "Открыто."
    "Нет ответа"
    play sound sfx_knock_door3_dull
    "Лишь стук."
    sh "Открыто!!"
    play sound sfx_knock_door3_dull
    "Опять стучат. Если это Уля балует, ух получит она." 
    "Снова. Придётся открыть дверь самому — чай не барин."
    scene ext_clubs_day with dissolve
    "Открыв дверь, я ожидаемо никого не увидел. Старая шутка {w}— открыть/закрыть,{w} пока не доведёшь до крика." 
    "Осмотрев по сторонам, я не увидел ничего подозрительного. {w}Но ведь стучали же!{w} Постояв на улице пару минут, я убедился, что тут никого нет, и вернулся внутрь."
    scene int_clubs_male_day with dissolve
    "На моём рабочем столе лежало спелое зелёное яблоко."
    "Откуда оно тут!?!"
    "Я подлетел к окну — неужто через открытую форточку закинули?{w} Нет, врятли.{w} Что тут происходит?{w} Мистика какая-то.{w} Хотя чему я удивляюсь, оказавшись в \"Совёнке\""
    "Но факт есть факт - мне подкинули свежий фрукт.{w} Есть или не есть? Да не вопрос."
    play sound sfx_eat_apple 
    "(хрум)"
    "Как и ожидалось, вкус феерический.{w} Проглотив первый кусочек, я высоко оценил доброту и заботу своего тайного поклонника. {w}Это самое то, что нужно." 
    "Сконцентрировавшись на поглошении свежего продукта{w}, я отринул все мысли{w}, какие терзали моё сознание. {w}Так приятно иногда отвлечься от забот и предаться простым удовольствиям."
    "Схрумкав всё до конца, Я задался вопросом: что там с Элом?"
    scene int_clubs_male2_night with dissolve
    show el normal pioneer with dissolve
    "Эл был обнаружен в груде коробок, занятый поиском деталей.{w} Чтож, не буду отвлекать его от столь интересного занятия."
    "Даже хорошо{w} - не будет мешаться.{w} Но что на счёт того вкусного яблока.{w} Кто его подсунул?"
    "Это нельзя оставить без внимания{w}, так что я пошёл искать улики."
    scene ext_clubs_day with dissolve
    "Облазив всё под окнами, я заметил следы{w}, и решил пойти по ним.{w} Путь вывел меня к воротам  лагеря. "
    scene ext_no_bus_sunset
    "Хм, никого. Я оглянулся, чтобы осмотреться по сторонам, но ничего подозрительного не заметил.{w} Может, я не туда пришёл? Я пошёл по дороге, в надежде найти что-нибудь по пути." 
    "Время близилось к ужину, и солнце не так жарило, что придавало мне спокойствие и комфорт в моём импровизированном путешествии."
    sh "Эххх, хорошо"
    "Вырвалось у меня."
    voice "А ты хочешь всё испортить?"
    "Раздалось за спиной."
    show monster with dissolve
    play music music_list["door_to_nightmare"]
    "Сказать, что я испугался {w}— ничего не сказать."
    voice "Не оборачивайся.{w} Стой и смотри вперёд"
    "Продолжил незнакомец."
    "Этот голос я слышу впервые, но могу точно сказать, что он женский."
    sh "Так. Стою."
    voice "Хорошо.{w} Слушай внимательно{w} — не вмешивайся в дела Семёна." 
    sh "А не то что? "
    "Сказал я и попытался повернуть голову."
    "Но сделать это не удалось{w}, поскольку я ощутил на шее нечто острое."
    play sound sfx_scary_sting
    "Нож или когти?{w} Да, видимо придётся подчиниться."
    voice "Не то вы все тут застрянете навеки."
    sh "Если ты так хорошо осведомлена{w}, то ты знаешь, сколько я тут проторчал.{w} Ещё немного, и сойду с ума."
    voice "Знаю, Саш{w}, но у тебя ещё так мало опыта. {w}Ты можешь всё испортить."
    sh "Но я стараюсь сделать как лучше!"
    voice "А получится как всегда.{w} А теперь закрой глаза.{w} И извини меня."
    show blink 
    "Что?{w} Но додумать я не успел, тк мне на глаза легла девичья рука, и я ощутил поцелуй в губы." 
    "Это так приятно...{w} что я..."
    hide blink
    scene ext_square_day
    play music music_list["into_the_unknown"] 
    show unblink
    "Открыл глаза я уже в лагере, на площади. {w}Как я сюда попал?" 
    "Всё вроде без изменений, но что-то тут не так.{w} И тут меня как молнией ударило!{w} Сколько сейчас времени!{w} Я посмотрел на часы — до обеда ещё ой как далеко.{w} Как это?!"
    "Так, спокойно.{w} Я переместился во времени или в пространстве?{w} Надо проверить."
    scene ext_clubs_day with dissolve
    "Я пошёл до радио-клуба, в надежде увидеть Эла, и по его реакции понять, куда меня занесло.{w} Но клуб был закрыт. Странно, где он?"
    sh "Так, понятно."
    "И я двинул к столовой.{w} В лагере словно все вымерли, поскольку я никого не встретил по пути."
    scene  ext_dining_hall_away_day
    "Дойдя до здания, я решил заглянуть в окно. {w}То, что я увидел, повергло меня в шок"
    scene int_dining_hall_people_day with dissolve
    show pioneer normal with dissolve
    "Там был весь лагерь, и все чествовали Семёна!"
    show dv normal pioneer2 at right with dissolve
    show sl normal pioneer at left with dissolve
    "Его окружали все девушки, а также Дмитриевна. Неподалёку стоял Эл... И я." 
    hide dv normal pioneer2 at right with dissolve
    hide sl normal pioneer at left with dissolve
    show sh normal pioneer at right with dissolve
    show un normal pioneer at left with dissolve
    "Что?"
    "Как это?"
    play sound sfx_scary_sting
    "В ужасе я отринул от окна, и побежал прочь. "
    scene  ext_houses_day with dissolve
    "Но почти сразу же остановился{w}, взяв себя в руки.{w} Одна деталь, которой я не придал внимания, вдруг осенила меня {w}— в столовой небыло Ули, хотя она должна была в первых рядах за куском торта."
    "Что я имею:{w} Семён тут, второй Я тоже, а Ули нет.{w} Быть может...{w}Я попал к ней? {w}Но как?{w} Неужто та незнакомка?{w} И её это «извини меня»"
    "Думаю, на эти вопросы я найду ответы, когда найду Улю."
    scene ext_playground_day with dissolve
    play music Freedom fadein 3
    "Найти ей не составило труда, хотя я был несколько удивлён увиденным.{w} Она была на площадке, одна, и чеканила мяч.{w} Выглядела она покинутой и удручённой."
    show us calml pioneer with dissolve
    sh "Ульян, а ты чего тут?"
    "Сделал я попытку включить дурака."
    "Перестав забавляться с мячом, Уля подошла ко мне"
    show us normal pioneer with dspr
    us "А ты чего тут делаешь?{w} Разве ты не должен со всеми торт есть?"
    sh "Я не голоден.{w}  И ты не ответила на мой вопрос."
    show us upset pioneer with dspr
    us "Не лезут в меня больше торты."
    "Торты???"
    sh "Ульяна, а сколько смен ты тут?"
    "Решил я играть в открытую. "
    "Она удивилась такому вопросу."
    show us surp2 pioneer with dspr
    us "Не помню точно. Я тут часто бываю.{w} А почему ты спрашиваешь?"
    sh "И каждый раз тебя тортом потчуют?{w} Может, это тебе кажется, что ты приезжала? Может, ты и не уезжала ни разу?"
    show us fear pioneer with dspr
    us "Саш, ты что говоришь-то? {w}Ты себя хорошо чувствуешь?"
    "Подул тёплый ветер, разогнавший тучи.{w} Освободившееся вечернее солнце приветливо обогрело нас.{w} Такой порыв ветра слегка растрепал её прическу, и Уля стала спешно поправлять её. {w}Она что-то скрывает, я чувствую это. "
    sh "Ульяна, почему ты тут одна?{w} Где остальные ребята, где Алиса?{w} С Семёном?"
    "И тут её прорвало:{w} она зарыдала, и уселась на поле."
    show us cry2 pioneer with dspr
    us "Она всё время с ним.{w} Все бегают вокруг него, и им весело.{w} Я тоже пытаюсь, но он не замечает меня.{w} Каждый раз я пытаюсь придумать новое, но ничего не получается. "
    sh "А чем он так тебя привлёк?"
    us "Он напоминает мне моего папу, которого я так давно не видела."
    sh "Как давно?"
    us "Я... Я не помню."
    sh "Сколько ты здесь смен?"
    us "Три, насколько я помню." 
    "Мои предположения оказались верны. {w}Что ж, это шанс."
    sh "Уль, а что если я тебе скажу,{w} что и я не первый раз в «Совёнке»"
    "Она к этому моменту уже успокоилась, и даже слегка улыбнулась"
    show us grin pioneer with dspr
    us "А я догадалась, что ты не местный.{w} Того Шурика на поле не затишить в принципе. {w}Хотя ты меня пугаешь — я думала, что тут только я настоящая.{w} Кто ты?"
    sh "Буду краток.{w} Здесь много «Совят», и в каждом заперты живые люди в окружении кукол. {w}Куклы не отличаются от человека ничем — так же свободно думают, чувствуют и дышат. {w}Но спроси их об этом месте, и никто тебе ответа не даст. "
    sh "Ты вспомнила про свои приезды сюда, на 410 автобусе."
    us "Да, я тут уже 3 недели. {w}Снова."
    sh "А я тут уже сотни, но не суть.{w} Нам всем надо выбраться в реальный мир."
    show us shy pioneer with dspr
    us "А как это сделать? "
    sh "Семён"
    show us surp1 pioneer with dspr
    us "Что значит Семён?"
    sh "Он ключ к нашей свободе."
    show us upset pioneer with dspr
    us "Вот этот тормоз?"
    "Она удивилась"
    us "И как он это сделает?"
    sh "Не этот — он кукла. {w}Настоящий Сёма, единственный и настоящий{w}, находится не здесь."
    us "А где он?"
    sh "Увы, координаты в этих лагерях не существуют, и я не знаю, как провести тебя туда."
    show us normal pioneer with dspr
    us "А как ты ко мне-то попал?"
    sh "Нууу, меня поцеловала девушка, и вот я тут."
    "Уля рассмеялась"
    show us laugh pioneer with dspr
    us "Хороший способ, нечего сказать. А обратно ты как попадёшь?"
    sh "В прошлый раз специально потерял сознание." 
    us "И всё??"
    sh "Нет. Я так понял, должно быть сильное чувство к человеку, чтобы перенестись к нему."
    us "И какое же чувство у тебя к Сёме? "
    show us grin pioneer with dspr
    "Она захихикала"
    sh "Ненависть."
    "Такой ответ вмиг остудил её хорошее настроение."
    show us sad pioneer with dspr
    us "Ты какой-то странный. За что ненавидишь?"
    sh "За то, что по его вине мы оказались тут."
    us "А с чего ты взял, что он виноват? "
    "Хм, а это имеет смысл."
    sh "Есть основания так думать.{w} Хорошо, что ты еще другого не встречала."
    show us dontlike pioneer with dspr
    us "Ты меня совсем запутал. Какой такой «другой»?"
    pi "А вот такой."
    "Cказал появившийся из ниоткуда Пионер."
    show pi smile at left with dissolve
    play music pioneer_theme 
    sh "Вспомнишь солнце — вот и лучик" 
    show us calml pioneer with dspr
    us "Семён?{w} Ты то что тут делаешь?!"
    pi "Захотел поговорить со старым другом."
    show pi normal1 at left with dissolve
    sh "Не бойся, он ничего с нами сделать не может, только настроение портит и воздух."
    pi "Могу, если захочу.{w} Но не пугайтесь.{w} Так, мелкая, а ну кышь отсель, {w}большим дядям поговорить надо."
    "И этот подонок пнул девочку в бедро{w}, да так, что она кубарем полетела в сторону.{w} Видимо пнул не больно, но сам факт!"
    hide us calml pioneer with dissolve
    show us calml pioneer with moveinleft
    show us cry pioneer at right with dissolve
    us "Да как ты..."
    pi "Пошла отсюда"
    "Рявкнул он."
    "Уля попятилась, и по ней видно, что ей очень страшно. "
    show us fear pioneer with dspr
    "Ладно, погуляли и хватит. {w}Я снял очки и встал между ними."
    sh "Говоришь, можешь и сделать.{w} А это работает в обе стороны?"
    show pi smile  at left with dissolve
    pi "Ух, баюсь-баюсь.{w} Успокойся, я пришёл спросить, и всё.{w} Даже помогу тебе, в знак доброй воли."
    sh "Короче."
    pi "Как ты тут оказался? "
    sh "А ты?"
    show pi normal1 at left with dissolve
    pi "Вопросом на вопрос.{w} Хорошо.{w} Я захотел, и появился здесь."
    sh "А меня направили."
    pi "Она представилась?"
    "Откуда он знает, что это была девушка? {w}Он что-то скрывает"
    pi "Судя по твоему лицу, я угадал.{w} Хех, а она забавная. {w}Ладно, я получил то что мне нужно. А теперь ты получи своё."
    with hpunch
    show us sad pioneer with dspr
    us "Саша!"
    stop music
    show blink
    $ renpy.pause(3)
    hide us sad pioneer with dissolve
    hide pi normal1
    play music alex_theme fadein 5
    $ renpy.music.set_volume(0.5, .5, channel="music")
    scene int_aidpost_night
    show unblink
    "Я открыл глаза.{w} Белый потолок, горит свет.{w} Дико болит челюсть - Видно этот гад меня вырубил.{w} Сев на кровать, я узнал мед.кабинет.{w} Открылась дверь, и внутрь вошла Виола."
    show cs normal body glasses with dissolve
    cs "А, очнулся, пионЭр. {w}Чтож ты из лагеря-то ушёл."
    sh "Что со мной произошло."
    cs "В обморок упал, опять.{w} Тебе же нельзя перенапрягаться, а ты такое творишь."
    sh "Да ладно, с кем не бывает."
    cs "Со всеми не бывает.{w}  Вот чего ты попёрся за ворота? {w}Только не говори, что гайки искать - не поверю."
    sh "Да я это..."
    cs "Ладно, можешь не отвечать. Ты б об остальных подумал бы."
    "Так ведь и думаю"
    cs "Вон Ольга вся на нервах.{w} Принесла тебя на руках сюда. Кстати, вот и она."
    "На пороге стояла Дмитриевна, с весьма измотанным видом"
    show mt rage pioneer panama at right with dissolve
    mt "Да ты... Да тебя... Да я!"
    show cs smile body glasses with dspr
    cs "Успокойся Ольга, он всё понял.{w} Вам обоим стоит отдохнуть."
    "Дмитриевна пыталась выговорить мне всё что думает,{w} но не находила слов. Виола подошла ко мне, и дала таблетку."
    cs "Успокоительное.{w} Для тебя сон это действительно лучшее лекарство."
    "Без пререканий я принял препарат, и снова улёгся в кровать.{w} На удивление, меня быстро стал одолевать сон.{w} Пока я проваливался, я смог расслышать разговор двух женщин"
    show mt scared pioneer panama at right with dspr
    mt "Виол, с ним всё хорошо будет?"
    cs "Да, выспится и будет как новенький.{w} Я,{w} на всякий случай{w}, за ним присмотрю."
    show cs shy body glasses with dspr
    mt "Я так испугалась. Ведь должна была обратить внимание - ребята говорили, что он странно себя вёл, а я думала, что просто устал."
    show cs normal body glasses with dspr
    cs "Не вини себя.{w} Мальчишки в его возрасте всё держат в себе, и молчат как партизаны."
    hide mt scared pioneer panama at right with dissolve
    "Сон начал побеждать, и остальную часть я не расслышал.{w} Единственное, что за этот вечер я успел уловить, как Виола села на мою кровать и погладила меня по голове"
    show cs shy body glasses with dissolve
    cs "Спокойной ночи{w}, путешественник."
    stop music
    jump day_3
    
label day_3:
    $ backdrop = "1 день до приезда"
    $ new_chapter(-1, u"1 день до приезда")
    scene int_aidpost_day with dissolve
    play music music_list["eternal_longing"] fadein 3
    
    $ persistent.sprite_time = 'day'
    $ day_time()

    "Проснулся я рано утром, ещё до побудки.{w}Около меня, на стуле, спала Виола.{w} Неужто она не отходила от меня всю ночь?"
    "Я встал, оделся, и приготовился идти умываться."
    cs "Встал? Как себя чувствуешь?"
    "Раздался голос Виолы"
    show cs smile body glasses with dissolve
    sh "Прекрасно! Готов к труду и обороне."
    cs "Молоток. Значит слушай сюда."
    show cs normal body glasses with dspr
    "Её голос стал по холодному деловой"
    cs "Никаких нагрузок сегодня, никакого кофе и  алкоголя.{w} Если почувствуешь недомогание — сразу ко мне. Я Ольгу предупредила."
    sh "Алкоголя?"
    cs "Не делай такое лицо.{w} У вас{w}, парней{w}, наверняка есть заначка.{w} Так вот - ни капли, понял?"
    sh "Понял."
    cs "Хорошо. Свободен{w},пионЭр"
    "Она перешла на свой стандартный, томный стиль"
    show cs shy body glasses with dspr
    cs "Если что, заходи.{w} Я о тебе позабочусь."
    "Почувствовав, что краснею как рак,{w} я пулей вышел из мед-кабинета."
    scene ext_houses_day with dissolve
    play music music_list["lightness"]
    "Раннее утро так прекрасно летом{w}, особенно когда никто не попадается тебе на глаза с невыспавшимся лицом и плохим настроением. {w}У умывальников никого не было, так что я спокойно умылся и пошёл по своим делам."
    "Погода была так хороша,{w} что я решил прогуляться по спящему лагерю."
    "День только начинается,{w} и планов у меня не много:{w} всего лишь научиться путешествовать сквозь время и пространство.{w} Легко, как резистор припаять.{w} Как тот упырь говорил: «Захотел и появился»."
    "Как он это делает?{w} Появляется из ниоткуда и уходит в никуда, на нервы действует."
    "Оказаться тут стоило мне огромных усилий и времени,{w} не искать же в самом деле по кустам ту незнакомку,{w} которая меня поцеловала, чтобы просить её меня перемещать."
    "Нееет, всё должно быть проще."
    show prologue_dream with dissolve
    show us grin pioneer with dissolve
    us "И какое же чувство у тебя к Сёме? "
    "Она захихикала"
    sh "Ненависть."
    
    scene ext_square_day with dissolve
    "Да,{w} я терпеть не могу этого доходягу, поэтому то я тут."
    "Но что на счёт девушек?{w} Что я к ним чувствую? "
    "Симпатия?{w} Да."
    "Любовь?{w} Нет."
    "Презрение?{w} Нет."
    "Жалость?{w} Да."
    "Всё это мелко, даже не стоит обращать внимание.{w} Я хочу всех вытащить отсюда, помочь.{w} Но не больше. "
    "Так,{w} пойдём с другой стороны.{w} С кем бы я сейчас пообщался?{w} Пошутил бы вместе, поговорил бы о жизни?"
    "На ум приходит только Славя.{w} Она всегда слушает, уж такая она.{w} Да, я хочу увидеть её сейчас.{w} Из всех аборигенов она — самый лучший выбор."
    "Я закрыл глаза и представил образ Слави:"
    show blink
    show prologue_dream with dissolve
    $ renpy.pause(2)
    show sl smile body behind prologue_dream with dissolve
    "Её голос, запах, её тело. Этого явно не хватает, нет ключевого элемента... Нет чувства, которого я к ней испытываю. Самого сильного, самого яркого."
    "Вот оно, это чувство"
    
    menu:
        "Теплоты и понимания, исходящей от неё":
            $ sl_love += 1
        "Любопытства и навязчивости, присущие только ей.":
            $ sl_love -= 1
    
    "Вдруг меня охватило странное ощущение — мне вроде бы стало холодно и трудно двигаться. Такой поворот немного испугал меня, и я тут же открыл глаза."
    hide prologue_dream with dissolve
    hide sl smile body with dissolve
    stop music 
    $ renpy.pause(2)
    
    show ext_square_night
    hide blink 
    play music Freedom_2
    $ persistent.sprite_time = 'night'
    $ night_time()
    show unblink
    "Увиденное меня шокировало{w} — раннее утро сменилось на поздний вечер, а я сам оказался на площади. "
    "Я осмотрелся — вроде ничего необычного, только одинокая фигура стоит около памятника.{w} При ближайшем рассмотрении это оказалась та, кто именно мне и нужен — Славя."
    show sl normal pioneer with dissolve
    play sound sfx_broom_sweep
    sh "Привет Славь, как дела?"
    sl "О, Шур, привет.{w} Ты чего тут делаешь?"
    "Хороший вопрос однако"
    sh "Мимо проходил, смотрю — ты тут маешся"
    sl "Хах, труд облагораживает."
    sh "А чего одна?"
    sl "А зачем ещё людей то тащить?{w} Сама справлюсь."
    sh "А что грустная такая?{w} Случилось что?"
    sl "Не Саш, всё хорошо."
    "Последнее «хорошо» прозвучало уж слишком натянуто.{w} Так, этот цирк мне надоел,{w} надо играть в открытую."
    sh "С Семёном проблемы?"
    stop sound
    "У неё из рук метла вывалилась."
    show sl sad pioneer with dspr
    sl "С его ты взял?{w} У нас всё отлично"
    sh "Отлично от хорошего?"
    sl "Саш, не смешно."
    show sl angry pioneer with dspr
    sh "Дай угадаю:{w} Вы встретились,{w} понравились друг другу,{w} много общались,{w} даже меня вместе искали.{w} А сейчас вроде «прошла любовь, завяли помидоры»?"
    sl "..."
    sh "Ты думаешь, что это «курортный» роман, ни к чему не обязывающий.{w} Так ведь?"
    show sl surprise pioneer with dspr
    "Она смотрит на меня глазами, полными непонимания."
    sh "По крайней мере для него.{w} А себя ты пытаешся убедить в этом.{w} Но не выходит, верно?"
    sl "Верно..."
    sh "И в довершение ты не знаешь, как это исправить?"
    show sl scared pioneer with dspr
    "Ещё немного, и она заплачет.{w} Терпи,{w} это для твоего же блага."
    sh "Наверно ты думала, что встретила свою «вторую половинку»,{w} а тут любовью и не пахнет.{w} Вот сейчас ты и машешь тут метлой в одиночестве."
    "Под лунным светом видно{w}, как по щекам девушки катятся слёзы.{w} То ли гордость,{w} то ли выдержка не дают ей разреветься по полной."
    sl "Зачем ты всё это наговорил? "
    sh "Затем, что твои мучения напрасны.{w} Он не оценит твоих чувств — он просто не в состоянии сделать это.{w} Есть другой."
    sl "Это ты про себя?"
    sh "Нет конечно.{w} Ты не для меня. {w}В тебе нуждается другой человек. "
    sl "Кто же это?"
    "Видимо она на грани истерики."
    show sl angry pioneer with dspr
    sh "Семён.{w} И да, ты не ослышалась{w}, и я в своём уме. "
    show sl sad pioneer with dspr
    sl "Я тебя не понимаю.{w} То ты говоришь, что  он не оценит, то говоришь, что я ему нужна."
    sh "Разъясняю популярно: Ты тут уже не одну смену.{w} Приезжаешь на 410-м{w}, проводишь тут «великолепные» каникулы{w}, и уезжаешь обратно.{w} И так много-много раз."
    sh "И в твоём лагере только ты — настоящий человек.{w} Остальные — лишь имитация. "
    sl "Но ты..."
    sh "Я другое дело, но обо мне позже. {w}Ты влюбилась в Семёна с первой встречи{w}, так ведь? Не отвечай — знаю.{w} Но у вас не клеится. И будет ещё долго, но рано или поздно вы вместе отсюда уедете, чтобы опять вернуться. {w}Замкнутый круг."
    show sl angry pioneer with dspr
    sl "Чушь ты говоришь, честное слово."
    sh "Дальше больше.{w} В один непрекрасный момент ты вспомнишь о том, что бывала тут много раз.{w} И прекрасная сказка обратится в ужасный кошмар."
    sl "Ой, ну тебя, глупости несёшь."
    show sl serious pioneer with dspr
    sh "Ты можешь мне не верить, но это так..."
    "Чёрт, как её убедить?{w} Вот почему Семёну дано разговаривать с ними{w}, а мне нет?"
    sh "Всё будет повторяться вновь и вновь,{w} но я могу помочь тебе вырваться, и зажить вместе с Семёном долго и счастливо."
    sl "Если на секунду представить, то весь этот бред, то ты наговорил — правда, то у меня вопрос — а кто тебя просил спасать меня и остальных? "
    sh "Никто,{w} просто по отдельности нам не выбраться."
    sl "Может ты хочешь сам уйти, и всё?"
    sh "Я не..."
    "И тут я не смог ответить. "
    show sl angry pioneer with dspr
    sl "Молчишь?{w} Ну и молчи дальше. Иди по своим делам,{w} иди куда хочешь, только с глаз моих долой."
    sh "Я уйду, но Славь{w}, пожалуйста{w}, запомни мои слова."
    "Она отвернулась, а я молча пошёл к радиоклубу.{w} Эх, всё прошло не так как надеялся.{w} Станет ли она помогать мне после такого. {w}Я Закрыл глаза и сделал глубокий вдох.{w} Как всё сложно."
    show blink
    hide sl angry pioneer with dissolve
    
    
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_dining_hall_people_day
    show unblink
    play ambience ambience_dining_hall_full
    "Открыв глаза, я обнаружил себя у столовой.{w} Видимо завтрак, не иначе."
    show el normal pioneer with dissolve
    el "Саш, чего застрял?"
    sh "Да-да, иду."
    "Завтрак прошёл без происшествий, я даже с Элом только пару раз перекинулся ничего не значащими фразами."
    "Всё время меня не покидало чувство, что слова Славяны не лишены смысла на счёт меня.{w} Нет,{w} если она хочет оставаться тут на веки вечные — пускай, её дело."
    "Но остальные!{w} Ничего, я смогу её переубедить.{w} Вариантов у меня не так уж и много."
    "Кстати об оных.{w} Лена сидела тише обычного{w}, насколько это вообще возможно.{w} Надо будет подойти к ней,{w} поскольку появилась блестящая идея."
    "На выходе я поймал её"
    scene ext_dining_hall_near_day with dissolve
    sh "Лен, что такая кислая?{w} На тебе лица нет."
    stop ambience
    play music music_list["lets_be_friends"]
    show un normal pioneer with dissolve
    un "Привет, Саш.{w} Да вот, делать нечего. "
    sh "Это ты к Дмитриевне обратись.{w} Мигом тебе работу найдёт."
    "Лена улыбнулась."
    show un smile pioneer with dspr
    un "Это я всегда успею.{w} В свободное время делать тут...{w} Почти нечего."
    show un normal pioneer with dissolve
    "И тут я вспомнил важную вещь"
    sh "Лен, так нашёл я книгу!"
    show un surprise pioneer with dspr
    un "Да?"
    sh "Уверен.{w} Пошли."
    scene ext_houses_day with dissolve
    "Дойдя до моего домика, я остановился."
    sh "Ты заходи, не стой на пороге."
    show un smile pioneer with dissolve
    un "Не, я тут подожду. Вон,{w} за нами следят уже."
    "И она кивнула в сторону кустов,{w} откуда виднелись красные косы."
    sh "Вот мелкая пакость."
    scene alex home day with dissolve
    "После непродолжительных поисков я всё же нашёл эту книгу.{w} Да, такое точно для неё."
    "Нехорошо заставлять девушку ждать подарок,{w} даже если эта девушка — бездушный механизм."
    scene ext_houses_day with dissolve
    sh "На, держи." 
    show un surprise pioneer with dissolve
    un "Откуда такое у тебя?{w} Не думала, что ты читаешь романы."
    sh "Нашёл в домике,{w} а лишний раз связываться с Женей неохота."
    un "«Унесённые ветром».{w} Как раз то, что я хотела. "
    show un smile2 pioneer with dspr
    "Лена вновь улыбнулась,{w} а я ещё раз поразился качеством этих существ."
    "Ну да ладно, «Я подумаю об этом позже»."
    sh "И Лен, я обязательно придумаю,{w} как разогнать твою скуку."
    show un smile pioneer with dspr
    un "Серьёзно?"
    sh "Абсолютно.{w} Твой кислый вид всех удручает{w}, а такой, как ты не пристало унывать."
    sh "О!{w} Ты в карты умеешь играть?"
    show un shy pioneer with dspr
    un "Ну, немного, а что?"
    sh "Так, любопытство."
    "Улыбнулся я и мы пошли по своим делам."
    stop music
    
    scene ext_clubs_day with dissolve
    play music alex_theme
    $ renpy.music.set_volume(0.5, .5, channel="music")
    "Пока шёл до клуба, я задался одним вопросом"
    "Придумал ли Эл ту карточную забаву, или тут я её сделал?"
    scene int_clubs_male_day with dissolve
    "Эл был найдён в радиоклубе{w}, сидящим за столом{w}, и что-то активно пишущим."
    show el shocked pioneer with dissolve
    sh "Чем занят товарищ?{w} Стихи для Жени пишешь?"
    el "Нет, что ты.{w} Я так, по мелочи,{w} мысли записываю"
    show el surprise pioneer with dspr
    "Быстро выпалил он,{w} пряча блокнот в карман"
    el "А сам какими судьбами?"
    sh "Да вот мыслишка пришла в голову{w} — надо бы развеселить народ, а то сегодня на завтраке все были, мягко говоря, слишком тихими."
    show el normal pioneer with dspr
    el "Я тоже заметил.{w} Что предлагаешь?"
    sh "Турнир!"
    show el scared pioneer with dspr
    el "Какой турнир?"
    sh "Карточный.{w} Я уже и правила придумал, пока шёл."
    el "Итересно."
    "Пару минут ушло на разъяснение идеи и правил. Эл выглядел удивлённым"
    show el surprise pioneer with dspr
    el "Сань, ну ты голова! "
    sh "Идея сыровата,{w} но, думаю, будет интересно.{w} Ты можешь доработать её? У меня опыта мало."
    show el normal pioneer with dspr
    el "У меня не намного больше, ну да ладно. "
    sh "Мы всех позовём. Смекаешь?"
    show el smile pioneer with dspr
    "Эл покраснел — видимо понял, к чему я клоню."
    el "Саня, умён..."
    sh "Пойду пока к вожатой,{w} договорюсь."
    stop sound
    
    scene ext_house_of_mt_day with dissolve
    play music music_list["timid_girl"]
    "Я быстро дошёл до домика вожатой, но был удивлён тем, что там было подозрительно много народу.{w} Дмитриевна{w}, Славя{w}, Женя и ещё несколько пионеров."
    sh "Зачем стоим?{w} Что дают?"
    show mz normal pioneer glasses with dissolve
    mz "Привезли продукты и прочее.{w} Вот думаем, что куда класть."
    show mt normal pioneer panama at right with dissolve
    mt "О{w}, Саш{w}, хорошо что ты появился. Поможешь."
    "Ну прекрасно"
    mt "Иди, там уже Славя ждёт"
    "Взяв тележку, я пошёл к воротам." 
    scene ext_no_bus with dissolve
    "Там лежали мешки, коробки и прочее.{w} Фура, видимо, уже давно уехала{w}, да и была ли она?{w} Неважно."
    sh "Сколько всего"
    "Выдохнул я."
    show sl normal pioneer with dissolve
    sl "Да уж — давай начнём с самого тяжёлого{w}, а там легче пойдёт. "
    sh "Угу"
    "Мрачно кивнул я."
    "С большим трудом взгрузив мешки с сахаром на телегу,{w} мы медленно двинулись в путь."
    scene ext_houses_day with dissolve
    sh "Славь, мы так далеко не уедем вдвоём.{w} Надо ещё людей позвать"
    "Простонал я."
    show sl sad pioneer with dissolve
    sl "У других своих дел хватает, но да, тяжело.{w} Слушай, а давай мы к вам в клуб завезём?{w} У вас в кладовке места много."
    sh "Я против.{w} Там не место для съестных припасов.{w} Там куётся наука!!"
    show sl angry pioneer with dissolve
    sl "Тогда тащи до столовой."
    sh "Хорошо, ты меня убедила."
    
    scene ext_clubs_day with dissolve
    show el scared pioneer with dissolve
    "Добравшись до места, и не обращая внимания на шокированного Эла, я сгрузил мешки в кладовой."
    "Конечно, это безобразие{w}, но не мне их отсюда утаскивать."
    scene int_clubs_male2_night with dissolve
    play sound sfx_put_sugar_cart
    sh "Чтобы я ещё когда-либо..."
    show sl smile pioneer with dissolve
    sl "Не сломался же, чего ворчишь."
    "Я зло посмотрел на неё, но промолчал.{w} Не знаю, заметила ли она, но ответной реакции не последовало. "
    sl "Кстати Саш, тебя Ольга Дмитриевна просила подойти."
    show sl serious pioneer with dspr
    sh "Зачем?"
    sl "Сказала, но видно дело срочное, раз всех собирают."
    "Действительно странно. Ну ладно, разберусь."
    
    scene ext_square_day with dissolve
    "Мы пришли на площадь, где стояла Дмитриевна в окружении пионеров. "
    show mt normal pioneer panama with dissolve
    play music music_list["eat_some_trouble"]
    mt "А, вот и Саша со Славей пришли.{w} Теперь можно начинать собрание. Хотя...{w} Куда делась Ульяна?{w} Ох и получит у меня она. Что за непоседа."
    us "Да тут я! Сказала же — мигом сбегаю."
    show us normal pioneer at left with dissolve
    mt "Принесла?"
    show us upset pioneer at left with dspr
    us "Нет. Всё обыскала."
    mt "Ну что же ты. "
    "Я ухмельнулся"
    show mt angry pioneer panama with dspr
    mt "Что-то смешное?{w} Расскажи, все посмеёмся."
    show us normal pioneer at left with dspr
    sh "Не, все нормально, это я так."
    show mt grin pioneer panama with dspr
    mt "Раз так, иди ты.{w} В моём домике лежит список{w}, найди и неси сюда."
    sh "А что в нём?"
    mt "Имена тех, кто приедет."
    sh "А их много? "
    show mt normal pioneer panama with dspr
    mt "Смотря как распределят, может все приедут, а может один.{w} Не задавай лишних вопросов."
    "Вот попал. "
    "Собравшись проклянуть мир и медленно пойти за списками, я заметил лыбящуюся Улю.{w} Вот мелкая."
    show us grin pioneer at left with dspr
    mt "Ах да, и Улю возьми с собой.{w} Потом пойдёте на причал  — посчитаете,{w} сколько у нас вёсел и шезлонгов осталось"
    show us angry pioneer at left with dspr
    us "Ну Ольга Дмитриевна!!"
    show mt grin pioneer panama with dspr
    mt "Никаких «Ольга Дмитриевна».{w} Идите."
    "Всё же есть справедливость."
    hide mt grin pioneer panama with dspr
    sh "Знаешь, хорошо что ты засмеялась.{w} Мне одному долго пришлось бы возится."
    show us grin pioneer at left with dspr
    us "Без проблем, обращайся.{w} По секрету скажу, что ты всё равно пошёл бы ."
    sh "Знаешь, не сомневаюсь."
    
    scene ext_house_of_mt_day with dissolve
    "Оказавшись на месте, мы приступили к поискам."
    show int_house_of_mt_day
    show us normal pioneer with dissolve
    us "Это бесполезно.{w} Я всё обыскала!{w} Ну нету тут этого списка.{w} Может, она его потеряла, или забыла где."
    "Я осмотрел полку, столик."
    sh "А в книгу ты заглядывала?"
    us "Зачем?"
    sh "Эх, молодёжь."
    "Как я и думал, список был использован как закладка. Так,{w} посмотрим. "
    play music semion_theme
    $ renpy.music.set_volume(0.1, .5, channel="music")
    "Да уж, имён не мало.{w} Даже небольшое досье{w}, что неудивительно."
    "Я быстро прочитал имена{w}, и остановился на том,{w} которое мне так неприятно."
    "Семён Семперсунов."
    "На секунду меня обуяла ненависть{w}, но я быстро взял себя в руки.{w} Не время и не место."
    sh "Вот он.{w} А теперь пошли до причала."
    show us surp1 pioneer with dspr
    us "Во ты глазастый! Не даром четыре глаза."
    scene ext_house_of_mt_day with dissolve
    "Пропустив мимо ушей эту подколку, я вышел из домика вожатой и пошёл к причалу.{w} Уля семенила рядом, поглядывая на меня с любопытством."
    show us grin pioneer with dissolve
    us "Обиделся?"
    sh "Я буду просто выше твоего юмора."
    "Коротко сказал я."
    us "Ой, ну прям сама серьёзность"
    "Засмеялась мелкая."
    sh "Давай побыстрее закончим, а то неохота после обеда сюда возвращаться. "
    us "Да, давай."
    
    scene ext_boathouse_day with dissolve
    $ renpy.music.set_volume(1, .5, channel="music")
    play music music_list["eat_some_trouble"]
    "Оказавшись на месте, я заглянул внутрь — мда{w}, там много всего{w}, придётся попотеть. "
    show us angry pioneer with dissolve
    sh "Уля, давай ты шезлонги считай{w}, а я вглубь полезу, за веслами."
    us "Ну тебя, самое интересное себе."
    hide us angry pioneer with dissolve
    "Вёсла оказались в самом дальнем углу{w}, и потребовались некоторые усилия, чтобы туда пробраться.{w} Уля в это время закончила пересчёт, и всем видом показывала, что её очень скучно"
    "Я обернулся посмотреть, что она творит, и не зря - мелкая сложила их в стопку и балансировала на них, прямо на краю"
    sh "Осторожно, а не то упадёшь!{w} Мне тебя вытаскивать потом неохота."
    show us laugh2 pioneer with dissolve
    us "Не боись, всё будеееее..."
    hide us laugh2 pioneer with dissolve
    "И она закономерно полетела вниз."
    us "Ай, ой"
    play sound sfx_water_emerge
    "Только и послышалось из воды."
    sh "А я предупреждал."
    "С улыбкой на лице я подошёл к барахтающийся Уле.{w} Сие действо было весьма забавно, особенно её бесполезные попытки выбраться."
    menu:
        "Посмеялись и хватит. Вытащить её.":
            $ us_happy += 1
            jump d3_us_1
        "На некоторые вещи можно смотреть бесконечно":
            $ us_happy -= 1
            jump d3_us_2
            
    
label  d3_us_1:
    play music music_list["i_want_to_play"]
    sh "Ну что же ты так?"
    "Сказал я и начал вытаскивать неумеху."
    sh "Не ушиблась?"
    show us laugh pioneer with dissolve
    us "Не, всё в полном порядке."
    sh "Я же тебе говорил!{w} Почему не послушала?"
    show us grin pioneer with dspr
    us "Я не подумала..."
    sh "Не подумала.{w} Теперь думай, как перед Дмитревной отчитываться будешь, почему промокла насквозь."
    show us normal pioneer with dspr
    sh "Ладно, пошли обратно."
    show us grin pioneer with dspr
    "Всю дорогу Уля лыбилась, радуясь произошедшему «приключению». Как мало надо кукле для счастья."
    jump d3_dinn


label  d3_us_2:
    play music alex_theme
    us "Что стоишь, помоги!"
    "Послышался голос из воды."
    sh "Э нееет, сама полезла, сама и выбирайся!"
    us "Ну Саш..."
    sh "Нет, я сказал."
    "Она начинает хныкать."
    us "Помоги."
    us "Пожалуста"
    "Может действительно ударилась?{w} Если с ней что случится{w}, Дмитриевна с меня голову снимет."
    "Быстро сиганув в воду{w}"
    play sound sfx_underwater_dive
    "Я вытащил мелкую на свет божий."
    show us grin pioneer close with dissolve
    us "Что испугался?"
    "И я в тот же момент бросил её туда, где взял."
    play sound sfx_water_emerge
    sh "Не смешно Уль, совсем не смешно."
    us "Да ладно тебе, что ты такой серьёзный?{w} Уж и пошутить нельзя."
    "Но я уже был на пути к площади{w}, и не слышал её бред."
    "Всю обратную дорогу Уля лыбилась, радуясь, по её мнению, хорошей шутке. {w}Как мало надо кукле для счастья."
    jump d3_dinn

label d3_dinn:
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    scene ext_houses_sunset with dissolve
    play music music_list["trapped_in_dreams"]
    "Из-за того, что мы особо не спешили возвращаться, мы явились под самый конец этого собрания. Вожатая уже заканчивала, и до меня донеслось"
    scene ext_square_sunset
    mt "...и пожалуйста,{w} будьте добрее с новенькими.{w} Эта смена должна стать для них особенной."
    show mt normal pioneer panama with dissolve
    mt "А, вот и вы.{w} Ну, рассказываёте."
    sh "А что рассказывать? {w}Всё посчитано и проверенно.{w} На всех хватит, вот список."
    "Дмитриевна мельком пробежалась взглядом по моим закарючкам, и увиденное ей понравилось."
    show mt smile pioneer panama with dspr
    mt "Молодцы, а теперь марш на обед."
    "Хоть что-то хорошее произойдёт за этот день!{w} Неспешно двинув к столовой, я задался вопросом — где мой верный товарищ Сыроежкин?{w} Неужто мне опять придёться сидеть с этими фуриями?"
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    show el smile pioneer at right with dissolve
    show mz normal pioneer glasses with dissolve
    "Предчувствия меня не обманули, и я увидел Эла сидящем рядом с Женей.{w} Что странно, они о чём-то разговаривали.{w} А у меня появился нелёгкий выбор"
    menu:
        "Алиса":
            $ dv_happy += 1
            jump d3_dinn_dv
            
        "Лена":
            $ un_love += 1
            jump d3_dinn_un
            
label d3_dinn_dv:
    $ persistent.sprite_time = 'day'
    scene int_dining_hall_people_day with dissolve
    "Надо выбрать меньшее из зол, поэтому я решил пообедать с рыжей катастрофой."
    sh "Алис, можно?"
    show dv normal pioneer with dissolve
    dv "Можно."
    "Спокойно сказала та."
    "Я сел за стол и начал поглощать свой обед.{w} Алиса, в свою очередь, задумчиво ковырялась вилкой, и всячески давала понять, что занята своими мыслями. "
    sh "О чём задумалась?{w} Над речью Дмитревны?"
    show dv sad pioneer with dspr
    dv "Да."
    "Но она тут же взяла себя в руки"
    show dv normal pioneer with dspr
    dv "А тебе какое дело?"
    sh "Я всё пропустил, и мне интересно, что было."
    show dv angry pioneer with dspr
    dv "Ты ничего не потерял.{w} Она говорила о поведении, общении и отношении." 
    sh "По мне, так ты не сильно довольна."
    dv "А то.{w} Как маленьких выстроила, и пальчиком погрозила.{w} «Хорошо себя ведите, а не то сладкого не получите». {w}А если новенькие плакать будут, в угол поставит."
    sh "Тебя послушать, так ты ожидала приезда матёрых бандюганов{w}, а тебе интелентишек подсунули."
    show dv sad pioneer with dspr
    dv "Ты не понял.{w} Я тут со скуки дохну, только Уля выручает{w}, да гитара с Мику.{w} И всё! "
    sh "Вот не надо рассказывать о том, что тут делать нечего.{w} Было бы желание."
    dv "Ты нотации мне не читай, не дорос ещё."
    sh "Грубить не обязательно.{w} Я знаю, что местная компания тебе не нравится.{w} Может, новенькие будут из твоего круга?{w} Хотя нам тогда точно не поздоровится."
    show dv guilty pioneer with dspr
    dv "Опять не понял.{w} Компания-то хорошая, только за рамки выходить боится. "
    sh "А ты прямо жаждешь приключений."
    dv "Была бы не против."
    "Будут тебе Алиса приключения {w}- но я промолчал."
    stop ambience
    jump  d3_beach
    
label d3_dinn_un:
    $ persistent.sprite_time = 'day'
    scene int_dining_hall_people_day with dissolve
    sh "Лен, к тебе можно?"
    show un normal pioneer with dissolve
    "Она еле заметно кивнула."
    "Я сел за стол и начал поглощать свой обед. Лена, в свою очередь, задумчиво ковырялась вилкой, и всячески давала понять, что занята своими мыслями. "
    sh "О чём думаешь?"
    show un sad pioneer with dspr
    un "Ольга Дмитриевна попросила быть добрее с новенькими.{w} Никогда такого не слышала от неё."
    sh "Ты думаешь, что это не простые ребята к нам приедут?"
    show un normal pioneer with dspr
    un "Да, ведь такое уже было. "
    sh "Не знал.{w} Расскажешь?"
    show un shy pioneer with dspr
    un "Я сама мало про это знаю."
    sh "Ну врятли это беженцы или инвалиды.{w} Может, сироты?"
    show un sad pioneer with dspr
    un "Ты плохую тему для разговора затеял."
    sh "Извини, забылся.{w} А ты чего такая грустная?"
    un "Я переживаю, что им не понравится."
    sh "Это ты придумала.{w} Тут так красиво и хорошо!"
    un "Да, но ведь главное  - это с кем проводить время в «хорошем и красивом» месте."
    sh "Я  тебя что-то не понимаю.{w} Ты думаешь, им тут будет скучно?"
    show un smile pioneer with dspr
    "Она улыбнулась"
    un "Дмитриевна скучать не даст, это точно. "
    sh "Хех, согласен. "
    un "Знаешь, вся эта суета затягивает, и забываешь о проблемах там{w}, дома."
    sh "В этом и суть отдыха!"
    show un normal pioneer with dspr
    un "Но каково будет возвращение обратно?"
    sh "Теперь ты уже не ту тему завела."
    show un smile pioneer with dspr
    "Она снова улыбнулась"
    un "Да, я увлеклась."
    sh "Могу лишь сказать, что всё будет хорошо.{w} Может приедет парень, который тебе понравится."
    "Она покраснела словно рак."
    show un shy pioneer with dspr
    un "Да ну тебя."
    stop ambience
    jump  d3_beach

label d3_beach:
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    "Сытно пообедав, я задался вопросом, как скоротать оставшееся время? "
    scene ext_beach_sunset with dissolve
    play music music_list["silhouette_in_sunset"]
    "Ответ был найден поразительно быстро — пойти на пляж.{w} Вряд ли там много народа, и Дмитриевну я не видел."
    "Каково же было моё удивление, когда я обнаружил, что пляж буквально набит пионерами!{w} Тут и мелкие бегают{w}, и старшие в волейбол играют.{w} Даже Вожатая играла с ними."
    "Мдааа, уединением тут и не пахнет.{w} Но и уходить отсюда не хочется.{w} Я снял обувь, расстегнул рубашку и уселся на шезлонг."
    "Погода, конечно, прекрасная, а свежий ветер разгонял облака, освобождая солнце, а шум толпы воспринимался мною как приятный фон. {w}Кажется, я засыпаю...{w} Но мяч{w}, приземлившийся в паре сантиметров от меня{w}, вывел меня из медитативного состояния."
    show us grin swim with dissolve
    us "Саш, не спи, замёрзнешь"
    "Крикнула Уля.{w} Наверняка это она в меня кинула.{w} Вот мелкая."
    hide us grin swim with dissolve
    "Я взял мячик{w}, и со всей силой кинул обратно.{w} Расслабиться тут не удастся, так что будем отдыхать, не теряя бдительности."
    "Тем временем девчонки устроили большую игру в волейбол."
    show us grin swim at right with dissolve
    show un smile swim at cright with dissolve
    show sl smile sport  with dissolve
    show mt smile swim at left with dissolve
    "Лена, Славя и Мику против Алисы, Ули и Дмитриевна.{w} Я без особого интереса наблюдал за игрой{w} — результат был очевиден."
    "Через некоторое время Дмитриевна подозвала Эла, и он её заменил, уравняв тем самым шансы.{w} Алиса сильно протестовала, но Старшая спокойно пошла в мою сторону."
    hide  us grin swim at right with dissolve
    hide  un smile swim at cright with dissolve
    hide  sl smile sport  with dissolve
    "Она улеглась на соседний шезлонг{w}, и сделала вид{w}, что только заметила меня"
    show mt grin swim  with moveinleft
    mt "Ой, Саш, а ты чего тут?"
    sh "Принимаю солнечные ванны."
    mt "А что с остальными не играешь?{w} Давай, давай к ним."
    sh "Ольга Дмитриевна, если я вам мешаю, так и скажите.{w} Я найду себе другое место для отдыха."
    show mt sad swim  with dissolve
    play music semion_theme
    $ renpy.music.set_volume(0.1, .5, channel="music")
    mt "Нет, ты не так понял.{w} Я смотрю, ты всё отдаляешься ото всех.{w} В начале так общался со всеми{w}, кружок даже завёл{w}, всех ещё зазывал в него, несмотря на отказы.{w} А сейчас...{w} Случилось что?"
    sh "Всё в порядке."
    show mt normal swim  with dissolve
    mt "Всё не в порядке, хотя ты и не скажешь причину."
    "Она вздохнула."
    show prologue_dream with dissolve
    show mt smile body with dissolve
    "Оля-Оля. Я понимаю твоё волнение и мысли.{w} Счастливые дети{w}, довольные взрослые.{w} И ты очень стараешся сделать так.{w} От тебя исходит столько тепла"
    "Прижаться бы к тебе и рассказать о всех своих проблемах.{w} Ты бы с лёгкостью выслушала и дала бы совет."
    "Столько заботы, а отдать её некому.{w} Но{w} мне{w} она{w} не нужна."
    hide mt smile body with dissolve
    hide prologue_dream with dissolve
    show mt normal swim  with dissolve
    mt "Наслаждайся отдыхом, а проблемы оставь на потом. {w}Лето проходит, лови момент."
    sh "Да{w}, скоро кончится лето."
    "Я встал и пошёл вдоль пляжа, а вожатая смотрела на меня с грустью." 
    hide mt normal swim  with dissolve
    voice "Саш, айда к нам"
    "Услышал я. Ребята, наигравшись, побежали купаться."
    scene ext_beach_sunset with dissolve
    "Я обернулся посмотреть на них.{w} Эл, аки акула, всё кружил вокруг Жени"
    show el smile pioneer at right with dissolve
    show mz normal pioneer glasses with dissolve
    "Забавно наблюдать за ними"
    hide el smile pioneer at right with dissolve
    hide mz normal pioneer glasses with dissolve
    show sl smile sport at right with dissolve
    show un smile swim at cright with dissolve
    "Славя и Лена спокойно лежали в воде{w}, о чём-то болтали."
    play sound sfx_water_splash
    "Улька незаметно обрызгала Алиску с ног до головы"
    show us grin swim  with moveinleft
    show dv laugh swim with moveinleft
    "И теперь с криками пыталась убежать от праведного наказания."
    show us grin swim with moveinright
    show dv laugh swim with moveinright
    hide us grin swim with dissolve
    hide dv laugh swim with dissolve
    mi "Ой, Саня.{w} А ты чего тут? Давай к нам!"
    show mi happy swim with dissolve
    sh "О, а я тебя не заметил. Я с собой плавки не взял, так что я на берегу."
    show mi grin swim with dspr
    mi "Ой, да ладно тебе, высохнуть успеешь. Вода сейчас такая тёплая! Так приятно и хорошо, а потом за ракушками нырять будем, весело будет! Поплескаемся! Поплаваем!"
    mi "А потом все вместе в волебол поиграем. А потом..."
    sh "Не{w}, Ми, я пас."
    show mi sad swim with dspr
    mi "Много теряешь "
    sh "Переживу."
    mi "Ну Сааааш"
    hide sl smile sport at right with dissolve
    hide un smile swim at cright with dissolve
    hide mi sad swim with dissolve
    "Но я уже не слушал и шёл дальше.{w} Вы все такие «счастливые»{w}, так изображаете радость и веселье{w}, что я не могу больше видеть это.{w} Как вы надоели!"
    show dv normal swim with dissolve
    dv "Саш, подожди."
    sh "Да, что такое?"
    show dv normal swim close with dissolve
    "Алиса подошла ко мне , и тихо спросила."
    dv "Что такое? {w}У тебя такой убитый вид. "
    sh "Ты проявляешь заботу?{w} Спасибо."
    dv "Должен будешь."
    "Она стала говорить тише"
    dv "Рассказывай, что за проблемы, может помогу."
    sh "Не знаю, с чего это вы все стали так обо мне заботиться. Говорю, всё нормально."
    show dv grin swim close with dspr
    dv "Ты голову мне можешь не морочить — я знаю это чувство, когда никого видеть не хочешь. Но уйти от всех не выход, я проверяла."
    "Удивить её?"
    menu:
        "Да":
            $ dv_trust += 1
            jump d3_beach_dv_1
        "Нет":
            jump d3_beach_dv_2
        
label d3_beach_dv_1:
    play music painful_truth
    $ renpy.music.set_volume(0.25, .5, channel="music")
    sh "Давай присядем{w}, в ногах правды нет."
    "Усевшись на песок, я мечтательно посмотрел в небо."
    show dv normal swim close with dspr
    dv "Ну, вещай, страдалец."
    "Сказала Алиса.{w} Я знаю, что она способна на теплоту и понимание.{w} В мере её программы, разумеется."
    sh "Знаешь, это то чувство, когда ничего не хочется.{w} Вообще.{w} В последнее время оно меня не покидает."
    show dv surprise swim close with dspr
    dv "Никогда бы не подумала, что у тебя может быть такое."
    sh "Однако это есть факт.{w} Всё окружающее лишь на некоторое время сбивает эту хандру."
    show dv normal swim close with dspr
    dv "А потом она возвращается, и всё становится ещё гаже?{w} Знакомо."
    sh "И как ты справлялась?"
    dv "Ну пить ты точно не будешь, сопьёшься ещё.{w} Либо пахать как лошадь, чтобы не думать.{w} Но такое я даже тебе не посоветую."
    show dv smile swim close with dspr
    dv "В твоём случае может помочь только одно — поставить цель и добиваться её.{w} Когда сделал, идёшь к следующей." 
    dv "И жизнь борьба{w}, и удовлетворение от успеха."
    sh "Это ты мощно задвинула."
    show dv laugh swim close with dspr
    dv "А то.{w} Учись, пока я тут."
    "Она встала и пошла к воде."
    scene d2_2ch_beach with dissolve:
        zoom 0.5 
        yalign .5 subpixel True 
        xalign .5 subpixel True 
    dv "Подумай об этом. И не делай такую кислую морду.{w} Грустью ничего не решишь."
    sh "Хех.{w} Спасибо."
    jump d3_beach_true

label d3_beach_dv_2:
    sh "Алис, спасибо тебе большое, но я со своими проблемами сам разберусь.{w} Они... {w} Не такие серьёзные, чтобы нагружать ими других людей."
    show dv normal swim close with dspr
    dv "Дурак ты.{w} Вы всё держите в себе — а это путь в могилу."
    jump d3_beach_true
    
label d3_beach_true:
    scene ext_beach_sunset with dissolve
    play music treck_op
    "Она вернулась к остальным, а я вольготно расположился на свободном шезлонге{w}, загорая до самого вечера."
    "Делать ничего не хотелось{w}, даже на ужин идти.{w} Всё это время я думал.{w} Как на моём месте поступил бы Семён?{w} Остался ли в стороне или присоединился бы к остальным?"
    "Думаю...{w} Если бы его позвала та, которая ему понравилась{w}, то он не задумывался бы.{w} Ради Лены{w}, Слави{w} или Алисы он бы изменился{w}, переступил бы через себя.{w} А я?{w} Ради чего или кого мне переступать через себя?"
    "Не найдя ответа на эти вопросы, я решил пройтись к столовой.{w} До ужина не так уж много времени осталось{w}, буду первым."
    scene int_dining_hall_sunset with dissolve
    $ persistent.sprite_time = 'day'
    play ambience ambience_dining_hall_full
    play music music_list["reminiscences"]
    "Ужин прошёл спокойно и без откровений.{w} Со мной сидел Эл, и я его допытывал, что у него с Женей."
    show el normal pioneer  with dissolve
    sh "Ну давай, рассказывай, что у вас."
    show el surprise pioneer  with dspr
    el "А что у нас?{w} У нас всё нормально{w}, спокойно{w}, мирно."
    sh "Она тебя обругала{w}, да?"
    show el sad pioneer  with dspr
    el "Как догадался?"
    sh "Я вижу прошлое и будущее"
    el "Не смешно."
    sh "Не унывай."
    show el normal pioneer  with dspr
    "На этом и закончили."
    hide el normal pioneer  with dissolve
    "После ужина Ольга сказала, что у нас свободное время"
    show mt normal pioneer panama  with dissolve
    mt "Саш, а ты мне не поможешь?"
    sh "А у меня есть выбор?"
    show mt grin pioneer panama  with dspr
    mt "Только если есть совесть."
    sh "Что делать надо?"
    mt "Ничего такого.{w} Сходи до библиотеки и принеси пару комплектов формы."
    sh "А что там делает форма?"
    mt "Забыли, когда вещи и продукты разгружали"
    sh "Пффф, я-то думал."
    stop ambience
    scene ext_library_night with dissolve
    "Спокойным{w}, неторопливым шагом я направился уже знакомой дорогой.{w} Скоро, очень скоро послом{w}, а точнее всеми посылаемым человеком назначат другого.{w} Завтра приедет ОН."
    "Дойдя наконец до библиотеки, я увидел замок на двери.{w} А ключа у меня и нет."
    sh "Странно.{w} У кого ума хватило запереть?"
    "Сказал я вслух, надеясь, что ключник далеко не ушёл."
    "Но ответа не последовало."
    "И что мне теперь делать?{w} Со злости я пнул дверь, в душе надеясь её выбить."
    play sound sfx_slam_door_campus
    play music pioneer_theme
    $ renpy.music.set_volume(0.25, .5, channel="music")
    voice "Ну вот зачем ты это сделал?"
    show monster
    "Раздался голос за дверью.{w} Его хозяйка в прошлый раз отправила меня к Уле, так что я сразу её узнал."
    sh "Ты так и будешь скрываться от меня?"
    voice "Пока не время. "
    sh "А когда?{w} Завтра приезжает Семён, и у меня...{w} У нас остаётся всего семь дней на спасение."
    voice "Ну, не семь, это раз.{w} А во вторых, ты ему точно не помошник."
    sh "Это почему это?"
    voice "Ты себя уже плохо контролируешь.{w} Ещё немного и ты станешь как тот{w}, другой."
    sh "Ты что{w}, вроде надсмотрщика или охранника?{w} Покажись, не зли мненя."
    "Я ударил по двери кулаком."
    play sound sfx_slam_door_campus
    voice "Вот видишь. "
    play music alex_mind
    sh "Я...{w} Понял тебя.{w} Хорошо, говори, зачем пришла."
    voice "Саш, не мешай Семёну в его поиске себя.{w} Ты всё равно ему не помощник."
    sh "Ты просишь невозможного."
    voice "Твои усилия нужны в другом месте.{w} Понимаешь, тот другой может вмешаться, и всё испортить.{w} Но его силы можно подорвать.{w} Только вы двое умеете перемещаться, и больше никто. "
    voice "Но если остальные тоже научатся, то ЕМУ придётся прикладывать больше сил{w}, и тут он находиться будет меньше."
    sh "Хм, интересно.{w} Продолжай, я заинтересован."
    voice "Ты уже знаешь, как перемещаться, но ТАМ ты призрак, видение.{w} А быстро перенести сознание тебе пока не дано."
    sh "«Пока»?"
    voice "Да, потому что я тебя сейчас научу этому.{w}  Нужно собрать все воспоминания{w}, связанные с этим человеком.{w} И эмоция{w}, сильная."
    sh "Какая?"
    voice "Любая.{w} Всё вместе перенесёт тебя в тот момент, где человек испытывал тоже самое чувство. "
    voice "Страх, ненависть, любовь — всё сгодиться."
    sh "Я запомню это.{w} Спасибо, кем бы ты не была."
    voice "Действуй осторожно.{w} Им нужно твоё внимание."
    sh "Ха, им нужна помощь, не больше.{w} Но я сделаю это.{w} Семёну никто не помешает кадрить девок."
    hide monster
    "Но ответа мне не последовало. {w}Что ж, и на том спасибо."
    "Взяв форму, я пошёл до домика Дмитриевны.{w} Как мне повезло, ведь теперь я получил действительно дельный совет. "
    "Я смогу помочь ему, даже косвенно."
    scene ext_house_of_mt_night with dissolve
    play music music_list["sweet_darkness"]
    "Оказавшись на месте, я вежливо постучался"
    mt "Открыто."
    "Я зашёл внутрь"
    scene int_house_of_mt_noitem_night with dissolve
    $ persistent.sprite_time = 'day'
    show mt normal pioneer panama with dissolve
    sh "Вот, Ольга Дмитриевна, принёс. Всё глажено-чисто."
    "Вожатая сидела за столом и читала книгу."
    mt "Спасибо Саш, повесь в шкаф{w}, будь другом."
    "Сказанно - сделано.{w} Открыв шкаф, я заметил маленький блокнот."
    sh "Ольга Дмитриевна{w}, а что у вас за блокнот тут ?"
    show mt surprise pioneer panama with dspr
    mt "Нужен?"
    sh "Пригодился бы."
    mt "Бери и пользуйся."
    "Я улыбнулся"
    sh "Спасибо большое."
    show mt smile pioneer panama with dspr
    "Она улыбнулась в ответ"
    mt "Улыбайся чаще."
    "Я кивнул и отправился к своему домику."
    scene ext_square_night with dissolve
    "У меня уже созрел план, и я его исполню без промедления."
    stop music
    jump day_4
    
label day_4:
    $ backdrop = "1й день"
    $ new_chapter(1, u"1й день")
    scene alex home day
    play music painful_truth fadein 3
    
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    
    "Что ж, доброе утро, мир." 
    "Я неспешно проснулся, оделся и пошёл умываться."
    "Странно, я так ждал этот день, волновался, а теперь абсолютно спокоен."
    scene ext_washstand_day with dissolve
    "Уххх, вода ледяная.{w} Освежившись, и думается лучше."
    show sl normal sport with dissolve
    sl "Саш, доброе утро" 
    sh "Здравствуй, Славь, как спалось?"
    sl "Спасибо, хорошо." 
    show sl shy sport with dspr
    sh "Я так понимаю, тебе от меня что-то нужно."
    sl "Да. Не мог бы ты со мной встретить новеньких?"
    sh "Извини, но тут я пас.{w} Волнуюсь сильно при незнакомых людях."
    show sl smile sport with dspr
    sl "Что их бояться? Пошли!"
    sh "Нет"
    "Сказал я строго"
    sh "Славь, ты лицо почти официальное, тебе и карты в руки."
    hide sl smile sport with dissolve
    show el normal pioneer with dissolve
    "Увидев, что тут ей ни чего не светит, активистка помахала рукой и ушла готовится к встрече." 
    "Не готов я ещё лицезреть виновника торжества, могу не сдержаться." 
    scene ext_clubs_day with dissolve
    "Чёрт, но и оставить его не могу, а не то не ровен час распугает всех будущих поклонниц."
    scene int_clubs_male_sunset
    $ persistent.sprite_time = 'day'
    $ sunset_time()
    show el normal pioneer
    with dissolve
    "Надо к нему Эла заслать."
    el "Саш, а чего не пошёл-то? Вы вдвоём составили бы хорошее впечатление."
    sh "Не, Славяна идеально подходит на эту роль. Она и встретит, и объяснит. И тут такой я всю атмосферу порчу. Сюда приезжают отдохнуть, и мы не знаем, кого нам завезли."
    show el smile pioneer with dspr
    el "Вряд ли к нам всякое хулиганьё завезут."
    sh "Ты{w}, видимо{w}, про Дваче забыл."
    show el scared pioneer with dspr
    "Эла передёрнуло от клички нашей общей знакомой."
    el "Д-да, тут ты прав."
    sh "Я больше скажу. Нам надо новоприбывших в клуб пригласить." 
    sh "Несколько новых членов не помешает, заодно спасём их от нападок этих хулиганок."
    show el surprise pioneer with dspr
    el "Это ты ловко придумал. А как мы это сделаем?"
    sh "Сходи через пару минут на площадь. Дмитриевна будет рассказывать про лагерь, а ты потащиш их к нам. А я тут пока всё в порядок приведу."
    show el grin pioneer with dspr
    el "Хм, неплохо. Я их приведу, расскажу про лагерь, а ты будешь эдаким Мориарти, поджидающим их." 
    sh "Хорошо, что мы понимаем друг друга"
    "Я улыбнулся."
    stop music fadeout 3
    hide el grin pioneer with dissolve
    "Спустя некоторое время Эл встал, и вышел, по пути поправляя форму для солидности."
    play music alex_theme fadein 3
    "Может, он и сможет привести Семёна сюда, но я почему-то сомневаюсь в этом. В любом случае, всё идёт по плану."
    "Чтобы скоротать время, я решил заняться нашим роботом. "
    "Остались последние штрихи, на пару дней неспешной работы. А что потом ?"
    "Но мои размышления опять прервались стуком в дверь."
    play sound sfx_knock_door3_dull
    "Нет уж, на этот раз я с места не двинусь."
    sh "Ааааткрыта"
    "Заорал я."
    "Как всегда нет ответа."
    "Постучались снова"
    play sound sfx_knock_door3_dull
    "Да вы издеваетесь."
    "Открылась дверь"
    play sound sfx_open_door_clubs
    "Я повернулся, чтобы посмотреть на гостя...{w} И замер."
    show pioneer normal with dissolve
    stop music fadeout 3
    "Семён."
    "Нет, не он. Другой"
    show pi smile with dspr 
    hide pioneer normal
    play music pioneer_theme fadein 3
    pi "Представление начинается!"
    "Картинно выдал он."
    sh "Тебя сюда не звали."
    "Холодно сказал я"
    "Что он тут делает?! Почему? Как? "
    "И всё моё сосредоточение ушло в никуда -  одно его появление разрушило моё спокойствие и вселило панику."
    show pi normal1 with dissolve
    pi "Всё злишся из-за того удара?{w} Не будь плаксой.{w} И на счёт мелкой не волнуйся - не тронул её я."
    sh "Что ты тут забыл?"
    pi "Да вот хотел с тобой поболтать. Всё ж столько лет друг друга знаем."
    sh "Не действуй мне на нервы."
    pi "Хорошо, не буду."
    show pi smile with dissolve
    "Улыбнулся он"
    pi "Я в сторонке посмотрю."
    sh "Всё сказал?"
    pi "Неа, а что, у тебя планы?{w} Я тебя отвлекаю?"
    sh "Да, и очень сильно.{w} Прочь, нечисть."
    pi "Ой, планы по спасению мира? А может думаешь «А как мне поговорить с девушками?»?"
    pi "А я дам тебе пищу для размышлений — а с чего ты взял что тебе они поверят, и согласятся на твой план?"
    sh "Любой нормальный человек согласится, что реальность лучше фантазий.  И про тебя расскажу, не волнуйся." 
    pi "Думаешь избавиться от меня таким способом? Хороший план, интересный."
    show pi normal1 with dissolve
    "Он так спокойно говорит об этом. Что происходит?"
    pi "Знаешь, а я помогу тебе даже. Хоть какое-то действительно интересное занятие."
    show pi smile with dissolve
    "Он подошёл ближе."
    sh "Ты чего задумал?"
    "Сказал я, взяв в руки ножницы."
    pi "Ничего такого"
    "И он дал мне щелчка по лбу."
    stop music fadeout 3
    with hpunch
    show blink
    play music treck_op fadein 2
    $ persistent.sprite_time = 'night'
    $ sunset_time()
    show prologue_dream with dissolve
    "Мир померк.{w} Полная пустота.{w} Я даже не успел что-либо почувствовать.{w} Опять он меня вырубил.{w} Страшно.{w} Помогите. "
    "Но вряд ли кто мне поможет тут и сейчас.{w} Мне не хватает сил.{w} Помогите. {w}Пожалуйста. "
    "Эх, был бы я чуть сильнее.{w} Смелее.{w} Как...{w} Как Алиса."
    show dv smile body behind prologue_dream with dissolve
    "Да.{w} Как я хочу увидеть тебя сейчас.{w} Мне очень страшно.{w} Помоги мне Алиса!!{w} АЛИСА!! {w}Защити меня."
    scene ext_path_night
    stop music fadeout 3
    show unblink
    with hpunch
    "Бум."
    play music music_list["dance_of_fireflies"] fadein 3
    play ambience ambience_forest_night
    "Открыв глаза, я с удивлением обнаружил, что упёрся носом в траву. Где я??"
    "Встав и отряхнувшись, я решил собраться с мыслями. Так{w}, жив{w}, цел{w}, лес.{w} Лес? Действительно."
    "Причём вечерний. Я непонятным вечером в непонятном лесу. Уже лучше, но хотелось бы поподробней."
    "Но в следующую секунду мои опасения развеялись по ветру, ибо я учуял дым от костра. Одним вопросом меньше."
    play sound sfx_forest_fireplace
    scene ext_path2_night with dissolve
    "Как и ожидалось, у костра был почти весь отряд, не хватало лишь главных действующих лиц. И я знаю где они."
    "К счастью, искать их долго не пришлось - мимо меня пробежала Лена."
    show un shy pioneer with moveinleft
    play sound sfx_bush_leaves
    $ renpy.pause(5)
    hide un shy pioneer with dissolve
    "А за ней Семён."
    show pioneer normal with moveinleft
    play sound sfx_bush_leaves
    $ renpy.pause(5)
    hide pioneer normal with dissolve
    "Хех, знакомая картина, до боли просто."
    "Но не они меня интересовали, а та, которая осталась в темноте и в одиночестве.{w} Яркое солнышко{w}, сжигающее всех своими чувствами."
    stop music fadeout 3
    scene ext_polyana_night
    show dv sad pioneer 
    with dissolve
    play music Memory fadein 3
    "Нашёл я её сидящей на бревне, обхватившей голову руками."
    "Представляла она из себя жалкое зрелище, бледную тень самой себя.{w} Видимо ей «дали от ворот поворот», потому что на окружение она совсем не обращала внимания." 
    "Я подошёл ближе, стараясь не шуметь."
    dv "Чего крадёшся?"
    "Да, в разведку мне не ходить."
    sh "Проходил мимо, вижу — ты тут. Решил проверить жива или нет?"
    "Она усмехнулась"
    sh "Что случилось?"
    show dv shy pioneer with dspr
    dv "Это мои дела.{w} Не лезь{w}, не надо."
    "Внутреннее чувство подсказывало, что уходить ни в коем случае нельзя, и я заговорил."
    sh "Это всё Сёма, да?"
    "Нет ответа."
    show dv guilty pioneer with dspr
    sh "Ушёл с твоей подругой."
    "Молчание."
    sh "Хотя ты от него без ума."
    show dv rage pioneer with dspr
    dv "ДА ИДИ ТЫ НА ХРЕН!!"
    play sound sfx_face_slap
    with hpunch
    "Я задел за живое, посыпал соль на рану в душе молодой девушке, за что и получил по лицу.{w} Кажется это стало становиться обычаем или традицией.{w} Надо это прекращать."
    show dv sad pioneer with dspr
    "Она собралась уходить, но я знал как её остановить."
    sh "Если не одумаешся, так и останешся одна. Я просто хочу помочь."
    show dv shocked pioneer with dspr
    dv "С чего это вдруг?"
    sh "Несмотря на наши разногласия, мне непприятно смотреть  как ты страдаешь. Ты всегда такая живая и бойкая, а сейчас..."
    show dv sad pioneer with dspr
    dv "Вот не ожидала, что так низко паду, что даже ты меня жалеешь."
    sh "Можешь ещё ниже, если не послушаешь."
    "Oна промолчала."
    sh "Ты всеми силами пыталась привлечь его внимание, но опыта у тебя мало, да и выражать свои чувства толком ты не можешь."
    show dv normal pioneer with dspr
    dv "C каких пор ты в психологи подался?"
    sh "Да у тебя всё на лице написано, ничего сложного."
    dv "Хорошо."
    show dv smile pioneer with dspr
    dv "Трави дальше."
    sh "Поэтому когда он принял твою игру, показал, что ты ему не безразлична, даже сквозь твой паршивый характер и поведение, он был рядом."
    show dv surprise pioneer with dspr
    sh "Ты ведь в нём так нуждалась, а он свинтил с твоей подругой..."
    show dv guilty pioneer with dspr
    dv "Не подруга она мне больше..."
    sh "Пусть так. И что ты теперь делать будешь?"
    dv "Я..."
    show dv sad pioneer with dspr
    sh "Что «Я»?"
    dv "Я не знаю."
    "Она совсем поникла. Не думал, что увижу её такой."
    sh "Зато я знаю. Слушай. Этот Семён не стоит усилий."
    show dv surprise pioneer with dspr
    dv "Не поняла."
    sh "Неудивительно. Давай по другому. Тебе не кажется, что тут всё слишком идеально? Вожатая{w}, пионеры{w}, погода, да и остальное, по мелочи?"
    show dv normal pioneer with dspr
    "Она внимательно посмотрела на меня."
    sh "И только ты выбиваешся из всей картины.{w} Чувственная бунтарка.{w} Агрессивный вулкан страстей."
    show dv guilty pioneer with dspr
    "Она задумалась, и задумалась серьёзно. Видимо мои слова попали в самую точку."
    sh "И скорее всего у тебя бывали ощущения, что ты всё окружающее уже видела."
    dv "К чему ты клонишь?"
    show dv sad pioneer with dspr
    sh "К тому, что всё тут ненастоящее.{w} Иллюзия счастья.{w} Ты можешь и будешь переживать эту смену раз за разом, обретая счастье и теряя смысл жизни. Выхода из этого цикла для тебя нет."
    show dv scared pioneer with dspr
    dv "Саш, ты меня пугаешь."
    sh "Увы, но это факт."
    show dv normal pioneer with dspr
    dv "Сумасшедший."
    "Она собралась уходить, но я понял, как остановить её раз и навсегда."
    sh "Ты хочешь его вернуть?"
    show dv sad pioneer with dspr
    "Молчание"
    sh "Другого выхода у тебя нет."
    "Опять молчит. Вот ведь упрямая. Ну поддайся же своим чувствам - всем легче будет."
    sh "Сама понимаешь, что ещё немного, и тебе с ним не светит большой и чистой любви.{w} Будешь потом маяться."
    show dv guilty pioneer with dspr
    dv "Говори."
    "Хех, у каждого есть своя цена. Теперь я в этом убедился."
    sh "Слушай тогда, повторять не буду. Звучит дико, но тут, в этом лагере, только ты и я настоящие люди, из плоти и крови. Все остальные - лишь куклы, роботы, да кто угодно."
    show dv shocked pioneer with dspr
    sh "Последовательность их действий всегда одна и та же, да и реакция предсказуема. Знаю, что принять этот факт трудно."
    dv "Это да."
    show dv normal pioneer with dspr
    sh "Но есть настоящий Семён, тот который сможет понять и принять тебя такой какая ты есть. {w}И будет тебе верен."
    show dv surprise pioneer with dspr
    dv "И где же он?"
    "Я подошёл к ней"
    show dv normal pioneer close with dspr
    sh "Попытаюсь тебе показать.{w} Закрой глаза.{w} Не бойся, я с тобой."
    "Я также закрыл глаза"
    show blink
    stop ambience
    show prologue_dream with dissolve
    dv "Ну, что дальше?"
    sh "Представь Его, и вспомни все приятные моменты проведенные с ним."
    dv "Хорошо."
    "Хм, теперь нужны эмоции и чувства."
    sh "Вспомни что-либо хорошее, связанное с ним."
    "Она тихо захихикала"
    dv "Что за глупости..."
    sh "Не смейся! Сосредоточься."
    "Я прикоснулся к ней, вновь ощутив тепло её тела." 
    "Наверно со стороны это смотрится очень смешно, да и самому кажется, что это странно."
    "Но выбирать не приходится."
    dv "И долго мы так стоять будем?"
    sh "Нет."
    "Её нетерпение позабавило меня. Припоминаю я один такой момент, где тебе, Алиса, терпение явно не помешало бы." 
    show d6_dv_hentai_2 behind prologue_dream with dissolve
    dv "Ой, а как это он? Меня?"
    stop ambience
    stop music fadeout 3
    "Я открыл глаза, обнаружив себя в каких-то кустах, в обнимку с Алисой."
    
    
    scene ext_house_of_dv_night
    play music music_list["into_the_unknown"] fadein 3
    play ambience ambience_ext_road_night 
    show dv normal pioneer 
    show unblink
    sh "Пойдём."
    "Тихо сказал я."
    "Судьба забросила нас к домику этой рыжей бестии, в самый разгар бессонной ночи."
    "Я заглянул в окно, и увиденное мною меня нисколько не удивило."
    scene d6_dv_hentai_2 with dissolve
    "Да, мы точно оказались по адресу."
    scene ext_house_of_dv_night with dissolve
    sh "Вот{w}, полюбуйся."
    "Cказал я своей спутнице."
    show dv surprise pioneer far with dissolve
    "Алиса явно волновалась, но на моё приглашение отреагировало здраво{w}, с любопытством.{w} Надо отдать ей должное, умеет держать себя в руках."
    "Она тихонько пробралась к окну...{w} И замерла."
    stop music 
    show dv shocked pioneer far with dspr
    dv "Это..{w} Что такое?"
    play music alex_theme fadein 3
    sh "То, что видишь. Понимаешь..."
    "Но рассказать все события, предшествующие этому акту любви я не успел, поскольку Алиса посмотрела на меня с немым вопросом."
    show dv shocked pioneer with dspr
    sh "Что?{w} Ты хотела правды?{w} Вот смотри, запоминай, мотай, так сказать, куда можешь."
    stop music fadeout 3
    "Алиса села и прижалась ко мне."
    show dv guilty pioneer with dspr
    play music Freedom_2 fadein 3
    dv "Уведи меня отсюда."
    "Легко сказать." 
    sh "Мы тут не просто так.{w} Понимаешь, если бы это был «твой» лагерь, то ты бы сейчас была там, под ним. Но Алис{w}, ты здесь тут со мной, в кустах сидишь."
    show dv cry2 pioneer with dspr
    "Она посмотрела не меня. Вот это зрелище: она просто рыдала."
    dv "И?"
    sh "И то, что пошли искать местных. Хотя мне кажется, я знаю куда идти."
    scene ext_square_night with dissolve
    "Блуждать долго не пришлось, хотя я рассчитывал найти её быстрее." 
    "Славя."
    "Из всех, только она могла бы так стоически переносить страдания.{w} И помня мой прошлый неудачный опыт, я решил реабилитироваться в её глазах, раскрыв правду."
    stop ambience
    scene ext_beach_night with dissolve
    show dv sad pioneer
    with dissolve
    "Всю дорогу Алиса не проронила ни слова.{w} По ней было видно, что происходящее сильно на неё давит. Хех, со мной было точно также, так что её теперешние мучения для меня смехотворны."
    "Но стоит поддержать её, не то сорвётся{w} - мне она нужна целой и здоровой." 
    sh "Алис, ты как?"
    show dv guilty pioneer with dspr
    dv "Знаешь, странное чувство, когда смотришь на себя со стороны."
    sh "Понравилось?"
    show dv sad pioneer with dspr
    "В ответ молчание"
    sh "Не волнуйся, всё идёт по плану. Это была НЕ ты, а этот был НЕ Семён. {w}Просто повторяй себе это почаще."
    show dv normal pioneer with dspr
    dv "Легко тебе говорить."
    
    
    scene ext_beach_night with dissolve
    "Тем временем мы вышли к пляжу, и в свете луны я увидел Славю. Её вещи были аккуратно сложены на берегу."
    show sl smile body at right with dissolve
    "Она была абсолютно голой, и шла в воду. По какой-то причине мне стало страшно за неё, особенно когда она нырнула." 
    hide sl smile body at right with dissolve
    sh "Нашла время купаться!"
    show dv scared pioneer with dissolve
    stop music fadeout 3
    "Но Алиса не разделила мой юмор"
    dv "Давай быстрее!!"
    "Куда? Зачем?"
    play sound sfx_scary_sting
    "И тут меня самого пронзил ужас — почему она не всплывает за воздухом?!"
    play music alex_theme fadein 3
    "Вот почему всегда проблемы?"
    "Эта мысль пронеслась в голове, когда я со всех ног влетел в озеро, чтобы вытащить нашу блондинку."
    show dv rage pioneer with dspr
    play sound sfx_shoulder_dive_water
    with hpunch
    "Что самое странное, Алиса не отставала от меня ни на шаг."
    "Я уже начал проклинать себя за неспешность, когда вдруг Славя вынурнула прямо передо мной"
    play sound sfx_draw_water
    show sl surprise body at right with dissolve
    sl "Ой, а что вы тут делаете?"
    "Девушка была явно удивлена появившейся компании"
    sh "Да мы это..."
    show sl angry body at right with dspr
    sl "Опять ты!? Сказала же, убирайся прочь!"
    play sound sfx_face_slap
    with hpunch
    "И я опять получил по лицу.{w} Снова."
    show blink
    $ renpy.pause(5)
    show unblink
    hide blink
    "Когда уже сам выбрался на берег, девушки ждали меня с множеством вопросов."
    show sl smile body at right
    show dv rage pioneer
    with dspr
    sh "Здравствуй Славя."
    dv "Ты в своём уме, топиться из-за парня?"
    stop music fadeout 3
    show sl angry body at right with dspr
    play music music_list["gentle_predator"] fadein 3
    sl "Во-первых, я топиться не собиралась{w}, а во-вторых..."
    "Она посмотрела на меня."
    show dv normal pioneer with dspr
    sl "Во вторых я прислушалась к твоему совету"
    sh "А по лицу зачем тогда надо было бить?"
    sl "Я подумала, что это тот бабник пришёл извиняться."
    "Славя посмотрела на Алису с некоторой злостью, если не с ненавистью."
    sh "Успокойся, она тоже как и ты — настоящая."
    show sl smile body with dspr
    sl "Хм, ну здравствуй... Алиса"
    show dv grin pioneer with dspr
    dv "Ну привет-привет Славяна.{w} Не знала про твои увлечения."
    show dv smile pioneer with dspr
    "Алиса улыбнулась.{w} Это явно хороший знак. Я опасался, что их знакомство может обернуться проблемами."
    show dv angry pioneer with dspr
    dv "Саш, а ты чего глаза выпучил то? А ну, отвернись быстро"
    sh "Оу, извини, Славь."
    hide dv angry pioneer
    hide sl smile body
    with dissolve
    "Со всей этой суматохой я и не заметил, что она голая. Для меня такие вещи перестали быть значимыми. Одет/не одет, рядом/далеко, есть он/нет его."
    "Уже не важно совсем. Только бы выбраться отсюда — это единственное, что имеет значение."
    "Алиса помогла Славе одеться, и времени потребовалось совсем немного."
    dv "Всё, поворачивайся."
    show dv normal pioneer at right
    show sl normal pioneer
    with dissolve
    sh "Ну что, куда пойдём?" 
    show dv smile pioneer at right with dspr
    dv "Вот умные вопросы ты задаёшь Саш. Я тут по твоей милости, а она..."
    "Алиса кивнула на Славю"
    show sl surprise pioneer with dspr
    dv "Ей сейчас надо многое переварить."
    sh "Тогда пойдёмте до столовой, ключи у нас есть."
    "Теперь Я кивнул в сторону Слави."
    stop music fadeout 3
    scene ext_dining_hall_away_night with dissolve

    $ persistent.sprite_time = 'day'
    
    "Путь был быстрым  без приключений и разговоров."
    scene int_dining_hall_night with dissolve
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    sh "Проходите, устраивайтесь. Я сейчас чай заварю, ночь будет длинной."
    show dv normal pioneer at right
    show sl normal pioneer
    with dissolve
    "Хорошо что у нас в столовой было всё необходимое для самообеспечения. И чайник, и сахар, даже печенье нашлось."
    "Отрыв 3 самые чистые чашки, я разлил чай, и вышел к ждавшим меня гостьям."
    "Те сидели друг на против друга, в гробовой тишине и смотрели на меня."
    sh "Значит так.{w} Вот это тебе.{w} А это тебе."
    show sl shy pioneer with dspr
    sl "Спасибо"
    show dv shy pioneer at right with dspr
    dv "Хм, спасибо"
    "Тихо сказала Алиса"
    sh "Первый вопрос — вы помните как приехали в лагерь?" 
    show dv normal pioneer at right
    show sl normal pioneer
    with dissolve
    dv "Да"
    sl "Да"
    sh "Как всё было замечательно, весело и тому подобное.{w} А потом приехал ОН."
    show dv sad pioneer at right with dspr
    "Комната погрузилась в молчание."
    sh "Каждая из вас любит Сёму. Можете не мотать головой , Алис, я знаю. Идея проста:"
    sh "Вы попадёте в «Совёнок», где настоящий, главный Семён. И просто..."
    "И тут у меня комок в горле встал.{w} Как я им скажу, что его надо ПРОСТО влюбить в себя?{w} А как же их чувства?{w} Они откажутся от этого, да и вряд ли это вырвет меня{w}, то есть нас отсюда."
    show sl surprise pioneer with dspr
    sl "Что Саш?"
    show dv surprise pioneer at right with dspr
    dv "Что замолчал?{w} Надо говорить «А» и «Б». А то остановился на полуслове."
    sh "Просто исполнить ваши мечты. Каждая из вас хочет счастья.{w} Оно идёт к вам в руки."
    show dv guilty pioneer at right
    show sl sad pioneer
    with dspr
    "Девушки некоторое время обдумывали мои слова. Да уж, нелёгкий выбор."
    "Молчание первой нарушила Славя."
    stop music fadeout 3
    show sl serious pioneer  with dspr
    sl "Знаешь, я против этого. Должен быть другой способ."
    play music alex_theme fadein 3
    sh "Его нет."
    sl "Ты понимаешь, что окажись мы с Алиской с Семёном, то станем соперницами? И я думаю, что ты и про других девушек не забудешь."
    sh "В конкуренции сила"
    show dv normal pioneer at right with dspr
    dv "Мы тебе не товар, а живые люди. Я тоже против."
    "Вот бабы, что ж вы за народ такой? Я даю вам шанс на спасение, а ВЫ готовы бросить всё ради своего эгоизма."
    sh "Вы не так поняли. Сёма выберет одну из вас, влюбится по самое немогу. Он будет готов на всё, что ещё надо?"
    show dv angry pioneer at right with dspr
    dv "А ты о других подумал? Мне кажется, что единственный эгоист — это ты."
    show sl angry pioneer with dspr
    sh "Всем придётся чем то жертвовать, ради блага остальных. И не волнуйтесь, я буду помогать советом, и не только."
    sl "Вот если только мы окажемся у тебя ТАМ, кому ты поможешь?"
    sl "Говори, не стесняйся."
    "Вот этого я не ожидал."
    stop music fadeout 3
    menu:
        "Тебе Славь. Ты очаруешь его":
            $ sl_love += 1
            $ dv_happy -= 1
            jump sl_trust
        "Алисе. Она покорит его ":
            $ sl_love -= 1
            $ dv_happy += 1
            jump dv_trust
        "Уйти от ответа":
            $ sl_love -= 1
            $ dv_happy -= 1
            $ el_happy += 1
            $ un_love += 1
            $ us_happy += 1
            jump no_trust

label sl_trust:
    play music alex_mind fadein 3
    show dv surprise pioneer at right
    show sl surprise pioneer
    with dspr
    "Девушки явно не ожидали такого ответа."
    sh "Если сложится всё как ты описала, что вряд ли, то это самый логичный выбор."
    show sl normal pioneer with dspr
    dv "Постой, а как же я?!" 
    sh "Так будет лучше для всех. "
    show dv angry pioneer at right with dspr
    "Алиса начинает свирепеть прямо на глазах.{w} А что я могу ей сказать?"
    show sl scared pioneer with dspr
    sl "Алис, подожди, не горячись.{w} Мне тоже этот план не нравится, но я не хочу застрять тут навеки."
    show dv rage pioneer at right with dspr
    dv "Тебя, красота ты наша, не спрашивали.{w} Хуже Ленки, чёрт вас дери."
    sh "Что-то не нравится?{w} Иди к своему домику, третьей будешь."
    "Я начал терять терпение"
    show sl angry pioneer with dspr
    sl "Саша!"
    show dv sad pioneer at right with dspr
    "Алиса молча сидела на стуле со своей чашкой.{w} Может, я переборщил?"
    show sl serious pioneer with dspr
    sh "Алис, ты чего? Я не хотел..."
    show dv guilty pioneer at right with dspr
    dv "Я всё понимаю. Честное слово, всё всё."
    "Она молча встала, поставила нетронутый чай и пошла к выходу."
    show sl angry pioneer with dspr
    sl "Что ты сидишь?{w} Тоже мне, спаситель нашёлся." 
    "Славя бросилась к «подруге-по-несчастью».{w} Кто знает, что случилось бы, если дверь вдруг не открылась, и на пороге появилась до боли неприятная фигура."
    play sound sfx_open_door_2
    stop music fadeout 3
    show pi smile at left with dissolve
    play music pioneer_theme
    pi "Что, пионеры, чаи гоняем?" 
    show dv surprise pioneer at right with dspr
    dv "Ты?!"
    show sl surprise pioneer with dspr
    sl "Семён?"
    pi "Я вам, чёртовы куклы, сейчас аппетит испорчу."
    stop music 
    "С этими словами он отбросил Славю, а Алису поволок за дверь."
    play music music_list["doomed_to_be_defeated"] fadein 3
    "В любой другой момент я бы колебался.{w} Думал.{w} Может быть, струсил.{w} Но жажда жизни и ненависть не дали мне и секунды размышлений.{w} Схватив деталь от многострадального робота, я влетел в него со всей своей силой." 
    scene d4_sh_stay with dissolve
    play sound sfx_punch_washstand
    with hpunch
    "Он сильнее меня, и явно опытнее, но крыса, загнанная в угол, смертельно опасна."
    scene ext_dining_hall_near_night
    show pi smile
    with dissolve
    "Я повалил его и резко вскочив, хорошенько огрел его по спине железякой."
    play sound sfx_punch_washstand
    "Второй удар прошёл мимо, и он обезоружил меня."
    with hpunch
    "Но нет, меня так не остановить.{w} Мой следующий удар пришёлся ему прямо в кадык, отчего этот гад потерял всякое желание драться дальше."
    sh "Всё или ещё? Убирайся прочь!"
    "Скомандовал я."
    "Но моя радость была преждевременной.{w} Он просто притворялся, и выгодав удачный момент, схватил и перекинул меня." 
    with hpunch
    "Ай, как больно!"
    show blink
    "Удар ногой по голове."
    with hpunch
    stop music fadeout 3
    "Но 2го не последовало, и я отважился посмотреть причину."
    
    scene ext_dining_hall_near_night
    show unblink
    play music good_rage fadein 3
    "Алиса"
    show dv rage pioneer at right 
    show pi rage at left
    with dissolve
    "Она спасла меня."
    "Несмотря на то, что она слабее моего врага, Алиса  его била со всей силы.{w} Болевые приёмы, захваты, грязные удары. Пионер оказался на четвереньках, ловя воздух ртом."
    play sound sfx_punch_washstand
    dv "За то, что угрожал мне и моим...{w} Друзьям."
    play sound sfx_lena_hits_alisa
    "И Алиска хорошим, футбольным ударом припечатала ему по лицу.{w} Он буквально отлетел в ближайшие кусты."
    hide pi rage at left with dissolve
    dv "Готов."
    "Довольно сказала рыжая."
    show dv normal pioneer at right with dspr
    stop music fadeout 3
    sh "Алис... Ты спасла... Меня."
    "С трудом выговорил я."
    play music painful_truth fadein 3
    dv "Честно, на его месте мог быть ты, но тебе повезло."
    show dv smile pioneer at right with dspr
    "Разулыбалась та." 
    dv "Чтобы вы без меня делали, а?"
    show dv grin pioneer at right with dspr
    sh "Даже не знаю." 
    dv "Фуф, даже полегчало."
    show sl surprise pioneer with dissolve
    sl "Может нам стоит проверить, как он?"
    sh "Ненужно, его уже тут нет."
    show sl normal pioneer with dissolve
    "Однако как быстро прибежал, а?{w} Значит я всё делаю правильно, верно?"
    sh "Спасибо тебе, Алис."
    "Она только улыбнулась в ответ. Я попытался встать, но голова закружилась.{w} Так бы и упал, но крепкое плечо Алисы не позволило."
    show dv laugh pioneer at right with dspr
    dv "Пошли, чай стынет."
    stop music fadeout 3
    scene int_dining_hall_night
    show dv grin pioneer at right
    show sl scared pioneer
    with dissolve
    play music alex_mind fadein 3
    "Внутри Славя перевязала мне голову «что-под-руку-попалось»."
    sh "Я вижу, ты собой довольна."
    show dv laugh pioneer at right with dspr
    dv "Да, давно так не веселилась." 
    show sl serious pioneer with dspr
    sl "Алис, а ты как?"
    show dv normal pioneer at right with dspr
    dv "В полном порядке. Спасибо. Так, на чём мы остановились?"
    jump travel_back

label dv_trust:
    play music alex_mind 
    show dv surprise pioneer at right
    show sl sad pioneer
    with dspr
    dv "Ого."
    "Удивилась Алиса"
    "Славя сидела молча, видимо мой ответ оказался слишком прямолинейным для неё."
    show sl serious pioneer with dspr
    sl "То есть, ты предлагаешь мне быть как эти «куклы»?{w} Какой тогда вообще смысл?"
    sh "Ну может ты ему больше понравишся."
    "Начал мямлить я."
    sl "Вот спасибо тебе." 
    show dv guilty pioneer at right with dspr
    dv "Мда, что-то ты перемудрил. Ты ему что, целый гарем собираешь?"
    sl "Алиса, ты уж очень просто об этом говоришь. Это всё так сложно!" 
    show dv sad pioneer at right with dspr
    dv "Заметь, это сейчас не тебя там... "
    "Девушка замолчала."
    "Воцарилась пауза."
    "Девушки молча смотрели на меня и друг на друга.{w} А я спокойно попивал свой чай, и ждал их реакции."
    "Тишину первой нарушила Славя."
    show sl sad pioneer with dspr
    sl "Хорошо, я сделаю так как ты говоришь.{w} В конце концов я хочу, чтобы он был счастлив, даже если и не со мной."
    show dv cry pioneer at right with dspr
    dv "Славя..."
    "Я довольно кивнул, хотя в глубине разума завелась мысль, что не слишком ли грубо я поступил?"
    show sl normal pioneer with dspr
    "Славя встала, и хотя она старалась не подавать виду, было ясно, что она сильно расстроена."
    show dv normal pioneer at right with dspr
    "Могло произойти всё что угодно, истерика или что ещё похуже, но дверь столовой распахнулась{w}, и вошёл полуночный гость, визит который не нёс ничего хорошего."
    stop music fadeout 3
    play sound sfx_open_door_2
    show pi normal1 at left with dissolve
    play music pioneer_theme fadein 3
    pi "Что пионеры, чаи гоняем?" 
    sh "Ты что тут забыл?"
    "Я просто был шокирован его появлением." 
    show sl angry pioneer with dspr
    sl "А, явился не запылился."
    "Сказала славя и попыталась выйти из здания, но пионер преградил ей путь."
    "Он посмотрел на Алису, и с довольной физиономией сказал."
    pi "О, а ты быстро оклемалась! Готова ко второму заходу?"
    show pi smile at left with dissolve
    "Та, спокойно встала и медленно подошла к нему. Он улыбнулся и схватил её за талию."
    show sl scared pioneer with dspr
    stop music fadeout 3
    "Я просто кипел от ярости!{w} Он всё портит!{w} Но больнее было другое — реакция девушек на него.{w} Словно мотыльки на огонь слетелись."
    play music good_rage fadein 3
    "Но произошедшее следом ещё больше меня удивило."
    show dv smile pioneer at right with dspr
    dv "Даже не думай."
    show dv normal pioneer at right with dspr
    "Спокойно сказала Алиса и...{w} Выплеснула горячий чай прямо ему в лицо!"
    play sound sfx_water_splash
    show pi rage at left with dissolve
    pi "Ай, чтоб тебя!!" 
    "Запищал тот."
    show dv laugh pioneer at right with dspr
    dv "Он весь твой." 
    "Сказала рыжая."
    show sl angry pioneer with dspr
    "И Славя, до этого времени тихо стоявшая в стороне, взяла да и выставила его на порог, и дала пинка, для ускорения.{w} Послышались глухие удары тела о бетон."
    play sound sfx_lena_hits_alisa
    hide pi rage at left with dissolve
    with hpunch
    show sl laugh pioneer with dspr
    sl "Чтобы мы тебя здесь не видели!"
    show dv grin pioneer at right with dspr
    dv "Проваливай отсюда!"
    stop music fadeout 3
    "Со смехом прокричали девчонки ему в след."
    sh "Ну вы даёте."
    show sl normal pioneer with dspr
    play music alex_mind fadein 3
    sl "Давайте вернёмся к чаю.{w} Думаю тебе стоит нам многое рассказать."
    jump travel_back
    
label no_trust:
    play music alex_mind fadein 3
    "Так, это провокация!{w} Не поддаваться!"
    sh "Вы... Все для меня... Ценны и дороги. Я не могу сделать выбор."
    show sl normal pioneer with dspr
    sl "А ты думаешь, что Семён сможет?"
    show dv laugh pioneer at right with dspr
    "Алиса рассмеялась."
    dv "Ты посмотри Славь, как он покраснел!{w} Стесняшка ты наш."
    sh "Хватит, мы тут о важных вещах говорим, а вы цирк устраиваете."
    show dv grin pioneer at right with dspr
    dv "Хорошо-хорошо, как скажешь."
    "Не унималась рыжая."
    show sl shy pioneer with dspr
    sl "Ну, рассказывай."
    jump travel_back

label travel_back:
    $ renpy.pause(5)
    "Прошло некоторое время, пока я рассказывал девушкам что знаю.{w} О «Совятах», об этом пионере, о 410-м."
    sh " ...и, в заключение, давайте адресами обменяемся? Чтобы проверить, как всё прошло?"
    show sl smile pioneer with dspr
    sl "Давайте"
    show dv normal pioneer at right with dspr
    dv "Почему бы и нет?"
    "Хех, забавно.{w} Живём почти по соседству.{w} Даже уверен, что встречал их на улице, но просто прошёл мимо, даже не подумав познакомиться или просто улыбнуться."
    "Они, может быть, даже и остановились бы поговорить со мной.{w} Да уж."
    sh "Вот, возьмите по листку. Думаю, он останется при вас в любом случае." 
    show dv surprise pioneer at right with dspr
    dv "Хм, ну спасибо, хотя я запомнила." 
    show sl surprise pioneer with dspr
    sl "Саш, а чего ты свой адрес не скажешь?" 
    show dv normal pioneer at right with dspr
    sh "А зачем?"
    show dv surprise pioneer at right with dspr
    dv "Что за глупые вопросы?"
    "Девушки с удивлением посмотрели на меня. Надо бы ответить, раз уж на то пошло."
    menu:
        "Сказать настоящий адрес":
            $ sl_love += 1
            $ dv_happy += 1
            jump bsck_jump
        "Соврать":
             $ uv_trust = 0
             jump bsck_jump

label bsck_jump:
    sh "Записали? Тогда предлагаю расходиться."
    show dv normal pioneer at right with dspr
    dv "Ты о Славе подумал?"
    show sl normal pioneer with dspr
    sh "Ого, Алис, а ты быстро сориентировалась."
    show dv grin pioneer at right with dspr
    dv "Тут долго думать не надо — она тут, и ей утром отдуваться."
    "Так, а это уже меня пугает!{w} Не хочу я с Алиской вдвоём ночевать."
    sh "Надо проводить её."
    show sl scared pioneer with dspr
    sl "Ты думаешь, тот вернётся?"
    sh "Всякое может быть."
    show sl normal pioneer with dspr
    "Соврал я."
    stop music fadeout 3
    scene ext_square_night
    show dv normal pioneer at right
    show sl normal pioneer
    with dissolve
    play music music_list["waltz_of_doubts"] fadein 3 
    "Всю дорогу к домику я молчал, а девчонки активно переговаривались. Быстро же они сдружились, идут и обсуждают происходящее."
    "Видно, что обе волнуются, но находят силы друг в друге, поэтому и держатся рядом и так общительны.{w} Только на меня всё меньше внимания, хотя я всё это и затеял."
    scene ext_clubs_night
    show dv normal pioneer at right
    show sl normal pioneer
    with dissolve
    sl "Дальше сама дойду. Я бы вас пригласила, но..."
    sh "Не стоит." 
    show sl shy pioneer with dspr
    sl "Конечно глупо, но мы ещё встретимся?" 
    show dv smile pioneer at right with dspr
    dv "Обязательно встретимся!"        
    sh "Зачем устраивать такие прощания? Вы вполне можете, кхм, ходить друг к другу в гости."
    show dv normal pioneer at right with dspr
    dv "Угу, на чай." 
    show dv laugh pioneer at right 
    show sl laugh pioneer 
    with dspr
    "Девушки рассмеялись."
    sh "Давай, не прощаюсь." 
    "И с этими словами я пошёл в сторону ворот."
    scene ext_houses_sunset
    show dv normal pioneer
    with dissolve
    dv "Э, а я?"       
    sh "Не отставай."
    "Начинало рассветать, и первые лучи солнца робко пробивались через отступающую тьму."
    dv "Ну, какие планы Саш?"
    sh "Идём "
    "Махнул я рукой."
    scene ext_camp_entrance_night
    show dv normal pioneer
    with dissolve
    "Мы вышли к входу в «Совёнок». Ничего не изменилось{w}, да и могло ли?"
    scene ext_no_bus_sunset
    show dv surprise pioneer
    with dissolve
    dv "Теперь и нам пора. Ты знаешь что делать?"
    sh "Да, не волнуйся."
    show dv smile pioneer with dspr
    dv "Тебе легко говорить." 
    "Улыбнулась рыжая."
    show blink
    "Мы закрыли глаза, и я положил руку ей на плечо.{w} Она глубоко вздохнула, уж не загрустила ли? {w}В голове появились образы знакомых мест, вроде бы даже запахи и звуки."
    dv "Пока."
    "Раздался голос Алисы."
    "Я убрал руку, и постояв в тишине и в темноте пару секунд, открыл глаза."
    scene ext_no_bus_sunset
    show unblink
    "Её нет. Чтож, одну спровадил. Теперь себя."
    "Это оказалось заметно труднее. Мне показалось, что не хватает силы, а точнее импульса, рывка. Неприятное чувство страха стало прокрадываться в меня, и это сильно сбивало с мысли."
    "Мне нечего вспомнить о себе или Семёне. Нечего ощутить."
    show blink
    stop music fadeout 3
    scene ext_no_bus_sunset
    "В отчаянии я вновь открыл глаза, хотя лучше бы не делал этого."
    play music pioneer_theme fadein 3
    show unblink
    
    "Пионер стоял прямо передо мной, и смотрел на меня с... Одобрением?{w} Благодарностью?"
    show pi smile with dissolve
    pi "Неплохо!"
    "Сказал он и подойдя ко мне, щёлкнул пальцами прямо перед моим лицом. Рефлекторно я отпрянул и моргнул."
    show blink
    scene ext_square_day
    stop music fadeout 3
    $ persistent.sprite_time = 'day'
    $ day_time()
    show unblink
    play music music_list["my_daily_life"] fadein 3
    "Открыв глаза, я увидел, что неведомым способом я очутился на площади, на стремянке."
    show mt angry pioneer panama with dissolve
    mt "Саш, готово?"   
    sh "Что? Где? А, не, ещё нет."
    mt "Ну так давай быстрее! Говорила же, что важное задание, а вы «Ольга Дмитриевна, всё сделаем, моргнуть не успеете»"
    "Я быстро осмотрел то, над чем работало моё тело. Громкоговоритель, наверное, для танцев готовится. А меня с Электроником подписали ремонт производить."
    "Напаять бы вам сейчас на короткое... Но нет. Потерплю."
    sh "Всё, закончил. Будет работать как часы."
    show mt grin pioneer panama with dspr
    mt "Молодец, сразу бы так."
    sh "Эл, я пойду в клуб, отнесу инструмент, а ты новеньких найди."
    show el normal pioneer at right with dissolve
    el "Как скажешь."
    scene ext_clubs_day with dissolve
    "Сейчас мне как никогда нужна тишина и спокойствие, ведь столько всего произошло."
    scene int_clubs_male_day with dissolve
    "В клубе я обнаружил свою чашку, наполовину заполненную чаем и целый парад конфет и пряников — не сказать, что это так нужно, но голод — не тётка."
    "Но если судьбой или кем ещё предписано, что «покой нам только снится», значит так тому и быть, поскольку не успел я отхлебнуть целебного отвара, как в помещение ворвался Эл, с ужасом на лице и стал баррикадировать дверь."
    show el scared pioneer at right with dissolve
    sh "Что такое?"
    stop music fadeout 3
    "Я аж поперхнулся."
    play music music_list["that_s_our_madhouse"] fadein 3
    el "АЛИСА!!"
    "Чтож, исчерпывающе. Схватив пару стульев я рывком оказался у двери."
    sh "Что ты на этот раз натворил?"
    el "Назвал её..."
    play sound sfx_slam_door_campus
    "Но удар в дверь прервал его."
    dv "Открывай!"
    "По голосу стало понятно, что Эла не ждёт ничего хорошего, если последовать команде."
    "Пионерка продолжала ломиться в помещение еще пару минут, потом осада прекратилась."
    show el grin pioneer at right with dspr
    "Эл посмотрел на меня, и в его взгляде читалось «Неужто этот кошмар кончился?»."
    "Я же перевёл свой взгляд на открытое окно."
    "В которое уже влезала взбешённая Алиска."
    play sound sfx_scary_sting
    show dv rage pioneer with dissolve
    sh "Умная девочка."
    show el scared pioneer at right with dspr
    "Только и успел сказать я, после его был откинут Элом в сторону."
    hide el scared pioneer at right with dissolve
    "Тот просто просочился сквозь дверь в попытке бегства, но Алиса уже набрала темп."
    hide dv rage pioneer with dissolve
    "Далеко ему не уйти, жаль конечно."
    "Ну по крайней мере тишина мне обеспечена."
    scene ext_clubs_day with dissolve
    "Я выглянул на улицу {w}- «сладкая парочка» скрывалась из виду, постоянно набирая скорость. {w}Беги Электроник, беги.{w} Хотя это бесполезно."
    "Вся эта кутерьма порядком утомила меня, поскорей бы отбой!"
    play sound sfx_dinner_horn_processed 
    "Хотя на данный момент и пообедать весьма не плохо."
    "Особо не торопясь, я выдвинулся к столовой, попутно посматривая по сторонам, надеясь найти растерзанного Электроника.{w} Но его тела, увы, нигде не было видно."
    scene ext_dining_hall_away_day with dissolve
    "Вот и столовая показалась за поворотом."
    "И всё же хорошо, что вселенная наградила меня неплохой реакцией."
    show us laugh pioneer with moveinright 
    hide us laugh pioneer with dissolve
    "Буквально в миллиметрах от меня пронеслась Улька с довольнейшим лицом. Началось." 
    "И он побежит не в ту сторону. Так и есть. Хоть в чём — то постоянство."
    scene int_dining_hall_people_day
    play ambience ambience_dining_hall_full
    "Обед прошёл спокойно, что даже странно. Я сидел в стороне ото всех, тихо и спокойно восполняя свои силы."
    "Всё хорошо, только внутреннее напряжение от предстоящей встречи никак не даёт мне покоя."
    stop ambience 
    "Закончив обед, я поспешил обратно в клуб."
    scene ext_clubs_day with dissolve
    "Хотя внеочередные задания  мне больше не страшны, лишний раз находиться на виду у вожатой мне не хотелось. Сегодня столько всего произошло, а эти скачки времени, от заката до рассвета, совсем вымотали меня."
    scene int_clubs_male_day with dissolve
    "Оказавшись в клубе, я со спокойной душой запер дверь, поскольку у Эла есть свои ключи, и улёгся в кладовке подремать."
    scene int_clubs_male2_night with dissolve
    "Спать на мешках и ящиках не удобно, но и я не привередливый." 
    "Усталость взяла своё, и засыпая, я надеюсь, что проснусь в этом же помещении."
    stop music fadeout 3
    show blink
    
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene int_aidpost_night
    play music music_list["meet_me_there"] fadein 3 
    show prologue_dream 
    show mt angry pioneer behind prologue_dream 
    show cs normal at right behind prologue_dream 
    with dissolve
    mt "Сколько можно! Я так не могу!" 
    cs "Это для их же блага! Как ты не понимаешь!" 
    show mt rage pioneer behind prologue_dream with dspr
    mt "Как ты можешь быть такой бесчувственной? Это же их первая любовь! Она не забывается!"
    show cs_close at right behind prologue_dream with dspr
    cs "Я знаю. Поверь. Самой противно. Но нет другого выхода. Мы должны найти выход!" 
    show mt scared pioneer behind prologue_dream with dspr
    mt "Такой ценой? "
    hide cs_close at right behind prologue_dream with dspr
    show cs normal at right behind prologue_dream with dspr
    cs "Большей, если потребуется!"
    play sound sfx_face_slap
    with hpunch
    "Дмитриевна отвесила Виоле хорошую пощёчину."
    show mt rage pioneer behind prologue_dream with dspr
    mt "Ты себя послушай Виола! ЧТО ты несёшь?"
    show cs_close at right behind prologue_dream with dspr
    cs "А ты хочешь стать такой же как он?"
    mt "Нет. Никогда, слышишь!"
    cs "Если мы что-либо не придумаем, нас постигнет та же судьба."
    hide cs_close at right behind prologue_dream with dspr
    show cs normal at right behind prologue_dream with dspr
    mt "Ты предлагаешь страшные вещи."
    show mt normal pioneer behind prologue_dream with dspr
    cs "Оль, я чувствую тоже самое. Каждый из этих пионеров дорог мне.{w} Я, как и ты, люблю их и хочу им счастья и не повторения наших ошибок." 
    show cs_close at right behind prologue_dream with dspr
    cs "Но счастье, полученное без лишений и борьбы, не чувствуется таким важным. {w}Им будет казаться, что так и должно, просто и без объяснений."
    show mt scared pioneer behind prologue_dream with dspr
    mt "Посмотри на него, и ты увидишь, к чему привели лишения и борьба."
    hide cs_close at right behind prologue_dream with dspr
    show cs normal at right behind prologue_dream with dspr
    cs "Мне нечего сказать тебе."
    "Они замолчали. Какой интересный сон."
    show mt sad pioneer behind prologue_dream with dspr
    mt "Виола, ради нашего спасения я готова на всё, но всему есть предел."
    cs "Ты подожди, вот он её бросит, проблем не оберёшся."
    mt "Я верю в него"
    show cs normal at right behind prologue_dream with dspr
    cs "А я нет."
    mt "Спорить глупо, ни к чему не придём."
    cs "Как знаешь."
    hide mt sad pioneer behind prologue_dream with dissolve
    "Дмитриевна вышла из кабинета. Хм, всё интереснее и интереснее.{w} Богатая у меня фантазия однако."
    "Виола молча смотрела ей в след."
    cs "Дура." 
    show cs_close at right behind prologue_dream with dspr
    "Женщину трудно понять, порой кажется, что невозможно, но тут всё ясно: ей тяжело и трудно." 
    "Она обхватила голову и молча смотрела в пол."
    stop music fadeout 3
    "Что же дальше? Я хочу продолжения?"
    cs "Всё видел? Запомнил?"
    play music alex_theme fadein 3
    "Что?"
    cs "Да-да, я к тебе обращаюсь. Знаешь, если ты можешь спасти человека, но не делаешь этого, то ты преступник?"
    "Я сплю?"
    cs "Она мне не верит, надеется на лучшее. А я готовлюсь к худшему. Ты нужен."
    sh "Да? А нужны ли вы мне?" 
    hide cs_close at right behind prologue_dream with dspr
    show cs smile behind prologue_dream with dspr
    "Виола улыбнулась своей самой томной улыбкой из всех ей доступных."
    cs "Порой судьба вносит свои коррективы в наши планы.{w} Но иногда судьбе «надо» помочь."
    sh "К чему ты клонишь?"
    cs "Просто так."
    with hpunch
    show blink
    "Она чмокнула воздух, и мне словно вытолкнуло из этого кабинета, мира, реальности, сна."
    scene int_clubs_male2_night
    
    $ persistent.sprite_time = 'sunset'
    $ day_time()
    show unblink
    "Открыв глаза, я увидел, что всё также лежу на тюфяках и коробках."
    "Приснится же такое.{w} Я попытался убедить сам себя в том, что это просто сон, но внутри чувствовал, что это мне не почудилось.{w} Новая сила пытается влезть в мой план спасения." 
    "Но это мы ещё посмотрим."
    "Для успокоения я вышел подышать свежим воздухом, с удивлением обнаружив, что вечер уже в самом разгаре. Так можно и ужин пропустить."
    scene int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_full
    "Главного героя этой адской пьесы в столовой не обнаружилось, что не может не радовать."
    show el scared pioneer with moveinright 
    hide el scared pioneer with dissolve
    "Даже Эл, украдкой просочился поесть, надеясь не попасться Алисе на глаза.{w} Чтож, удачи ему в этом, безусловно, важном и интересном деле, учитывая, что она тут."
    "Но аппетит и восприятие мира мне всё ещё портил тот сон, и раздавшийся голос я и не признал сразу."
    voice "Свободно?"
    stop music fadeout 3
    menu:
        "Лена":
            jump d4_lena_din
        
        "Уля":
            $ us_happy += 1
            jump d4_ulia_din
            
label d4_lena_din:
    play music music_list["lets_be_friends"] fadein 3 
    
    $ persistent.sprite_time = 'day'
    
    "Той, кто вернул меня из кошмара моих мыслей, оказалась кроткая Лена."
    show un normal pioneer with dissolve
    sh "Ой, прости Лен, не признал. Конечно свободно."
    "Она села за стол и начала неспешно ужинать"
    sh "Ну как тебе новенький?" 
    show un smile pioneer with dspr
    un "Ну... Он такой... Странный"
    sh "О чём ты?{w} Эл сказал, что он славный парень, хоть и тихий. Как раз для тебя."
    show un shy pioneer with dspr
    "Лена покраснела, но отнекиваться не стала."
    un "Складывается впечатление, что ты всех тут переженить хочешь, особенно меня."
    show un smile2 pioneer with dspr
    "Она улыбнулась."
    sh "Да? "
    un "Точно."
    show un normal pioneer with dspr
    "И мы замолчали. Пару секунд спустя я решился нарушить неловкую тишину."
    sh "Знаешь,  мельком видел его..."
    "Стал подходить я из далека"
    sh "Мне он показался .. Грустным. Или что-то похожее."
    show un sad pioneer with dspr
    un "И я это почувствовала. Какой-то он отрешённый."
    sh "Одному быть совсем не весело."
    un "Ты прав."
    show un smile pioneer with dspr
    "Она слегка улыбнулась."
    un "Кстати, Саш, спасибо тебе за книгу. Всё хотела поблагодарить, но не получалось."
    sh "Да без проблем. Ты наверно уже всё прочитала?"
    show un laugh pioneer with dspr
    un "Что ты! Нет. Я до конца смены растяну."
    sh "Когда же ты читаешь? Вроде всегда при деле, со всеми."
    un "По вечерам, в домике."
    sh "В такую погоду? Духота же!"
    show un surprise pioneer with dspr
    "Она удивилась."
    show un normal pioneer with dspr
    un "А мне в самый раз. Да и спокойнее."
    "Она посмотрела на Ульянку."
    sh "Знаешь, мне нравиться читать книги вечером.{w} Все эти запахи{w}, шорохи и ощущения навивают воспоминания о детстве.{w} Может тебе стоит попробовать?"
    show un shy pioneer with dspr
    un "Звучит интересно, но с книгой я нахожу уединение сама с собой."
    menu:
        "Настоять":
            $ un_love += 1
            jump book_air
            
        "Оступить":
            $ uv_trust += 1
            jump book_home


label book_air:
    sh "Не попробуешь — не узнаешь. Да и мало кто потревожит тебя, видя то ты занята.{w} Даже у Ульки ума хватит."
    show un smile pioneer with dspr
    "Лена чуть видно улыбнулась, и встала из-за стола."
    un "Спасибо, Саш. Может я так и сделаю."
    sh "Думаю, ты не пожалеешь."
    "Лена пошла к выходу, но на пороге остановилась."
    show un smile3 pioneer with dspr
    un "Ты в этом уверен?"
    sh "Да."
    "И она скрылась из виду."
    stop music fadeout 3
    jump uv_hide
    
label book_home:
    "Вот почему они не прислушиваются ко мне? Я всего лишь хочу им добра."
    sh "Ну, моё дело предложить, твоё — отказаться."
    show un surprise pioneer with dspr
    "Это её смутило"
    un "Я не отказываюсь, просто никогда такого не делала."
    sh "А я не навязываю."
    show un angry2 pioneer with dspr
    un "Знаешь, ты порой тоже странный."
    "Да.{w} Бываю.{w} Вы не можете меня понять.{w} Никто не может.{w} Даже среди живых людей я увствую себя чужим. Я всего лишь хочу свободы."
    "Лена не стала дожидаться моего ответа, и пошла на выход. Я обернулся посмотреть, не обернётся ли она, и был приятно удивлён, что она это сделала. "
    show un smile pioneer with dspr
    "Еле заметно улыбнувшись, она ушла."
    stop music fadeout 3
    jump uv_hide


label d4_ulia_din:
    play music music_list["i_want_to_play"] fadein 3 
    $ persistent.sprite_time = 'day'
    
    sh "А, это ты Уль. Набегалась?"
    show us grin pioneer with dspr
    us "Ага. А он не так плох, хотя до меня далеко."
    sh "Вот скажи, надо было тебе Лену пугать, а?"
    show us angry pioneer with dspr
    us "Ну я же извинилась! "
    sh "А она и не обиделась. Но всё же, будь повзрослее а?"
    show us laugh2 pioneer with dspr
    us "Вот вырасту — буду."
    show us normal pioneer with dspr
    sh "Смотри Улька, когда-нибудь тебя тоже разыграют, смеяться не будешь."
    us "Ну это ты придумал! Я тут самая хитрая и умная."
    show us laugh pioneer with dspr
    "Она разулыбалась во все свои, пока, 32 зуба."
    sh "Самоуверенная. А может новенький тебя подловит?"
    show us laugh2 pioneer with dspr
    us "Он? Саш, ты что?"
    "Смейся-смейся."
    stop music fadeout 3
    jump uv_hide
    
label uv_hide:
    scene ext_dining_hall_away_sunset with dissolve
    play music music_list["lightness"] fadein 3 
    $ persistent.sprite_time = 'sunset'
    $ day_time()
    
    stop ambience
    "Выйдя из столовой, я со спокойной душой отправился в свой домик." 
    "Обеденный сон ни сколько не восстановил мои силы, и мне ужасно хотелось прилечь в свою уютную кровать. Но вновь, как это обычно бывает, у вселенной другие планы."
    scene ext_houses_sunset with dissolve
    "На подходе к площади меня окликнула Дмитриевна."
    show mt normal pioneer panama with dissolve
    mt "Саш, надо проверить радио и громкоговорители. Почему-то они барахлят, даже после вашего «качественного» ремонта."
    show mt grin pioneer panama with dspr
    "Она намекает на мой непрофессионализм? Как некультурно!"
    sh "Ну хорошо, Ольга Дмитриевна, я всё проверю."
    mt "Вот тебе ключи от административного корпуса. Думаю там что-то сломалось."
    "Задание надо выполнять, а не обсуждать."
    scene ext_clubs_day with dissolve
    "Я пошёл в клуб за необходимым инструментом, с надеждой, что Эл не забаррикадировался там снова."
    scene int_clubs_male_sunset with dissolve
    "Этого не случилось, и я начал собирать всё необходимое. Коего, к удивлению, оказалось крайне мало. Куда всё делось?"
    "Я заглянул в нашу кладовку."
    scene int_clubs_male2_night_nolight with dissolve
    "Да, темно, хоть глаза выколи. Я потянулся включить свет, но света не было."
    "Что тут происходит?"
    stop music fadeout 3
    show monster_light 
    play sound sfx_scary_sting
    play music music_list["sunny_day"] fadein 3
    "Только 2 жёлтых фонаря смотрели на меня из темноты." 
    "Послышалось шипение, а может что и пострашнее. Жуть какая."
    voice "Что, испугался?"
    "Раздался девичий смех" 
    sh "Не знаю, кто или что ты, но ТАК делать нельзя."
    "Выдал я, когда смог снова начать дышать и говорить."
    voice "Извини."
    sh "Зачем пришла? Если вдруг что, то путешествий на сегодня мне хватит!"
    voice "Да я не по этому. Ты всё правильно сделал, и я пришла поблагодарить тебя."
    sh "Странное у тебя чувство благодарности. Там и заикой остаться можно."
    voice "Ну хватит тебе. Я извинилась."
    sh "Ты только за этим пришла?"
    voice "Да. Хотя мне и отблагодарить тебя нечем, у меня вообще мало что есть, кроме запасов."
    sh "Мне твои запасы не нужны. Ты меня другим отблагодаришь."
    voice "Чем же?"
    "Видимо она удивилась"
    sh "Я видел сон. Но это не сон, я даже не знаю что это было.{w} Там были Ольга и Виола, но они вели себя очень странно.{w} А последняя со мной даже говорила, а я ей отвечал. Что это? Что происходит?"
    "Моя полуночная гостья задумалась, и ответила через несколько секунд."
    voice "Странно это слышать. Я не о чём таком не знаю."
    sh "Не ври мне. Знаешь про девушек, про пионеров, про меня, а тут ты вдруг и не знаешь."
    voice "Верь мне. Я честно нечего про это не знаю."
    "Она знает, но не говорит. Она что-то скрывает, другого объяснения нет."
    sh "Всё? Свободна."
    "Я вышел в комнату, и стал ждать, когда она уберётся восвояси. Свет я специально не включал, да и был ли смысл? Наверняка все лампы побила или повыкручивала."
    "Вскоре она показалась их кладовки, и направилась в сторону выхода." 
    voice "Ты становишся таким же."
    sh "Нет. Мне нужны ответы, а ты мне врёшь. Как я ещё должен реагировать?"
    voice "Терпение, Саш." 
    sh "Вот просто нельзя сказать всю правду и назваться. Зачем все эти тайны и загадки? Что тут меня может удивить? Что ты не человек? Это я и так понял." 
    voice "Хорошо, зажги свет. Та штука, которая светиться, лежит на столе."
    "Лампочка действительно оказалась на столе в груде барахла, и ввинтив я увидел её, мою « учительницу»."
    stop music fadeout 3
    hide monster_light 
    scene int_clubs_male2_night 
    show uv normal pioneer 
    with dissolve
    sh "Ну, я так себе примерно всё и представлял."
    play music painful_truth fadein 3
    dreamgirl "Вот видишь, я больше ничего от тебя не скрываю."
    sh "Как хоть звать тебя?"
    dreamgirl "А у меня нет имени." 
    sh "Нельзя без имени!"
    show uv upset pioneer with dspr
    "Она загрустила"
    dreamgirl "Ну вот так."
    sh "А я сейчас тебе его придумаю." 
    "Хм, нужно простое, но красивое. Как на зло ничего не приходит на ум."
    dreamgirl "Всё думаешь?"
    show uv grin pioneer with dspr
    "Улыбнулась она."
    "Странно. От неё исходит теплота и забота, которое я никогда не испытывал. Даже дома." 
    "ДОМ! Да, я придумал. ЮВАО. Нет, не то. Юля. Да, точно Юля."
    sh "Как тебе «Юля»?"
    voice "Ю.Л.Я. Красиво. Мне нравится."
    sh "Рад за тебя. Что теперь будешь делать?"
    uv "К себе пойду."
    "Почему-то мне не хотелось просто так её отпускать. Она раскрылась передо мной, а я её вроде как выгоняю на улицу.  Нужно что-то сделать!"
    menu:
        "Оставить ночевать":
             $ uv_trust += 1
             jump uv_in   
                
    
        
        "Прогнать":
            $ uv_trust -= 1
            jump uv_out

                
        "Проводить":
            $ sl_love += 1
            $ el_happy += 1
            $ un_love += 1
            $ dv_happy += 1
            $ us_happy += 1
            $ dv_trust += 1
            $ uv_trust += 1
            jump uv_love
        
            
 
label uv_love:
    sh "Знаешь, я тебя провожу. Нам есть о чём поговорить."
    show uv surprise pioneer with dspr
    uv "А если тебя увидят?" 
    sh "Нас не увидят — все заняты."
    scene ext_clubs_night with dissolve
    "Выйдя и заперев клуб, мы двинулись в сторону леса."
    scene ext_clubs_night
    
    $ persistent.sprite_time = 'night'
    $ day_time()
    show uv grin pioneer
    with dissolve
    sh "Скажи, кто ты такая? Откуда ты?"
    uv "Я тут всё время. Просто была тут, и всё. Живу, наблюдаю, припасы делаю."
    sh "Припасы?"
    show uv laugh pioneer with dspr
    uv "Да. Без них никак."
    sh "А чем ты ещё занимаешся?"
    uv "Наблюдаю за всеми вами. Вы забавные, честное слово."
    show uv grin pioneer with dspr
    sh "А ты не боишся, что тебя схватят?"
    show uv normal pioneer with dspr
    uv "Не, я осторожная и внимательная. Вы слишком громко ходите, я из далека ещё слышу и прячусь."
    sh "Но по лагерю ходят слухи о тебе, мол видели, как что-то у столовой копошилось."
    show uv smile pioneer with dspr
    "Она улыбнулась."
    uv "Да? Как интересно." 
    sh "Тебе стоит быть осторожнее, нельзя чтобы слухи имели реальное подтверждение. Будь осмотрительнее."
    "Она ничего не ответила на это, но посмотрела на меня своими яркими, янтарного цвета, глазами, и сказала:"
    show uv sad pioneer with dspr
    uv "Извини меня ещё раз."
    sh "За что? Ты ничего плохого не сделала же!"
    show uv upset pioneer with dspr
    uv "За то, что сравнила тебя с ним. Ты добрый и чуткий, хотя и не признаешся."
    "Я покраснел, как мальчишка. Саша, возьми себя в руки! Незнакомая кошко-девочка сделала тебе комплимент, и вот ты весь уже растаял!"
    sh "Спасибо тебе."
    "Только и смог выдавить я."
    show uv laugh pioneer with dspr
    "Она засмеялась, и этот искренний смех напомнил мне нечто давно забытое. Словно привет из далёкого детства, когда всё было искренне и честно. Когда смеялся от щекотки родителей."  
    "Когда я действительно жил, а не существовал."
    scene ext_camp_entrance_night
    show uv normal pioneer 
    with dissolve
    sh "Ну вот и ворота."
    "Сказал я."
    show uv laugh pioneer with dspr
    uv "Тебе пора обратно, а не то опять искать тебя будут." 
    sh "Не опять, а снова."
    "Улыбнулся я."
    uv "Тебе виднее."
    show uv grin pioneer with dspr
    sh "Скажи, а мы ещё встретимся? Вот так, по дружески?"
    show uv shocked pioneer with dspr
    uv "Меня ещё ни разу другом не называли."
    show uv smile pioneer with dspr
    "Она вновь улыбнулась."
    uv "Конечно, и не раз. Я же обещала помогать, вот и помогаю."
    sh "Хорошо... Тогда до встречи?"
    uv "Да."
    hide uv smile pioneer with dissolve
    "И она убежала в лес. Скоро ли я её увижу? Ощущение, что скоро, очень скоро."
    "И с этой позитивной мыслью я пошёл в клуб"
    scene ext_clubs_night with dissolve
    "Взял нужные инструменты и пошёл проверять, что случилось с аппаратурой."
    "Оказалось, ничего серьёзного, и ремонт я закончил быстро."
    scene ext_square_night with dissolve
    "Задерживаться на улице смысла больше не было, и я пошёл спать."
    jump day_5
    return

     
label uv_in:
    sh "А где ты живешь? Неужели в лесу?"
    show uv normal pioneer with dspr
    uv "Да, там."
    sh "И спишь прямо под открытым небом?!"
    show uv smile pioneer with dspr
    uv "У меня есть этот, как его называют ... А, гамак."
    sh "Ты его украла?"
    uv "Нет. Сделала из старых мешков из-под сахара. Повесила на дереве и там сплю."
    sh "А ешь что?"
    uv "Всё, что попадается."
    show uv rage pioneer with dspr
    "Она зловеще посмотрела на меня, да так, что  мурашки побежали по коже." 
    "Видя, что я напрягся, Юля снова залилась смехом."
    show uv grin pioneer with dspr
    uv "Ты что, поверил? В лесу много чего есть поесть."
    sh "Слушай, у меня к тебе столько вопросов. Давай ты тут переночуешь, заодно я тебя нормальной едой накормлю."
    "По быстрому открыв пару мешков и ящиков, я приготовил простой ужин на 2 персоны, благо и чайник, и плитка у нас в клубе есть."
    "Юля с опаской, но все же принялась за еду, да и мне в кампании есть приятнее."
    sh "Вот всё хочу тебя спросить: почему ты так долго скрывалась от меня?"
    show uv guilty pioneer with dspr
    uv "Я должна была проверить, что ты на стороне..."
    sh "Твоей?"
    uv "Семёна."
    sh "Теперь ты убедилась?"
    uv "Почти." 
    sh "Неужели у тебя ещё остались сомнения?"
    uv "Немного."
    show uv normal pioneer with dspr
    "Юля немного промедлила. Оно и понятно -  моя реакция на её появление в библиотеке была, мягко говоря, агрессивная."
    uv "Знаешь Саш, я никогда ещё не говорила так долго с человеком, и некоторые вещи я могу сказать неправильно."
    show uv smile pioneer with dspr
    uv "Я не знаю что ты сказал тем девушкам, но они послушали тебя, и я ощутила, как тот пионер буквально взвыл. Наверно они прямо сейчас пробуют прийти сюда."
    show uv sad pioneer with dspr
    uv "Может даже и получится. Но Саш, я даже сейчас чувствую, как ты нервничаешь и злишся, причём на себя. Но это ни к чему не приведёт." 
    sh "Я абсолютно спокоен. Тебе это кажется."
    "А может это кажется мне? Может я имею слишком завышенные ожидания от моей жизни?" 
    "Тогда почему я? Почему?"
    show uv normal pioneer with dspr
    uv "Саш, не стоит тебе так уж грустить. Ты, как это вы говорили, за-мы-ка-ешься в себе. А иногда помощь просто на вытянутой руке."
    sh "О чём ты?"
    uv "Скажу тебе одну вещь — Сёмен многогранен и многолик, как и все мы. Поговори с ним, он многое расскажет."
    "Юля встала из-за стола и пошла в кладовку." 
    
    scene int_clubs_male2_night
    $ persistent.sprite_time = 'day'
   
    show uv grin pioneer
    with dissolve
    uv "У вас тут тепло. И ты тоже запасы делаешь! Здорово! Потом поменяемся?"
    sh "Всё моё — твоё."
    "Сказал я, думая над тем, что мне сказала эта девушка."
    sh "Если хочешь, можешь переночевать тут. Я тебя запру, а окна оставлю открытыми." 
    show uv surprise2 pioneer with dspr
    "Юля обрадовалась моему предложению, и вальяжно улеглась на мешках."
    sh "Ладно, отдыхай. Я завтра рано встану, если что, разбужу тебя."
    show uv grin pioneer with dspr
    uv "Спасибо, но не стоит. Ведь кроме вас никто сюда не ходит?"
    sh "Да, ключи только у нас."
    uv "Вот и хорошо."
    show uv laugh pioneer with dspr
    "Она зевнула."
    uv "Сегодня столько всего произошло. Ты очень устал."
    sh "Ты просто видишь меня насквозь. Спокойной ночи."
    scene ext_clubs_night with dissolve
    "Я открыл окна и, выйдя на улицу, запер дверь." 
    "В одном она точно права — произошло сегодня много. Слишком много."
    "И я пошёл в свой домик."
    jump day_5
    return

label uv_out:
    "Оставить нежности. На кону слишком много, чтобы поддаться эмоциям."
    sh "Знаешь, тебе опасно оставаться тут. Могут увидеть, тогда проблем не оберёмся."
    show uv smile pioneer with dissolve
    uv "Ты прав."
    sh "Так что не будем задерживаться."
    scene ext_clubs_night
    
    $ persistent.sprite_time = 'night'
    $ day_time()
    show uv grin pioneer
    with dissolve
    "Мы вышли на улицу, и моя попутчица посмотрела  на меня."
    uv "Ну, я побежала."
    sh "Постой, а как тебя найти? Что если мне понадобится твоя помощь?"
    show uv laugh pioneer with dspr
    uv "Не волнуйся, я сама тебя найду." 
    sh "Ладно. Если тебе от меня что-либо потребуется, ты знаешь где меня искать. Дай знать, если что."
    uv "Конечно. Спасибо и до встречи."
    hide uv laugh pioneer with dissolve
    "И она побежала в лес. Быстро, что я почти сразу потерял её из виду."
    "Вот и славно — больше приключений сегодня не будет." 
    "Сегодня произошло слишком много, чтобы я ещё утруждал себя всяким ремонтом или другими вещами."
    jump day_5
    
    label day_5:
    $ backdrop = "2й день"
    $ new_chapter(2, u"2й день")
    scene alex home day
    show prologue_dream with dissolve
    play music music_list["meet_me_there"] fadein 3
    
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()    
    show un_night behind prologue_dream with dissolve
    "Эти зелёные глаза снились мне всю ночь, манили к себе, и я не мог перестать в них смотреть. Её слёзы огнём обжигали мою душу, и я хотел бросить весь мир к чёрту, лишь бы утешить её."
    "Что на меня нашло? Почему такая чувствительность и слабость? Нет, я не забыл, как она поступала, и просто простить её я не могу. Но где те чувства злости и ненависти, которые давали мне силы идти дальше?" 
    "Смотря в её глаза, я сам даю ответ на мой же вопрос — как можно её ненавидеть? Как можно их всех ненавидеть?"
    un "..."
    "Она что-то хочет сказать, но я не слышу."
    sh "..." 
    "Я даже не слышу свой голос. Он у меня есть? Хоть рот есть или нет? Если я хочу ей ответить, то придётся кричать изо всех сил."
    hide un_night with dissolve
    $ renpy.pause(5)
    "Стой! Куда?! Лена!!"
    sh "..."
    play sound sfx_dinner_horn_processed 
    hide prologue_dream with dissolve
    play music music_list["eat_some_trouble"] fadein 3
    "Уже завтрак? Я проспал? Первый раз такое. Да, точно проспал. Вот мне Дмитриевна выскажет... Надо поторопится."
    "Наспех одевшись, я побежал к умывальникам."
    scene ext_washstand_day with dissolve
    "Странное чувство, когда только у тебя проблемы, а у окружающих всё нормально"
    show sl surprise sport at right
    show un surprise sport at left
    with dissolve
    "Я умылся в рекордно короткие сроки, и побежал на завтрак."
    "Ещё немного, и я опоздал бы."
    hide sl surprise sport at right
    hide un surprise sport at left
    with dissolve
    scene ext_dining_hall_near_day 
    show mt normal pioneer panama
    with dissolve
    "На крыльце стояла Дмитриевна, и пристально изучала меня ещё на подходе."
    mt "Ну и где тебя носит? Завтра уже начался."
    sh "Извините Ольга Дмитриевна."
    mt "Ладно, заходи."
    scene int_dining_hall_people_day with dissolve
    play music music_list["afterword"] fadein 3
    play ambience ambience_dining_hall_full 
    "Да уж, не самое хорошее начало дня. Ещё этот сон... Чувствую, что сегодня будет очень весело."
    show sl scared pioneer at right
    show us sad pioneer at left
    with dissolve
    sl "Саш, что с тобой? Тебе плохо?"
    sh "А кому сейчас хорошо?"
    show us grin pioneer at left with dspr
    us "Шутит - значит здоров."
    show sl normal pioneer at right with dspr
    "Я посмотрел на них своим «лучезарным» взглядом, и у девушек явно поубавилось желания вести задушевные беседы."
    "Уля поняв, что ничего толкового не получится, скрылась у раздачи,"
    hide us grin pioneer at left with dissolve
    "Но от Слави так просто не уходят, и мне предстоит продержаться под осадой ещё некоторое время."
    show sl smile pioneer at right with dspr
    sl "Саша, я тут не просто так. Семён, новенький, сегодня заглянет к вам. У нас в отряде мало парней, так что вы проявите дружелюбие, но не затаскивайте его силком в ваш клуб."
    show sl serious pioneer at right with dspr
    "Захочет — вступит. "
    sh "Но нам нужны свежие люди! Новые идеи!"
    "Славя улыбнулась."
    show sl smile pioneer at right with dspr
    sl "Вы и так умные и способные, но увлекаетесь. Так что смотрите, не переборщите."
    stop music fadeout 3
    stop ambience 
    scene ext_houses_day with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 3
    "Закончив подпитывать свой организм, я пошёл в клуб — подготовится к приходу."
    "Мне очень не нравится идея устраивать представление перед ним, с этим клубом и «бегунком». Вообще странно общаться с человеком, которому от тебя ничего не надо, а ты ему что-либо говоришь или объясняешь."
    scene ext_clubs_day with dissolve
    "«Как об стенку горох» - самое точное определение. И наверняка он посчитает меня с Элом эдакими клоунами в этом «лагере любви»."
    "Самое противное — так и есть."
    
    scene int_clubs_male_day with dissolve
    $ persistent.sprite_time = 'day'
    $ day_time()    
    "Да уж, настроение хуже некуда. С этим я и пришёл в клуб. Эл был уже там, неспешно работая над платами. Мой приход не остался незамеченным."
    show el normal pioneer with dissolve
    el "О, Саш, доброе утро. Какие новости?"
    sh "Здравствуй.  Ничего нового — глухо как в танке. А ты чем занят?"
    show el smile pioneer with dspr
    el "Да вот паяю слегка."
    "Я подошёл посмотреть, что он напаял. Работа сделана хорошо, добротно. Если настоящий Электроник также хорош в этом, и если не бросит это увлечение, то он далеко пойдёт, поскольку у него талант."
    "Но опыта мало, о чём я не забыл напомнить."
    sh "Эл, что это? Ты собираешься эти резисторы паять? Да всё сгорит тут же!!"
    show el angry pioneer with dspr
    el "Другого нет!"
    sh "Быть не может. Пойду в кладовке посмотрю."
    scene int_clubs_male2_night
    "Да, Эл оказался прав — ничего толкового тут нет. Наши запчасти подходили к концу, и новых не планировались. Хотя... есть одно место, где стоит поискать."
    "Убежище под старым лагерем."
    play music semion_theme 
    play sound sfx_scary_sting
    "Ухххх, аж мурашки побежали по коже от этой мысли."
    "Но заглянуть туда надо, заодно может и Юлю встречу."
    "Я вышел, и встал как вкопаный."
    scene int_clubs_male_day
    show el normal pioneer at right
    show pioneer normal at left 
    with dissolve
    "Эл болтал с Семёном. На сей раз точно настоящим."
    el "Знакомься, это Шурик, он у нас главный!"
    show el smile pioneer at right with dspr
    me "А вас в клубе этом только двое, я так полагаю?"
    el "Ну, можешь считать, что уже трое."
    "Меня просто свело. Я не могу проронить ни слова! Но играть так играть. Я подошёл и протянул руку для знакомства."
    sh "Добро пожаловать!"
    "И вместо нормального ответа я получил лишь безликое «Угу». Да понял я, что тебе до нас дела нет, но проявить хоть немного уважения можно."
    "…"
    "Я говорю ему выученные фразы, пытаясь изобразить хорошую игру, а он не обращает никакого внимания. Ему это не интересно."
    "Ему вообще ничего не интересно. Только ныть о несовершенстве мира и его несправедливости. По его мнению особенно к нему."
    show sl normal pioneer with dissolve
    "Внезапно появившееся Славя закончила этот фарс."
    show sl serious pioneer with dspr
    "Я поставил свою роспись на листке и с удовольствием смотрел, как они уходят по своим делам."
    hide sl serious pioneer
    hide pioneer normal
    with dissolve
    stop music fadeout 3
    play music alex_theme fadein 3
    el "Да, не получилось его заинтересовать."
    "Печально выдохнул Эл."
    show el upset pioneer with dspr
    sh "Мальчик взрослый, сам поймёт, что ему нужно. Нам, Эл, о наших насущных проблемах думать надо."
    el "Запчасти? Где ты их достанешь?"
    sh "Бомбоубежище."
    "Эл стал белый, словно чистый лист."
    show el scared pioneer with dspr
    el "Ты что? Нам нельзя туда! Дмитриевна нас до конца смены картошку чистить заставит, если узнает, что мы в старый лагерь пошли."
    sh "А мы не пойдём."
    el "Не понял..."
    show el shocked pioneer with dspr
    sh "Я по старому туннелю пройду. Она даже не успеет заметить, что меня нет."
    el "Ты сильно рискуешь!"
    sh "Смелым помогает судьба!"
    scene ext_square_day with dissolve
    "Сказано — сделано. Буквально через пару минут мы были на площади, где  в спешке открывали старый люк. Я действую очень быстро, и врятли кто-либо обратит на нас внимание - «мало-ли что этим ботаникам в голову пришло»."
    "Идеальное прикрытие."
    show el shocked pioneer with dissolve
    play sound sfx_fall_metal_door
    sh "Всё, открыл. Я пошёл, прикрой меня."
    show el normal pioneer with dspr
    el "Хорошо Саш, ты только давай быстрее."
    stop music fadeout 3
    scene int_catacombs_entrance with dissolve
    
    $ persistent.sprite_time = 'night'
    $ night_time()    
    play music music_list["torture"] fadein 3
    "Спуститься по лестнице не составило особого труда." 
    scene int_mine_room with dissolve
    "Темно, как в хижине дяди Тома. Стараясь не задерживаться, я быстрым шагом добрался до убежища, поскольку дорога мне хорошо известна." 
    scene int_catacombs_living with dissolve
    "К сожалению, а может и к счастью, но в самом убежище никого не обнаружилось. А я уж понадеялся."
    "Беглым взглядом осмотрев комнату, я подметил несколько старых приборов, которые могут пригодится."
    "Распотрошив их, я со спокойной душой двинулся в обратный путь. Вот только как? "
    "Путь которым я пришёл заказан, а это значит, что мне нужно идти через старый лагерь." 
    "Вот только этого мне не хватало, но выбора нет."
    scene int_catacombs_entrance with dissolve
    "Мой большой опыт подсказывал, что в эти катакомбы есть проход из здания лагеря, чем я и воспользовался."
    "Какая гнетущая атмосфера! Я бывал тут много раз, но до сих пор чувствую страх, граничащий с паникой. Всё скрипит, кряхтит, а в остальном - гробовая тишина."
    scene int_catacombs_door with dissolve
    "Жуть какая."
    scene int_old_building_night with dissolve
    stop music fadeout 3
    "Так, спокойно. Просто паника, ты себе всё напридумывал.Это просто старое здание, ничего плохого с тобой тут не случится."
    $ persistent.sprite_time = 'day'
    pi "Туда ли ты зашёл, кибернетик?"
    show pi normal1 with dissolve
    play music pioneer_theme 
    "Оказалось - может."
    "Как меня бесит и одновременно пугает его привычка появляться сзади."
    pi "Так так так. Значит нарушаем правила лагеря? Ай как плохо Санёк. Ты же такой правильный и прилежный пионер."
    sh "Я могу этим похвастаться." 
    show pi smile with dspr
    pi "Шутник. Скучать не даешь. Поздоровались и будет. Я к тебе по делу."
    "Я кивнул, походу осматривая окрестности в поисках вещей, которыми можно огреть этого олигофрена."
    pi "Как твой день начался?" 
    sh "Спасибо хорошо, твоими молитвами."
    show pi normal1 with dspr
    pi "А вот у меня не очень. Понимаешь, есть один человечек, который сильно мне нервы портит. Я прямо не знаю что делать."
    "С этими словами он подошёл ближе. Нутро подсказывало мне, что сейчас начнутся проблемы." 
    "А собственно, хватит это терпеть! Пора действовать!"
    sh "Ты что удумал?"
    "Прощипел я."
    pi "Самое верное решение - самое простое, не так ли?" 
    show pi smile with dspr
    "И он замахнулся. Вот только зря он так долго разглагольствовал и болтал - я оказался готов к его выпаду."
    sh "ННаааа."
    play sound sfx_punch_washstand
    with hpunch
    "Хороший удар! Прямо в челюсть."
    pi "А ты хорош!"
    "И тут у меня в глазах померкло - его удар пришолся под дых."
    "Я осел, пытаясь вспомнить, как дышать."
    pi "И не надейся. Твои мытарства только начинаются."
    "И с этими словами он столкнул меня в дыру на полу."
    show blink
    "Мир на мгновенье моргнул."
    "Опять падение в никуда?"
    "Похоже я приноровился к этим перемещениям, поскольку не чувствую ни страха, не волнения."
    scene un home night with dissolve
    play music Memory fadein 3
    "Так...куда меня занесло? Вечер, никого, домик Лены. Постойте..."
    "Нет нет нет.  НЕТ!!"
    "Я мигом ворвался в домик, и зрелище шокировало меня."
    scene int_house_of_un_night
    show un cry body
    with dissolve
    "Лена ,сидя на стуле, ревёт и режет себе вены."
    "Видимо есть в этой реальности провидение — я успел вовремя. Одним прыжком я оказался около неё."
    "Моё появление оказалось для этой самоубийцы-истерички полной неожиданностью, что она даже и звука не издала, только уставилась на меня полными от удивления глазами." 
    "Точным ударом  левой руки я выбил у неё нож, да так, что он воткнулся в потолок, а правой отвесил добротную пощёчину."
    play sound sfx_face_slap
    with hpunch
    "Быть может я переборщил, но критическая ситуация требует критических решений."
    "Лену от удара откинуло на кровать."
    show un shocked body with dspr
    "Как она смеет так распоряжаться собой? Кто она такая, чтобы нарушать мои планы?"
    "Чувствуя как ненависть охватывает меня, я двинулся к ней, хватая её за горло. В её глазах читается ужас и непонимание."
    show un scared body with dspr
    sh "Что, тебе слишком трудно жить? Решила найти лёгкий выбор?  Раз и готово?"
    "Лена начинает плакать, а я отпускаю руку, и рву рубашку, чтобы сделать жгут."
    un "Ненадо..."
    sh "Неразделённая любовь,конечно ужасна, но думай об остальных."
    un "Но ведь он всё для меня..."
    "Прохныкала Лена."
    show un cry body with dspr
    "Я не слушаю её бред, не до этого сейчас."
    sh "Он не весь мир, пойми это."
    un "Но..."
    sh "Никаких «НО!»"
    play music alex_theme fadein 3
    play sound sfx_table_hit
    "Со злости я стукнул по столу кулаком. Нож, всё это время тихо наблюдавший за шоу, решил вмешаться, и вонзился около моей руки."
    sh "Это ведь не первый раз. Ты же помнишь. Эти сны, так похожие на реальность. Это чувство, когда ты видишь его лицо впервые. А кажется уже не одно столетие." 
    show un normal body with dspr
    "Лена смотрит на меня, и мне кажется она понимает смысл моих слов."
    sh "Его измена с Алисой и Мико. Ты ведь помнишь, тебе ведь снилось."
    un "Откуда ты …"
    show un surprise body with dspr
    sh "Неважно."
    un "Как ты тут вообще оказался?"
    "Лена начитает свирепеть. Дело плохо, совсем плохо."
    show un angry body with dspr
    sh "И это твоя благодарность за спасение?"
    un "Да кто тебя просил? Я всё решила, и не тебе, очкастому идиоту, меня останавливать."
    sh "Грубить не надо."
    "Лена оттолкнула меня со всей своей девчачьей силой в попытке получить свободу и убежать в ночь."
    show un normal body with dspr
    sh "Так, а теперь слушай сюда, ты, полоумная жертва неразделённой любви. Повторяю для не очень умных — Семён не является центром мира, и творить ради него такие вещи — верх идиотизма."
    sh "Посему хватит истерить."
    show un angry body with dspr
    un "Да пошёл ты!"
    hide un angry body with dspr
    "И она выбежала из домика в чём мать родила. Теперь мне её ловить. Схватив попавшееся под руку полотенцэ, я выскочил следом за ней."
    scene ext_square_night with dissolve
    play music Freedom fadein 3
    "Ох уж эти женщины. Принимают пустяки так близко к сердцу - думал я во время импровизированной погони - Подумаешь- парень бросил. Кто в этом виноват и что делать?"
    "Ну уж явно не вскрываться из-за этого. И почему она так болезненно переживает? И почему я чувствую жалость к ней?"
    "Между делом я её догнал и схватил за руку."
    show un angry body with dissolve
    un "Пусти сейчас же!"
    sh "Нет."
    un "Пусти, больно!"
    sh "А себе ты разве не пыталась сделать больно? Родным? Близким? Ты об остальных подумала, эгоистка?"
    un "Нет я..."
    show un surprise body with dspr
    sh "Да ты! Каждый раз ты устраиваешь кошмарное представление!"
    un "Что?"
    "Иногда её поведение меня просто бесит. Начнём с начала."
    sh "Лена."
    "Начал я спокойно и тихо."
    play music painful_truth fadein 3
    sh "Лена, ты тут не просто так. Тебе безумно нравится Сёма, ты готова на всё ради него." 
    "Я сжал её руку сильнее."
    show un cry body with dspr
    un "Ай!"
    sh "И ты не можешь без него. Но он не тот, который тебе подойдёт."
    un "Ты мне отец что-ли, указывать с кем гулять?"
    show un angry body with dspr
    sh "Старше, по крайней мере. Так что слушай и запоминай - этот пионер-лагерь не так прост, как кажется."
    un "О чём ты?"
    show un normal body with dspr
    "Она вырвала свою руку из моего хвата."
    sh "Может это эксперимент, или другая вселенная - я не знаю. Но я уверен, что тут только ты и я - настоящие люди. Всё остальные - муляжи."
    "Более того, ты не можешь отсюда выбраться. Закончится смена, ты уедешь вместе со всеми, и тут-же вернёшся, не помня ничего."
    show un surprise body with dspr
    "Видимо я перестарался."
    "Надо привести её в чувства, и побыстрее."
    "Я знаю несколько методов, но по лицу я её уже бил, а близости с ней мне не хочется, то остаётся ещё один способ."
    "Получилось на её подруге, сработает и на неё."
    sh "Закрой глаза. Быстро!"
    "Командным голосом сказал я. Девочка наверно на грани обморока - стресс, неудавшийся суицид, молодецкий удар, голая гонка и в завершение открытие тайн."
    "Сопротивляться она не посмела, чем я и воспользовался, быстро схватив её за руку и плечо."
    show blink
    show prologue_dream 
    show d3_un_dance behind prologue_dream with dissolve
    "Я видел все ваши встречи. Вашу радость и удовлетворение. Ненависть и ревность. Всё до конца. И ты увидишь тоже."
    show d2_sovenok behind prologue_dream with dissolve
    un "Ой, что это?"
    show d3_un_forest behind prologue_dream with dissolve
    sh "Это твоё, кхм, прошлое и будущее."
    show d7_un_hentai  behind prologue_dream with dissolve
    sh "Тебе ведь понравилось? Знаю что да."
    "Молчит. Ничего, сейчас заговоришь."
    show d7_un_suicide behind prologue_dream with dissolve
    sh "А как тебе это? И это только начало. Ты знаешь, как больно сделала этому человеку."
    "Человеку. После всего с нами случившегося, я называю его человеком. Забавно."
    un "Я не хотела этого...Я думала, что.."
    sh "Ты не думала, и ты не представляла, через что пришлось пройти нам всем после твоей глупости. Это был ад, понимаешь? Ведь ради тебя Семён готов был горы свернуть... как и я."
    un "Ты?!"
    sh "Но ты слишком избалованна и глупа, чтобы думать о других."
    un "Нет, я не хочу так!! Не надо!!"
    scene ext_square_night
    show unblink
    "Я открыл глаза. Лена сидит на земле, закрыв лицо руками и рыдает."
    show un cry body with dissolve
    un "Я...я...сделала так больно людям...я... плохой человек."
    sh "Ты добрая и отзывчивая, но давай не воспринимать всё так близко к сердцу."
    "Я сел около неё, и протянул полотенце."
    sh "На, держи, не то простудишся."
    show un shy pl with dspr
    un "С-с-спасибо."
    show un cry pl with dspr
    "Сквозь слёзы сказала Лена."
    "Я встал и протянул ей руку."
    sh "Пойдём."
    show un shocked pl with dspr
    un "Куда?"
    sh "Тащить верблЮда. Нам есть о чём поговорить."
    "Вернувшись в домик, я продолжил свой рассказ."
    scene int_house_of_un_night
    play music music_list["lets_be_friends"] fadein 3
    show un normal pl
    with dissolve
    sh "Лена, выслушай меня очень внимательно. Ты должна вспомнить все свои дни, проведённые тут. Вспомнить и обдумать."
    sh "Потому что ты скоро сядешь в 410й и твой цикл начнётся заново."
    sh "Вот тебе листок бумаги, напиши на нём для себя же послание, вдруг забудешь."
    show un cle pl with dspr
    un "Хорошо. Скажи, а Алиса, ну в смысле настоящая, где?"
    sh "Ты же её ненавидишь?"
    show un normal pl with dspr
    un "Вместе выросли. Просто так бросить её не могу."
    sh "Она, как и Славя, в своих «Совятах»."
    un "Они тоже пережили такое?"
    show un scared pl with dspr
    "Быстро соображает."
    sh "Да. Ты должна попасть к ним, как я к тебе."
    un "А как..."
    sh "Сейчас научу. Покажется странно, но ничего лучше пока нет.
    Быстро но чётко рассказывая свой метод, а заодно и цель всего предприятия, я задумался: вот приведу я всех к Семёну."
    "И что дальше? Ну уедет он с одной из них. А я? Нет, больше всего я жажду свободы, но не обманываю ли я себя, что эти девушки мне безразличны?" 
    "Нет, не время думать об этом."
    sh "Всё запомнила?"
    show un smile pl with dspr
    un "Да, всё."
    sh "Тогда напиши мне свой адрес, чтобы проверили, всё ли прошло как надо."
    un "Хорошо."
    "О, да она почти рядом с Алисой живёт, как ни странно. Далеко ходить не придётся."
    sh "Вот тебе адрес Слави, а Алису сама найдёшь."
    show un normal pl with dspr
    un "А ты теперь куда?"
    sh "К себе. У меня ещё дел полно."
    show un scared pl with dspr
    un "Подожди, ты меня тут бросаешь?"
    sh "Чего ты разволновалась? Эти куклы играют свою роль, а ты им подыграй. Делов-то?"
    "Она промолчала."
    show un cle pl with dspr
    un "Знаешь, я терпеть не могу фальши. И всё это время будет для меня большой проблемой."
    sh "У всех трудности. Я тут уже..."
    "А сколько? Я до сих пор не вспомнил свой дом, родных, самого себя."
    sh "...очень давно. Так что я тебя понимаю."
    un "А ты будешь ещё приходить?"
    show un normal pl with dspr
    sh "Вопрос сложный. Уж лучше ты к Семёну приди."
    un "Саш... Я не хочу ради нашей свободы жертвовать остальными девчонками."
    "И эта туда-же. Ну что ты будешь делать?"
    sh "Хочешь тут застрять?"
    un "Нет."
    sh "Тогда в чём проблема?"
    un "В том, как мы жить будем после этого."
    sh "Каждый сам за себя. Так было и будет. А остальные... забудут о Сёме при первой встрече с каким-либо богатеньким пареньком."
    un "Ты о всех такого мнения?"
    sh "Да."
    show un cle pl with dspr
    un "А я его не забуду."
    sh "Тогда что ты мне тут чушь несёшь про остальных и прочее. Иди к нему и будьте счастливы, что ещё надо?"
    un "Ты так легко об этом говоришь..."
    sh "Жизнь научила быть проше."
    "Лена посмотрела на меня с такой грустью, что у самого слёзы на глаза навернулись."
    show un clcr pl with dspr
    un "Тебе было так тяжело, а тут ещё и я. И остальные. Понятно, почему ты такой. Хорошо, я сделаю так как ты говоришь, и буду искать причины тому, почему я тут очутилась."
    sh "Умничка. Поиск ответов можешь начать с местного Семёна — они мастера в этом деле."
    sh "Много интересного узнаешь, но без меня - у меня ещё других дел полно."
    scene ext_square_night with dissolve
    play music alex_mind fadein 3
    "Выйдя из домика, я пошёл к клубу. После таких задушевных разговоров меня всегда туда тянет."
    "Странно, но это место я могу назвать домом. Но что-то не даёт мне покоя. Я всё правильно сделал, так что меня гложет?"
    "Я развернулся посмотреть, как там Лена,"
    show un smile pl with dissolve
    "а она стояла, и в свете луны робко помахала мне рукой."
    "Дурочка, иди в дом, замёрзнешь же!"
    "Я становлюсь сентиментальным. Смешно. Помахав ей в ответ, я продолжил свой путь." 
    scene ext_clubs_night with dissolve
    "Она такая ранимая, что аж страх берёт. За неё, за остальных, за себя. Это не жалость, это не её слабость. Это её суть с которой нужно смириться." 
    "Я поймал себя на мысли, что желая свободы больше всего на свете, я также хочу её, то есть ей счастья. Вот это на меня совсем не похоже. Но разве я не достоин вознаграждения за тот подвиг, который я совершу?"
    "Разве я не достоин счастья?"
    "Но не зря говорят «Cherchez la femme». В своих раздумьях о Лене и нашем будущем я совершенно не следил за окружающим миром. И мир этим воспользовался."
    "Последнее что я услышал, это быстро приближающиеся шаги и свист то-ли палки, то-ли ещё чего-то."
    play sound sfx_armature_swish
    "И я опал, как озимый."
    play sound sfx_bodyfall_1
    show blink
    "…"
    scene int_mine_room
    "Я открыл глаза."
    show unblink
    $ persistent.sprite_time = 'day'
    $ night_time()    
    play music music_list["get_to_know_me_better"] fadein 3
    el "САША!!"
    "Кто, что?"
    el "Саша!"
    show el scared pioneer with dissolve
    "Электроник."
    sh "О, привет. Ты что тут забыл?"
    el "Жив. Это я тебя хочу спросить. Сказал, что мигом обернёшся, и пропал. Тебя уже Дмитриевна ищет."
    sh "Понял, спасибо. Видимо упал."
    show el shocked pioneer with dspr
    el "Слушай, а может у тебя сотрясение?"
    sh "С такой высоты?"
    el "А много надо?"
    show el scared pioneer with dspr
    "Я попытался встать. Голова не кружиться, не тошнит. Вроде всё обошлось."
    el "САША!"
    show el scared pioneer with dspr
    sh "Да не ори! Голова болит!"
    el "У тебя кровь!"
    "Это плохо. Очень плохо."
    show el angry pioneer with dspr
    el "Так, пошли к докторше. Если трудно идти, я тебя понесу!"
    "В кризисный момент Эл повёл себя как истинный пионер и товарищ. Нести я себя не дал, но от товарищеского плеча не отказался."
    el "Держись, уже пришли."
    sh "Ты сумку с запчастями взял?"
    show el smile pioneer with dspr
    el "Сдались они тебе сейчас!" 
    "Выпалил он, но мой леденящий душу взгляд заставил его пересмотреть свою позицию."
    show el normal pioneer with dspr
    el "Взял, взял. Не волнуйся."
    scene ext_square_day
    $ persistent.sprite_time = 'day'
    $ day_time()    
    show el normal pioner
    with dissolve
    "Оказавшись в лагере мы быстрым шагом отправились к Виоле, надеясь, что нас никто не заметит."
    scene ext_aidpost_day with dissolve
    "На этот раз всемогущий рандом оказался на моей стороне, и ниодин посторонний глаз не увидел моё плачевное состояние."
    scene int_aidpost_day_apple 
    play music music_list["gentle_predator"] fadein 3
    show cs normal at right
    show el normal pioneer at left
    with dissolve
    cs "Что с ним?"
    "Профессионально-холодным голосом спросила медсестра, увидел меня на плече у Эла."
    sh "Шёл, споткнулся, упал, дальше не помню."
    cs "Клади его на кушетку."
    "Что Эл покорно и исполнил."
    play sound sfx_bed_squeak2
    cs "Молодец пионер, а теперь свободен. Сходи в столовую за обедом — этот кадр никуда пока не пойдёт."
    hide el normal pioneer at left with dissolve
    cs "Что же ты не бережёшь себя? Вот всё с тобой не как у людей."
    sh "Извините."
    "Только на это и хватило воображения — голова просто расскалывалась."
    cs "Болит?" 
    sh "Да."
    hide cs normal at right
    show cs_close at right
    with dspr
    cs "Ясно. Вот тебе — выпей."
    "Она протянула мне  таблетки."
    cs "Если сильно болит-бери большую, а если кружиться — то эти две маленькие."
    hide cs_close at right
    show cs normal at right
    with dspr
    "Ну раз врач говорит, то надо слушать."
    "Приняв препараты, я с удивлением обнаружил, что боль стала уходить незамедлительно. Я расслабился и готовился подремать."
    cs "Так, пионер, не спать!"
    "Она подошла, положила руку мне на лоб."
    cs "Хм, нормально. Не тошнит, слабости нет?"
    sh "Нет, всё нормально же!"
    cs "Нормальные сюда просто так не попадают. Смотри на кончик пальца."
    "Проверив мою реакцию, она удостоверилась, что всё в порядке."
    cs "Вроде ничего страшного." 
    "Сказала она, закончил обрабатывать мои ссадины и порезы."
    cs "Вот тебя угораздило. Ладно , отдыхай."
    show cs shy with dspr
    "О, знакомый тон. Значит всё хорошо."
    cs "Я о тебе позабочусь."
    sh "Спасибо не надо."
    "Не замедлил я с ответом."
    cs "Все вы такие. Не знаете от чего отказываетесь."
    "Я улыбнулся."
    sh "В другой раз."
    show cs smile with dspr
    cs "Я настаиваю. Кто тут кроме меня тебе поможет?"
    sh "Не стоит вам так волноваться. Со мной всё в порядке."
    "Последняя фраза далась мне с небольшим трудом, поскольку я стал быстро засыпать. Может действительно сотрясение? Совсем не к месту."
    cs "Всё с тобой хорошо, я тебе снотворное дала."
    "Опередила медсестра мои опасения."
    "Тогда зачем снотворное?"
    menu:
        "Бороться":
            jump d5_1
        "Поддаться":
            jump d5_2
    
label d5_1:
    sh "Зачем?"
    show cs normal with dspr
    cs "Ну, я подумала, что ты не высыпаешся, и решила помочь - вид у тебя плохой. Весь какой-то измученный, уставший."
    sh "Я потерплю."
    "Я попытался встать, но снотворное начало действовать. Не знаю, что мне вкатили, но я отключаюсь просто на глазах."
    sh "Что...ты...задумала?"
    play music music_list["heather"] fadein 2
    show cs smile with dspr
    cs "Я же говорила, что судьбе надо немного помочь."
    "Я не усну, не сейчас!!"
    "Она подошла ко мне и села на кровать."
    hide cs smile 
    show cs_lust 
    with dspr
    cs "А ты упорный, я люблю таких. Как долго ты собираешся бороться с собой?"
    "Веки стали такими тяжёлыми, что я с трудом сдерживаюсь."
    sh "Да пошла ты, старая кошёлка."
    "Из последних сил выдавил я."
    "Виола рассмеялась мне в лицо."
    cs "Сам находится на честном слове, а огрызается до победного. Ты мне нравишся Саш, очень. Продолжай, сопротивляйся, докажи мне и себе что ты на многое способен,"
    cs "и так просто не сдашся."
    "Дело плохо. Силы покинули меня. Но неужели я просто так дам себя победить? Я не отступлю. Я не могу отступить. Я прокладывал путь, где его небыло, и разрушал все препятствия на пути."
    "Это не конец."
    "Я попытался встать, но Виола крепко схватив меня, уложила на кровать. А чтобы убедиться, что я уже не попытаюсь снова, легла на меня сверху."
    hide cs_lust 
    show cs shy 
    with dspr
    cs "Молодец.Ты нравишся мне больше и больше."
    "И своей рукой она закрыла мне глаза."
    show blink
    "Но перед тем как окончательно провалиться в никуда, я ощутил прикосновение её губ к моим, и её , честно сказать, чарующий аромат духов."
    "Этот раунд за тобой, но я вернусь. Вернусь..."
    jump d5_od
    
label d5_2:
    "Я действительно устал, так какой смысл в борьбе?"
    sh "А что если..."
    cs "Ни о чём не волнуйся. Спи."
    "С этими словами она села на кровать."
    show cs normal with dspr
    cs "Ты много сделал, ты уже заслужил благодарность."
    "Она погладила меня по голове. Чёрт, я начинаю превыкать к этому. От неё приятно пахнет, и веет добротой."
    "Повезёт её мужу и детям."
    cs "Голова не болит?"
    sh "Нет."
    show cs smile with dspr
    cs "Вот и славно."
    "Она наклонилась ко мне, и я смог уловить тонкий запах её парфюма. Что за женщина!"
    cs "Отдыхай и наберись сил. Они очень скоро тебе потребуются."
    "Мне захотелось прижаться к ней, и видимо она почувствовала моё желание."
    "Пересев на кровать, она взяла мою руку.  У неё такая нежная кожа! Никогда в жизни не чувствовал мягче."
    "Если так подумать, то я о ней ничего толком и не знаю. есть ли она настоящая? Интересно какая она? Может стоит найти её?"
    hide cs smile 
    show cs_lust 
    with dspr
    cs "Эххх, чудный у тебя сейчас возраст - сил просто девать некуда. Спи давай, Дон Жуан."
    show blink
    jump d5_od
    
label d5_od:
    scene alex home day
    $ persistent.sprite_time = 'sunset'
    $ day_time()
    play music Freedom fadein 3
    show unblink 
    "Не знаю, сколько прошло времени, но меня разбудило утреннее солнце."
    "Открыв глаза, я увидел знакомую картину своего домика. Может я заснул на весь день? Это сколько я времени и возможностей упустил!!"
    "Так, спокойно. Последнее что помню — днём заснул в медкабинете, а сейчас утро."
    play sound sfx_dinner_horn_processed 
    "Завтрак? Да, точно."
    "Есть не хочется, но делать нечего — скандалы мне не нужны."
    scene ext_houses_day with dissolve
    "На пути мне попалась вожатая."
    show mt normal pioneer with dissolve
    "Вроде ничего странного, но что-то в ней было не так, не по сценарию, так сказать."
    sh "Доброе утро Ольга Дмитриевна."
    mt "О, Саша, доброе утро. Как спалось? Готов к труду и обороне?"
    sh "Конечно, всегда готов!"
    play music semion_theme fadein 3
    $ renpy.music.set_volume(0.25, .5, channel="music")
    "Её словно подменили , когда она услышала мои слова. Что это с ней таоке случилось?"
    show mt surprise pioneer with dspr
    mt "Эээммм, ну это, завтракай, и на линейку."
    sh "Не волнуйтесь, буду в срок."
    "Она улыбнулась, и пошла в сторону своего домика."
    mt "Саша, давай на «ты»."
    "Что? Это куда я попал? Неужели эта Ольга — настоящая?"
    "Надо это проверить."
    "Но всё потом — сейчас надо играть свою роль, и молча идти на завтрак. "
    scene int_dining_hall_people_day with dissolve
    play music music_list["timid_girl"] fadein 2
    $ renpy.music.set_volume(1.0, .5, channel="music")
    play ambience ambience_dining_hall_full
    "В столовой всё было без изменений, да и могло-ли что быть по другому в этом месте? Думаю нет."
    "Получив свою порцию я , стараясь не привлекать ничего внимания, уселся в самом углу и начал подпитывать свои изнурённые путешествиями и истериками организм."
    "Окружающее не вызывало у меня подозрений — всё было тихо. Даже слишком тихо. Это меня и беспокоило."
    "Вот Алиса с Ульянкой перешёптываются,"
    show dv smile pioneer at right
    show us smile pioneer at left
    with dissolve
    "там в стороне Лена тихо обедает, изредка перекидываясь словами с Женей,"
    hide dv smile pioneer at right
    hide us smile pioneer at left 
    with dissolve
    show un normal pioneer at right
    show mz bukal glasses pioneer at left
    with dissolve
    "а Мику что-то тараторит Славе, на счёт концертов, не иначе."
    hide un normal pioneer at right
    hide mz bukal pioneer at left 
    with dissolve
    show mi smile pioneer at right
    show sl smile pioneer at left
    with dissolve
    "Электроник , опоздавший по необъяснимым причинам, засел в свободное место и быстро запихивает в себя свою порцию. Ты глотал хотя бы!  А Семён...а что Семён? Сидит один в стороне."
    "Как обычно."
    hide mi smile pioneer at right
    hide sl smile pioneer at left
    with dissolve
    "Мои наблюдения так ничего мне и не дали бы, если в столовую не заглянула вожатая."
    show mt sad pioneer with dissolve
    "Ольга Дмитриевна осмотрела обедающих пионеров, но в её взгляде я уловил некоторую тоску."
    "Если глаза умели бы говорить, то она буквально кричала « Ну что вы такие тихие, такие грустные?». Но на её взгляд никто не обратил внимание — все заняты были своими делами."
    show mt sad pioneer with dspr
    "Когда же она посмотрела на меня, как мне показалось с некоторым любопытством,  в ответ я подмигнул ей. Мне была интересна её реакция на такое, и она не заставила себя ждать."
    show mt smile pioneer with dspr
    "Она буквально расцвела, улыбнувшись мне в ответ."
    "Есть контакт!"
    "Я слегка наклонил голову и состроил смешную рожицу. Как давно я это делал. Просто покривляться, немного пошалить ? Я ничего этого не помню."
    show mt angry pioneer with dspr
    "Дмитриевна сердито посмотрела на меня."
    "« Что ты делаешь! Ты же пионер!!»."
    "На мой виноватый взгляд же она весело рассмеялась."
    show mt grin pioneer with dspr
    "Я рассмеялся в ответ. И меня совсем не волновало, что на нас могли смотреть окружающие, что они подумают и тому подобное."
    "Надо будет зайти к Ольге, поговорить по душам. Думаю, её есть что мне сказать."
    stop ambience
    scene ext_house_of_mt_day with dissolve
    play music aha_takeonme
    "После завтрака я быстрым шагом направился к её домику. Раз что-либо решил - надо действовать — сказал я себе, когда подходил к двери."
    "Со словами:"
    sh "Ольга Дмитриевна, тут ..."
    "Я открыл дверь."
    play sound sfx_open_door_2
    "И замер."
    scene d2_mt_undressed with dissolve
    mt "Стучаться надо."
    sh "А я ...это...ну..."
    "Да, получилось не очень хорошо."
    scene d2_mt_undressed_2 with dspr
    mt "Что стоишь на пороге с открытой дверью? Заходи."
    sh "Ддда."
    "Ну дела. Я даже не знаю что делать."
    scene int_house_of_mt_day
    show mt pl bra
    with dissolve
    mt "Что рот открыл? Понравилась?"
    sh "Да. То есть нет. В смысле я не в том смысле."
    mt "Тебе подсказать? — отвернись уже наконец."
    "Что я и выполнил."
    "Вот чего-чего, а такой реакции я не ожидал. Будто я не чужой, а свой, родной и любимый человек, которому позволяют некоторые вольности."
    show mt angry bra
    with dissolve
    sh "Ольга Дми..."
    mt "Я же сказала, что на «ты»."
    show mt grin bra with dspr
    "Сквозь смех  сказала та."
    sh "Оля, я тут подумал..."
    mt "Это конечно хорошо, что ты думаешь, но у нас линейка. Так что пошли скорее, по дороге поговорим."
    "Вот так всегда — на самом важном месте." 
    scene ext_houses_day
    show mt normal pioneer
    with dissolve
    mt "Ну и о чём ты думал?"
    sh "Ольг..."
    "Она сурово посмотрела на меня."
    show mt angry pioneer with dspr
    sh "Оля, я хотел сказать, что ...что очень рад быть сейчас тут, с тобой, со всеми вами."
    mt "Неужели ради этого стоило вламываться к голой женщине?"
    "Она улыбнулась."
    show mt smile pioneer with dspr
    sh "Да. Особенно сегодня. Мне показалось , что это будет важно сказать."
    mt "А что ты остальным это не скажешь?"
    sh "Поймут не правильно."
    "Если вообще поймут."
    sh "И я решил сказать...тебе об этом."
    mt "Спасибо Саша. На твою честность всегда можно положиться."
    scene ext_square_day
    show mt normal pioneer
    with dissolve
    "Линейка прошла без происшествий и откровений. Дмитриевна говорила про планы на оставшееся время, про важность соблюдения установленных правил."
    "Хотя мало кто её слушал."
    "Только я один вникал в суть слов, которые говорит Оля. Это не обычный спич, плоский и бездушный. Нет, она говорит с чувством, с отдачей." 
    mt "...И наконец. Сегодня мы идём в поход, так что все подготовьтесь к этому важному мероприятию."
    "Одобрительный шёпот прошёлся по строю." 
    "Как реакция на это вожатая строго нас осмотрела."
    show mt angry pioneer with dspr
    mt "Собираемся после ужина. А теперь все свободны. Увижу кого заплывающим за буйки — со мной за ручку в поход пойдёте."
    "Алиса и Ульяна нервно переглянулись."
    show dv scared pioneer at right
    show us angry pioneer at left
    with dissolve
    "Что сказать — строго, но справедливо."
    hide dv scared pioneer at right
    hide us angry pioneer at left
    with dissolve
    "Я уже настроился на серьёзный разговор с вожатой, но и тут она перехватила инициативу."
    show mt smile pioneer with dspr
    mt "А вас, Александр, я попрошу остаться."
    sh "Да, Оля."
    mt "Слушай, пошли со мной. Надо одну вещь обдумать."
    "Опаньки, интересно."
    scene ext_house_of_mt_day with dissolve
    play music music_list["eat_some_trouble"] fadein 3
    "Путь наш лежал обратно до её домика."
    scene int_house_of_mt_day
    show mt smile pioneer 
    with dissolve
    "Семёна, что странно, там не обнаружилось, так что нам никто не помешает, чем бы мы не занимались."
    "Эта Ольга была самая  что ни на есть настоящая, и мне было немного не по себе, ведь я даже не представляю, что у неё на уме."
    mt "Саша, нам надо сделать так, чтобы они не забыли этот поход!"
    sh "Есть идеи?"
    "Осторожно ответил я."
    show mt grin pioneer with dspr
    mt "Да. Из всех только ты сможешь выполнить мой план."
    "Хм, она что, не понимает своего положения?"
    mt "Ты возьмёшь с собой вот это."
    "Оля протянула мне аккуратно сложенную ткань."
    sh "Что мне с этим делать?"
    show mt normal pioneer with dspr
    mt "Когда устроим костёр, все будут рассказывать страшилки. Когда же я начну рассказывать свою, ты незаметно спрятавшись, наденешь это и начнёшь по кустам шуршать."
    mt "А когда все дойдут до кондиции, ты выпрыгнешь, и всех распугаешь."
    "Она задорно захихикала."
    show mt grin pioneer with dspr
    mt "Я уже представляю, как Улька с Алисой завизжат."
    sh "Не слишком-ли круто?"
    mt "В самый раз."
    show mt smile pioneer with dspr
    sh "Ну раз ты так уверена, то я согласен."
    mt "Хорошо, тогда бери свой костюм и спрячь его."
    scene ext_clubs_day with dissolve
    "Лучшего места для этого чем наш клуб я  не знаю. Так что незаметно, с перекатами, я добрался до нужного места, и буквально протёк в дверь."
    scene int_clubs_male2_night with dissolve
    "Эла на месте также не обнаружилось. Да где они все? Ладно, сначала дело, потом отдыхаем смело. Надёжно спрятав ткань в кладовой, я направился к одному месту, где все точно могут находится, когда лагерь пуст — на пляж."
    scene ext_beach_day with dissolve
    "Предчувствия меня не обманули — тут были все. Весь лагерь весело резвился в тёплой воде."
    "Вскоре я заметил и Олю, дав кивком понять, что дело сделано." 
    show mt normal swim with dissolve
    "Она слегка подмигнула."
    show mt smile swim with dspr
    "« Молодец, а теперь отдыхай» - таково было её послание. Но отдых в мои планы не входит."
    play music treck_op fadein 3
    "Я чувствую, что она буквально рвётся мне что-то сказать, и эта идея с костром и ужасами лишь прикрытие. Может она меня проверяет?"
    "Внезапно перейти на «ты»? Это на неё точно не похоже. Вот не люблю я эти недосказанности и тайны. Если тебе что нужно, то надо говорить прямо, не скрываясь за холодными и фальшивыми масками напускных эмоций."
    "Что я и сделаю. Здесь и сейчас."
    sh "Оль, можно тебя на пару слов?"
    mt "Можно, но никуда не пойду."
    show mt grin swim with dspr
    "Замурлыкала та."
    sh "Почему ты позволяешь мне такие вольности? На «ты» внезапно? Без какого-либо смущения переодевалась при мне? С чего такие перемены?"
    mt "Ради более непринуждённого общения."
    show mt normal swim with dspr
    "Стала выкручиваться она."
    sh "Угу, я так и поверил. Что это за проверка? Настоящий я или как эти куклы? Оля, не надо лапшу тут развешивать."
    show mt sad swim with dspr
    mt "Саша, с тобой всё хорошо? Может тебе к Виоле?"
    sh "Сходил я к ней разок — теперь тут с простынями бегать буду. Сколько уже ты смен тут руководишь этим театром?"
    show mt normal swim with dspr
    play music painful_truth fadein 3
    mt "Ах вон оно что. Много. Но они не куклы, просто не помнят произошедшего. И я каждый раз пытаюсь им помочь."
    sh "Даже костёр?"
    mt "Особенно костёр."
    sh "А с чего ты взяла, что я отличаюсь от них?"
    show mt sad swim with dspr
    mt "Ты реагируешь по другому. Словно ты кукла, марионетка."
    sh "Но я настоящий!!"
    mt "Докажи."
    show mt normal swim with dspr
    sh "И чем мне доказать, что я настоящий?"
    mt "Удиви меня."
    "Я подошёл и поцеловал её в щеку."
    sh "Этого хватит?"
    show mt surprise swim with dspr
    mt "...да."
    "Фуф, а мне понравилось."
    sh "Едем дальше. Скажи, что ты знаешь про Семёна?"
    show mt normal swim with dspr
    mt "Сема? Спокойный, тихий парень. По нему тут все девчонки сохнут. А тебе он зачем?"
    sh "Он наш ключ к свободе."
    mt "А остальные ? Разве они не часть происходящего?"
    sh "Статисты, не более. Сёма всему виной, и только если он сможет отсюда выбраться, сможем и все мы."
    mt "Знаешь, звучит бредово. С чего это ему быть настолько важным, что всё здесь вокруг него и крутится?"
    sh "Ну а разве не он один тут романы стоит?"
    show mt shy swim with dspr
    mt "Нет. Все мальчишки за девками бегают. Даже Электроник пытается произвести на Женю впечатление."
    sh "Это понятно..."
    show mt normal swim with dspr
    mt "Все, кроме тебя. Именно ты и ведёшь себя странно — всех сторонишся, сидишь у себя в клубе как сыч. Ни разу тебя на танцах не видела."
    sh "Желания нет."
    "Ольга внимательно посмотрела на меня, и после небольшой паузы продолжила."
    show mt sad swim with dspr
    mt "Извини если оскорбила."
    sh "Всё в порядке. Вернёмся к главному — как нам выбраться отсюда."
    mt "У тебя есть план?"
    show mt normal swim with dspr
    sh "Да. Я бывал в других «Совятах», где живыми были другие персонажи нашей пьесы. Алиса, Славя, Уля, даже Лена теперь знают правду, и готовы помочь."
    sh "А план прост — переместиться в лагерь к настоящему, главному Семёну и влюбить его в себя."
    "От этих слов Ольга расхохоталась."
    show mt grin swim with dspr
    mt "Ахахаха, интересный план, но я уверена, что я не во вкусе Семёна. Да он с сверстницами слова связать не может, а ты тут меня предлагаешь."
    sh "Да, этот момент я упустил."
    mt "Не волнуйся. Если у остальных девчонок получится твоё «перемещение», то они его быстро оформят, тот и понять ничего не успеет."
    mt "Так что я не нужна."
    "Ольга на миг поникла, но сразу взяла себя в руки."
    show mt normal swim with dspr
    sh "Зря ты так Оль. Я хочу , чтобы мы все выбрались отсюда. Иначе какой смысл? Ты помнишь свой адрес и как сюда попала?"
    show mt shy swim with dspr
    mt "Конечно! Тебе написать?"
    sh "Угу, у меня и бумага с собой."
    "Она быстрыми движениями написала свои координаты, а затем ознакомилась с адресами других."
    show mt smile swim
    mt "Слушай, а мы все близко живём." 
    sh "Я тоже обратил на это внимание. Когда всё закончится, надо будет найти друг друга."
    mt "А твой адрес?"
    sh "Ты перепиши эти , а потом и мой."
    "За разговором я не заметил, как пришло время обеда, и пионеры ушли с пляжа, забыв про вожатую."
    mt "Ой, а куда они все? Обед же!!"
    scene ext_house_of_mt_day 
    play music music_list["i_want_to_play"] fadein 2
    show mt surprise swim
    with dissolve
    "Выдохнула Ольга и побежала к домику. Я  помчался в след за ней. На бегу осмотрел её листок — там переписаны все адреса, кроме моего."
    "Оля бежала впереди меня, так что я сполна оценил её достоинства. Интересно, она много занимается спортом? И остальные девушки также будут выглядеть в её возрасте?"
    scene int_house_of_mt_day with dissolve
    "Подбегая к двери, я заметил, что она приоткрыта. Как это возможно, я не представлял, но что-то внутри, на автомате указало путь действия."
    "Когда Ольга открыла дверь, я аккуратно но сильно оттолкнул её в сторону, получив за место её ледяной душ и ведром по голове."
    show blink
    with hpunch
    play sound sfx_drop_pipe
    play sound sfx_water_emerge
    sh "Найду — поотрываю рыжие патлы."
    "Прогундел я из под ведра."
    scene int_house_of_mt_day
    show mt like swim
    show unblink
    "Сняв ведро с головы и продолжая вспоминать Улю и Алису всеми словами, я посмотрел на Олю."
    "Та лежала на полу, молча смотря на меня своими зелёными глазами."
    mt "Точно как тогда..."
    "Шёпотом сказала  она."
    sh "Не ушиблась? Давай помогу."
    show mt smile swim with dspr
    "Ольга  взялась за протянутую руку без долгих размышлений и рассуждений о смысле этого поступка."
    sh "Я пойду переоденусь, и объясню кое-кому жизнь."
    "Сказал я и вышел."
    scene ext_house_of_mt_day with dissolve
    "Быстро сбегав до домика и переодевшись, я побежал на обед, в надежде хоть что-то перехватить."
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    "В общем мне это удалось без проблем, хотя и остался без десерта. Закончив свой «космический» обед, я решил найти Ольгу, чтобы выяснить её дальнейшие планы по нахождению тут, а заодно разобраться в себе и в том, почему меня перенесли сюда."
    "Но этот разговор отложился на неопределённое время, поскольку Оли в домике не оказалось, как и на площади и в административном здании."
    stop ambience
    scene ext_square_day with dissolve
    "Где её носит? Не спрашивать же у всех встречных, куда делась наша вожатая?"
    "Тут как на зло я вспомнил про поход, и ту ткань, что оставил в себя в клубе."
    scene ext_clubs_day with dissolve
    "Ладно, на этом похоже я с ней и переговорю, а сейчас за «костюмом» - не хочу её расстраивать."
    scene int_clubs_male_day
    play music alex_theme fadein 3
    show el scared pioneer 
    show dv normal pioneer at right
    show mi smile pioneer at left
    with dissolve
    "Забежав в клуб, я обнаружил там Электроника, Алису и Мику."
    sh "Ого Эл, да ты прям первый парень на деревне — вон сколько девок к тебе ходит, прямо табуны."
    show el shocked pioneer with dspr
    "Электроник покраснел пуще Лены — оно и понятно : Эла привыкли видеть в кампании Жени, а тут какие горячие дивчины  егo окружили."
    show mi upset pioneer at left with dspr
    mi "У нас провод сломался, репетировать не можем."
    "Почти плача сказала Мику."
    show dv angry pioneer at right with dspr
    dv "А ты , умник, вместо шуток помог бы нам."
    sh "Ты хоть представляешь объём работ?"
    show dv grin pioneer at right with dspr
    dv "А кто сказал что вы за просто так?"
    "Рыжая кокетливо посмотрела на нас с Элом."
    sh "И что ты предлагаешь?"
    show dv smile pioneer at right with dspr
    dv "На танцах разрешим пригласить себя на медляк."
    sh "Я мзду не беру, мне за науку обидно."
    "На Эла надеяться смысла нет — он в обморочном состоянии. Придётся спроваживать их своими силами."
    show mi cry pioneer at left with dspr
    mi "Ну Сааааааааш, ну помогите нам."
    sh "После похода подумаем, что и как, но не сейчас!"
    show mi grin pioneer at left with dspr
    mi "Честно-честно?"
    sh "Честно-честно!"
    show dv rage pioneer at right with dspr
    dv "Смотрите электрические, мы договорились."
    "Не удалось подкупить, так угрожает. Алис, в следующий раз попытайся получше."
    hide dv rage pioneer at right 
    hide mi grin pioneer at left
    with dissolve
    "Спровадив красоток куда подальше и приведя Эла в сознание, я взял то, зачем приходил. Но как я без особых проблем пронесу это, чтобы никто не заметил?"
    "Взяв старый мешок, закинул в него ткань, походную аптечку, старый фотоаппарат, сачок, даже сухпай нашёлся, не говоря уже о целом переда других полезных вещей."
    "Нельзя сказать, что всё это необходимо, но когда начинаешь готовится к походу, трудно остановится. Остальные могут подумать, что я переборщил, но так даже и лучше — нас и так считают странными, так что всё нормально."
    "Схватив рюкзак в одну руку, а Эла в другую, я  побежал на площадь, где уже строились пионеры." 
    scene ext_square_sunset with dissolve
    play music music_list["reminiscences"] fadein 3
    $ persistent.sprite_time = 'day'
    $ sunset_time()
    "Ольга уже была там, руководя и проверяя всё и вся."
    show mt normal pioneer with dissolve
    mt "А где электронные...а вот и вы. Теперь все в сборе. Разбейтесь на пары и идём."
    "Семён встал с Женей, Эл со Славей, и остальные тоже нашли себе пару."
    scene ext_path_sunset with dissolve
    "Я же шёл один. Как всегда. Это могло бы быть обидно, но в данном случае это сыграет на руку коварному плану Дмитриевны немного растормошить народ."
    "Весь путь я думал, как подойти поговорить с ней. Ведь есть о чём, да и я просто хочу этого."
    "Иногда простые вещи такие сложные. Я более чем уверен, что она сыграет свою странную, но от того не меньшую по значимости роль в нашем освобождении."
    "Ведь то, что она тоже настоящая, хотя и не является девушкой в гареме Семёна, а такой же случайный участник этих злоключений, которому не повезло."
    "А может...она мой ключ к свободе, а я её? "
    "Приятная мысль, но не реальная. Кто она, а кто я."
    scene ext_polyana_sunset with dissolve
    "Тем временем мы вышли на поляну, на которой разбили лагерь."
    "Все сразу засуетились, буквально растеклись по округе. Я остался у будущего костра , разводя руками."
    sh "А где все??"
    "Пришлось отправиться на поиски остальных."
    $ persistent.sprite_time = 'night'
    $ night_time()
    scene ext_polyana_night with dissolve
    play music Freedom_2 fadein 3
    "За поисками я и не заметил, как стемнело. Хотя в чаще я смог разглядеть одинокую фигуру, как раз там, где находится лесное озеро."
    sh "Оль, это ты?"
    show mt normal pioneer with dissolve
    mt "Да, я ждала тебя Саша, все эти годы."
    "Ольга вышла из тени."
    sh "Меня??"
    show mt scared pioneer with dspr
    mt "Ты разве не помнишь? Тогда, когда я сама ещё приезжала сюда отдыхать, ты был тут. Ты совсем не изменился, а я..."
    sh "Ты меня с кем-то путаешь!"
    show mt smile pioneer with dspr
    mt "Нет. Я не знаю, что это чудо или фокус, но вот ты передо мной — всё такой же молодой, честный и надёжный."
    sh "Быть того не может!!"
    "Она подошла ближе."
    show mt shy pioneer with dspr
    mt "Может. Судьба вновь свела нас. Вспомни...пожалуйста."
    "И она поцеловала меня в лоб."
    show blink
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene ext_square_old
    show prologue_dream with dissolve
    show mt_young at cleft behind prologue_dream with dissolve 
    show sh_unknown at cright behind prologue_dream with dissolve
    "Видение? Да. Но подобного я не помню! Вот этот парень похож на меня, а кто это за девушка? Неужели Оля?  Да, она."
    "Они счастливы, и улыбаются друг другу."
    "Неужели это я? Как я мог такое забыть?"
    sh "Но как..."
    mt "Я боялась, что я обозналась, но нет. Саша, я так счастлива! Мы теперь вместе."
    "Стоп. Значит...я тут так давно? И она, она отсюда вырывалась!!"
    "Спокойно Саша, не теряй контроль. Это шанс узнать ещё один способ освобождения."
    scene ext_polyana_night
    show mt shy pioneer 
    $ persistent.sprite_time = 'night'
    $ night_time()
    show unblink
    sh "Оля, нам о стольком надо поговорить..."
    mt "Пошли обратно в лагерь, там нам не помешают. И веселье уже само по себе началось."
    "Улыбнулась та."
    "Я посмотрел в её зелёные глаза. Словно свежая трава после росы!"
    sh "Теперь Оля, я пойду хоть на край света."
    scene ext_path_night with dissolve
    mt "Тогда пошли?"
    scene ext_house_of_mt_night_without_light with dissolve
    "Обратная дорога заняла намного меньше времени, как ни странно, но свежий воздух и физические нагрузки аля таскание  тяжелейших мешков сделали своё дело — я начал засыпать."
    scene int_house_of_mt_night2
    show mt normal pioneer 
    with dissolve
    mt "С тобой всё хорошо?"
    sh "Спать хочу, сил нет."
    mt "Я ждала много лет этой встречи."
    show mt sad pioneer with dspr
    "Она явно не обрадовалась моему состоянию."
    mt "Но подождать ещё пару часов в состоянии."
    play sound sfx_bed_squeak2
    hide mt normal pioneer with dissolve
    "Упав на кровать Семёна, я провалился в глубокий и сладкий сон. Но ощущение того, что я что-то не сделал, не давало мне покоя даже в царстве Морфея."
    "Не знаю, как мало я проспал, но просыпаться я начал весьма активно."
    
            
    return
