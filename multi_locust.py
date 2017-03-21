from random import randint
from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession

def index(l):
    l.client.get("/")

class LocustBehavior(TaskSet):
    tasks = {index: 1}


    def execute_task(self, task, *args, **kwargs):
        host = get_random_host()
        self.locust.client = HttpSession(host)
        super(LocustBehavior, self).execute_task(task, *args, **kwargs)
    
class SharedUser(HttpLocust):
    task_set = LocustBehavior
    min_wait = 1000
    max_wait = 3000
    user = randint(1, 3000)

def get_random_host():
    return "http://testdomain" + str(randint(1, 3000)) + ".com"
