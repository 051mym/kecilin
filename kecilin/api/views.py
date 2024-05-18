from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response
from mutation.models import Uang_masuk, Uang_keluar
from django.db.models import Sum

# Create your views here.


class MutationList(APIView):
    allowed_methods = ['GET',]

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get(
            'start_date', timezone.now().replace(day=1))
        end_date = request.GET.get('end_date', timezone.now())
        # user_id = request.GET.get("user_id", None)

        result = []

        current_date = start_date
        while current_date <= end_date:
            date_formated = current_date.strftime("%Y-%m-%d")

            total_uang_masuk = Uang_masuk.objects.filter(datetime__date__lte=date_formated).aggregate(
                total=Sum('nominal', default=0))['total']
            total_uang_keluar = Uang_keluar.objects.filter(datetime__date__lte=date_formated).aggregate(
                total=Sum('nominal', default=0))['total']

            result.append({
                'date': date_formated,
                'uang_masuk': Uang_masuk.objects.filter(datetime__date=date_formated).aggregate(total=Sum("nominal", default=0))['total'],
                'uang_keluar': Uang_keluar.objects.filter(datetime__date=date_formated).aggregate(total=Sum("nominal", default=0))['total'],
                'saldo': total_uang_masuk - total_uang_keluar,
            })
            current_date += timedelta(days=1)

        return Response({
            'status': status.HTTP_200_OK,
            'message': "Request successfully",
            'result': result
        })
