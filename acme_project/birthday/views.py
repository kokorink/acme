# from django.shortcuts import get_object_or_404, redirect, render
# from django.core.paginator import Paginator
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm

# def birthday(request, pk=None):
#     if pk is not None:
#         # Получаем объект модели или выбрасываем 404 ошибку.
#         instance = get_object_or_404(Birthday, pk=pk)
#     else:
#         # Связывать форму с объектом не нужно, установим значение None.
#         instance = None
#     form = BirthdayForm(request.POST or None,
#                         files=request.FILES or None,
#                         instance=instance)
#     # Создаём словарь контекста сразу после инициализации формы.
#     context = {'form': form}
#     # Если форма валидна...
#     if form.is_valid():
#         form.save()
#         # ...вызовем функцию подсчёта дней:
#         birthday_countdown = calculate_birthday_countdown(
#             # ...и передаём в неё дату из словаря cleaned_data.
#             form.cleaned_data['birthday']
#         )
#         # Обновляем словарь контекста: добавляем в него новый элемент.
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday_form.html', context)


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.order_by('id')
#     paginator = Paginator(birthdays, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     # Передаём их в контекст шаблона.
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html',
#                   context)


# def delete_birthday(request, pk):
#     instance = get_object_or_404(Birthday, pk=pk)
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     if request.method == 'POST':
#         instance.delete()
#         return redirect('birthday:list')
#     return render(request, 'birthday/birthday_form.html', context)

class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context
