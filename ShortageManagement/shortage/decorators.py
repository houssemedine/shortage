from django.shortcuts import render
from django.contrib.auth.models import User

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func (request, *args, **kwargs):
            message=''
            username='bibas'
            user=User.objects.all().filter(username=username).first()
            if user:
                if user.is_active:
                    #Traitement SSO here  
                    if user.groups.exists():#test if user exists in groups
                        group=user.groups.all()[0].name
                        if  group and (group in allowed_roles):
                            return view_func (request, *args, **kwargs)
                    else:
                            message='not allowed to acces !'
                            return render(request,'shortage/error.html',{'username':username,'message':message})
                else:
                    message='is not active'
                    return render(request,'shortage/error.html',{'username':username,'message':message})
            else:  
                message='not found'
                return render(request,'shortage/error.html',{'username':username,'message':message})
        return wrapper_func
    return decorator
