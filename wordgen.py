# Copyright (c) LJC
#
# SPDX-License-Identifier: BSD-2-Clause
#
# Script for generating Alzipar root entries in the dictionary.
#
# rewrite in java later

import json



# Descriptor Forms
df1 = {} # Adverb form:    1a2o3
df2 = {} # Adjective form: 1i2o3

def _get_root():
    rt = input("Enter triconsonantal root (1-2-3): ").upper()
    explaination = input("Enter the general meaning of the root: ")
    exampleWords = input("Enter example words (w1, w2, w3, etc.): ")
    exampleTranslations = input("Enter example words translated to English (in relative order): ")

    return {
        "word": rt,
        "uses": [
            {
                "hasBadge": False,
                "badgeText": "",
                "type": "ROOT",
                "explaination": explaination,
                "example": exampleWords,
                "gloss": "",
                "exampleTranslation": exampleTranslations
            }
        ]
    }

def _get_word(word, type, r1, r2, r3, hasRoots = True):
    explaination = ""
    example = ""
    exampleTranslation = ""
    if (hasRoots):
        print(f"{type} form of {r1.upper()}-{r2.upper()}-{r3.upper()}: {word}")
        explaination = input("Enter the meaning of this form of the root: ")
        example = input("Enter an example sentence using this form of the root: ")
        exampleTranslation = input("Enter translation of the example sentence: ")
    else:
        explaination = input("Enter the meaning of the word: ")
        example = input("Enter an example sentence using this word: ")
        exampleTranslation = input("Enter translation of the example sentence: ")
    return {
        "word": word,
        "uses": [
            {
                "hasBadge": False,
                "badgeText": "",
                "type": type,
                "explaination": explaination,
                "example": example,
                "gloss": "",
                "exampleTranslation": exampleTranslation
            }
        ]
    }

def _get_verb_forms(r1, r2, r3):
    words = []

    # (V1) Intransative: 1a2a3a/Ya12a3a
    words.append(_get_word(f"{r1.upper()}a{r2}a{r3}a", "(V1) Intransative Verb", r1, r2, r3))
    # (V2) Transative: 1u2a3a/Yu12a3a
    words.append(_get_word(f"{r1.upper()}u{r2}a{r3}a", "(V2) Transative Verb", r1, r2, r3))
    # (V3) Causative: A12a3a/Yu12i3u
    words.append(_get_word(f"A{r1}{r2}a{r3}a", "(V3) Causative Verb", r1, r2, r3))
    # (V4) Reflexive: Ta1a2a3a/Yata1a2a3a
    words.append(_get_word(f"Ta{r1}a{r2}a{r3}a", "(V4) Reflexive Verb", r1, r2, r3))
    # (V5) Cooperative: Ta1a2u3a/Yata1a2u3a
    words.append(_get_word(f"Ta{r1}a{r2}u{r3}a", "(V5) Cooperative Verb", r1, r2, r3))
    # (V6) Transformative: I12a3a/Yai12a3a
    words.append(_get_word(f"I{r1}{r2}a{r3}a", "(V6) Transformative Verb", r1, r2, r3))
    # (V7) Inquisitive: Ista12a3a/Yasta12a3a
    words.append(_get_word(f"Ista{r1}{r2}a{r3}a", "(V7) Inquisitive Verb", r1, r2, r3))
    return words

def _get_noun_forms(r1, r2, r3):
    words = []

    # (N1) Singular: 1i2a3
    words.append(_get_word(f"{r1.upper()}i{r2}a{r3}", "(N1) Singular Noun", r1, r2, r3))
    # (N2) Dual:     1u2a3
    words.append(_get_word(f"{r1.upper()}u{r2}a{r3}", "(N2) Dual Noun", r1, r2, r3))
    # (N3) Plural:   1u2u3
    words.append(_get_word(f"{r1.upper()}u{r2}u{r3}", "(N3) Plural Noun", r1, r2, r3))
    # (N4) Agent:    Mu12i3
    words.append(_get_word(f"Mu{r1}{r2}a{r3}", "(N4) Agent Noun", r1, r2, r3))
    # (N5) Location: Ma12a3
    words.append(_get_word(f"Ma{r1}{r2}a{r3}", "(N5) Location Noun", r1, r2, r3))
    return words

def _get_descriptor_forms(r1, r2, r3):
    words = []

    # (D1) Adverb: 1a2o3
    words.append(_get_word(f"{r1.upper()}a{r2}o{r3}", "(D1) Adverb", r1, r2, r3))
    # (D2) Dual:     1i2o3
    words.append(_get_word(f"{r1.upper()}i{r2}o{r3}", "(D2) Adjective", r1, r2, r3))

def generate_rootless_word():
    return _get_word(input("Enter word: "), input("Enter type: "), "", "", "", hasRoots = False)

def generate_words():
    words = []
    r1, r2, r3 = "", "", ""

    root = _get_root()
    words.append(root)
    r1, r2, r3 = root["word"].split("-")[0].lower(), root["word"].split("-")[1].lower(), root["word"].split("-")[2].lower()
    if (input("generate verb forms?[y/N]: ").lower() == "y"):
        for word in _get_verb_forms(r1, r2, r3):
            words.append(word)
    if (input("generate noun forms?[y/N]: ").lower() == "y"):
        for word in _get_noun_forms(r1, r2, r3):
            words.append(word)
    if (input("generate descriptor forms?[y/N]: ").lower() == "y"):
        for word in _get_descriptor_forms(r1, r2, r3):
            words.append(word)

    return words

def main():
    words = []

    while(True):
        if(input("Continue generating words?[y/N]: ").lower() != "y"):
            break
        if(input("Generate rootless word?[y/N]: ").lower() == "y"):
            words.append(generate_rootless_word())
        else:
            for word in generate_words():
                words.append(word)

    for word in words:
        json_str = json.dumps(word, indent=4)
        print(json_str)

if __name__ == "__main__":
    main()