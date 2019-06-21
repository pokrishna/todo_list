from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from todo_app.mixins import SerializeMixin,HttpResponseMixin
from todo_app.utils import is_json
from .models import todo_list
from .forms import listform
from django.contrib import messages
from django.core.serializers import serialize
from todo_app import utils
import json

def is_json(data):
    try:
        p_data=json.loads(data)
        valid=True
    except:
        valid=False
    return valid
def home(request):
    if request.method=="POST":
        form = listform(request.POST or None)
        try:
            if form.is_valid():
                form.save()
                all_items = todo_list.objects.all()
                #messages.success(request,("item has been added to list"))
                form=listform()
                return render(request, "home.html", {'all_items':all_items,'form':form})
            else:
                raise ValidationError("Data Incorrect")
        except:
            return HttpResponse("Please enter Correct Data")
    else:
        form=listform()
        all_items=todo_list.objects.all()
        return render(request, 'home.html', {'all_items':all_items,'form':form})
def delete(request,id):
    item=todo_list.objects.get(id=id)
    if item:
        item.delete()
        return redirect('home')
    return redirect('home')

def update(request,id):
    item=todo_list.objects.get(id=id)
    form=listform(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('home')
    all_items = todo_list.objects.all()
    return render(request,'home.html',{'all_items':all_items,'form':form})

class todo_listAPI(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            item=todo_list.objects.get(id=id)
        except todo_list.DoesNotExist:
            item=None
        return item
    def get(self,request,*args,**kwargs):
        data=request.body
        print(data)
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Pls Send me valid data'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            item=self.get_object_by_id(id)
            if item is None:
                json_data=json.dumps({'msg':'Not available match id'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.serialize([item,])
            return self.render_to_http_response(json_data)
        qs=todo_list.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)
