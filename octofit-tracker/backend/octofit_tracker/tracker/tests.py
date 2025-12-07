from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        user1 = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        user2 = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        Activity.objects.create(user=user1, type='Running', duration=30, calories=300, date='2025-12-07')
        Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        Leaderboard.objects.create(team=marvel, total_calories=300, total_duration=30)

    def test_user_team(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Team.objects.count(), 2)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
