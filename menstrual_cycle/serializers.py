from rest_framework import serializers
from menstrual_cycle.models import MenstrualCycle


class MenstrualCycleSerializer(serializers.ModelSerializer):
    Cycle_average = serializers.IntegerField(max_value=40)
    Period_average = serializers.IntegerField(min_value=1)
    class Meta:
        model = MenstrualCycle
        fields = ['Last_period_date','Cycle_average','Period_average','Start_date','End_date']