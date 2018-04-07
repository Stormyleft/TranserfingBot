# -*- coding: utf-8 -*-
# Texts
start_message = 'Привет!\nЭто бот-аудиокнига.'
books_message = ['Приятного чтения.\nЕсли это можно так назвать 🤔',
                 'Реальность существует независимо от вас. До тех пор, пока вы с этим согласны.',
                 'Лучший способ предсказать своё будущее – стать его создателем.',
                 'Безусловная любовь — это чувство без права обладания.',
                 'Необходимо просто перестать биться как муха о стекло и перенаправить намерение '
                 'на развитие достоинств, не заботясь о своём положении на лестнице превосходства.',
                 'Своими мыслями вы строите уникальную, индивидуальную версию своего мира.',
                 'Что бы ни происходило, объявляйте своей волей Вершителя: все идет как надо.',
                 'Вы получите все, что намерены иметь, если убеждены, что это ваше, без всяких оговорок и условий.',
                 'Радуйтесь всему, что имеете в данный момент. Позитивный настрой всегда ведёт к успеху и созидани',
                 'Чтобы достигнуть желаемого, думайте о цели, а не о богатстве. '
                 'Деньги придут сами, поскольку являются сопутствующим атрибутом.',
                 'Когда вы чересчур сильно хотите чего-либо получить - так, что готовы все поставить на карту, '
                 'то создаете огромный избыточный потенциал, нарушающий равновесие. '
                 'Равновесные силы отбросят вас на линии жизни, где желаемого предмета нет и в помине.',
                 'Не цель достигается с помощью денег, а деньги приходят на пути к цели.',
                 'Единственным препятствием на пути к исполнению желания является искусственно созданная важность.',
                 'Душа хочет не денег, а того, что можно на них купить. Вы точно знаете, чего хотите? '
                 'Скорее всего, нет. Вот и спросите себя, чего на самом деле хочется от жизни. '
                 'Что превратит вашу жизнь в праздник? Определите свою цель.',
                 'Научитесь балдеть от плохой погоды, от очередей, пробок, проблем, любого негатива. '
                 'Такой вот своего рода мазохизм постепенно расчистит небо над Вашим миром. '
                 'Вам следует задумываться лишь над тем, какой выгодой обернется для Вас то или иное '
                 'досадное обстоятельство. А так оно и будет — сами в том убедитесь неоднократно.',
                 'Сложнее всего — уметь ждать, сохраняя при этом спокойствие хозяина ситуации. '
                 'Необходимо выдержать испытание паузой, в течение которой ничего не происходит',
                 'Позволить себе быть собой — значит принять себя со всем своим несовершенством. '
                 'Позволить другому быть другим — значит снять с него проекции своих ожиданий. '
                 'В результате ситуация, когда один хочет то, чего другой не приемлет, '
                 'непостижимым образом разрешится сама собой',
                 'Ваш Смотритель не должен спать. Одергивайте себя всякий раз, когда по привычке, '
                 'как во сне, принимаете игру маятника, то есть проявляете беспокойство, '
                 'выказываете недовольство, негодование, участвуете в деструктивных обсуждениях и так дале',
                 'Проявляя недовольство чем-либо или ругая кого-либо — правительство, госслужащих, '
                 'футболистов, погоду, коллег, соседей, близких, не говоря уж о детях, — вы транслируете '
                 'в зеркало мира неприглядный образ и получаете соответствующую реальность в отражении',
                 'Чудо произойдет только в том случае, если вы сломаете привычный стереотип и '
                 'будете думать не о средствах достижения, а о самой цели.',
                 'В любой проблеме зашифрованы ключи к ее решению. Самый первый ключ — двигаться по пути '
                 'наименьшего сопротивления. Люди, как правило, ищут сложные решения, потому, что, воспринимают '
                 'проблемы как препятствия, а препятствия, как известно, преодолевать положено с напряжением сил. '
                 'Необходимо выработать привычку выбирать самый простой подвернувшийся вариант решения проблемы.',
                 'Если вам приходится себя уговаривать, значит, душа говорит «нет».',
                 'Склонность к негативизму порождает все новые неприглядные черты в зеркале.  Думайте о хорошем!',
                 'Когда начинаешь жить для себя, делать, что нравится, — все остальное в мире подтягивается, '
                 'чтоб соответствовать. Все очень просто: если душа и разум пребывают в согласии, '
                 'остальное налаживается автоматически.',
                 'Когда человек наполнен радостным вдохновением, его душа «поет», а разум «удовлетворенно '
                 'потирает руки». Именно в таком состоянии человек способен творить.',
                 'Если порядок дел не имеет принципиального значения, просто делайте так как делается, '
                 'двигайтесь вместе с потоком, отвяжите свой разум от влияния маятников',
                 'Сны не являются иллюзиями в обычном понимании этого слова. Разум не воображает их, '
                 'а действительно видит.',
                 'К жизни нужно относиться проще. Не пренебрегать, но и не приукрашивать. Поменьше размышлять о том, '
                 'какие люди – хорошие или плохие. Принимать мир в его обыденном проявлении.',
                 'Наши мысли оказывают непосредственное влияние на ход событий нашей жизни.',
                 'Прежде чем браться за решение проблемы, необходимо снизить ее важность. '
                 'Тогда равновесные силы не будут мешать, и проблема решится легко и просто.'
                 'Скажите себе, что ваш мир обо всем позаботится, и больше ни о чем не беспокойтесь.']
