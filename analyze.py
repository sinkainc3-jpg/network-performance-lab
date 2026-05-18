import os
import pandas as pd
import matplotlib.pyplot as plt
from config import CSV_FILE

def main():
    os.makedirs("plots", exist_ok=True)

    df = pd.read_csv(CSV_FILE)

    plt.figure()
    plt.plot(df["latency_ms"])
    plt.title("Latency Over Time")
    plt.xlabel("Samples")
    plt.ylabel("Latency (ms)")
    plt.savefig("plots/latency.png")
    plt.close()

    plt.figure()
    plt.plot(df["download_mbps"], label="Download")
    plt.plot(df["upload_mbps"], label="Upload")
    plt.title("Bandwidth Over Time")
    plt.xlabel("Samples")
    plt.ylabel("Speed (Mbps)")
    plt.legend()
    plt.savefig("plots/speed.png")
    plt.close()

    print("Graphs saved in /plots")

if __name__ == "__main__":
    main()