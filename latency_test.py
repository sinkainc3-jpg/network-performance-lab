from ping3 import ping
from config import SERVERS

def measure_latency():
    results = {}

    for server in SERVERS:
        try:
            latency = ping(server, timeout=2)
            results[server] = round(latency * 1000, 2) if latency else None
        except Exception:
            results[server] = None

    return results