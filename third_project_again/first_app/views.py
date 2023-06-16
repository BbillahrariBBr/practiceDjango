from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, './first_app/index.html',{'courses':[
        {
            'id': 1,
            'course': 'c',
            'teacher': 'Rahim'
        },
         {
            'id': 2,
            'course': 'c++',
            'teacher': 'Kahim'
        },
         {
            'id': 3,
            'course': 'java',
            'teacher': 'fahim'
        },
    ]})