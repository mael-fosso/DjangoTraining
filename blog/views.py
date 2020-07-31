from django.shortcuts import render

def index(request):
   # posts = ['Erste Post', 'Sekonde Post', 'dritte Post']
   posts =[
       {'id':'1','title': 'Erste Post', 'body':'b1'},
       {'id':'2','title': 'Sekonde Post', 'body':'b2'},
       {'id':'3','title': 'dritte Post', 'body': 'b3'}
   ]
   return render(request, 'blog/index.html', {'posts':posts})

