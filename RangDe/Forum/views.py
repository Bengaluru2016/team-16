import os
from django.core.wsgi import get_wsgi_application
from django.core.mail import EmailMultiAlternatives
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "classproject2.settings")
application = get_wsgi_application()
from django.template import loader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.shortcuts import render
from Forum.models import *
from django.views.generic import TemplateView,ListView
from django.http.response import HttpResponse


def mail(request):
    return render(request, 'email.html')

def send_email(request):
    import smtplib
    fromaddr = 'srujanbelde18@gmail.com'
    toaddrs = request.GET.get('mail')
    name=request.GET.get('name')
    us=user(name=name,password='abcd',user_email=toaddrs,phoneNumber='12234')
    us.save()
    inv=Investor(investor_id=us,amount_invested=0,amount_returned=100)
    inv.save()
    msg = MIMEText("http://127.0.0.1:8000/new/")
    msg['Subject'] = 'subject'
    msg['From'] = 'xxx'
    msg['To'] = 'xxx'
    username = 'srujanbelde18@gmail.com'
    password = 'xxxx1234XXXX'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
    except Exception as e:
        print e
    return render(request, 'success.html')

def insert_answer(Request):
    l=Answers.objects.all()
    template=loader.get_template("bot.html")
    result=template.render(context={'list':l})
    return HttpResponse(result)

def Answerslist(Request):
    print Request.GET
    k = Request.GET.get('ne','name')
    docs1 = [

        ["I'm confused, Whats this initiative about?",
         "Rang De is a web based social initiative that supports rural entrepreneurs from low income households by providing access to low cost microcredit. We aim to address credit needs for business and education of the low income households we reach out to. Rang De microcredit for business and education is funded by individuals and corporate social investors."],

        ["What's the difference between the Rang De model and traditional micro-finance?",

         "Rang De is an innovative attempt to bring down the cost of microcredit by enabling individuals to lend small sums of money via our online portal (www.rangde.org). The main difference between Rang De and traditional microfinance is Rang De's focus on its mission to lower the interest rate and its fund raising model. By raising social investments from individuals, Rang De is able to bring down the cost of microcredit and offer loans to people at rates that were once unthinkable. "],

        ["Is Rang De a non-profit organisation?",

         "Yes, we are and we will always be. Read more about our organisation structure."],

        ["How is Rang De different from other peer-to-peer lending models?",

         "Rang De leverages the internet and the peer to peer model to lower the cost of microcredit. We ensure that we make good use of getting low cost capital from social investors and transfer the benefit to the end user. Our interest rates to the end user ranges from 6%flat p.a. to 10% flat p.a. Interest rates that the borrower pays for every loan product is published on the website. Rang De's field partners are not allowed to charge documentation charges or loan processing fees.If these come to light, depending on the severity, the partnership is either terminated or suspended. And yes, we do believe that just like there can be good stories, there are distress stories as well - both of which are shared with social investors."],

        ["What is the interest rate breakup on the loan products that Rang De offers?",
         "The interest rate breakup of borrower repayments (in flat rates) for each of our loan products is shown below. *APR interest rates are calculated on a monthly repayment schedule. The interest rate breakup of the yield to each stakeholder (in APY) for each of our loan products is shown below. *APY interest rates are calculated on a monthly repayment schedule."],

        ["What is the minimum and maximum investment?",

         "The minimum investment amount is INR 100 and the maximum investment amount can be anything the investor is willing to invest. A social investor can invest to fulfil the loan amount for a borrower or split their investments amongst multiple borrowers."]]

    def find_ques(query, vec, joinqa):
        dist = []
        query_vec = text_to_vector(query)
        for question in vec:
            dist.append(get_cosine(query_vec, question))
        max_value = max(dist)
        max_index = dist.index(max_value)
        return joinqa[max_index], max_value

    def tovec(doc):
        vec = []
        for qa in doc:
            vec.append(text_to_vector(qa))
        return vec

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    import re, math
    from collections import Counter

    WORD = re.compile(r'\w+')

    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    ### Converting a qunsetion answer to tf*idf vector
    def getqa(doc):
        qa = []
        ##joining question and answers to one vec
        for i in doc:
            qa.append(" ".join(i).lower())

        return qa

    joinqa = getqa(docs1)

    answer, _ = find_ques(k, tovec(joinqa), joinqa)
#    print("Most Similar Question: \n", question)
#    print("Similarity: \n", similarity)
    z = Answers(answer=answer)
    z.save()
    l=Answers.objects.all()
    template=loader.get_template("bot.html")
    result=template.render(context={'list':l})
    return HttpResponse(result)


def home(request):
    return render(request, 'index.html')

def register(Request):
    return render(Request, 'login.html')

def register_upload(request):
    a = request.GET.get('name','username')
    b = request.GET.get('password','password')
    c = request.GET.get('mail','abc@gmail.com')
    d=request.GET.get('number','1234567890')
    k = user(name=a, password=b, phoneNumber=d,user_email=c)
    k.save()
    return render(request, 'index.html.bak')


def login(Request):
    return render(Request, 'login.html')

def login_check(request):
    a = request.GET.get('name','username')
    b = request.GET.get('password','password')
    k=user.objects.all().filter(name=a)
    if(k.count()==0):
        return render(request, 'failed_page.html')
    ob=k.get(name=a)
    if(ob.password==b):
        return render(request, 'dashboard.html',{'user':k})
    return render(request, 'failed_page.html')
