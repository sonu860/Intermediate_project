import speedtest
import time

class SpeedTest:

    def __init__(self):
        pass
    
    def format_speed(self, bps):
        return f"{bps / 1_000_000:.2f} Mbps"
    
    def speed_test(self):
        print("\n===== INTERNET SPEED TEST =====")
        print("Testing... Isme 30-60 seconds lag sakte hain.")

        st = speedtest.Speedtest()

        print(f"Finding best server.....")
        st.get_best_server()
        print(f"✅ Server: {st.results.server['name']}, {st.results.server['country']}")

        # test ping
        ping = st.results.ping
        print(f"📶 Ping: {ping:.2f} ms")

        #test downloading
        print("⬇️ Testing download speed...")
        
        down_start = time.time()
        download_bps = st.download()
        download_time = time.time() - down_start

        # test upload
        print("⬆️ Testing upload speed...")

        upload_start = time.time()
        upload_bps = st.upload()
        upload_time = time.time() - upload_start

        print("\n===== RESULTS =====")
        print(f"📶 Ping: {ping:.2f} ms")
        print(f"⬇️ Download: {self.format_speed(download_bps)}")   # ✅ self. lagaya
        print(f"⬆️ Upload: {self.format_speed(upload_bps)}")       # ✅ self. lagaya
        print(f"⏱️ Test completed in {download_time + upload_time:.1f} seconds")

        # Rating based on speed
        speed_mbps = download_bps / 1_000_000
        if speed_mbps >= 50:
            print("🌟 Rating: Excellent! Very fast connection.")
        elif speed_mbps >= 25:
            print("👍 Rating: Good. Suitable for HD streaming.")
        elif speed_mbps >= 10:
            print("👌 Rating: Fair. Basic browsing and SD streaming.")
        else:
            print("⚠️ Rating: Slow. May face buffering issues.")

    def error_handler(self):
        try:
            self.speed_test()
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
if __name__ == "__main__":
    speed = SpeedTest()
    speed.error_handler()