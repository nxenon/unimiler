"""
Unimiler (Unicode Normalizer): a script for normalizing unicode, for bypassing purposes
"""
import unicodedata


def normalize_unicode(input_string):
    try:
        NFC = ascii(unicodedata.normalize("NFC", input_string))
        NFD = ascii(unicodedata.normalize("NFD", input_string))
        NFKC = ascii(unicodedata.normalize("NFKC", input_string))
        NFKD = ascii(unicodedata.normalize("NFKD", input_string))
    except Exception as e:
        print(f'Error occurred: {e}')
        return

    print(f'NFC: {NFC}')
    print(f'NFD: {NFD}')
    print(f'NFKC: {NFKC}')
    print(f'NFKD: {NFKD}')


if __name__ == '__main__':
    while True:
        text = input('Enter text to normalize:')
        normalize_unicode(text)
