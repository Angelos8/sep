import textract
from django.core.files.storage import default_storage
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views import View
from pymongo import MongoClient

# create Mongo DB client for connecting to the database
client = MongoClient('db', 27017) 
# get attackflow database
db = client['attackflow']

# Pages
def login_page(request: HttpRequest):
    """

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: _description_
    """
    return HttpResponse('<p> home page </p>')

# process login request
def login(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse('successful login')
    else:
        return HttpResponse('get request')

# process signup request
def signup(request: HttpRequest):
    pass

# return user page
def user_page(request: HttpRequest, user_id: int):
    pass

# test for a class based view
# handler for extractind data from the uploaded report
def upload_report(request: HttpRequest):
    if request.method =='POST':
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        # text is extracted as a byte string and needs to be decoded
        text = textract.process(file_name).decode()
        # delete file after use
        default_storage.delete(file_name)
        return HttpResponse(text)

def annotation_view_page(request: HttpRequest, report_id):
    return HttpResponse('<p>annotate view page</p>')

def annotation_edit_page(request: HttpRequest, report_id):
    return HttpResponse('<p>annotate edit page</p>')

def annotate_redirect(request: HttpRequest, report_id):
    return redirect(f'/annotate/{report_id}/view')

def create_annotations(request: HttpRequest):
    pass

def home_page(request: HttpRequest):
    collections = db.list_collection_names()
    # Convert the list to a string
    collections_str = ', '.join(collections)
    
    # Create an HTML response with the collections
    response_html = f'<p>Collections: {collections_str}</p>'
    
    return HttpResponse(response_html)
    # return HttpResponse('<p>home page</p>')

def settings_page(request: HttpRequest):
    pass

def logout(request: HttpRequest):
    pass

def get_report(requst: HttpRequest):
    pass