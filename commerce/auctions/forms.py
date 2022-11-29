from django import forms


category_choices = [
    ('1', 'Fashion'),
    ('2', 'Toys'),
    ('3', 'Electronics'),
    ('4', 'Home'),
    ('5', 'Hardware')
]

class NewList(forms.Form):
    Title = forms.CharField(label='Title', max_length=100, required=True)
    Description = forms.CharField(label='Description', max_length=100, required=True)
    Starting_bid = forms.IntegerField(label='Starting Bid', required=True)
    Image = forms.URLField(label='Image', max_length=100, required=False)
    Category = forms.ChoiceField(
        label='Category', required=False,
        choices=category_choices
    )
