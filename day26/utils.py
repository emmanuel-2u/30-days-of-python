from functools import reduce

def only_words(string):
    return [return_only_alpha(word).lower() for word in string.strip().split(' ') if word]
    
def return_only_alpha(string):
    word = ''.join([char for char in string if char.isalpha()])
    return word

def string_length(string):
    # Not using regex because I'll have to join the string together which
    # might add more spaces. e.g Hello  there! will add 1 more space if
    # findall and ' '.join is used
    stripped_string = ''.join([char for char in string.strip() if char.isalpha() or char.isspace()])
    return len(stripped_string)
    
def num_of_words(list):
    words_frequency = {}
    for word in list:
        if word in words_frequency:
            words_frequency[word] = words_frequency[word] + 1
        else:
            words_frequency[word] = 1
    return sorted(words_frequency.items(), key=lambda x: x[1], reverse=True)

def total_words(list):
    return len(list)

# Using custom_length cause after the 2 elements has been processed
# one of the parameter will be int
def total_characters(list_of_words):
    return reduce(lambda a, b: custom_length(a) + custom_length(b), list_of_words)

def custom_length(string):
    return string if type(string) == int else len(string)

def most_occuring_word(list):
    return '' if not list else list[0][0]
    
def process_content(content):
    words = only_words(content)
    t_words = total_words(words)
    t_characters = string_length(content)
    word_frequency = num_of_words(words)
    m_occuring = most_occuring_word(word_frequency)
    return [t_words, t_characters, word_frequency, m_occuring]
    
# Could not implement this lexical_density cause nltk requires a lot of download
# def lexical_density(sentence):
#     nltk_part_of_speech = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WRB']