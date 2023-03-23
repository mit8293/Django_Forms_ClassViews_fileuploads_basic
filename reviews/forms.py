from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=30, label='Your name', error_messages={
#         "required": "Your name must not be empty!",  # arguments as keys
#         "max_length": "Please enter a shorter name!",  # message are values
#     })

#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200, required=False)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# This can bring fields and validations from the model and create form for us.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields you can import from model . if we want to import all fields we can just write '__all__'
        # if we want to exclude only one field we can use
        # exclude = ['']
        fields = ['user_name', 'review_text', 'rating', ]
        # Labels are lost
        labels = {
            "user_name": "Your name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        # nested dictionary for error messages
        error_messages = {
            "user_name": {
                "required": "I wont except empty",
                "max_length": "Please enter a shorter name!"
            }
        }
