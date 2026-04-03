import os 
from PIL import Image

class ImageResizer:

    def __init__(self):
        self.supported_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
    
    def resize_single(self,input_path,output_path,new_width=None,new_height=None,percent=None):
        img = Image.open(input_path)
        width , height = img.size

        #conditon 
        if percent:
            new_w = int((new_width * percent) / 100)
            new_h = int((new_height * percent)/ 100)
        elif new_width and new_height:
            new_w , new_h = new_width, new_height
        elif new_width:
            ratio =  height/width
            new_w = new_width
            new_h = int(new_width * ratio)
        elif new_height:
            ratio = width / height
            new_h = new_height
            new_w = int(ratio * new_height)
        else:
            new_h , new_w = new_height,new_width
        
        resizer = img.resizer((new_w,new_h),Image.Resampling.LANCZOS)
        resizer.save(output_path)
        return (new_h , new_w)
    

    def batch_resizer(self,input_folder,output_folder,**kwargs):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        resize_file = []
        for f in os.listdir(input_folder):
            if f.lower().endswith(self.supported_ext):
                in_path = os.path.join(input_folder,f)
                ou_path = os.path.join(output_folder,f)
                new_size = self.resize_single(in_path,ou_path,**kwargs)
                resize_file.append((f,new_size))
        return resize_file

resizer = ImageResizer()
resizer.resize_single("example.jpg","output.jpg",new_width=600)
resizer.batch_resizer("Photos","resizephots_folder",percent=50)