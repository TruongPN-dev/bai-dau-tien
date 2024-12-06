import torch
import torchvision.transforms as transforms
from PIL import Image, ImageFilter  
import requests
from io import BytesIO

# Load pre-trained ESRGAN model
model = torch.hub.load('xinntao/ESRGAN', 'esrgan')

# Define transformation
pre_process = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to upscale and sharpen an image
def upscale_and_sharpen(image_path):
    # Load image
    img = Image.open(image_path).convert('RGB')
    img = pre_process(img).unsqueeze(0)
    
    # Upscale image using ESRGAN
    with torch.no_grad():
        output = model(img).clamp(0.0, 1.0)
    
    # Convert output tensor to PIL image
    output = (output.squeeze().permute(1, 2, 0) * 255).cpu().numpy().astype('uint8')
    output_image = Image.fromarray(output)
    
    # Apply sharpening filter
    output_image = output_image.filter(ImageFilter.SHARPEN)
    
    return output_image

# Example usage
image_url = r'C:\Users\phamn\OneDrive\Máy tính\zalo.jpg'  # URL của ảnh bạn muốn xử lý
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

result_image = upscale_and_sharpen(image)

# Lưu ảnh kết quả
result_image.save(r'C:\Users\phamn\OneDrive\Máy tính')

# Hiển thị ảnh kết quả
result_image.show()
