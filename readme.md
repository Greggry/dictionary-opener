# dictionary-opener

The way this script works:
- main python script file takes arguments in following order: browser, lanuage, mode
- .sh files are created as a demonstration. One can bind them to a key combination in order to quickly search for a term wherever they are.

examples:
- python dictionary-opener.py firefox english auto
- python dictionary-opener.py chrome german

As you can see, the last argument can be omitted. When it's auto, the script asks for just one term to search, and it shuts down by itself. Then the last argument is not present, the script asks for terms to search one at a time, and doesnt shut down.

Currently, the program supports 3 languages / dictionaries, english (oxfordlearnersdictionaries.com), german (collinsdictionary.com) and polish->english (dictionary.cambridge.org). One can add more by inserting a search link to the dictionary and to list of available languages in the python script.
