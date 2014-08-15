from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from exercises import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'profproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', login),
    url(r'^logout/$', views.logout_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exercises/$', views.ExerciseIndex, name='exercise_index'),
    url(r'exercises/([\w ]+)/(\d+)/$', views.ExerciseForm, name='exercise_form'),
    url(r'exercises/results/$', views.ExerciseResult, name='exercise_result'),
    url(r'exercises/results/choice$', views.ExerciseResultChoice, name='exercise_choice'),
]