back_message = 'Выбери книгу'
back_button = 'Назад'

# Апокрифический Трансерфинг
apokr_parts = {'0. Вадим Зеланд': 'CQADAgADBAEAAp0HkUqg0oi_736zFQI',
               '1. Мы проснулись в Другой Реальности': 'CQADAgADBQEAAp0HkUpFmlttPi9u4QI',
               '2. Цель, путь, или пункт назначения. Стр 1': 'CQADAgADBgEAAp0HkUoVvzWugaRHMgI',
               '3. Цель, путь, или пункт назначения. Стр 2': 'CQADAgADCAEAAp0HkUpM-kJ5bXXsxwI',
               '4. Цель, путь, или пункт назначения. Стр 3': 'CQADAgADCQEAAp0HkUr8HD9VGBD3ZgI',
               '5. Кредо Вершителя': 'CQADAgADCgEAAp0HkUp2mjwvN29o4AI',
               '6. Мир Сновидений': 'CQADAgADDAEAAp0HkUqjJWNayKs5swI',
               '7. Здравствуйте, товарищи Киборги!': 'CQADAgADDQEAAp0HkUq6juzbHcuwvgI',
               '8. Паразиты сознания': 'CQADAgADDgEAAp0HkUoYaHhiev95cAI',
               '9. Поговорим о Кексе. Стр 1': 'CQADAgADDwEAAp0HkUqhvGVwv76ofgI',
               '10. Поговорим о Кексе. Стр 2': 'CQADAgADEQEAAp0HkUqp7FCDEhMzSQI',
               '11. Стакан Воды': 'CQADAgADEgEAAp0HkUpWSpo8_gZ59gI',
               '12. Вторая Цивилизация. Стр 1': 'CQADAgADEwEAAp0HkUpWYhS9shSYogI',
               '13. Вторая Цивилизация. Стр 2': 'CQADAgADFQEAAp0HkUrP6UF032w0ggI',
               '14. Шаг из Строя': 'CQADAgADFgEAAp0HkUreQZ3L6qA0VAI',
               '15. Механика Старения': 'CQADAgADGAEAAp0HkUrJco-wuW7kpQI',
               '16. Скрытая Угроза': 'CQADAgADGQEAAp0HkUo3VNvNAAHwoSYC',
               '17. Паразиты Тела': 'CQADAgADGgEAAp0HkUr9eoou1pc4CQI',
               '18. Архитекторы Матрицы': 'CQADAgADGwEAAp0HkUqXSdNm0keNMAI',
               '19. Живая Вода. Стр 1': 'CQADAgADHAEAAp0HkUrDfllNr1bpOAI',
               '20. Живая Вода. Стр 2': 'CQADAgADHQEAAp0HkUozxdsMjJjeGgI',
               '21. Живая Вода. Стр 3': 'CQADAgADHgEAAp0HkUpqXBKlM9OzXwI',
               '22. Хрустальный Камертон': 'CQADAgADHwEAAp0HkUqqz1q4sLIhJQI',
               '23. Живой Воздух': 'CQADAgADIAEAAp0HkUqujE3Fa4oKzAI',
               '24. И снова Вперед в Прошлое': 'CQADAgADIQEAAp0HkUo9ZQEojTlcPgI',
               '25. Процесс Старения идет Вспять': 'CQADAgADIgEAAp0HkUo0ctLTvh8plwI',
               '26. Знание не для Всех': 'CQADAgADIwEAAp0HkUpRzzoI7tJscwI',
               '27. Живая Пища. Стр 1': 'CQADAgADJAEAAp0HkUpze6TkMNpTQwI',
               '28. Живая Пища. Стр 2': 'CQADAgADJQEAAp0HkUpVdCtTjxXafgI',
               '29. Живая Пища. Стр 3': 'CQADAgADJgEAAp0HkUr41gdaWVSo7AI',
               '30. Энергия Намерения': 'CQADAgADJwEAAp0HkUr38e6CtktrPwI',
               '31. Намерение Здоровья. Стр 1': 'CQADAgADKAEAAp0HkUq_Ab3aKzRITgI',
               '32. Намерение Здоровья. Стр 2': 'CQADAgADKQEAAp0HkUr31FSot17eBgI',
               '33. Приложение 1. Стр 1': 'CQADAgADLwEAAp0HkUquFZWr_jxeTAI',
               '34. Приложение 1. Стр 2': 'CQADAgADMQEAAp0HkUrDQjHG-nxbTAI',
               '35. Приложение 1. Стр 3': 'CQADAgADMgEAAp0HkUr868Gn-Zh1nwI',
               '36. Приложение 1. Стр 4': 'CQADAgADMwEAAp0HkUpsufWGNt-i3gI',
               '37. Приложение 1. Стр 5': 'CQADAgADNAEAAp0HkUqklpaMJEAR-gI',
               '38. Приложение 2. Стр 1': 'CQADAgADNQEAAp0HkUoSuHmf2vtg9AI',
               '39. Приложение 2. Стр 2': 'CQADAgADNgEAAp0HkUoWoDqdhP9QugI',
               '40. Приложение 3': 'CQADAgADNwEAAp0HkUqQpe6NZEozVAI',
               '41. Приложение 4. Стр 2': 'CQADAgADOAEAAp0HkUrxn1EzmmC37QI',
               '42. Приложение 5. Стр 1': 'CQADAgADOQEAAp0HkUpdwNEqimL-MAI',
               '43. Приложение 5. Стр 2': 'CQADAgADOgEAAp0HkUrrsR4RKAgargI',
               '44. Приложение 6. Стр 1': 'CQADAgADOwEAAp0HkUq4fyryVErwjAI',
               '45. Приложение 6. Стр 2': 'CQADAgADPAEAAp0HkUqHereqGDfW0AI',
               '46. Приложение 7': 'CQADAgADPQEAAp0HkUq9QsC9nv8fqwI'}

