import random
import string
from http import client
from urllib import parse

from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from backstage.models import User


def login_port(request):
    #登录用户展示页面
    print('in_login_port')
    if request.GET.get('error'):
        #如果页面登录逻辑错误，返回错误展示用户端
        error = '请检查用户名与验证码是否正确'
        return render(request,'Signin.html',{'error':error})
    #正常返回登录页面
    return render(request,'Signin.html')



def login_logic(request):
    #设置登录逻辑
    u = request.POST.get('username')
    p = request.POST.get('password')
    re = request.POST.get('rem')

    captcha=request.POST.get('captcha')
    code = request.session.get('message_code')
    print(u,p,re,'admin-view@236',captcha,code)
    #
    if User.objects.filter(username=u,password=p):
        response = redirect('home:index')
        # 设置session保存
        request.session['admin'] = u
        if re:
            #设置cookie信息
            response.set_cookie(u,max_age=24*60*60)
        return response
    else:
        return redirect('/app_admin/page/login/?error=1')




def phone(request):
    #登录手机验证码连接
    # 请求的路径
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 用户名是登录ihuyi.com账号名（例如：cf_demo123）
    account = "C03823094"
    # 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
    password = "385f386c45a350f05843faaf870e5a17"
    #设置手机验证码连接
    mobile=request.POST.get('mobile')
    code=random.sample(string.digits,4)
    code = ''.join(code)
    print('@250',mobile,code)
    # 拼接成发出的短信
    text = "您的验证码是：" + code + "。请不要把验证码泄露给其他人。"
    # 把请求参数编码
    params = parse.urlencode(
        {'account': account, 'password':password, 'content': text, 'mobile': mobile, 'format': 'json'})
    # 请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 通过全局的host去连接服务器
    conn = client.HTTPConnection(host, port=80, timeout=30)
    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 得到服务器的响应
    response = conn.getresponse()
    # 获取响应的数据
    response_str = response.read()
    # 关闭连接
    conn.close()
    # 把验证码放进session中
    request.session['message_code'] = code
    print(eval(response_str.decode()))

    # 使用eval把字符串转为json数据返回
    return JsonResponse(eval(response_str.decode()))



