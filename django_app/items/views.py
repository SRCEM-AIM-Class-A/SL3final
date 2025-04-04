from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    form = ItemForm()
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('home')
    
    return render(request, 'items/home.html', {
        'items': items,
        'form': form
    })

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully!')
    return redirect('home') 