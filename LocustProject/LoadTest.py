from locust import HttpLocust, TaskSet, task
import random
import json
class UserTaskGetAndPost(TaskSet):
    @task(1)
    def get_and_post(self):
        price = random.randint(1, 5)
        with self.client.get("/GET/"+str(price), catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                getvalueresult = response.json
                postresponse = self.client.post("/POST/",  data=getvalueresult, headers={'Content-Type': 'application/json'})
                if postresponse.status_code == 200:
                    response.success()
                else:
                    response.failure('Post request Failed!')
            else:
                response.failure('Get request Failed!')
    @task(2)
    def just_get(self):
        price = random.randint(1, 5)
        with self.client.get("/GET/"+str(price), catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Get request Failed!')





class UserOne(HttpLocust):
    task_set = UserTaskGetAndPost
    weight = 1
    min_wait = 100
    max_wait = 300
    stop_timeout = 1
    host = "http://127.0.0.1:5000"

if __name__ == '__main__':
    UserOne().run()
