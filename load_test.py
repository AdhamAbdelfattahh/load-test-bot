import requests
import time
import concurrent.futures
import random

URL = "https://www.youtube.com/watch?v=q_qFydLjmv8&list=PLEzOcs9Uvqogl1CFAMLt2utB6nAgCv21N&pp=gAQB"   # <-- Replace with your website
BOT_COUNT = 5                      
MIN_RUN = 5 * 60                   
MAX_RUN = 20 * 60                  
REST_TIME = 2 * 60                 

def hit_site(session_id):
    try:
        response = requests.get(URL, timeout=5)
        print(f"[Bot {session_id}] Status: {response.status_code}")
    except:
        print(f"[Bot {session_id}] Error")

def run_load_cycle():
    run_time = random.randint(MIN_RUN, MAX_RUN)
    end_time = time.time() + run_time
    print(f"\n=== Running load for {run_time // 60} minutes with {BOT_COUNT} bots ===")

    while time.time() < end_time:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(hit_site, range(BOT_COUNT))

    print("=== Cooling down for 2 minutes ===")
    time.sleep(REST_TIME)

if __name__ == "__main__":
    while True:
        run_load_cycle()
