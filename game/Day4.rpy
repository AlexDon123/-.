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
    return

