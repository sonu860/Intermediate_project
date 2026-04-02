import os 
from send2trash import send2trash

class DesktopCleaner:

    def __init__(self,unwanted_extension = None,safe_mode=True):
        self.desktop_path = os.path.join(os.path.expanduser("~"),"Desktop")
        self.unwanted_extension = unwanted_extension or [
            '.tmp', '.log', '.bak', '.DS_Store', 
            '.ini', '.cache', '.temp', '.swp', '.~'
        ]
        self.safe_mode = safe_mode
        self.delete_file = []

    
    def scan_desktop(self):
        print(f"Scanning => {self.desktop_path}")
        if not os.path.exists(self.desktop_path):
            print("Not found file path")
            return 
        
        for item in os.listdir(self.desktop_path):
            item_path = os.path.join(self.desktop_path,item)
            if os.path.isfile(item_path):
                ext = os.path.splitext(item_path)[1].lower()
                if ext in self.unwanted_extension:
                    self.delete_path(item_path)
    
    def delete_path(self,item_file):

        try:
        
            if self.safe_mode:
                print(f"File send to trash")
                send2trash(item_file)
                print(f"Moved to trash mode {os.path.basename(item_file)}")
            else:
                os.remove(item_file)
                print(f"permanently remove from os {os.path.basename(item_file)}")
            
            self.delete_file.append(item_file)
        except Exception as e:
            print(f"File detected fail {item_file}" , e)
    @staticmethod
    def summery_file():
        if self.delete_file:
             print(f"\n✅ Cleaned {len(self.delete_file)} files.")
        else:
            print("\n✨ No unwanted files found.")

if __name__ ==  '__main__':
    # Customize unwanted extensions
    extensions = ['.tmp', '.log', '.bak', '.DS_Store', '.ini', '.cache']
    cleaner = DesktopCleaner(unwanted_extension=extensions, safe_mode=True)
    cleaner.scan_desktop()