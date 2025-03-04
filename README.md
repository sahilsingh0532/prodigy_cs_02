﻿# Prodigy_cs_02
## Pixel Manipulation for Image Encryption

## Task Overview
This project implements an **image encryption tool** using pixel manipulation techniques. The program allows users to encrypt and decrypt images by modifying pixel values through swapping or mathematical operations.

## How It Works
Pixel manipulation-based encryption involves modifying the pixel values of an image using reversible transformations to obscure the original content. Some common techniques include:
- Swapping pixel positions.
- Applying mathematical operations (e.g., XOR, addition, or bitwise shifts) on pixel values.
- Using a secret key for controlled transformations.

## Features
- Encrypt an image by modifying pixel values.
- Decrypt an encrypted image to retrieve the original.
- Support for common image formats (JPEG, PNG, BMP, etc.).
- User-defined encryption key for enhanced security.

## Installation & Setup
Ensure you have Python installed on your system. If not, download and install it from [Python Official Website](https://www.python.org/downloads/).

### Required Libraries:
```bash
pip install pillow numpy
```

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/sahilsingh0532/prodigy_cs_02
   ```
2. Navigate to the project folder:
   ```bash
   cd prodigy_cs_02
   ```
3. Run the program:
   ```bash
   main.py
   ```

## Usage
1. Run the script and select an image.
2. Enter an encryption key (optional).
3. Choose to encrypt or decrypt.
4. The encrypted/decrypted image will be saved.


## Contributing
Feel free to fork this repository and submit pull requests to enhance the project.

## License
This project is licensed under the MIT License.

