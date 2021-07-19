from rest_framework import permissions, status,response
from rest_framework.generics import CreateAPIView,UpdateAPIView
from menstrual_cycle.serializers import MenstrualCycleSerializer
from menstrual_cycle.models import MenstrualCycle
from helpers.utils import period_start_dates
from django.db import IntegrityError



class CreateCycleView(CreateAPIView,UpdateAPIView,):
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

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        Last_period_date = user_data.get('Last_period_date', '')
        Cycle_average = user_data.get('Cycle_average', '')
        Period_average = user_data.get('Period_average', '')
        Start_date = user_data.get('Start_date', '')
        End_date = user_data.get('End_date', '')
        
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        owner =request.user
        name=owner.fullname
        period_dates = period_start_dates(Last_period_date,Cycle_average,Start_date,End_date)
        try:
            cycle,created = MenstrualCycle.objects.update_or_create(Last_period_date=Last_period_date,Cycle_average=Cycle_average,
                                                Period_average=Period_average,Start_date=Start_date,
                                                End_date=End_date,owner=owner
                                                )
            print(cycle)
            cycle.save()
        except IntegrityError:
            return response.Response({'message':'record for user already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'name':name,'total_created_cycles':len(period_dates)}, status=status.HTTP_201_CREATED)

    def put(self, request, **kwargs):
        update_period = self.get_object()
        serializer = MenstrualCycleSerializer(data=request.data, partial=True)
        self.check_object_permissions(request,update_period)
        if serializer.is_valid():
            serializer.instance = update_period
            serializer.save()
            user_data = serializer.data
            Last_period_date = user_data.get('Last_period_date', '')
            Cycle_average = user_data.get('Cycle_average', '')
            Start_date = user_data.get('Start_date', '')
            End_date = user_data.get('End_date', '')
            period_dates = period_start_dates(Last_period_date,Cycle_average,Start_date,End_date)
            owner =request.user
            name=owner.fullname
            return response.Response({'name':name,'total_created_cycles':len(period_dates)}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   