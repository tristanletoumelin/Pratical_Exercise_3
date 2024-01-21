
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, JsonResponse, FileResponse 
from django.template import Template, Context
import os

# Create your views here.
def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None) 
        msg = request.POST.get("msg", None) 
        time = datetime.now()
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == 'GET':
        userC = request.GET.get("userC", None)
        if userC != None:

            with open("msgdata.txt", 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt+1
                        d = {"userA": linedata[1], 'msg':linedata[2], 'time':linedata[3]} 
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MsgSingleWeb.html", {"data": datalist})

def homeproc(request):
    response = HttpResponse()
    response.write("<h1>This is the home page, for specific functions, please visit<a href='./msggate'>here</a></h1>") 
    response.write("<h1>This is the second line</h1>")
    return response
#return HttpResponse("<h1>This is the home page, for specific functions, please visit<a href='./msggate'>here</a></h1>")

def homeproc1(request):
    response = JsonResponse({'key': 'value1'})
    return response


def homeproc2(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/file_example_MP4_480_1_5MG.mp4", "rb")) 
    response[ 'Content-Type'] = 'application/octet-stream'
    response[ 'Content-Disposition'] = 'attachment; filename="Sample-MP4-Video-File-Download.mp4"' 
    return response
   
def pgproc(request):
    template = Template("<h1>The name of this program is{{ name }}</h1>")
    context = Context({"name":"Experiment platform"})
    return HttpResponse(template.render(context))