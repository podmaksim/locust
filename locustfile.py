from locust import HttpUser, task, TaskSet


class MyLoc(TaskSet):

    def on_start(self):
        self.client.verify = False

    @task(1)
    def index(self):
        self.client.get("")


class WebsiteUser(HttpUser):
    tasks = [MyLoc]
    min_wait = 5000
    max_wait = 9000