# Ступень 1 - Пространство Вариантов
stup1_parts = {'1. Шелест Утренних Звезд': 'CQADAgADEQEAAp4uqEoV7UBTV2YzYQI',
               '2. Загадка Смотрителя ч.1': 'CQADAgADYQAD9le4Sohq189gN4u9Ag',
               '3. Загадка Смотрителя ч.2': 'CQADAgADYgAD9le4Sib9vDAfCLUuAg',
               '4. Резюме 1-С1': 'CQADAgADEwEAAp4uqEphCW3r-B-sTAI',
               '5. Деструктивные Маятники': 'CQADAgADFAEAAp4uqEqkjLcnegtVvgI',
               '6. Битва Маятников': 'CQADAgADFQEAAp4uqEqYt7CrovayVQI',
               '7. Нити Марионеток': 'CQADAgADFgEAAp4uqEqENfxBTPS6LAI',
               '8. Вы Получаете То Чего Не Хотите': 'CQADAgADFwEAAp4uqEqAExlpKtd4dQI',
               '9. Провал Маятника': 'CQADAgADGAEAAp4uqEpb5YFBrywP3gI',
               '10. Гашение Маятника': 'CQADAgADGQEAAp4uqEoqns0WgsItmgI',
               '11. Простые Решения Сложных Проблем': 'CQADAgADGgEAAp4uqEoSMrKf6V3p5AI',
               '12. Подвешеное Состояние': 'CQADAgADGwEAAp4uqEoBvVYYWZf6xAI',
               '13. Резюме 2-С1': 'CQADAgADHAEAAp4uqEqYUtiwwlhiOQI',
               '14. Антипод Маятника': 'CQADAgADHQEAAp4uqEpm9dCZiFYnxgI',
               '15. Бумеранг': 'CQADAgADHgEAAp4uqEp87IfX8EIjQgI',
               '16. Трансляция': 'CQADAgADHwEAAp4uqEpsWGr9_HBN3QI',
               '17. Магические Ритуалы': 'CQADAgADIAEAAp4uqEre_VYkHGO3fwI',
               '18. Резюме 3-С1': 'CQADAgADIQEAAp4uqEqGarfQLYIkGQI',
               '19. Избиточние Потенциалы': 'CQADAgADIgEAAp4uqEr7zG4W3MVv_wI',
               '20. Недовольство и Осуждение': 'CQADAgADIwEAAp4uqEo-UjX97F-1PgI',
               '21. Отношение Зависимости': 'CQADAgADJAEAAp4uqEqNYB6ixVOAXwI',
               '22. Идеализация и Переоценка': 'CQADAgADJQEAAp4uqEpdW-BLcwABWfkC',
               '23. Презрение и Тщеславие': 'CQADAgADJgEAAp4uqEqrL6EKdbxRzQI',
               '24. Превосходство и Неполноценность': 'CQADAgADJwEAAp4uqEqOG6QVMy93aQI',
               '25. Желание Иметь и Не Иметь': 'CQADAgADKAEAAp4uqEqzVnBLms5fZwI',
               '26. Чувство Вины': 'CQADAgADKQEAAp4uqEoEoxkgAAFuR-0C',
               '27. Деньги': 'CQADAgADKgEAAp4uqEoj0Cdup6qMfwI',
               '28. Совершенство': 'CQADAgADKwEAAp4uqEpO1GpM0K45sAI',
               '29. Важность': 'CQADAgADLAEAAp4uqEqA5en918gg4AI',
               '30. От Борьбы к Равновесию': 'CQADAgADLQEAAp4uqEqrmn4uqZGRsgI',
               '31. Резюме 4-С1': 'CQADAgADLgEAAp4uqErHA5ufM_g0PAI',
               '32. Смещение Поколений': 'CQADAgADLwEAAp4uqEqsFuhjm8-HeQI',
               '33. Воронка Маятника': 'CQADAgADMAEAAp4uqEpvh4F95LGSNQI',
               '34. Катастрофа': 'CQADAgADeAADni6wSiFNc9VgFrEZAg',
               '35. Война': 'CQADAgADMQEAAp4uqEqXAuOymsyOUwI',
               '36. Безработица': 'CQADAgADMgEAAp4uqErP-YACMS043AI',
               '37. Эпидемия': 'CQADAgADMwEAAp4uqEpo_-Ef2JhBAAEC',
               '38. Паника': 'CQADAgADNAEAAp4uqEqT4fes8d4RHAI',
               '39. Нищета': 'CQADAgADNQEAAp4uqEqxE1TwvR1c2wI',
               '40. Резюме 5-С1': 'CQADAgADNgEAAp4uqEpILIqbSFyE_QI',
               '41. Поле Информации': 'CQADAgADNwEAAp4uqEpruI9nIUqjNgI',
               '42. Знания Ниоткуда': 'CQADAgADOQEAAp4uqEpXv9TSUOW-UAI',
               '43. Проситель, Обиженный и Воитель': 'CQADAgADOgEAAp4uqEqh9wsEDkSHyAI',
               '44. Движение по Течению': 'CQADAgADOwEAAp4uqEps71UgSo6ViQI',
               '45. Путеводные Знаки': 'CQADAgADPAEAAp4uqErGfFJn9Go8wQI',
               '46. Отпустить Ситуацию': 'CQADAgADPQEAAp4uqEpINr3clubQ1gI',
               '47. Резюме 6-С1': 'CQADAgADPgEAAp4uqErnDcJe9nls4QI'}

