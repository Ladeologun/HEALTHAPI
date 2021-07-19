from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from menstrual_cycle.models import MenstrualCycle
from rest_framework.test import APIClient
from authentication.models import User


class CreateCycleViewTest(APITestCase):
    """ Test module for creating a new cycle """
    client = APIClient()

    def setUp(self):
        self.test_user = User.objects.create_user(email='testuser@gmail.com', 
                                                  password='testuser123.', 
                                                  fullname='testuser10',
                                                  mobile_number='07060165309',
                                                  age=23,)
        self.valid_payload = {
            "Last_period_date":"2020-06-20",
            "Cycle_average":27,
            "Period_average":5,
            "Start_date":"2020-07-25",
            "End_date":"2021-07-25"
        }
        self.invalid_payload = {
            "Last_period_date":"",
            "Cycle_average":27,
            "Period_average":5,
            "Start_date":"2020-07-25",
            "End_date":"2021-07-25"
        }
        self.invalid_cycle_average_payload = {
            "Last_period_date":"2020-06-20",
            "Cycle_average":"",
            "Period_average":5,
            "Start_date":"2020-07-25",
            "End_date":"2021-07-25"
        }
        self.invalid_start_date_payload = {
            "Last_period_date":"2020-06-20",
            "Cycle_average":"",
            "Period_average":5,
            "Start_date":"",
            "End_date":"2021-07-25"
        }
        self.valid_cycle_payload = {
            "Last_period_date":"2020-06-20",
            "Cycle_average":27,
            "Period_average":5,
            "Start_date":"2020-07-25",
            "End_date":"2021-07-25"
        }

        self.register_url = reverse('create-cycle')

    def test_user_cannot_create_cycle_with_no_data(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_cycle_valid_data(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(
            self.register_url,
            self.valid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_create_cycle_invalid_payload(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(
            self.register_url,
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_cycle_average(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(
            self.register_url,
            self.invalid_cycle_average_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_start_date(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(
            self.register_url,
            self.invalid_start_date_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_cycle_payload(self):
        self.client.force_authenticate(user= self.test_user)
        res = self.client.post(
            self.register_url,
            self.valid_cycle_payload,
            format='json'
        )
        self.assertEqual(res.data["total_created_cycles"], 13)
        self.assertEqual(res.data["name"], 'testuser10')


class TestLearnerCourseList(APITestCase):
    client = APIClient()

    def setUp(self):
        self.test_user = User.objects.create_user(email='testuser@gmail.com', 
                                                  password='testuser123.', 
                                                  fullname='testuser10',
                                                  mobile_number='07060165309',
                                                  age=23,)

        self.cycle_data = MenstrualCycle.objects.create(
                        Last_period_date="2020-06-20",
                        Cycle_average=27,
                        Period_average=5,
                        Start_date="2020-07-25",
                        End_date="2021-07-25",
                        owner = self.test_user
                        )
        
        self.register_url = reverse('list-cycle')

    def test_get_cycle_without_auth(self):
        "this tests unauthorized users"
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_cycle_with_auth(self):
        "this tests authorized users"
        self.client.force_authenticate(user= self.test_user)
        res = self.client.get('/women-healths/api/cycle-event/?date=2020-08-4')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['event'], "post_ovulation_window")
        
