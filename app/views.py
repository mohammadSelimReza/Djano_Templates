from django.shortcuts import render,redirect,get_object_or_404
from .models import ItemModel
from .forms import ItemForm
# Create your views here.
def home(request):
    items = ItemModel.objects.all()
    return render(request,'base.html',{'items':items})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print("error")
    else:
        form = ItemForm()
    return render(request,'add.html',{'form':form})

def update_item(request,pk):
    item =get_object_or_404(ItemModel,item_id=pk)
    if request.method == "POST":
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ItemForm(instance=item)
    return render(request,'update.html',{'form':form})
    
    
def delete_item(request,pk):
    item = get_object_or_404(ItemModel,item_id=pk)
    item.delete()
    return redirect('homepage')
