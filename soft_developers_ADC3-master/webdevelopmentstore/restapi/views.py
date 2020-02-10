from django.shortcuts import render,redirect
from software.models import Software
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def api_data(request):
	software = Software.objects.all()
	if request.method == "GET":
		dict_type = {"software": list(software.values("title", "name"))}
	return JsonResponse(dict_type)


@csrf_exempt
def update_api_data(request, pk):
	software = Software.objects.get(pk=pk)
	if request.method == "GET":

		return JsonResponse({"name":software.name, "title":software.title})


	else:
		json_data = request.body.decode('utf-8')
		update_data = json.loads(json_data)
		software.title = update_data['title']
		software.save()
		return JsonResponse("Updated !", safe=False)


def api_software(request,PAGENO,SIZE):
	if request.method == "GET":
		skip = SIZE * (PAGENO -1)
		software = Software.objects.all() [skip:(PAGENO*SIZE)]
		dict_type = {"software": list(software.values("title", "name", "stw"))}
	return JsonResponse(dict_type)

@csrf_exempt
def delete_api_data(request,pk):
	software = Software.objects.get(pk=pk)
	if request.method == "GET":
		return JsonResponse({"name":software.name, "title":software.title})

	else:
		software.delete()
		return JsonResponse("Deleted !", safe=False)

@csrf_exempt
def post_api_data(request):
	if request.method == "POST":
		software = Software()
		json_body = request.body.decode('utf-8')
		json_data = json.loads(json_body)
		software.title = json_data['title']
		software.name = json_data['name']
		software.stw = json_data['stw']
		software.save()
		return JsonResponse("Uploded !", safe=False)

