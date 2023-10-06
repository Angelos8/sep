import textract
from django.core.files.storage import default_storage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from pymongo import MongoClient
from django.urls import reverse
from django.contrib import messages
from .forms import *

# create Mongo DB client for connecting to the database
client = MongoClient('db', 27017) 
# get attackflow database
db = client['attackflow']

def delete_all_users(request: HttpRequest):
    """
     summary: This is built for testing purpose
     Request Methods: [GET]

    Args:
        request HttpRequest:

    Returns:
        HttpResponse: All users have been deleted.
    """
    # Delete all existing users and reset id counter
    collection = db['users']
    collection.delete_many({})
    counters_collection = db['counters']
    counters_collection.update_one(
        {"_id": "user_id"},
        {"$set": {"seq": 0}},
        upsert=True
    )
    return HttpResponse("All users have been deleted.")


def display_all_users(request:HttpRequest):
    """
     summary: This is built for testing purpose
     Request Methods: [GET]

    Args:
        request HttpRequest:

    Returns:
        HttpResponse: display_user page html.
    """
    collection = db['users']
    documents = collection.find()
    return render(request, 'display_user.html', context={'db':documents})

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
    return render(request, 'home.html')

def login(request: HttpRequest): 
    """
    Summary: log in, if the request is get, return a simple html file with
             empty logInForm, if the request is post, fill the form with the post
             info, check if the user has exist or not. Warning display if user not
             exist

    Request Methods: [GET]

    Args:
        request HttpRequest:

    Returns:
        HttpResponse: Settings page html
    """
    # if the user has logged in, redirect to home page
    if 'user_id' in request.session:
        return redirect(reverse('home_page'))
    
    if request.method == 'POST':
        # fill the form with info from post
        form = LoginForm(request.POST)
        # check if the submit form is valid
        if form.is_valid():
            form_data = form.cleaned_data
            # connect to the database and save user info
            collection = db['users']
            username = form_data['username']
            password = form_data['password']
            user_info = collection.find_one({"username": username, "password": password})
            # if the user info is found, save the user id into current session cookie
            # display notice and redirct to home page
            if user_info:
                # Storing user ID in session
                request.session['user_id'] = user_info['_id']
                messages.success(request, 'you are logged in!')
                return redirect(reverse('home_page'))
            else:
                # if the user info submitted does not exist
                # display error and re-render login page
                form.add_error(None, 'Invalid username or password')

    else:
        # get empty form when the request is not post
        form = LoginForm()
    return render(request, 'login_page.html', context={'form': form})

# process signup request
def signup(request: HttpRequest):
    """
    Summary: sign up, if the request is get, return a simple html file with
             empty signInForm, if the request is post, fill the form with the post
             info, check if the username has been taken or not. Warning display if the 
             username been taken and re-render the signup page

    Request Methods: [GET]

    Args:
        request HttpRequest:

    Returns:
        HttpResponse: Settings page html
    """
    # if the user has logged in, redirect to home page
    if 'user_id' in request.session:
        return redirect(reverse('home_page'))
    if request.method == 'POST':
        # fill the form with info from post
        form = SignupForm(request.POST)
        # check if the submit form is valid
        if form.is_valid():
            # connect to the database and save user info
            collection = db['users']
            username = form.cleaned_data['username']
            existing_user = collection.find_one({'username': username})
            # if the user info submitted has already existed
            # display error and re-render signup page
            if existing_user:
                form.add_error('username', 'Username already taken')
                return render(request, 'sign_up_page.html', {'form': form})

            # auto increment id
            counters_collection = db['counters']
            counter = counters_collection.find_one_and_update(
                {"_id": "user_id"},
                {"$inc": {"seq": 1}},
                upsert=True,
                return_document=True
            )

            # Prepare the data to save
            user_data = {
                "_id": counter["seq"],
                "username": username,
                "password": form.cleaned_data['password'],  
                "first_name": form.cleaned_data['first_name'],
                "last_name": form.cleaned_data['last_name'],
            }
            # Save the data to MongoDB
            collection.insert_one(user_data) 
            # display message to the user
            messages.success(request, 'Your account has been created successfully. You can now log in.') 
            # Redirect to the login page
            return redirect(reverse('login_page'))  
    else:
        # get empty form when the request is not post
        form = SignupForm()
    return render(request, 'sign_up_page.html', {'form': form})

def login_view(request: HttpRequest):
    """
    Summary: Login page

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: Login page html
    """
    pass

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

def logout(request: HttpRequest):
    """
    Summary: Logout

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: redirct to login page 
    """
    # delete user info in the cookie
    # redirct to login page
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect(reverse('login_page'))

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

    pass

def login_redirect(request: HttpRequest):
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
    if 'user_id' in request.session:
        return redirect(reverse('home_page'))
    
    else:
        return redirect(reverse('login_page'))

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
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        # text is extracted as a byte string and needs to be decoded
        text = textract.process(file_name).decode()
        # delete file after use
        default_storage.delete(file_name)
        return HttpResponse(f'<p>{text}</p>')

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
    if 'user_id' in request.session:
        
        if request.method == 'POST':
            pass
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

def signup_view(request: HttpRequest):
    """
    Summary: signup page

    Request Methods: [GET]

    Args:
        request HttpRequest

    Returns:
        HttpResponse: signup html
    """
    pass

def verify_signup(request):
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
        HttpResponseRedirect: Redirect to login page
    """
    pass

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