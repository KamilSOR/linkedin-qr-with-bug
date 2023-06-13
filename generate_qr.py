import qrcode
from PIL import Image

def create_linkedin_qr(linkedin_url, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image = qr_image.convert("RGBA")

    image_path = "magnifying_glass.png"  # Ścieżka do pliku z obrazkiem lupy
    magnifying_glass = Image.open(image_path)
    magnifying_glass = magnifying_glass.resize((100, 100), Image.ANTIALIAS)

    qr_width, qr_height = qr_image.size
    mg_width, mg_height = magnifying_glass.size
    qr_image.paste(magnifying_glass, (int((qr_width - mg_width) / 2), int((qr_height - mg_height) / 2)), mask=magnifying_glass)

    qr_image.save(output_file)

linkedin_url = "https://www.linkedin.com/in/kamil-sorys-856641270"
output_file = "linkedin_qr.png"
create_linkedin_qr(linkedin_url, output_file)
