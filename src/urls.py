
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , homepage , name="home"),
    path('<int:tag_id>' , homepage , name="tags_search"),
    path('<slug:vacancy_slug>/' , job_details , name="job_detail"),
    path('companiesemails' , companies_emails , name="emails" ),
    path('companiesemails/<int:category_id>/' , emaildetails , name='emaildetails'),
    path('getting/service' , services , name="services"),
    path('getting/service/<int:service_id>' , service_detail , name = "servicedetail"),
    path('createCV/fillData' , createcv , name="createcv"),
    path('site/policy/' , policy , name="policy"),
    path('terms&/policy/' , termspolicy , name="terms"),
    path('contact/us', contact , name="contactus"),
    path('easy-apply/<int:job_id>/<int:profile_id>', easy_apply, name='easy_apply'),
    path('accounts/' , include('accounts.urls')),
    path('success_sent' , emailsent , name="successsent"),
    path('view-cv/<int:choise>/<int:profile_id>/', view_cv, name='view_cv'),
    path('override/<int:choises>/<int:profile_pk>' , override_cv , name="override"),
    path('del/<int:profile>/' , del_file , name='del_file'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
