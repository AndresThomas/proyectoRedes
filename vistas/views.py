from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

class vistaClass(View):

    #template = 'index.html'

    def get(self, request, *arg, **kargs):
        return render(request,'index/index.html')
    
    def post(self, request, *arg, **kargs):
        print('hola')
        messages.info(request, 'Despachando alimento')

        #
        # aqui iria todo el codigo para que el servo se active
        #
        #
        #
        #
        #
        #
        return render(request,'index/index.html')