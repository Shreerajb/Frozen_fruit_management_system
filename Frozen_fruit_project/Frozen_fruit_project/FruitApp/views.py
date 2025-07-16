from django.shortcuts import render
from .models import Fruit
from .forms import OrderForm
from django.contrib import messages


def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request,'fruit_list.html',{'fruits':fruits})

from django.contrib import messages
from django.shortcuts import render
from .forms import OrderForm

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            fruit = form.cleaned_data['fruit']
            requested_qty = form.cleaned_data['quantity_ordered']

            if requested_qty <= fruit.quantity_in_kg:
                order = form.save()
                fruit.quantity_in_kg -= requested_qty
                fruit.save()
                return render(request, 'order_success.html')
            else:
                messages.error(request, f"Only {fruit.quantity_in_kg} kg of {fruit.name} is available. Please reduce your quantity.")

                return render(request, 'place_order.html', {'form': form})
        else:

            return render(request, 'place_order.html', {'form': form})
    else:

        form = OrderForm()
        return render(request, 'place_order.html', {'form': form})
