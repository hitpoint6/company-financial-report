from .serializers import CompanySerializer, ReportSerializer
from rest_framework import generics
from .models import Company, Report

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class CompanyReportsListView(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        company_pk = self.kwargs['company_pk']
        return Report.objects.filter(company_id=company_pk)