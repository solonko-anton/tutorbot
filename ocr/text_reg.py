import cv2
import easyocr
import torch

reader = easyocr.Reader(['uk'], gpu=True if torch.cuda.is_available() else False) 

def process_image(image_path):
    img = cv2.imread(image_path)
    
    height, width = img.shape[:2]
    img_cropped = img[:, :width // 2] 
    
    results = reader.readtext(img_cropped, detail=1, paragraph=False)
    
    all_text = []
    for item in results:
        text = item[1].strip()  
        if text:  
            all_text.append(text)
    
    full_text = " ".join(all_text)
    print(full_text)

    return full_text

process_image('image.png')