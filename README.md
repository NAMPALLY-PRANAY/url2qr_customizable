# url2qr_customizable
# Customized QR Code Generator

This is a **Customized QR Code Generator** built using **Python** and **Tkinter**. It allows users to generate QR codes with custom colors, background colors, and embedded center images.

## Features
- Enter a URL to generate a QR code
- Choose a custom **QR code color**
- Choose a **background color**
- Upload an image to embed in the center of the QR code
- Ensures **high contrast** between QR code and background for better scanning
- Displays the generated QR code within the application

## Requirements
Make sure you have **Python 3.x** installed, and install the required libraries using:

```bash
pip install pillow qrcode tkinter
```

## Usage
Run the Python script:

```bash
python customqr.py
```

## Code Structure
- **`QRCodeGenerator`**: The main class that handles the UI and QR code generation.
- **`create_widgets`**: Creates the Tkinter UI components.
- **`choose_qr_color` & `choose_bg_color`**: Allow users to pick colors.
- **`upload_image`**: Enables uploading an image for embedding.
- **`generate_qr_code`**: Generates and displays the QR code.
- **`is_contrast_sufficient`**: Ensures the QR code is readable by checking color contrast.

## Screenshot
![image](https://github.com/user-attachments/assets/3732d173-f4b4-4580-817c-719a1f9633c3)


## License
This project is open-source and free to use.

