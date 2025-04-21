# python import
import json
import os

_language = "en"
_translations = {}

def load_locale(lang_code):
    global _language, _translations
    _language = lang_code
    path = os.path.join(os.path.dirname(__file__), 'locales', f'{lang_code}.json')
    try:
      with open(path, encoding="utf-8") as f:
          _translations = json.load(f)
    except FileNotFoundError:
        print(f'⚠️ Translation file not found: {path}')
        _translations = {}

def t(key, **kwargs):
    text = _translations.get(key, key)
    return text.format(**kwargs)
