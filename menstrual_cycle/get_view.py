from rest_framework import permissions, status,response
from rest_framework.generics import ListAPIView
from menstrual_cycle.serializers import MenstrualCycleSerializer
from menstrual_cycle.models import MenstrualCycle
from helpers.tools import get_closest_date_from_list,cycle_event_analyst


class ListCycleEvent(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    """Creates new menstrual cycle info in the system"""
    serializer_class = MenstrualCycleSerializer

    def get_queryset(self):
        user = MenstrualCycle.objects.filter(owner=self.request.user)
        if not user:
            return response.Response({"invalid_user":"no record found"}, status=status.HTTP_400_BAD_REQUEST)
        return user

    def get_object(self):
        queryset = self.get_queryset()
        return queryset[0]
    def get(self,request):
        user_data = self.get_object()
        serializer = self.serializer_class(user_data)
        cycle_event = self.request.query_params.get('date')
        Last_period_date = serializer.data.get('Last_period_date', '')
        Cycle_average = serializer.data.get('Cycle_average', '')
        Period_average = serializer.data.get('Period_average', '')
        Start_date = serializer.data.get('Start_date', '')
        End_date = serializer.data.get('End_date', '')
        date_data = get_closest_date_from_list(cycle_event,Last_period_date,Cycle_average,Start_date,End_date)
        try:
            last_periods = date_data[0]
            next_periods = date_data[1]
        except KeyError:
            return response.Response({"error":"date no in range of record available"}, status=status.HTTP_400_BAD_REQUEST)
        user_info = cycle_event_analyst(last_periods,cycle_event,Cycle_average,Period_average,next_periods)

        return response.Response(user_info, status=status.HTTP_200_OK)
