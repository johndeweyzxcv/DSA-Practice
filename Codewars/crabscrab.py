# https://www.codewars.com/kata/52b305bec65ea40fe90007a7

def crabscrab(word, possible_words):
    word_sort = sorted(list(word))
    a_list = []

    for i in possible_words:
        if word_sort == sorted(list(i)):
            a_list.append(i)
    
    return a_list
    