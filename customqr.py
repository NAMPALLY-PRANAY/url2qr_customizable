import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Customized QR Code Generator")

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # URL Entry
        tk.Label(self.root, text="Enter URL:").pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        # Color Selection
        tk.Button(self.root, text="Select QR Code Color", command=self.choose_qr_color).pack(pady=5)
        self.qr_color = "#000000"  # Default color

        tk.Button(self.root, text="Select Background Color", command=self.choose_bg_color).pack(pady=5)
        self.bg_color = "#ffffff"  # Default color

        # Image Upload
        tk.Button(self.root, text="Upload Center Image", command=self.upload_image).pack(pady=5)
        self.image = None

        # Generate QR Code
        tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code).pack(pady=10)

        # Display QR Code
        self.qr_code_label = tk.Label(self.root)
        self.qr_code_label.pack(pady=10)

    def choose_qr_color(self):
        color_code = colorchooser.askcolor(title="Choose QR Code Color")
        if color_code[1]:
            self.qr_color = color_code[1]

    def choose_bg_color(self):
        color_code = colorchooser.askcolor(title="Choose Background Color")
        if color_code[1]:
            self.bg_color = color_code[1]

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")

    def generate_qr_code(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        # Check if the QR code color and background color contrast is sufficient
        if not self.is_contrast_sufficient(self.qr_color, self.bg_color):
            messagebox.showwarning("Contrast Warning", "The QR code and background colors do not have enough contrast. Please select colors with higher contrast for better scanning.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color=self.qr_color, back_color=self.bg_color).convert("RGBA")

        if self.image:
            # Resize image to fit in QR code
            img_size = qr_img.size[0] // 4  # Adjust size as needed, not too large
            resized_image = self.image.resize((img_size, img_size), Image.LANCZOS)

            # Paste the image in the center
            position = ((qr_img.size[0] - resized_image.size[0]) // 2, (qr_img.size[1] - resized_image.size[1]) // 2)
            qr_img.paste(resized_image, position, resized_image)

        # Convert to ImageTk format for display
        tk_img = ImageTk.PhotoImage(qr_img)
        self.qr_code_label.config(image=tk_img)
        self.qr_code_label.image = tk_img

    def is_contrast_sufficient(self, qr_color, bg_color):
        # Simplistic contrast check: ensure that the QR code color and background color are not too similar
        qr_color_rgb = self.hex_to_rgb(qr_color)
        bg_color_rgb = self.hex_to_rgb(bg_color)

        # Calculate contrast ratio (simple difference in RGB values)
        contrast = sum(abs(q - b) for q, b in zip(qr_color_rgb, bg_color_rgb))
        return contrast > 300  # Threshold for sufficient contrast, adjust as needed

    def hex_to_rgb(self, hex_color):
        # Convert hex color to RGB tuple
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Create the main window
root = tk.Tk()
app = QRCodeGenerator(root)
root.mainloop()
