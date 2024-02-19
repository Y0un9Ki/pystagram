from django.shortcuts import render, redirect

# Create your views here.
def feeds(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")

    # request.user는 view함수에 요청(request)을 한 사용자(요청자)에 대한 정보를 가져오는 속성이다.
    # user = request.user
    # is_authenticated = user.is_authenticated
    # print('user:', user)
    # print("is_authenticated:", is_authenticated)
    # 위에 코드는 로그인을 했을때 어떠한 값이 나오는지를 보기위한 코드이다. is_authenticated는 불리안 값으로 나온다.
    return render(request, "posts/feeds.html")