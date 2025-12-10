import requests
import time
import concurrent.futures
import random

# -----------------------------
# CHANGE THIS TO YOUR STAGING URL
# -----------------------------
URL = "https://www.youtube.com/watch?v=q_qFydLjmv8&list=PLEzOcs9Uvqogl1CFAMLt2utB6nAgCv21N&pp=gAQB"

BOT_COUNT = 5       # Number of parallel bots
MIN_RUN = 5 * 60    # 5 minutes
MAX_RUN = 20 * 60   # 20 minutes
REST_TIME = 2 * 60  # 2 minutes

def hit_site(bot_id):
    """Single bot hitting the website."""
    try:
        r = requests.get(URL, timeout=5)
        print(f"[Bot {bot_id}] Status: {r.status_code} Time: {r.elapsed.total_seconds():.2f}s")
    except Exception as e:
        print(f"[Bot {bot_id}] Error: {e}")

def run_load_cycle():
    """Run the traffic cycle with multiple bots."""
    run_time = random.randint(MIN_RUN, MAX_RUN)
    end_time = time.time() + run_time

    print(f"\n=== Running load for {run_time // 60} min with {BOT_COUNT} bots ===")

    while time.time() < end_time:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(hit_site, range(1, BOT_COUNT + 1))
    
    print("=== Cooling down for 2 minutes ===")
    time.sleep(REST_TIME)

if __name__ == "__main__":
    while True:
        run_load_cycle()
