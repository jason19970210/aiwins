import sys
#from imp import reload
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
from dateutil.relativedelta import relativedelta
#from chatterbot.comparisons import levenshtein_distance
import random

app = Flask(__name__)

mytchTimeExpression1 = "時間";
mytchTimeExpression2 = "幾點";
mytchTimeExpression3 = "現在幾點";

mytchDayExpression1 = "星期幾" #which day of the week

mytchDateExpression1 = "幾月幾號" #What's the date of the month
mytchDateExpression2 = "日期"    #What's the date of the month

mytchDateExpression3 = "幾號" #What's the date of the month

#"星期一" #Monday
#"星期二" #Tuesday
#"星期三" #Wednesday
#"星期四" #Thursday
#"星期五" #Friday
#"星期六" #Saturday
#"星期天" #Sunday

day = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]

today = "今天" #Today
yesterday = "昨天" #Yesterday
tomorrow = "明天" #Tomorrow
dayBeforeYesterday = "前天" #The day before Yesterday
dayAfterTomorrow = "後天" #The day after tomorrow


mytchTime = "現在幾點？"
tchtimeStatements = [ "現在時間是" ]
tchdateStatements = [ "今天日期是" ]
tchdayStatements  = [ "今天是" ]
now = datetime.datetime.now()
date_now = str(now.year)+"年"+str(now.month)+"月"+str(now.day)+"號"
time_now = str(now.hour)+"點"+str(now.minute)+"分"+str(now.second)+"秒"
weekday = datetime.datetime.today().weekday()

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.tchinese.cgmhbot")
english_bot.train("chatterbot.corpus.tchinese.medical")
english_bot.train("chatterbot.corpus.tchinese.medical_knowledge")
#english_bot.train("chatterbot.corpus.tchinese.medicalknowledge")
english_bot.train("chatterbot.corpus.tchinese.Breast_Surgery_Clinic")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
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
    #if sys.version[0] == '2':
        #reload(sys)
        #sys.setdefaultencoding("utf-8")
    app.run(host='163.25.101.53', port=5000)
