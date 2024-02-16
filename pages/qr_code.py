import qrcode

# Web link to convert into QR code
web_link = "https://canine-classifier.streamlit.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(web_link)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save or display the QR code
qr_image.save("images/qrcode.png")  # Save QR code as PNG image
qr_image.show()  # Display QR code
