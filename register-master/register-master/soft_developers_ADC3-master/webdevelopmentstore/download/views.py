from django.shortcuts import render
from .forms import OForm
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from software.models import Software
# Create your views here.

def download(request):
	return render(request=request, template_name="download/download.html", context={"download": software.objects.all()})

def upload_stw(request):
	form = OForm()
	if request.method == "POST":
		myfile = request.FILES['stw']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = filename
		softwares = Software(title=request.POST.get('title'),name=request.POST.get('name'),stw=uploaded_file_url)
		softwares.save()
		return HttpResponseRedirect('/download/soft_list')
	return render(request, "download/upload.html", {"form": form})

def soft_list(request):
	softwares = Software.objects.all()
	if request.GET:
	 	query = request.GET['q']
	 	softwares = get_data_queryset(str(query))
	 	#print()
	return render(request, "download/soft_list.html", {"software": softwares})


def delete_stw(request, pk):
	softwares = Software.objects.get(pk=pk)
	softwares.delete()
	return HttpResponseRedirect("/download/soft_list")


def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		softwares = Software.objects.filter(
				Q(name__icontains=q) |
				Q(title__icontains=q)
			)

		for software1 in softwares:
			queryset.append(software1)

	return list(set(queryset))



# def api_data(request):
# 	software = software.objects.all()
# 	if request.method == "GET":
# 		dict_type = {"software": list(software.values("title", "name"))}

# 		return JsonResponse(dict_type)


# @csrf_exempt
# def update_api_data(request, pk):
# 	software = software.objects.get(pk=pk)
# 	if request.method == "GET":
# 		return JsonResponse({"name": software.name, "title": software.title})


# 	else:
# 		json_data = request.body.decode('utf-8')
# 		update_data = json.loads(json_data)
# 		software.title = update_data['title']


# 		return JsonResponse({"message": "Sucessfully completed!!"})