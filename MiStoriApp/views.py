from django.shortcuts import render
import openai
openai.api_key = "use your api key"
# Create your views here.

def home(request):
    model_engine = "davinci"
    prompt = "Hello, OpenAI!"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return render(request, 'home.html', {'message': message})
#def home(request):
    #message = ""
    #return render(request, 'home.html', {'message': message})
