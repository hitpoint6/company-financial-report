from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanyListCreateView, ReportListCreateView, CompanyReportsListView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('reports/', ReportListCreateView.as_view(), name='report-list-create'),
    path('companies/<int:company_pk>/reports/', CompanyReportsListView.as_view(), name='company-reports-list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)