from django.shortcuts import HttpResponse, render_to_response, RequestContext


# Create your views here.
def index(request):
	
	view_content={"title":"title show","content":"this is page content"}
	return render_to_response("index.html",view_content)
