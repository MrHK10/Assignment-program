import pandas as pd
def punjabi_to_english_dict(file_name, punjabi_column_name, english_column_name):
    punjabi_to_eng = {}
    df = pd.read_excel(file_name)  
    for index, row in df.iterrows():
        english_word = row[english_column_name]
        punjabi_words = [row[col] for col in punjabi_column_name if pd.notnull(row[col])]
        for punjabi_word in punjabi_words:
            punjabi_to_eng[punjabi_word] = english_word
    return punjabi_to_eng
def searchenglishword(punjabi_word, punjabi_to_eng_dict):
    return punjabi_to_eng_dict.get(punjabi_word, "Word not found in the dictionary")
def main():
    file_name = 'Book1.xlsx' 
    pcolumn = ['pu', 'pu1','pu2'] 
    ecolumn = 'eg'  
    p_to_e_dict = punjabi_to_english_dict(file_name, pcolumn, ecolumn)
    word_to_search = input("Enter the Punjabi word to search: ")
    english_translation = searchenglishword(word_to_search, p_to_e_dict)
    print(f"The English word for '{word_to_search}' is '{english_translation}'")
if __name__ == "__main__":
    main()

