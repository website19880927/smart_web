from django.shortcuts import render

# Create your views here.



def show_index(request):
    #展示首页索引
    print('in show _index')

    return  render(request,'index.html')

def show_components(request):
    #展示组成界面
    print('in components')
    return  render(request,'components.html')

def show_forms(request):
    #图表界面
    print('in forms')
    return  render(request,'forms.html')

def show_tables(request):
    #表格界面
    print('in tables')

    return render(request,'tables.html')

def show_notification(request):
    # 通知界面
    print('in notification')
    return  render(request,'notifications.html')

def show_typography(request):
    #板式
    print('in typography')
    return render(request,'typography.html')

def show_icons(request):
    #icon
    print('in icons')
    return render(request,'icons.html')