"""Base views for cryptomonsters."""
from django.shortcuts import render


def home_view(request):
    """Cryptomonster home view."""
    return render(request, 'cryptomonsters/home.html')


def profile_view(request):
    return render(request, 'cryptomonsters/profile.html')


# class ProfileView(DetailView):
#     """Display user data."""

#     user = User
#     first = user.first_name
#     last = user.last_name
#     email = user.email
#     redirect_field_name = '/accounts/login'
#     template_name = 'cryptomonsters/profile.html'

#     def get_context_data(self, **kwargs):
#         """Queryset of all photos in album."""
#         username = kwargs['object'].user.filter(album=kwargs['object'].pk)
#         context = super().get_context_data(**kwargs)
#         context['photo'] = photo
#         return context


# class ProfileView(DetailView):
#     """Profile view for a single user."""

#     template_name = 'imager_profile/profile.html'
#     model = ImagerProfile
#     slug_field = 'user__username'
#     slug_url_kwarg = 'username'

#     def get(self, *args, **kwargs):
#         """Redirect home if not logged in."""
#         if not self.kwargs['username']:
#             self.kwargs['username'] = self.request.user.get_username()
#             if self.kwargs['username'] == '':
#                 return redirect('home')

#         if self.kwargs['username'].endswith('/'):
#             self.kwargs['username'] = self.kwargs['username'][:-1]
#         return super(ProfileView, self).get(*args, **kwargs)

#     def get_context_data(self, **kwargs):
#         """Get the user's profile, photos, and albums."""
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         username = kwargs['object'].user.username

#         owner = False
#         if username == self.request.user.username:
#             owner = True

#         context['owner'] = owner

#         photos = Photo.objects.filter(user__username=username)
#         albums = Album.objects.filter(user__username=username)

#         if not owner:
#             photos = photos.filter(published='PUBLIC')
#             albums = albums.filter(published='PUBLIC')

#         context['albums'] = albums
#         context['album_private_count'] = albums.filter(published='PRIVATE').count()
#         context['album_public_count'] = albums.filter(published='PUBLIC').count()

#         context['photos'] = photos
#         context['photo_private_count'] = photos.filter(published='PRIVATE').count()
#         context['photo_public_count'] = photos.filter(published='PUBLIC').count()

#         return context
