from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

# Create your views here.

# Naive way to store files
# here dest means destination
# with is a keyword


# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

#################################################
# with Create View
# You can delete your form class with this. This is very handy
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
#################################################
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form,
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid:
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             # passing this argument as file while calling that function
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect('/profiles')
#         return render(request, 'profiles/create_profile.html', {
#             'form': submitted_form,
#         })


class ProfilesListView(View):
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, 'profiles/user_profiles.html', {
            'profiles': profiles,
        })
