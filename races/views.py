from django.shortcuts import render
from django.views import View
from . import models



# Create your views here.
class RacesListView(View):
    def get(self, request):
        races_list = models.objects.all()
        limit = 20;
        return render(request, 'races/race.html',
                      {'races_list': races_list, 'all': range(1, races_list.count() // limit + 1)})


#todo  单个race的展示
class RacevView(View):
    def get(self,request):
        pass