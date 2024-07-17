from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat 

from django.utils import timezone

from transformers import pipeline 




# openai_api_key = ''
# openai.api_key = openai_api_key

# Initialize the Hugging Face pipeline
model_path = 'EleutherAI/gpt-j-6B'
model_path2 = 'EleutherAI/gpt-neox-20b'
model_path3 = 'EleutherAI/gpt-neo-12b'
model_path4 = 'gpt2'
model_path5='MetaAI/llama-30b'
generator = pipeline('text-generation', model=model_path) 

# def ask_openai(message):
#     #here is the ai part
#     response = openai.ChatCompletion.create(
#         model = "text-davinci-003",
#         prompt = message,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7,
#         messages=[
#             {"role": "system", "content": "You are an helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )
    
#     answer = response.choices[0].message.content.strip()
#     return answer

# # Create your views here.
# def chatbot(request):
#     if request.user.is_authenticated:
#         chats = Chat.objects.filter(user=request.user)
#         if request.method == 'POST':
#             message = request.POST.get('message')
#             response = ask_openai(message)

#             chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
#             chat.save()
#             return JsonResponse({'message': message, 'response': response})
        
#     else:
#         return redirect('login') 
    

    
#     return render(request, 'chatbot.html', {'chats': chats})

def ask_huggingface(message):
    # Generate a response using Hugging Face's model
    # response = generator(message, max_length=10, do_sample=True, num_return_sequences=1, temperature=0.9)
    response = generator(message, max_length=10, do_sample=True,  temperature=0.9)
    # Extract the generated text
    answer = response[0]['generated_text']
    return answer

# Create your views here.
def chatbot(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(user=request.user)
        if request.method == 'POST':
            message = request.POST.get('message')
            response = ask_huggingface(message)

            chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
            chat.save()
            return JsonResponse({'message': message, 'response': response})
    else:
        return redirect('login')
    
    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
