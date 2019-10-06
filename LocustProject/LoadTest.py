from locust import HttpLocust, TaskSet, task
import random
import json
complex

posturl='http://127.0.0.1:5000'
class UserTaskGetAndPost(TaskSet):
    @task(1)
    def get_and_post(self):
        price = random.randint(1, 1000)
        Coupon = random.randint(1, 1000)
        with self.client.get("/GET?Price="+str(price)+'&Coupon='+str(Coupon), catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                getvalueresult = response.content
                #postresponse = requests.post(posturl+'/POST', json=json.loads(getvalueresult), headers={'Content-Type': 'application/json'})
                with self.client.post(url=posturl+'/POST'+'?Coupon='+str(Coupon), data=getvalueresult, headers={'Content-Type': 'application/json'}, catch_response=True) as PostResponse:
                    if PostResponse.status_code == 200:
                        PostResponse.success()
                    else:
                        PostResponse.failure("Assert failed with post request!")
            else:
                response.failure('Get request Failed!')
    @task(2)
    def just_get(self):
        price = random.randint(1, 1000)
        Coupon = random.randint(1, 1000)
        with self.client.get("/GET?Price="+str(price)+'&Coupon='+str(Coupon), catch_response=True) as response:
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
    host = posturl

if __name__ == '__main__':
    import os
    os.system("locust -f LoadTest.py")
