import requests
import redirect
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index_html = open("content/index.html").read()
    context = {
        "content": index_html
    }
    return render(request, "base.html", context)

def my_projects(request):
    project_html = open("content/project.html").read()
    context = {
        "content": project_html
    }
    return render(request, "base.html", context)

def my_blog(request):
    blog_html = open("content/blog.html").read()
    context = {
        "content": blog_html
    }
    return render(request, "base.html", context)


def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    send_simple_message(name, email, message)
    
    # Do something with these three variables...
    return redirect("/send-email")
    # Return a redirect!

def send_simple_message(name, email, message):
    print("print start")
    requests.post(
        "https://api.mailgun.net/v3/sandbox5384f59555ca4eae8a3c0af12e96c56a.mailgun.org/messages",
        auth=("api", "1e92efcdeed183daba323fb246ecbd4c-acb0b40c-3dd21064"),
        data={"from": email,
              "to": "syedhussainqa@gmail.com",
              "subject": "Hello" + name,
              "text": message}
              )

# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://api.github.com/users/michaelpb/repos')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)

