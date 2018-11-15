from django.shortcuts import render,HttpResponse, redirect
from templates.login.forms import UserForm, RegisterForm
from goods.models import *
# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = Users.objects.get(name=username)
                print(user)
                if user.password == password:
                    print(user.password,user.name)
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = Users.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = Users.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = Users.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        cls = request.POST.get('cls')
        id_ = request.POST.get('id')

        #向数据库中添加
        Class.objects.create(name = cls, id = id_)

        return redirect('add_class.html')


def add_production(request):
    pass


def add_ingre(request):
    pass


def add_foods(request):
    if request.method == "GET":
        ingres = Ingre.objects.all().values('name')
        cls = Class.objects.all()
        prod = Production.objects.all()
        return render(request, 'add_foods.html', locals())
    else:
        name_ = request.POST.get('name')
        price_ = int(request.POST.get('price'))
        id_ = request.POST.get('id_')
        # 获取配料
        ingre_list = request.POST.getlist('ingres')
        print(ingre_list)
        #获取种类
        cls = request.POST.get('food_class')
        print(cls)
        #获取生产厂家
        prod = request.POST.get('prod')
        print(prod)

        #向数据库中插入数据
        cls_obj = Class.objects.get(name=cls)
        prod_obj = Production.objects.get(name=prod)
        Foods.objects.create(name=name_, id = id_, sum = 1,price=price_, cls=cls_obj,production=prod_obj)

        #向foods_ingre表中插入数据
        foods_obj = Foods.objects.filter(name = name_)[0]
        # 百威
        # ingre_list:[小麦 水 白糖]
        for item in ingre_list:
            ingre_obj = Ingre.objects.get(name=item)
            foods_obj.ingre.add(ingre_obj)

        return redirect('goods/get_foods.html')


def get_foods(request):
    foods_obj = Foods.objects.all()
    return render(request, 'get_foods.html', locals())


def edit_foods(request):
    id_ = request.GET.get('id')
    price_ = request.GET.get('price')

    Foods.objects.filter(id = id_).update(price=price_)
    return HttpResponse("hello")
    #Foods.objects.filter(id=id_).delete()


def delete_foods(request):
    id_ = request.GET.get('id')

    try:
        #ret = Foods.objects.filter(id = id_).delete()
        ret = Foods.objects.get(id = id_)
        print(ret)
        ret.delete()
        msg = "success"
    except Exception :
        msg = "error"
    return HttpResponse(msg)