import easyocr

if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('test.jpg')
    print(text)
