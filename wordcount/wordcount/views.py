from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    user_data=request.GET['data']
    print(user_data)
    word_list=user_data.split()
    word_dic={}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

            final_list=sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
            print (final_list)

    return render(request,'count.html',{'user_data':user_data,'count':len(word_list),'word_dic':final_list})
