from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserPurpose,UserDetails
from django.shortcuts import render
from .models import LoanRequest

from django.contrib.auth import authenticate, login


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if role == 'borrower':
                return redirect('create_loan_request')
            elif role == 'lender':
                return redirect('lender_dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    


def loan_request(request):
    return render(request, 'create_loan_request.html')

# def registeruser(request):
#     return render(request, 'register.html')

def give_loan(request):
    
    return render(request, 'lender_dashboard.html')


def register_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        
        # Create a new User object and save it to the database
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # Create a new UserPurpose object for login page
        Userdetails= UserDetails(username=username, password=password,email=email,phone=phone)  # Assuming default role is borrower
        Userdetails.save()
        
        return redirect('login')  # Redirect to login page after successful registration
    else:
        return render(request, 'register.html')



def view_loan_requests(request):
    # Retrieve all loan requests from the database
    borrow_requests = LoanRequest.objects.all()

    # Pass the loan requests to the template as part of the context
    context = {
        'borrow_requests': borrow_requests
    }

    # Render the template with the loan request data
    return render(request, 'view_loan_requests.html', context)



from django.shortcuts import render
from .models import LoanRequest

def view_loan_requests(request):
    # Retrieve all loan requests along with user information
    borrow_requests = LoanRequest.objects.select_related('user').all()

    # Pass the loan requests to the template as part of the context
    context = {
        'borrow_requests': borrow_requests
    }

    # Render the template with the loan request data
    return render(request, 'view_loan_requests.html', context)


def create_loan_request(request):
    return render(request, 'create_loan_request.html') 