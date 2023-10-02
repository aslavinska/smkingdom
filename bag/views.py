from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, PrintOptions

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
  
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        prints = (request.POST.get('prints'))
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                if prints in bag[item_id]['items_by_size'][size]['prints'].keys():
                    bag[item_id]['items_by_size'][size]['prints'][prints] += quantity
        
                    messages.success(request, f'Updated size {size.upper()} {product.name} {prints} quantity to {bag[item_id]["items_by_size"][size]["prints"][prints]}')
                    print("bag: ",bag)
                    print("prints: ",[prints])
                else:
                    bag[item_id]['items_by_size'][size]['prints'][prints] = quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} {prints} quantity to {bag[item_id]["items_by_size"][size]["prints"][prints]}')
                    print("bag here 1: ",bag)
             
            else:
                print("bag2.3: ",bag)
                print("size: ",size)
                print("prints: ",prints)
             #   bag[item_id]['items_by_size'][size] = quantity
               # bag[item_id] = {'items_by_size': {size:  {'prints': {prints : quantity} }}}
               # print("bag2.1: ",bag)
              #  messages.success(request, f'Added size {size.upper()} {product.name}  {prints} to your bag')
                #print("bag2: ",bag)
            #                    print("bag HERE C : ",bag)
                if prints in bag[item_id]['items_by_size'][size]['prints'].keys():
                        print("bag HERE D : ",bag)
                        bag[item_id]['items_by_size'][size]['prints'][prints] += quantity
                
                        messages.success(request, f'Updated size {size.upper()} {product.name} {prints} quantity to {bag[item_id]["items_by_size"][size]["prints"][prints]}')
                        print("bag HERE B: ",bag)
                        print("prints: ",[prints])
                else:
                       # bag[item_id]['items_by_size'][size]['prints'][prints] = quantity
                        print("bag HERE E: ",bag)
                        bag[item_id] = {'items_by_size': {size:  {'prints': {prints : quantity} }}}
                        messages.success(request, f'Updated size {size.upper()} {product.name} {prints} quantity to {bag[item_id]["items_by_size"][size]["prints"][prints]}')
                        print("bag here 1: ",bag)



        else:
            print("bag HERE F : ",bag)
            bag[item_id] = {'items_by_size': {size:  {'prints': {prints : quantity} }}}
            messages.success(request, f'Added size {size.upper()} {product.name} {prints} to your bag')
            print("bag3: ",bag)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
   # prints = PrintOptions.objects.filter(printname=product)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        prints = request.POST['prints']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} {prints.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)