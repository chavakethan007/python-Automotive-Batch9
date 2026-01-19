import qrcode
from PIL import Image
import urllib.parse

# Correct base URL (matches Flask route)
BASE_URL = "http://127.0.0.1:5000/student"

# Number of students
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    sid = input("Student ID: ")
    name = input("Student Name: ")
    subject = input("Subject Details: ")
    marks = input("Enter marks: ")

    # Data stored in QR (URL parameters)
    data = {
        "id": sid,
        "name": name,
        "Subject": subject,
        "Marks": marks
    }

    # Create dynamic URL
    url = BASE_URL + "?" + urllib.parse.urlencode(data)

    # Create QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(
        fill_color="darkblue",
        back_color="lightyellow"
    ).convert("RGB")

    # Optional logo
    try:
        logo = Image.open("OIP.jpg")
        logo = logo.resize((80, 80))
        pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2
        )
        qr_img.paste(logo, pos)
    except:
        pass

    filename = f"{sid}_{name.replace(' ', '_')}.png"
    qr_img.save(filename)

    print(f"QR code generated successfully: {filename}")
