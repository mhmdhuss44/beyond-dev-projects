import time
import traceback
import unittest
from infra.wrapperPage import base
from logic.event_validation_logic import checkEventsList
from logic.events_creation_logic import addEvent
from logic.new_event_type_logic import addEventType

# these tests are mostly on the events feature in the app
class TestAppiumEvents(unittest.TestCase):
    def setUp(self):
        self.baseCade=base()
        self.driver = self.baseCade.driver_set_up()

    def tearDown(self) -> None:
        self.driver.quit()



    # these three tests , test the same process with different inputs!

    # trying to add a new event with the 'important' category'
    def test_add_new_event_important_type(self):
        try:
            self.addedEvent = addEvent(self.driver, "doctor visit","doctor appoitemnt at 9:00",1)
            self.addedEvent.add_task_flow()
            time.sleep(3)
        except Exception as e:
            traceback.print_exc()
            self.fail(f"An unexpected error occurred: {e}")
            # Assert that there were no errors
        self.assertTrue(True, "No errors occurred during execution")


    # trying to add a new event with the 'forget' category'
    def test_add_new_event_forget_type(self):
        try:
            self.addedEvent = addEvent(self.driver, "birthday","dont forget mohammeds birthday",3)
            self.addedEvent.add_task_flow()
            time.sleep(3)
        except Exception as e:
            traceback.print_exc()
            self.fail(f"An unexpected error occurred: {e}")
            # Assert that there were no errors
        self.assertTrue(True, "No errors occurred during execution")


    # trying to add a new event with the 'task' category'
    def test_add_new_event_task_type(self):
        try:
            self.addedEvent = addEvent(self.driver, "beyondDev course","dont forget to wake up on 8:30 each day",2)
            self.addedEvent.add_task_flow()
            time.sleep(3)
        except Exception as e:
            traceback.print_exc()
            self.fail(f"An unexpected error occurred: {e}")
            # Assert that there were no errors
        self.assertTrue(True, "No errors occurred during execution")


    # verify that the new event succefully appears on the events list
    def test_add_new_event_important_type(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_flow()
        time.sleep(3)
        assert result, "Test failed: test wasnt added successfully"

    # verify that the new event succefully appears on calendar! events list
    def test_event_on_calendar(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_flow_calendar()
        time.sleep(3)
        assert result, "Test failed: test wasnt added successfully"

    # verify that the new event succefully appears on week page when pressing on the wanted date!
    def test_event_on_week(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_flow_week()
        time.sleep(3)
        assert result, "Test failed: test wasnt added successfully"


    # verify that we can add a new type succefullly
    def test_add_new_event_important_type(self):
        self.newType = addEventType(self.driver, "LoveType")
        result=self.newType.add_new_type_flow()
        time.sleep(5)
        assert result, "Test failed:new type wasnt added succefully"

    # verify that we can add a new type succefullly and create a new event with it
    def test_add_new_event_important_type(self):
        try:
            self.newType = addEventType(self.driver, "LoveType")
            result=self.newType.add_new_type_flow()
            time.sleep(3)
            self.addedEvent = addEvent(self.driver, "mothers day","bring some flowers",4)
            self.addedEvent.add_task_flow()
            time.sleep(3)
        except Exception as e:
            traceback.print_exc()
            self.fail(f"An unexpected error occurred: {e}")
            # Assert that there were no errors
        self.assertTrue(True, "No errors occurred during execution")

    # verify that we can delete an event succefullly
    def test_delete_event(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_delete_flow()
        time.sleep(3)
        assert not result, "Test failed: event still exist"


    # verify that we can still see the event after clicking no on the verfication question (if we sure we want to delete)
    def test_delete_event(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_not_delete_flow()
        time.sleep(3)
        assert result, "Test failed: event was deleted"

    # verify that we modify an event name
    def test_modify_event(self):
        self.addedEvent = addEvent(self.driver, "doctorVisit","doctor appoitemnt at 9:00",1)
        self.addedEvent.add_task_flow()
        time.sleep(3)
        self.valid=checkEventsList(self.driver,"doctorVisit")
        result=self.valid.verify_modify_flow("mhmds")
        time.sleep(1)
        assert result, "Test failed: event was not updated"
        time.sleep(3)













