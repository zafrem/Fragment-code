from googletrans import Translator

def google_trans(str, target):
    translator = Translator()
    translation = translator.translate(str, dest=target)
    return translation.text


def google_trans_detect(str):
    translator = Translator()
    return translator.translate(str).src


if __name__ == "__main__":
    lang = google_trans_detect("この文章は日本語") #jo
    print(lang)
    lang = google_trans_detect("English") #en
    print(lang)
    lang = google_trans_detect("한글") #ko
    print(lang)
    lang = google_trans_detect("谢谢") #zh-CN
    print(lang)
    lang = google_trans("谢谢. 我学汉文", "en")
    print(lang)

# Output
# Detected(lang=ja, confidence=None)
# Detected(lang=en, confidence=None)
# Detected(lang=ko, confidence=None)
# Detected(lang=zh-CN, confidence=None)
# Thank you. I learn Chinese