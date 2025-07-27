from collections import OrderedDict

programming_glossary = OrderedDict()

programming_glossary['Variable'] = 'A reserved memory location to store values.'
programming_glossary['Function'] = 'A block of code which only runs when it is called.'
programming_glossary['Loop'] = ' An instruction that repeats multiple times as long as some condition is met.'
programming_glossary['Array'] = ' A data structure that stores values of the same type.'
programming_glossary['Boolean'] = 'A result that can only have one of two possible values: true or false.'

for term, meaning in programming_glossary.items():
    print(f'{term}: {meaning}')
