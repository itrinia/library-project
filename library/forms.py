from django import forms
from .models import Book, Borrow, Category, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'categories']

from django import forms
from .models import Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book', 'member', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        borrow_date = cleaned_data.get('borrow_date')
        return_date = cleaned_data.get('return_date')

        if book is None or borrow_date is None:
            raise forms.ValidationError("Book and borrow date must be provided.")

        current_instance_id = self.instance.id if self.instance else None

        if Borrow.objects.filter(book=book, return_date__isnull=True).exclude(id=current_instance_id).exists():
            raise forms.ValidationError(f"The book '{book}' is already borrowed by another member.")

        if Borrow.objects.filter(book=book, borrow_date__lte=return_date, return_date__gte=borrow_date).exclude(id=current_instance_id).exists():
            raise forms.ValidationError(f"The book '{book}' is already borrowed during the selected period.")

        return cleaned_data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] 

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']