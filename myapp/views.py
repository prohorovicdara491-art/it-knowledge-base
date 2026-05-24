from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    
    query = request.GET.get('q', '')
    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    
    tech_category = request.GET.get('tech_category', '')
    if tech_category:
        notes = notes.filter(tech_category=tech_category)
    
    category = request.GET.get('category', '')
    if category:
        notes = notes.filter(category=category)
    
    return render(request, 'myapp/note_list.html', {
        'notes': notes,
        'query': query,
    })

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'myapp/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка создана!')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'myapp/note_form.html', {'form': form, 'title': 'Создать заметку'})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка обновлена!')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'myapp/note_form.html', {'form': form, 'title': 'Редактировать заметку'})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Заметка удалена')
        return redirect('note_list')
    return render(request, 'myapp/note_confirm_delete.html', {'note': note})
