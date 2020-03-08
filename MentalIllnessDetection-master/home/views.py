from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aog import conv
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from home.funcs import get_all_responses
from .forms import MessageForm, cbtForm

def homepage(request):

    context = {
        "data" : "Template Django Project",
    }

    return render(request,'home/home.html',context)


#this view is for integrating the BOT with DialogFlow 
@csrf_exempt
def dialogflow(request):
	res = ""

	if request.method == 'POST':
		content = json.loads(request.body)
		
		if conv.isfrom(content, 'Results'):
			val = get_all_responses(content)
			
			print(val)
			
			res = conv.close("Thank You for taking this quiz ")

	return JsonResponse(res, safe=False)


def feedback(request):

	if request.method == 'POST':
		feedback = MessageForm(request.POST)
		feedback.save()
	
	else :
		feedback = MessageForm()

	return render(request, 'home/feedback.html',{"form" : feedback})