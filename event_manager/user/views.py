from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


User = get_user_model()


# -------------------------
# LOGIN VIEW
# -------------------------
def login_view(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            login(request, user)

            # 🔥 ROLE BASED REDIRECT
            if hasattr(user, 'role'):
                if user.role == 'student':
                    return redirect('student_dashboard')
                elif user.role == 'organizer':
                    return redirect('organizer_dashboard')

            return redirect('index')

        messages.error(request, "Invalid User ID or Password")
        return redirect('login')

    return render(request, 'user/login.html')


# -------------------------
# REGISTER VIEW
# -------------------------
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        user_id = request.POST.get('user_id')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')   # student / organizer

        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # User already exists check
        if User.objects.filter(username=user_id).exists():
            messages.error(request, "User ID already exists")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=user_id,
            email=email,
            password=password1
        )

        user.first_name = full_name

        # 🔥 assign role (IMPORTANT)
        if hasattr(user, 'role'):
            user.role = role

        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'user/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'user/profile.html')