from random import choice, randint
import time

axiom = 'S'

rules = dict()

rules['S'] = ['SOS', '(S)', 'D', 'DN']
rules['O'] = ['+', '-', '*', '/']
rules['D'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
rules['N'] = ['NN', '', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def apply_rules(sentence):
    if sentence == axiom:
        return 'SOS'

    s_or_n = True
    while True:

        if ('S' in sentence or 'O' in sentence):
            i = randint(0, len(sentence)-1)

            if sentence[i] == 'S':
                rl = choice(rules['S'])
                sentence = sentence[:i] + rl + sentence[i + 1:]
                break
            elif sentence[i] == 'O':
                rl = choice(rules['O'])
                sentence = sentence[:i] + rl + sentence[i + 1:]
                break
        else:
            s_or_n = False
            break

    if s_or_n == False:
        return None

    while ('D' in sentence or 'N' in sentence):
        i = randint(0, len(sentence)-1)
        if sentence[i] == 'D':
            rl = choice(rules['D'])
            sentence = sentence[:i] + rl + sentence[i + 1:]
        if sentence[i] == 'N':
            rl = choice(rules['N'])
            sentence = sentence[:i] + rl + sentence[i + 1:]

    


    return sentence


print(axiom + ' -> ', end='')
sen = apply_rules(axiom)
print(sen + ' -> ', end='')
   

while True:
    sen = apply_rules(sen)
    if sen == None:
        print('END')
        break
    print(sen + ' -> ', end='')
    
     
