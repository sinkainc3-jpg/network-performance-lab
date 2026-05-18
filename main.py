import time
from config import INTERVAL
from latency_test import measure_latency
from speed_test import measure_speed
from logger import init_log, log_results

def run():
    init_log()
    print("Starting network monitoring...")

    while True:
        latency = measure_latency()
        speed = measure_speed()

        print("Latency:", latency)
        print("Speed:", speed)

        log_results(latency, speed)

        time.sleep(INTERVAL)

if __name__ == "__main__":
    run()