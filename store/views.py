from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models.customer import Customer
from django.views import View
# Create your views here.


def user(request):
    all_customers = Customer.objects.all()
    print(all_customers)
    return render(request, 'user.html',
                  {'all_customers': all_customers})


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postdata = request.POST
        first_name = postdata.get('Firstname')
        last_name = postdata.get('lastname')
        mobile_number = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        re_password = postdata.get('repassword')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': mobile_number,
            'email': email,
        }

        print(first_name, last_name, mobile_number, email, password)
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=mobile_number,
                            email=email,
                            password=password,
                            re_password=re_password)

        error_message = None

        if len(customer.phone) < 10:
            error_message = "Enter valid phone number"

        elif len(customer.password) < 6:
            error_message = "Password must atleast 6 characters"
            if customer.password != customer.re_password:
                error_message = "Password and confirm Password are not same"

        elif customer.isExists():
            error_message = "Email Already Registered Please Login"
        if not error_message:
            print(first_name, last_name, mobile_number, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)





