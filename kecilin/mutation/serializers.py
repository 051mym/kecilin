from rest_framework import serializers
from .models import Uang_keluar, Uang_masuk

class MutasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uang_masuk
        fields = ['id', 'user_id', 'datetime', 'nominal']