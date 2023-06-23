from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './first_app/index.html',
                  {"name": "I am Rahim",
                   "marks": 86,
                #    "lst": [24,3,10,5],
                #    "blog": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente ipsam mollitia laudantium odit iusto repellendus voluptatum, reprehenderit esse illum eos! Laborum sint cum quia, voluptates repudiandae ut numquam assumenda molestias."}
                #   {
                      'courses':[
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
    ]}
                  )
    
def about(request):
    return render(request,'./first_app/about.html' )