# Ступень 2 - Шелест Утренних Звезд
stup2_parts = {'1. Пробуждение во Сне': 'CQADAgADcgEAAp4uqEpEjv3s_mGe7wI',
               '2. Пространство Сновидений': 'CQADAgADcwEAAp4uqErH0kpdLIs7vwI',
               '3. Волшебная Сила Намерения': 'CQADAgADdAEAAp4uqErjXz-8JPd_XwI',
               '4. Внешнее Намерение ч.1': 'CQADAgADYwAD9le4Smi_AxwdE1HcAg',
               '5. Внешнее Намерение ч.2': 'CQADAgADZAAD9le4SnWz1Fid_nv-Ag',
               '6. Сценарий Игры': 'CQADAgADdgEAAp4uqEqo8RfqXMSNsQI',
               '7. Игра по Вашим Правилам': 'CQADAgADeAEAAp4uqErOir1Z92xgawI',
               '8. Очистка Намерения': 'CQADAgADegEAAp4uqEqH4MMGZiP-UwI',
               '9. Резюме 1-С2': 'CQADAgADewEAAp4uqErIxfGQCU65mQI',
               '10. Иллюзии': 'CQADAgADfAEAAp4uqEqJQWsXftYtVgI',
               '11. Искривление Реальности': 'CQADAgADfQEAAp4uqEpRer48RFU7_QI',
               '12. Позитивние Слайды': 'CQADAgADfgEAAp4uqEqnpjr-ftizZwI',
               '13. Расширение Зоны Комфорта': 'CQADAgADfwEAAp4uqEozbom5elGPjwI',
               '14. Визуализация Цели': 'CQADAgADgAEAAp4uqEo8LVx1VQsoHQI',
               '15. Визуализация Процесса': 'CQADAgADgQEAAp4uqEreWznZM5_uvAI',
               '16. Трансферние Цепочки': 'CQADAgADggEAAp4uqEr7axG1KrzjEwI',
               '17. Резюме 2-С2': 'CQADAgADgwEAAp4uqEpp-aumKR4ePAI',
               '18. Ветер Намерения': 'CQADAgADhAEAAp4uqEq0d3sgpOapNwI',
               '19. Парус Души': 'CQADAgADhQEAAp4uqEoPAyehLDOm1AI',
               '20. Волшебник Внутри Нас': 'CQADAgADhgEAAp4uqEoJedekm_rHBAI',
               '21. Мираж': 'CQADAgADhwEAAp4uqEptHVv8dbdn8QI',
               '22. Ангел Хранитель': 'CQADAgADiAEAAp4uqEoIsWcuioqOtgI',
               '23. Футляр Для Души': 'CQADAgADiQEAAp4uqEpZvn9J_KQJHAI',
               '24. Фреиле': 'CQADAgADigEAAp4uqEq-pV3YU1IpGwI',
               '25. Единство Души и Разума': 'CQADAgADiwEAAp4uqEo5B4EeowABuZIC',
               '26. Звуковые Слайды': 'CQADAgADjAEAAp4uqEp8CKeIKNDQsAI',
               '27. Окно в Пространство Вариантов': 'CQADAgADjQEAAp4uqEpcY9WGtJbe_QI',
               '28. Фрейм': 'CQADAgADjgEAAp4uqEpuV4-VWovYjQI',
               '29. Резюме 3-С2': 'CQADAgADjwEAAp4uqEq_9aN-8QXJ0AI',
               '30. Как Выбирать Свои Вещи': 'CQADAgADkAEAAp4uqErhH4-N6xI7jgI',
               '31. Как Диктовать Моду': 'CQADAgADkQEAAp4uqEr9VeGk3XsLAQI',
               '32. Чужие Цели': 'CQADAgADkgEAAp4uqEr9MHv8RWcjvgI',
               '33. Взлом Стереотипов': 'CQADAgADkwEAAp4uqEpshKBp8KxrUwI',
               '34. Ваши Цели': 'CQADAgADlAEAAp4uqEoCV5TgLjJeFQI',
               '35. Ваши Двери': 'CQADAgADlQEAAp4uqEp3cYW2juN3FwI',
               '36. Намерение': 'CQADAgADlgEAAp4uqEoucMIy227yBgI',
               '37. Реализация': 'CQADAgADlwEAAp4uqErAmPD6p19anwI',
               '38. Вдохновение': 'CQADAgADmAEAAp4uqEqiVfIOucNA5QI',
               '39. Реанимация Цели': 'CQADAgADmQEAAp4uqEqWqt-kCiME9QI',
               '40. Резюме 4-С2': 'CQADAgADmgEAAp4uqErYmiNgSYpAxgI'}

