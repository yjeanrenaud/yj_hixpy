# Calculates the Hohenheimer Verstaendlichkeitsindex (HIX), see https://klartext.uni-hohenheim.de/hix or https://doi.org/10.1007/978-3-658-23053-1_10
# yjCalcHIX (text) expects text to be a string and returns a numeric value (from 0 to 20) indicating the understandability of the *German* text.
# Yves Jeanrenaud, 2024.

import re

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

    # Average sentence length
    avg_sentence_length = total_words / len(sentences)
    # Average word length
    avg_word_length = total_syllables / total_words
    # calc HIX
    HIX = 30 * (avg_sentence_length / avg_word_length) + 3.1291

    return HIX
