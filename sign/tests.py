from django.test import TestCase
from sign.models import Event, Guest

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True,
                             limit=2000, address='shenzhen', start_time="2016-08-31 02:18:22")
        Guest.objects,create(id=1, event_id=1, realname='alen',
                             phone='13711001101', email='alen@mail.com')

    def test_event_modules(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, "shenzhen")
