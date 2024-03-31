from PIL import Image
import pytesseract


def extract_text_from_image(image_path):

    print("Зчитування тексту...")
    image = Image.open(image_path)
    try:
        custom_config = r'--oem 3 --psm 4 --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" -l ukr'
        print("...")
        extracted_text = pytesseract.image_to_string(image, config=custom_config)
        print("...Зчитав")
        return extracted_text
    except:
        print("тесеракт не знайдений")

    return 0


def save_text_to_file(text, output_file):
    with open(output_file, 'x', encoding='utf-8') as f:
        f.write(text)
    print("Файл з текстом збережений біля фото")

