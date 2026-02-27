import json

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


User = get_user_model()

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set"})

def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        mail = data.get("mail")
        password = data.get("password")

        try:
            user = User.objects.get(email=mail)
        except User.DoesNotExist:
            return JsonResponse({"error": "Credenciais inválidas"}, status=400)

        user = authenticate(request, username=user.username, password=password)

        if user:
            login(request, user)
            return JsonResponse({"success": True})

        return JsonResponse({"error": "Credenciais inválidas"}, status=400)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"detail": "Logout realizado com sucesso"})
    
    return JsonResponse({"detail": "Método não permitido"}, status=405)

def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "id": request.user.id,
            "email": request.user.email,
        })

    return JsonResponse({"detail": "Unauthorized"}, status=401)