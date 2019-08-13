import datetime
import random

from django.shortcuts import render

# Create your views here.
# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >>> 로직 작성 <<<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 변수를 딕셔너리에 담아서 (보통 context라고 부름)
    context = {'numbers': numbers}
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)!
    return render(request, 'lotto.html', context)

def dinner(request):
    menu_box = ['홍루이젠', '맘스터치', '컵라면', '푸라닭', '편의점도시락']
    pick = random.choice(menu_box)
    context = {
        'pick': pick,
        'menu_box': menu_box,
        'users': [],
        'sentence': 'Life is short, You need Python + django!',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google.com'
    }
    return render(request, 'dinner.html', context)

def cube(request, num):
    context = {
        'num': num,
        'result': num**3,
        'numbers': [1, 2, 3],
        'students': {'지수': '지수!', '태수': '태수!'}
    }
    return render(request, 'cube.html', context)

def about(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'about.html', context)

def isitgwangbok(request):
    today = datetime.datetime.now()
    if today.month == 8 and today.day == 15:
        result = '예'
    else:
        result = '아니오'
    context = {
        'isit': result,
    }
    return render(request, 'isitgwangbok.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    print(request.GET) 
    # QueryDict {'data': '안녕하세요'}
    data = request.GET.get('data')
    context = {
        'data': data
    }
    return render(request, 'pong.html', context)

def signup(request):
    return render(request, 'signup.html')

def signup_result(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirm')
    if password == password_confirm:
        result = '{}님, 회원가입을 완료하였습니다.'.format(username)
    else:
        result = '패스워드가 일치하지 않습니다.'
    context = {
        'result': result
    }
    return render(request, 'signup_result.html', context)