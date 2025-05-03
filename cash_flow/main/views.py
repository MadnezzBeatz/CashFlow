from django.shortcuts import render
from .models import Records, Category, Subcategory
from .form import FilterForm
from django.http import JsonResponse



def index(request):
    form = FilterForm(request.GET or None)
    records = Records.objects.all()

    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        status = form.cleaned_data.get('status')
        record_type = form.cleaned_data.get('record_type')
        category = form.cleaned_data.get('category')
        subcategory = form.cleaned_data.get('subcategory')

        if date_from:
            records = records.filter(date__gte=date_from)
        if date_to:
            records = records.filter(date__lte=date_to)
        if status:
            records = records.filter(status=status)
        if record_type:
            records = records.filter(type=record_type)
        if category:
            records = records.filter(category_id=category)
        if subcategory:
            records = records.filter(subcategory_id=subcategory)

    return render(request, 'main/index.html', {'form': form, 'records': records})


def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

