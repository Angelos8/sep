import textract
from django.core.files.storage import default_storage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from pymongo import MongoClient

# create Mongo DB client for connecting to the database
client = MongoClient('db', 27017) 
# get attackflow database
db = client['attackflow']

# NOTE: Pages (GET requests). All pages end with _view
def home_view(request: HttpRequest):
    """
    Summary: Home page

    Request Methods: [GET]

    Args:
        request HttpRequest:

    Returns:
        HttpResponse: Settings page html
    """
    collections = db.list_collection_names()
    # Convert the list to a string
    collections_str = ', '.join(collections)
    
    # Create an HTML response with the collections
    response_html = f'<p>Collections: {collections_str}</p>'
    
    return HttpResponse(response_html)
    
def login_view(request: HttpRequest):
    """
    Summary: Login page

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: Login page html
    """
    return HttpResponse('<p>home page</p>')

def users_view(request: HttpRequest, user_id: int):
    """
    Summary: Users pages, requires user login

    Request Methods: [GET]

    Args:
        request HttpRequest
        user_id int

    Returns:
        HttpResponse: Users page html based on provided user id
    """

    return HttpResponse('<p>user page</p>')

def settings_view(request: HttpRequest):
    """
    Summary: Settings page

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: Settings page html
    """
    pass

def logout_view(request: HttpRequest):
    """
    Summary: Logout page

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: Logout page html
    """
    pass

# Handlers/methods (page request handlers)
def verify_login(request: HttpRequest):
    """
    Summary: Verify submitted user information

    Request Methods: [POST]

    Args:
        request HttpRequest

    Returns:
        HttpResponseRedirect: Redirect to correct user page
    """
    user_id = 1
    return redirect(f'/users/{user_id}')

def users_redirect(request: HttpRequest):
    """
    Summary: 
        Conditional redirect to login page or user page
        depending on whether user is logged in

    Request Methods: [GET]

    Args:
        request HttpRequest:
            .session: {
                'user_id'
            }

    Returns:
        HttpsResponseRedirect
    """
    if request.user:
        pass

def upload_report(request: HttpRequest) -> HttpResponse:
    """
    Summary: Upload and process an attackflow report and redirect to the annotation page

    Request Methods: [GET]

    Args:
        request HttpRequest:
            .FILES: {
                'report': FILE
            }

    Returns:
        HttpResponse: Redirect to annotation page with report text
    """
    if request.method =='POST':
        # file = request.FILES['file']
        # file_name = default_storage.save(file.name, file)
        # # text is extracted as a byte string and needs to be decoded
        # text = textract.process(file_name).decode()
        # # delete file after use
        # default_storage.delete(file_name)
        return HttpResponse('<p>uploaded report</p>')

def approve_pending_report(request: HttpRequest):
    """
    Summary: Approve pending report based on id

    Request Methods: [POST]

    Args:
        request HttpRequest:
            .POST: {
                'pending_report_id': int
            }
            
    Returns:
        HttpResponse: Status response
    """
    pass

def reject_pending_report(request: HttpRequest):
    """
    Summary: Reject pending report based on id

    Request Methods: [POST]

    Args:
        request HttpRequest:
            .POST: {
                'pending_report_id': id
            }
            
    Returns:
        HttpResponse: Status response
    """
    pass

def inspect_annotations_view(request: HttpRequest, report_id: int):
    """
    Summary: Retrieve report and return content

    Request Methods: [GET]

    Args:
        request HttpRequest
        report_id int

    Returns:
        HttpResponse: Report content
    """
    return HttpResponse('<p>annotate view page</p>')

def edit_annotations_view(request: HttpRequest, report_id: int):
    """
        Summary: Edit existing annotations

        Request Methods: [GET]

        Args:
            request HttpRequest

        Returns:
            HttpResponse: Edit annotations html
    """
    return HttpResponse('<p>annotate edit page</p>')

def annotation_redirect(request: HttpRequest, report_id: int):
    """
        Summary: Redirect to inspect report

        Request Methods: [GET]

        Args:
            request HttpRequest

        Returns:
            HttpResponse: inspect annotations html
    """
    return redirect(f'/annotate/{report_id}/view')

def annotate_new_report_view(request: HttpRequest):
        """
        Summary: Create new pending report

        Request Methods: [GET]

        Args:
            request HttpRequest

        Returns:
            HttpResponse: Annotation view
        """
        return HttpResponse(f'<p>{request["text"]}</p>')

def create_pending_report(request: HttpRequest):
        """
        Summary: Create new pending report

        Request Methods: [POST]

        Args:
            request HttpRequest:
                .POST: {
                    'plaintext': str,
                    'annotations': #! TO BE DECIDED / UNSURE
                }


        Returns:
            HttpResponse: Status response
        """
        return HttpResponse()

def create_user():
    """
    Summary: Create new user

    Request Methods: [POST]

    Args:
        request HttpRequest:
            .POST: {
                'username': str,
                'password': str
            }

    Returns:
        HttpResponseRedirect: Redirect to user page
    """
    return HttpResponse()

def update_user(request: HttpRequest):
    """
    Summary: Update user information

    Request Methods: [POST]

    Args:
        request HttpRequest:
            .POST: {
                'new_username': str,
                'new_password': str
            }

    Returns:
        HttpResponse:
            .status_code: 200
    """
    return HttpResponse(status_code=200)

def delete_user(request: HttpRequest):
    """
    Summary: Delete user (verify password before deleting)

    Request Methods: [POST]

    Args:
        request HttpRequest:
            .POST: {
                'user_id': int,
                'password': str
            }

    Returns:
        HttpResponse:
            .status_code: 200
    """
    return HttpResponse(status_code=200)