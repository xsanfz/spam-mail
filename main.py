from idlelib.replace import replace
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


my_name = "Сергей"
friend_name = "Дмитрий"
website = "https://dvmn.org/profession-ref-program/sergey.myamin/TK540/"
title = "Приглашение!"
sender = "rewaqz1@yandex.ru"
recipient = 'am1dok@yandex.ru'
content = "text/plain; charset='UTF-8';"

letter = ("""
From: {s}
To: {r}
Subject: {t}
Content-Type: {c}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format
          (t=title, s=sender, r=recipient, w=website, m=my_name,f=friend_name, c=content))

letter = letter.replace('%friend_name%', friend_name)

letter = letter.replace('%my_name%',my_name)

letter = letter.replace('%website%', website)

letter = letter.encode("UTF-8")

my_login = os.getenv("my_login")

my_pass = os.getenv("my_pass")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)

server.login(my_login, my_pass)

server.sendmail(sender, recipient, letter)

server.quit()
