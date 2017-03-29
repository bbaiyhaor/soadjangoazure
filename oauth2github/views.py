#encoding=utf-8
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
# Create your views here.
import requests
import redis
myredis = redis.Redis(host='localhost', port=6379, db=0)
r_session = requests.session()
client = '3220497fa6d85d277f83'
client_secret = '3a1f65a7e484dfaca244c7fd588fa12c611a7f12'
oauth_url = 'https://github.com/login/oauth/access_token'
api_url = 'https://api.github.com/user'
user_name = ''
email = ''

def index(request, username, email):
    dict = {'username': username, 'email' : email}
    return render(request, 'oauth2github/index.html', {'dict' : dict})

def red(request):
    code = request.GET.get('code')

    data = {
        'code': code,
        'client_id' : client,
        'client_secret' : client_secret,
    }
    headers = {'Accept' : 'application/json'}
    req = r_session.post(oauth_url, data=data, headers=headers)
    rej = req.json()
    if (rej.get('access_token') == None):
        return  HttpResponseRedirect('/login')
    urlr = api_url + '?' + 'access_token=' + rej.get('access_token')
    req = r_session.get(urlr)
    rej = req.json()
    global user_name, email
    user_name = rej['login']
    email = rej['email']
    dict = {'username':rej['login'], 'email':rej['email']}
    return HttpResponseRedirect(reverse("site_index", kwargs=dict))

def login(request):
    dict = {'client_id' : client}
    c = {'dict': dict}

    return render(request, 'oauth2github/login.html', c)

def cmp(dict):
    return dict['hi']

def search(request):
    domain = request.GET.get('domain')
    pros = myredis.smembers(domain)
    #print len(pros)
    list = []
    for it in pros:
        pro = myredis.hgetall(it)
        list.append(pro)
    slist = sorted(list, key=cmp)
    list = []
    for it in slist:
        st = 'name: ' + it['name'] + ' ---- ' + 'hi: ' + it['hi']
        index = it['index']
        list.append({'st':st,'index':index})
    #print len(list)
    dict = {'professor': list}
    return JsonResponse(dict)

def domainapi(request):
    domain = request.GET.get('domain')
    pros = myredis.smembers(domain)
    print len(pros), domain
    list = []
    for it in pros:
        pro = myredis.hgetall(it)
        list.append(pro)
    slist = sorted(list, key=cmp)
    list = []
    for it in slist:
        list.append({'name': it['name'], 'index': it['index'], 'hi':it['hi']})
    dict = {'professor': list}
    return JsonResponse(dict)

def coauapi(request):
    author = request.GET.get('author')
    pros = myredis.hgetall(author)
    list = []
    for it in pros:
        k = 'pro' + it
        co = myredis.hgetall(k)
        list.append({'name': co.get('name', u'暂时无数据'), 't': pros[it]})
    slist = sorted(list, key=cmp1)
    return JsonResponse({'dict': slist})


def cmp1(dict):
    return dict['t']

def coauth(request):
    author = request.GET.get('author', 'hehe')
    pros = myredis.hgetall(author)
    list = []
    for it in pros:
        k = 'pro' + it
        co = myredis.hgetall(k)
        list.append({'name':co.get('name', u'暂时无数据'), 't' : pros[it]})
    slist = sorted(list, key=cmp1)
    global user_name, email
    c = {'username':user_name, 'email':email}
    return render(request, 'oauth2github/coauth.html', {'dict':c, 'list':slist})


