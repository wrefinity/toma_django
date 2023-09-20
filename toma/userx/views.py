from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View


class SignupView(View):
    template_name = './pages/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            User.objects.get(username=request.POST['username'])
            mess = 'Username is already taken!'
            return render(request, self.template_name, {'error': mess})
        except User.DoesNotExist:
            passx = request.POST['password']
            user = User.objects.create_user(
                request.POST['username'], password=passx)
            print("user created: ", user)
            auth.login(request, user)
            return redirect('home')


class LoginView(View):
    template_name = 'pages/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        passx = request.POST['password']
        user = request.POST['username']
        user = auth.authenticate(username=user, password=passx)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            mess = 'Username or password is incorrect!'
            return render(request, self.template_name, {'error': mess})


class HomePageView(View):
    template_name = "pages/main.html"

    def get(self, request):
        # if 'uid' in request.session and 'role' in request.session:
        #     return redirect('dashboard')
        # else:
        return render(request, self.template_name)


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('home')
