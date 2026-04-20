from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is None:
            return rating
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5")
        return rating


"""
def clean_name(self):
    name = self.cleaned_data.get("name")
    if name and len(name.strip()) < 3:
        raise forms.ValidationError("Name too short")
    return name
    
    


from datetime import date

def clean_event_date(self):
    d = self.cleaned_data.get("event_date")
    if d and d < date.today():
        raise forms.ValidationError("Date cannot be in the past")
    return d



"""
