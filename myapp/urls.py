from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    # if we created function based view 
    path('',views.index,name=''),
    # makeing a dynamic url - for access and perform a operation on particular items using unique id 
    path('home/<int:id>/',views.index,name=''),
    # if we created class based view 
    path("about/",TemplateView.as_view()),
    
]


#------------------------------------------------- more about urls --------------------------------

# urls parameters         :- used a angle braces < > for passing a intiger and string value 
# regular expression      :- used for match more complex patteren
# Namespaceing            :- define seprate urls with in app and include in projects urls for avoid namespacing 
# reverse urls resulation :- for match the reverse urls patteren use urls in form action attributes  