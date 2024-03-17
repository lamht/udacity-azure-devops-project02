from locust import HttpUser, between, task

import time


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def home(self):
        for item_id in range(10):
            self.client.get("/")
            time.sleep(1)

    def predict(self):
        self.client.post("/predict", json={"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}})