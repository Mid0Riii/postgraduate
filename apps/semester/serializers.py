from rest_framework import serializers
from .models import Score,Departure


class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ("sco_sem",'sem_name', "sco_course", 'sco_score')
    sem_name = serializers.ReadOnlyField(source='sco_sem.sem_name')

class DepartureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields=('depart_type','depart_datetime','depart_loc','depart_semster')