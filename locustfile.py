import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def get_index(self):
        self.client.get("/")

    def on_start(self):
        self.client.get("/")

