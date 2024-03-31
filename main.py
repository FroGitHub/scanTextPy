import tessORC

import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            textOfImg = tessORC.extract_text_from_image(file_path)

            file_path = file_path.replace(".jpg", ".doc")
            file_path = file_path.replace(".png", ".doc")

            tessORC.save_text_to_file(textOfImg, file_path)
        except:
            print("Файл уже створений з таким же іменем, як і фото або проблеми при зчитуванні")


def start():
    print("Made by Сhepchik \nProgram started")

    root = tk.Tk()
    root.title("Завантаження файлу")

    # Створення кнопки "Завантажити файл"
    button = tk.Button(root, text="Завантажити файл", command=open_file)
    button.pack(pady=10)

    # Запуск головного циклу обробки подій
    root.mainloop()


if __name__ == '__main__':
    start()

