from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from .models import Post, Account, Example
from .serializers import AccountSerializer, ExampleSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def login_page(request):
    return render(request, 'main/login.html')


def signup(request):
    return render(request, 'main/signup.html')


def blog(request):
    postlist = Post.objects.all()
    # dictionary single quote 없으면 데이터 안넘어감
    return render(request, 'main/blog.html', {'postlist': postlist})


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'post': post})

# account


@csrf_exempt
def account_list(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def account(request, pk):
    obj = Account.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def find_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = Account.objects.get(email=search_email)
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def update_account_point(request):
    if request.method == 'POST':
        update_point = Account.objects.update(
            point=request.POST['point']
        )
    return redirect('/accounts/')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = Account.objects.get(email=search_email)

        if data['password'] == obj.password:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

# example


@csrf_exempt
def example_list(request):
    if request.method == 'GET':
        query_set = Example.objects.all()
        serializer = ExampleSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExampleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def example(request, pk):
    obj = Example.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ExampleSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExampleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def solve(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_answer = data['answer']
        obj = Example.objects.get(answer=search_answer)

        if data['answer'] == obj.answer:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def save_point(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        search_email = data['email']
        add_point = data['point']
        user = Account.objects.get(email=search_email)

        if user:
            point = Account.objects.get(email=search_email).point
            Account.objects.filter(email=search_email).update(
                point=point + add_point)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def use_point(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        user = Account.objects.get(email=search_email)

        if user:
            point = Account.objects.get(email=search_email).point
            if point > 0:
                Account.objects.filter(email=search_email).update(
                    point=point - 1)
                return HttpResponse(status=200)
            else:
                return JsonResponse({'message': '이런! 남은 포인트가 없어요!'}, status=201)
        else:
            return HttpResponse(status=400)

@csrf_exempt
def change_status(request):
    if request.method == 'POST':
        data = JSONParser.parse(request)
        search_email = data['email']
        change_status = data['status']

        user = Account.objects.get(emial=search_email)
        if user:
            Account.objects.filter(email=search_email).update(
                status = change_status
            )
            return HttpResponse(status=200)
        else:
            return JsonResponse(status=400)
