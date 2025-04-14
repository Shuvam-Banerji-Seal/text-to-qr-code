#!/usr/bin/env python3

import argparse
import qrcode
from PIL import Image

def create_qr_code(data, file_name="qr_code.png", dpi=600):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGB")
    img.save(file_name, "PNG", dpi=(dpi, dpi))
    print(f"✅ QR code saved as '{file_name}' with {dpi} DPI.")

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code PNG from input text.")
    parser.add_argument("-i", "--input", required=True, help="Text or URL to encode in QR code.")
    parser.add_argument("-o", "--output", default="qr_code.png", help="Output file name (PNG).")
    parser.add_argument("--dpi", type=int, default=600, help="DPI for output image (default: 600).")

    args = parser.parse_args()
    create_qr_code(args.input, args.output, args.dpi)

if __name__ == "__main__":
    main()
