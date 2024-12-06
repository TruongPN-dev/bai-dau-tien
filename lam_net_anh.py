import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("your_model.h5")

def deep_learning_sharpen(image_path, output_path):
    # Load ảnh
    image = cv2.imread(image_path)
    if image is None or image.size == 0:
        print("Không thể đọc ảnh nguồn hoặc ảnh rỗng.")
        return

    # Chuyển đổi ảnh sang định dạng RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Scale ảnh về khoảng [0, 1]
    image_rgb = image_rgb.astype("float32") / 255.0

    # Sử dụng mô hình deep learning để làm nét ảnh
    sharpened_image = model.predict(np.expand_dims(image_rgb, axis=0))[0]

    # Scale ảnh về khoảng [0, 255]
    sharpened_image = (sharpened_image * 255).astype("uint8")

    # Lưu ảnh đã làm nét
    cv2.imwrite(output_path, cv2.cvtColor(sharpened_image, cv2.COLOR_RGB2BGR))

    print("Ảnh đã được làm nét và đã được lưu thành công!")

# Thay đổi đường dẫn của ảnh đầu vào và đường dẫn để lưu ảnh đã làm nét
input_image_path = r"C:\Users\phamn\OneDrive\Máy tính\zalo.jpg"
output_image_path = r"C:\Users\phamn\OneDrive\Máy tính\da_lam_net.jpg"

# Gọi hàm để làm nét ảnh bằng deep learning
deep_learning_sharpen(input_image_path, output_image_path)