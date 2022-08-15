from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

# Create your views here.
#function view
'''
def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

def details(request,item_id):
    item_list=Item.objects.get(pk=item_id)
    context={
        'item':item_list,
    }
    return render(request,'food/details.html',context)

def add_item(request):
form=ItemForm(request.POST or None)
if form.is_valid():
    form.save()
    return redirect('food:index')

return render(request,'food/item_form.html',{'form':form})


'''

def item(request):
    return HttpResponse("Item View")


def update_item(request,id):
    item=Item.objects.get(id=id)
    form= ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete_item.html',{'item':item})

#class view for details
class FoodDetails(DetailView):
    model=Item
    template_name='food/details.html'

#class view for listing items
class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'

#class view for adding items
class AddItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_img']
    template_name: 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user

        return super().form_valid(form)

