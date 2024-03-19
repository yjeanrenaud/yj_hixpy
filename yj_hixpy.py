# Calculates the Hohenheimer Verstaendlichkeitsindex (HIX), see https://klartext.uni-hohenheim.de/hix or https://doi.org/10.1007/978-3-658-23053-1_10
# yjCalcHIX (text) expects text to be a string and returns a numeric value (from 0 to 20) indicating the understandability of the *German* text.
# Yves Jeanrenaud, 2024.

import re

def is_foreign_word(word):
    # Beispiel einer sehr simplen Heuristik: Wörter, die mit typischen fremdsprachigen Suffixen enden
    # Dies ist lediglich ein Platzhalter und sollte durch eine robustere Logik ersetzt werden
    foreign_suffixes = ('-tion', '-ity', '-logy','-mus','-ix', '-ist', '-ik', '-ie','-tor','-tät','-ine','-iv','-ös','-iell','-ieren','-ine','-ät','-är','-que','-ik','-eur','-um')
    return any(word.endswith(suffix) for suffix in foreign_suffixes)

def yjCalcHIX(text):
    # get rid of special chars and split the sentences.
    sentences = re.split(r'[.!?]', text)
    # get rid of emtpy strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    total_words = 0
    total_syllables = 0
    for sentence in sentences:
        # count amount of words per sentence
        words = sentence.split()
        total_words += len(words)
        # count syllables per word
        for word in words:
            # simplified hyphenation by number of vowels per word
            num_vowels = len(re.findall(r'[aeiouyäöüAEIOUYÄÖÜ]', word))
            # Consider words with less than 3 letters as one syllable
            if num_vowels == 0:
                num_vowels = 1
            total_syllables += num_vowels
             # Erkennung von Fremdwörtern
            if is_foreign_word(word):
                total_foreign_words += 1

    # Average sentence length
    avg_sentence_length = total_words / len(sentences)
    # Average word length
    avg_word_length = total_syllables / total_words
    # Foreign word / word ratio
    foreign_word_ratio = total_foreign_words / total_words if total_words > 0 else 0
    
    # calc HIX
     HIX = 30 * (avg_sentence_length / avg_word_length) + 3.1291 - (foreign_word_ratio * 50)

    return HIX
