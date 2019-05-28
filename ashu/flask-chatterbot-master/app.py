import sys
#from imp import reload
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
from dateutil.relativedelta import relativedelta
from chatterbot.comparisons import levenshtein_distance
import random

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter", logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            'threshold': 0.70,
            'default_response': '抱歉，我目前只知道有關醫療方面的知識，您可以跟我多聊聊這方面的事情。'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')

english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")
english_bot.train("chatterbot.corpus.tchinese.cgmhbot")
english_bot.train("chatterbot.corpus.tchinese.medical")
english_bot.train("chatterbot.corpus.tchinese.medical_knowledge")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
    now = datetime.datetime.now()
    date_now = str(now.year)+"年"+str(now.month)+"月"+str(now.day)+"號"
    time_now = str(now.hour)+"點"+str(now.minute)+"分"+str(now.second)+"秒"
    weekday = datetime.datetime.today().weekday()
    if mytchTimeExpression1 in userText :
        return str(random.choice(tchtimeStatements)+ time_now)
    elif mytchTimeExpression2 in userText :
        return str(random.choice(tchtimeStatements)+ time_now)
    elif mytchTimeExpression3 in userText :
        return str(random.choice(tchtimeStatements)+ time_now)
    elif mytchDateExpression1 in userText :
        return isToday(userText)
    elif mytchDateExpression2 in userText :
        return isToday(userText)
    elif mytchDateExpression3 in userText :
        return isToday(userText)
    elif mytchDayExpression1 in userText :
        return isWeekDay(userText)
    elif today in userText :
        print("here")
        return today+"是"+day[weekday]
    elif tomorrow in userText :
        weekday = (weekday + 1)%7
        return tomorrow+"是"+day[weekday]
    elif yesterday in userText :
        weekday = (weekday - 1)%7
        return yesterday+"是"+day[weekday]
    elif dayBeforeYesterday in userText :
        weekday = (weekday - 2)%7
        return dayBeforeYesterday +"是"+day[weekday]
    elif dayAfterTomorrow in userText :
        weekday = (weekday + 2)%7
        return dayAfterTomorrow+"是"+day[weekday]
    else:
        print(str(english_bot.get_response(userText)))
        return str(english_bot.get_response(userText))


def isToday(userText):
   print("here")
   if tomorrow in userText :
      date_after_month = datetime.datetime.today()+ relativedelta(days=1)
      date_now = str(date_after_month.strftime('%Y'))+"年"+str(date_after_month.strftime('%m'))+"月"+str(date_after_month.strftime('%d'))+"號"
      return tomorrow+"是"+date_now
   elif yesterday in userText :
      date_after_month = datetime.datetime.today()+ relativedelta(days=-1)
      date_now = str(date_after_month.strftime('%Y'))+"年"+str(date_after_month.strftime('%m'))+"月"+str(date_after_month.strftime('%d'))+"號"
      return yesterday+"是"+date_now
   elif dayBeforeYesterday in userText :
      date_after_month = datetime.datetime.today()+ relativedelta(days=-2)
      date_now = str(date_after_month.strftime('%Y'))+"年"+str(date_after_month.strftime('%m'))+"月"+str(date_after_month.strftime('%d'))+"號"
      return dayBeforeYesterday+"是"+date_now
   elif dayAfterTomorrow in userText :
      date_after_month = datetime.datetime.today()+ relativedelta(days=2)
      date_now = str(date_after_month.strftime('%Y'))+"年"+str(date_after_month.strftime('%m'))+"月"+str(date_after_month.strftime('%d'))+"號"
      return dayAfterTomorrow+"是"+date_now
   else:
      date_now = str(now.year)+"年"+str(now.month)+"月"+str(now.day)+"號"
      return today+"是"+date_now

def isWeekDay(userText):
   weekday = datetime.datetime.today().weekday()
   if tomorrow in userText :
      weekday = (weekday + 1)%7
      return tomorrow+"是"+day[weekday]
   elif yesterday in userText :
      weekday = (weekday - 1)%7
      return yesterday+"是"+day[weekday]
   elif dayBeforeYesterday in userText :
      weekday = (weekday - 2)%7
      return dayBeforeYesterday +"是"+day[weekday]
   elif dayAfterTomorrow in userText :
      weekday = (weekday + 2)%7
      return dayAfterTomorrow+"是"+day[weekday]
   else:
      return today+"是"+day[weekday]


if __name__ == "__main__":
    app.run(host='163.25.101.53', port=5000)
