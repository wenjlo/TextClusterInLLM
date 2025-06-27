import re
import opencc
import jieba
converter = opencc.OpenCC('s2t.json')
stop_words_file = './cn_stop_words.txt'


def filter_out_non_chinese_strings(text):
    # 正則表達式模式，匹配常見的中文字元 Unicode 範圍
    # [\u4E00-\u9FFF]: 這個範圍包含了絕大多數的 CJK (中日韓) 統一表意文字，也就是中文字元。
    chinese_pattern = re.compile(r'[\u4E00-\u9FFF]')

        # 使用 search() 方法在字串中尋找模式
        # 如果找到任何中文字元，search() 會回傳一個匹配對象（在布林上下文中為 True）
        # 如果沒找到，則回傳 None（在布林上下文中為 False）
    if chinese_pattern.search(text):
        return text
    else:
        return ''


def s2t(text):
    global converter
    return converter.convert(text)


def load_stopwords(filepath):
    """Loads a Chinese stop word list from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = {line.strip() for line in f if line.strip()}
    return stopwords


chinese_stopwords = load_stopwords(stop_words_file)

def remove_chinese_stopwords(text, stopwords):
    """
    Segments Chinese text and removes stop words.
    Args:
        text (str): The input Chinese text.
        stopwords (set): A set of Chinese stop words.
    Returns:
        list: A list of words after segmentation and stop word removal.
    """
    # Segment the text
    words = jieba.cut(text)

    # Filter out stop words
    filtered_words = [word for word in words if word.strip() and word.strip() not in stopwords]
    return filtered_words


def skip_stop_words(text):
    global chinese_stopwords
    cleaned_words = remove_chinese_stopwords(text, chinese_stopwords)
    cleaned_text = "".join(cleaned_words)
    if cleaned_text == '':
        return cleaned_text
    else:
        return text


def skip_image_files(text):
    file_type = text.split('.')[-1]
    if file_type in ['png', 'jpg', 'jpeg','gif','avi','mp4']:
        return ''
    else:
        return text