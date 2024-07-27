import smtplib
import os

site = "https://dvmn.org/referrals/zQu8DE2BQc416VQUX2ZzGcJYXgrJgGQvX87L5UMo/"
friends_name = "Марина"
my_name = "Бершнев Марик"

letter = f"""From: bershnev.marik@yandex.ru
To: marpank@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friends_name}! {my_name} приглашает тебя на сайт {site}!

{site} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {site}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {site}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.encode("UTF-8")

my_login = os.environ['YA_LOGIN']
my_password = os.environ['YA_PASSWORD']
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(my_login, my_password)
server.sendmail("bershnev.marik@yandex.ru", "marpank@yandex.ru", letter)
server.quit()