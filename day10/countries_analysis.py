import sys, os

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path)

from countries_data import data

def no_of_langs(data):
    total_langs = 0
    for country in data:
        total_langs += len(country['languages'])
    return total_langs

def most_spoken_lang(data):
    langs = {}
    # Create a dictionary of languages to amount appeared
    for country in data:
        for lang in country['languages']:
            if lang in langs:
                langs[lang] = langs[lang] + 1
            else:
                langs[lang] = 1
    # Get most spoken languages
    sorted_langs = sorted(langs.items(), key=lambda lang: lang[1], reverse=True)
    return sorted_langs

def most_populated_country(data):
    sorted_countries = sorted(data, key=lambda country: country['population'], reverse=True)
    result = []
    for country in sorted_countries:
        result.append([country['name'], country['population']])
    return result

# def 
print('Number of languages ', no_of_langs(data))
print('10 most spoken languages are ', most_spoken_lang(data)[0:10])
print('10 most populated country are ', most_populated_country(data.copy())[0:10])