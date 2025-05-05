# pages/3_Rune_Translator.py

import streamlit as st
from functions import handle_chat_tab

def english_to_rune_tab():
    instruction = '''
    Convert the following English text into Elder Futhark-style runes using this mapped guide for letters a-z:
    {
      'a': 'ᚨ',
      'b': 'ᛒ',
      'c': 'ᚲ',
      'd': 'ᛞ',
      'e': 'ᛖ',
      'f': 'ᚠ',
      'g': 'ᚷ',
      'h': 'ᚺ',
      'i': 'ᛁ',
      'j': 'ᛃ',
      'k': 'ᚲ',
      'l': 'ᛚ',
      'm': 'ᛗ',
      'n': 'ᚾ',
      'o': 'ᛟ',
      'p': 'ᛈ',
      'q': 'ᛩ',
      'r': 'ᚱ',
      's': 'ᛋ',
      't': 'ᛏ',
      'u': 'ᚢ',
      'v': 'ᚡ',
      'w': 'ᚹ',
      'x': 'ᛉ',
      'y': 'ᛃ',
      'z': 'ᛉ'
    }

    Other than this, write as the original character or symbol.
    '''
    handle_chat_tab("english_to_rune", "English to Rune Translator", instruction, "gpt-4o")

st.set_page_config(page_title="Rune Translator")
english_to_rune_tab()