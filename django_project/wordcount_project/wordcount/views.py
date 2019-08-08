from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    name = 'jone'
    age = 29
    return render(request, 'about.html', {'name': name, 'age': age})

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            # Increase
            word_dict[word] += 1
        else:
            # add to the dictionary
            word_dict[word] = 1
    
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    return render(request, 'count.html', 
            {'fulltext': fulltext, 'count': len(wordlist), 'sorted_words': sorted_words})
