import cv2
import numpy as np

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)  
    encrypted_img = img ^ key  
    cv2.imwrite("encrypted_image.png", encrypted_img)  
    return encrypted_img

def decrypt_image(encrypted_img, key):
    decrypted_img = encrypted_img ^ key  
    cv2.imwrite("decrypted_image.png", decrypted_img)  
    return decrypted_img

key = np.random.randint(0, 256, (1, 1, 3), dtype=np.uint8)  
image_path = "input.png"

enc_img = encrypt_image(image_path, key)

dec_img = decrypt_image(enc_img, key)
