from django import forms

class NewSearchForm(forms.Form):
    def __init__( self, *args, **kwargs ):
        super(NewSearchForm, self).__init__( *args, **kwargs )
        self.fields['title'].label = ""
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))


class NewPageForm(forms.Form):
    def __init__( self, *args, **kwargs ):
        super(NewPageForm, self).__init__( *args, **kwargs )
        self.fields['title'].label = ""
        self.fields['content'].label = ""

    title = forms.CharField(
        help_text="<p class='text-secondary'>Please refer to <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> for guidance on how to use markdown.</p>",
        widget= forms.TextInput(attrs={
            'placeholder':'Enter Title', 
            'class':'col-sm-11'})
        )

    content = forms.CharField( 
        widget= forms.Textarea(attrs={
            'placeholder':'Enter markdown content', 
            'class':'col-sm-11', 
            'style': 'height: 35em;'})
    )


class NewEditForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(NewEditForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
    
    content = forms.CharField(
        help_text="<p class='text-secondary'>Please refer to <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> for guidance on how to use markdown.</p>",
        widget=forms.Textarea(attrs={
            'class': 'col-sm-11',
            'style': 'height: 35em;'
        })
    )