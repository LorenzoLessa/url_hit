import requests
import concurrent.futures

# Loadbalancer URL
url = 'http://hello-hello-1fy7g2xrtsbth-1535519657.us-east-1.elb.amazonaws.com/'

def make_request(url):
    response = requests.get(url)
    return response.text

with concurrent.futures.ThreadPoolExecutor(max_workers=1000000) as executor:
    futures = [executor.submit(make_request, url) for _ in range(33000)]

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
