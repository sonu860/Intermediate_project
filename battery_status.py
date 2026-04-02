import time
import psutil
from plyer import notification

#class 
class BatteryNotifier:

    #constructor
    def __init__(self):
        self.config = self.load_config()
        self.last_low_alert = False
        self.last_full_alert = False

    def load_config(self):
        return {"low": 20, "full": 95, "interval": 60}
    
    def notify(self,title,message):
        """  Send message Alert User """
        notitication.notify(title = title,message= message,timeout=5)
    

    def get_battery_status(self):
        """ Return (plugged and percentage) safetyly """
        try:
            battery = psutil.sensors_battery()
            if battery:
                return battery.percent , battery.power_plugged
            else:
                return None,None
        except  OSError:
                return None , None


    def get_check_status(self):
        percent , plugged = self.get_battery_status()
        
        if  percent  is None:
            print("Battery not detected  ,Stopping monitering")
            return False

        if percent <= self.config['low'] and not plugged:
            if not self.last_low_alert:
                self.notify("Battery is Low","Please plugged your device")
                self.last_low_alert =True

            else:
                self.last_low_alert = False
        

        if percent >= self.config['full'] and plugged:
            if not self.last_full_alert:
                self.notify("Battery is full","Please unplugged your device")
                self.last_full_alert = True
            
            else:
                self.last_full_alert = False
        
        return True
    
    def start_monitoring(self):
        """Start the infinite monitoring loop."""
        print(f"Battery Notifier Started. Checking every {self.config['interval']} seconds.")
        print(f"Low battery alert: <= {self.config['low']}% (when not charging)")
        print(f"Full battery alert: >= {self.config['full']}% (when charging)")

        while True:
            if not self.get_check_status():
                    break
            time.sleep(self.config['interval'])

if __name__ == "__main__":
    notifier = BatteryNotifier()
    notifier.start_monitoring()