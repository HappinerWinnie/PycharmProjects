from django.shortcuts import render

# Create your views here.
data = []
for x in range(1,10001):
    data.append(x)


def show(request):
    per = 10
    current_pn = request.GET.get('page')
    if current_pn ==None:
        page_no = 1
    else:
        page_no = int(current_pn)

    if page_no ==0:
        page_no = 1
    page_data = data[(page_no - 1)*per:page_no*per]
    page_sum = len(data)//10
    return render(request, 'show.html', {'page_data':page_data, 'page_no':page_no, 'page_sum':page_sum})


