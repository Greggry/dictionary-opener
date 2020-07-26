import os # os.system(cmd)
import sys # sys.argv

AVAILABLE_LANGUAGES = ['english', 'german']

if len(sys.argv) >= 3 and len(sys.argv) <= 4:
    
    # first argument, browser command (ex. 'firefox')
    BROWSER = sys.argv[1]

    # second argument, language from AVAILABLE_LANGUAGES
    LANG = sys.argv[2]
    
    if AVAILABLE_LANGUAGES.count(LANG) == 0:
        print(str(LANG) + ' is not a supported language')
        print('supported languages: ' + ', '.join(AVAILABLE_LANGUAGES))
        exit(1)
    
    if len(sys.argv) == 4:
        # third argument, close method. default: type an empty message to leave
        CLOSE_METHOD = sys.argv[3]
    else:
        # default
        CLOSE_METHOD = ''

else:
    print()
    print('usage: python dictionary-opener.py <BROWSER> <LANGUAGE> <CLOSING_METHOD>')
    print('ex. python dictionary-opener.py firefox german auto')
    print('CLOSING_METHOD can be omitted')
    print()
    
    exit(1)
    

def askForPhrase(browser_name, language):
    phrase = input('Phrase: ')
    
    if phrase == '':
        print('Empty message received')
        return phrase
    
    print('looking up ' + str(phrase))
    if language == 'german':
        os.system(BROWSER + ' https://www.collinsdictionary.com/dictionary/german-english/' + str(phrase))
    
    if language == 'english':
        os.system(BROWSER + ' https://www.oxfordlearnersdictionaries.com/definition/english/' + str(phrase) + '?q=' + str(phrase))
    
    return phrase

if CLOSE_METHOD == 'auto':
    print('Type a phrase in ' + LANG + ' to look up, the program will shut down by itself afterwards.')
    askForPhrase(BROWSER, LANG)
else:
    print('Type a phrase in ' + LANG + ' to look up, the program shuts down if you type an empty message')
    while askForPhrase(BROWSER, LANG) != '':
        continue

print('Shutting down...')