stup3_parts = {'1. Энергетика': 'CQADAgADUAADni6wSqkcXTTPcjb5Ag',
               '2. Стресс и Релаксация': 'CQADAgADUQADni6wSjDZSbetoHCbAg',
               '3. Энергетические Вампиры': 'CQADAgADUgADni6wSqMmwQUFA_UtAg',
               '4. Защитная Оболочка': 'CQADAgADUwADni6wSu_JROBeWSn4Ag',
               '5. Повышение Энергетики': 'CQADAgADVAADni6wShUbEuBhJu5dAg',
               '6. Энергия Намерения': 'CQADAgADVQADni6wSkxEpi2VzQopAg',
               '7. Шаг Намерения': 'CQADAgADVgADni6wSrRFGtybl_h-Ag',
               '8. Маятники Болезней': 'CQADAgADVwADni6wSlsoNQdMq6-jAg',
               '9. Резюме 1-С3': 'CQADAgADWAADni6wSrVOI4cZ-cXcAg',
               '10. Намерение Отношений': 'CQADAgADWQADni6wShtdmCm1pA7AAg',
               '11. Течение Отношений': 'CQADAgADWgADni6wSn4MuGd96K6RAg',
               '12. Настройка на Фреиле': 'CQADAgADWwADni6wSsR7uFh12_jFAg',
               '13. Энергия Отношений': 'CQADAgADXAADni6wSq2b8wLTCTfoAg',
               '14. Индулгенция': 'CQADAgADXQADni6wSgNbh7YTWemwAg',
               '15. Поиск Работы': 'CQADAgADXgADni6wSvzaEPnoKI50Ag',
               '16. Резюме 2-С3': 'CQADAgADXwADni6wSgt4K4RE0b8mAg',
               '17. Лабиринт Неуверенности': 'CQADAgADYAADni6wSlKJDPEWMxYmAg',
               '18. Координация Важности': 'CQADAgADYQADni6wSuqjVhrNwPtDAg',
               '19. Битва с Глиняным Болваном': 'CQADAgADYgADni6wSvW-iiKTtj5MAg',
               '20. Прекращение Битвы': 'CQADAgADYwADni6wSpDIHxk1pZ6wAg',
               '21. Освобождение': 'CQADAgADZAADni6wSnmVXz5tBLRgAg',
               '22. Координация Намерения': 'CQADAgADZQADni6wSnc1dOpC_nt6Ag',
               '23. Яблоки Падают в Небо': 'CQADAgADZgADni6wSl3mNJHSVaQjAg',
               '24. Резюме 3-С3': 'CQADAgADZwADni6wSl3lOcN8RKyeAg',
               '25. Транзакция': 'CQADAgADaAADni6wSvXGlF-NlFKaAg',
               '26. Оттенки Декораций': 'CQADAgADaQADni6wSgusZTOkBDBZAg',
               '27. Скольжение.': 'CQADAgADdwADni6wSnvas4bPXwTeAg',
               '28. Резюме 4-С3': 'CQADAgADagADni6wSlEPRTuPUnn7Ag',
               '29. Черные Полосы': 'CQADAgADawADni6wStZ7urDtCvUHAg',
               '30. Игра Партнеров': 'CQADAgADbAADni6wSuIY9sYiVDyVAg',
               '31. Благотворительность': 'CQADAgADbQADni6wSmPz-32UdiWBAg',
               '32. Эзотерическое Знание': 'CQADAgADbgADni6wSl4P-68QcS-8Ag',
               '33. Как Вернуть Любимых': 'CQADAgADbwADni6wSg0dZtmo_Mi1Ag',
               '34. Намерение': 'CQADAgADcAADni6wSrUGy-cmmPndAg',
               '35. Потенциалы Важности. Стр 1': 'CQADAgADcQADni6wSvEa6CNb1d62Ag',
               '36. Инверсия Реальности': 'CQADAgADcgADni6wSpH4McqN3LdrAg',
               '37. Странная Реальность': 'CQADAgADcwADni6wSlNuLNpkbv3AAg',
               '38. Намерение Древних Магов': 'CQADAgADdAADni6wStLhLV8XYiNyAg',
               '39. Эпилог С3': 'CQADAgADdQADni6wSv4Uq90bLwjiAg'}

# Книги
books = ['Ступень 1 - Пространство Вариантов',
         'Ступень 2 - Шелест Утренних Звезд',
         'Ступень 3 - Вперёд в Прошлое']          # 1
not_used_books = ['Апокрифический Трансерфинг',
                  'empty',
                  'empty']
books_parts = [stup1_parts, stup2_parts, stup3_parts]        # 2
not_used_books_parts = [apokr_parts]


"""
Дополнительные операции

"""
count = 0
books_all = {}
for i in books:
    books_all[i] = books_parts[count]
    count = count + 1
all_parts = {}
for i in books_parts:
    all_parts.update(i)
all_parts_keys = list(all_parts.keys())

"""
Комментарии:



"""
