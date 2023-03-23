from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# for class based views
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView


# Create your views here.

# We can create class based view for less code and easy functionality.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form,
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, 'reviews/review.html', {
#             'form': form,
#         })

############### Best method for forms #################
###################### FormView , Create View###############
# from django.views.generic.edit import FormView, CreateView


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"  # Here completes teh get method..
#     success_url = "/thank-you"
# # to get data that we entered and saving in database

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

###############################################################
# Delete forms.py. It will make form for us directly from models.
# It wont take labels and error messages like we did in forms.py
# class ReviewView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

# it will handle all by itself save too.

##########################################################################

def review(request):
    # if request.method == 'POST':  # Method gives us method that was used for submitting the data
    #     # .POST key = gives a dictionary of given data. In html file input name will be key and entered data will be a value.
    #     entered_username = request.POST['username']
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    # else:
    #     pass
    if request.method == 'POST':
        # for updateing data
        # existing_data = Review.objects.get(pk=1)
        form = ReviewForm(request.POST)  # ,instance=existing_data)
        if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating'])
            # review.save()

            # since we are using model Form we can skip above steps
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
        'form': form
    })

# I dont like template view. Never using it.


class ThankYouView(TemplateView):  # (View)
    # def get(self, request):
    #     return render(request, 'reviews/thank_you.html')
    # This  will be get() method directly.
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works!"
        return context
# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')


class ReviewsListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, "reviews/review_list.html", {
            "reviews": reviews,
        })


# OR

# We can use ListView to get list of data directly through the model
# class ReviewsListView(ListView):
#     template_name = "reviews/review_list.html"
#     model = Review
#     context_object_name = "reviews" #to pass context name instead of object_list for templates
    # We can also pass querries for data filtering
    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data


class SingleReviewView(View):
    def get(self, request, **kwargs):
        # reviews = Review.objects.all()
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        return render(request, 'reviews/single_review.html', {
            "review": selected_review,
        })


# OR

# when we want to fetch single piece of data from models and show in template

# from django.views.generic import DetailView
# class SIngleReviewView(DetailView):
#     template_name = "reviews/single_review.html"
#     model = Review
