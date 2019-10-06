from locust import HttpLocust, TaskSet, task
import requests

#r = requests.post('http://127.0.0.1:5000/POST', json={'Price': 5, 'Face': 10}, headers={'Content-Type': 'application/json'})
#print(r.status_code)
r = requests.get('http://127.0.0.1:5000/GET?Price=119&Coupon=256', headers={})
print(r.status_code)
#print(r.json())
