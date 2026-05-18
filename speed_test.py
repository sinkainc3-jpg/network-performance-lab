import speedtest

def measure_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000  # Mbps
    upload = st.upload() / 1_000_000      # Mbps

    return {
        "download": round(download, 2),
        "upload": round(upload, 2)
    }