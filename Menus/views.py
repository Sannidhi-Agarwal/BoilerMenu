from django.shortcuts import render, redirect
from .models import Menu, User
from .forms import UserRegistrationForm, UserLoginForm, UserPreferencesForm, ItemPreferencesForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import requests
import json

def scraper(request):
    cookies = {
    'api_gac': '390fa50b-675a-42c9-bbda-d5119e8fd886',
    'CookieControl': '{"necessaryCookies":[],"optionalCookies":{"analytics":"accepted"},"statement":{},"consentDate":1725030992628,"consentExpiry":90,"interactedWith":true,"user":"60046416-305B-40C2-BA3D-B6AD57F74F6B"}',
    'BIGipServer~WEB~pool_wpvwebasp03-01-19_api.hfs.purdue.edu_web': '!7OuXuqSMw8Tv/fHstmuMAE7ECixZ9HfMk91sg/bQZkapMwAzIjG6aEpEVcEh3W6C6aFUPkyRRA==',
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'api_gac=390fa50b-675a-42c9-bbda-d5119e8fd886; CookieControl={"necessaryCookies":[],"optionalCookies":{"analytics":"accepted"},"statement":{},"consentDate":1725030992628,"consentExpiry":90,"interactedWith":true,"user":"60046416-305B-40C2-BA3D-B6AD57F74F6B"}; BIGipServer~WEB~pool_wpvwebasp03-01-19_api.hfs.purdue.edu_web=!7OuXuqSMw8Tv/fHstmuMAE7ECixZ9HfMk91sg/bQZkapMwAzIjG6aEpEVcEh3W6C6aFUPkyRRA==',
        'DNT': '1',
        'Origin': 'https://dining.purdue.edu',
        'Referer': 'https://dining.purdue.edu/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
        'accept': '/',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-gpc': '1',
    }

    json_data = {
        'operationName': 'getLocationMenu',
        'variables': {
            'name': 'Hillenbrand',
            'date': '2024-10-28',
        },
        'query': 'query getLocationMenu($name: String!, $date: Date!) {\n  diningCourtByName(name: $name) {\n    address {\n      city\n      state\n      street\n      zip\n      __typename\n    }\n    formalName\n    id\n    bannerUrl\n    logoUrl\n    name\n    latitude\n    longitude\n    googlePlaceId\n    normalHours {\n      id\n      name\n      effectiveDate\n      days {\n        dayOfWeek\n        meals {\n          endTime\n          name\n          startTime\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    dailyMenu(date: $date) {\n      notes\n      meals {\n        endTime\n        startTime\n        notes\n        name\n        status\n        stations {\n          iconUrl\n          id\n          name\n          notes\n          items {\n            specialName\n            item {\n              isFlaggedForCurrentUser\n              isHiddenForCurrentUser\n              isNutritionReady\n              itemId\n              name\n              traits {\n                name\n                svgIcon\n                svgIconWithoutBackground\n                __typename\n              }\n              components {\n                name\n                isFlaggedForCurrentUser\n                isHiddenForCurrentUser\n                isNutritionReady\n                itemId\n                traits {\n                  name\n                  svgIcon\n                  svgIconWithoutBackground\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.hfs.purdue.edu/menus/v3/GraphQL', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"operationName":"getLocationMenu","variables":{"name":"Earhart","date":"2024-10-26"},"query":"query getLocationMenu($name: String!, $date: Date!) {\\n  diningCourtByName(name: $name) {\\n    address {\\n      city\\n      state\\n      street\\n      zip\\n      __typename\\n    }\\n    formalName\\n    id\\n    bannerUrl\\n    logoUrl\\n    name\\n    latitude\\n    longitude\\n    googlePlaceId\\n    normalHours {\\n      id\\n      name\\n      effectiveDate\\n      days {\\n        dayOfWeek\\n        meals {\\n          endTime\\n          name\\n          startTime\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    dailyMenu(date: $date) {\\n      notes\\n      meals {\\n        endTime\\n        startTime\\n        notes\\n        name\\n        status\\n        stations {\\n          iconUrl\\n          id\\n          name\\n          notes\\n          items {\\n            specialName\\n            item {\\n              isFlaggedForCurrentUser\\n              isHiddenForCurrentUser\\n              isNutritionReady\\n              itemId\\n              name\\n              traits {\\n                name\\n                svgIcon\\n                svgIconWithoutBackground\\n                __typename\\n              }\\n              components {\\n                name\\n                isFlaggedForCurrentUser\\n                isHiddenForCurrentUser\\n                isNutritionReady\\n                itemId\\n                traits {\\n                  name\\n                  svgIcon\\n                  svgIconWithoutBackground\\n                  __typename\\n                }\\n                __typename\\n              }\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}"}'
    #response = requests.post('https://api.hfs.purdue.edu/menus/v3/GraphQL', cookies=cookies, headers=headers, data=data)


    data=json.loads(response.text)
    # Safely access the nested data in the JSON
    dining_court = data.get('data', {}).get('diningCourtByName', {})
    daily_menu = dining_court.get('dailyMenu', {})

    # Initialize a list to store food items and their traits
    food_items = []

    # Ensure 'meals' is a list and iterate through it
    meals = daily_menu.get('meals', [])
    if isinstance(meals, list):
        for meal in meals:
            stations = meal.get('stations', [])
            
            # Ensure 'stations' is a list and iterate through it
            if isinstance(stations, list):
                for station in stations:
                    items = station.get('items', [])
                    
                    # Ensure 'items' is a list and iterate through it
                    if isinstance(items, list):
                        for item_appearance in items:
                            item = item_appearance.get('item', {})
                            
                            # Ensure 'item' is a dictionary
                            if isinstance(item, dict):
                                item_name = item.get('name', 'Unknown Item')
                                traits = item.get('traits', [])
                                
                                # Ensure 'traits' is a list and iterate through it
                                if isinstance(traits, list):
                                    trait_names = [trait.get('name', 'Unknown Trait') for trait in traits]
                                    
                                    # Store the item and traits in a dictionary
                                    food_items.append({
                                        'name': item_name,
                                        'traits': trait_names
                                    }
                                    )
    
    for food_item in food_items:
        name = food_item['name']
        vegetarian = False
        vegan = False
        glutenFree = False
        peanuts = False
        dairy = False
        soybean = False
        wheat = False
        eggs = False
        coconut = False
        fish = False
        shellfish = False
        sesame = False
        for trait in food_item['traits']:
            if trait == "Vegetarian":
                vegetarian = True
    
            elif trait == "Vegan":
                vegan = True
            
            elif trait == "Gluten":
                glutenFree = True
        
            elif trait == "Peanuts":
                peanuts = True
            
            elif trait == "Milk":
                dairy = True
        
            elif trait == "Soy":
                soybean = True
        
            elif trait == "Wheat":
                wheat = True
        
            elif trait == "Eggs":
                eggs = True
        
            elif trait == "Coconut":
                coconut = True
        
            elif trait == "Fish":
                fish = True
        
            elif trait == "Shellfish":
                shellfish = True
        
            elif trait == "Sesame":
                sesame = True
    
        item = Menu(name=name, vegetarian=vegetarian, vegan=vegan, glutenFree=glutenFree, peanuts=peanuts, dairy=dairy, soybean=soybean, wheat=wheat, eggs=eggs, coconut=coconut, fish=fish, shellfish=shellfish, sesame=sesame)
        item.save()

    return redirect('Menus:display_menu')



def home(request):
    return render(request, 'Menus/home.html')

def register(request):
    context={}
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            return redirect('Menus:dashboard')
        context['register_form']=form
    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, 'Menus/register.html', context)

def login(request):
    context={}
    if request.method == 'POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('Menus:dashboard')
        else:
            context['login_form']=form
    else:
        form=UserLoginForm()
        context['login_form']=form
    return render(request, 'Menus/login.html', context)

def logout(request):
    if not request.user.is_authenticated:
        return redirect('Menus:home')
    auth_logout(request)
    return redirect('Menus:home')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('Menus:login')
    user = request.user
    return render(request, 'Menus/dashboard.html', {'user' : user})

def display_menu(request):
    if not request.user.is_authenticated:
        return redirect('Menus:login')
    items = Menu.objects.all()
    user = request.user
    if user.vegetarian:
        items = items.filter(vegetarian=True)
    if user.vegan:   
        items = items.filter(vegan=True)
    if user.glutenFree:
        items = items.filter(glutenFree=True)
    if user.dairy:
        items = items.filter(dairy=False)
    if user.peanuts:
        items = items.filter(peanuts=False)
    if user.soybean:
        items = items.filter(soybean=False)
    if user.wheat:
        items = items.filter(wheat=False)
    if user.eggs:
        items = items.filter(eggs=False)
    if user.coconut:
        items = items.filter(coconut=False)
    if user.fish:
        items = items.filter(fish=False)
    if user.shellfish:
        items = items.filter(shellfish=False)
    if user.sesame:
        items = items.filter(sesame=False)
    return render(request, 'Menus/display_menu.html', {'items' : items})

# def item_details(request, item_id):
#    item = Menu.objects.get(pk=item_id)
#    return render(request, 'Menus/menu_item_details.html', {'item': item})

def user_set_preferences(request):
    if not request.user.is_authenticated:
        return redirect('Menus:login')
    context={}
    if request.method == 'POST':
        form=UserPreferencesForm(request.POST)
        user = request.user
        user = User.objects.get(pk=user.id)
        if form.is_valid():
            if 'vegetarian' in request.POST:
                user.vegetarian = True
            else:
                user.vegetarian = False
            if 'vegan' in request.POST:
                user.vegan = True
            else:
                user.vegan = False
            if 'glutenFree' in request.POST:
                user.glutenFree = True
            else:
                user.glutenFree = False
            if 'dairy' in request.POST:
                user.dairy= True
            else:
                user.dairy = False
            if 'peanuts' in request.POST:
                user.peanuts = True
            else:
                user.peanuts = False
            if 'soybean' in request.POST:
                user.soybean = True
            else:
                user.soybean = False
            if 'wheat' in request.POST:
                user.wheat = True
            else:
                user.wheat = False
            if 'eggs' in request.POST:
                user.eggs = True
            else:
                user.eggs = False
            if 'coconut' in request.POST:
                user.coconut = True
            else:
                user.coconut = False
            if 'fish' in request.POST:
                user.fish = True
            else:
                user.fish = False
            if 'shellfish' in request.POST:
                user.shellfish = True
            else:
                user.shellfish = False
            if 'sesame' in request.POST:
                user.sesame = True
            else:
                user.sesame = False
            user.save()
            return redirect('Menus:dashboard')
        context['preferences_form']=form
    else:
        form=UserPreferencesForm()
        context['preferences_form']=form
    return render(request, 'Menus/user_set_preferences.html', context)

def item_set_preferences(request):
    if not request.user.is_authenticated:
        return redirect('Menus:login')
    context={}
    if request.method == 'POST':
        form=ItemPreferencesForm(request.POST)
        if form.is_valid():
            try:
                items = Menu.objects.all()
                if 'vegetarian' in request.POST:
                    items = items.filter(vegetarian=True)
                if 'vegan' in request.POST:   
                    items = items.filter(vegan=True)
                if 'glutenFree' in request.POST:
                    items = items.filter(glutenFree=True)
                if 'dairy' in request.POST:
                    items = items.filter(dairy=False)
                if 'peanuts' in request.POST:
                    items = items.filter(peanuts=False)
                if 'soybean' in request.POST:
                    items = items.filter(soybean=False)
                if 'wheat' in request.POST:
                    items = items.filyer(wheat=False)
                if 'eggs' in request.POST:
                    items = items.filter(eggs=False)
                if 'coconut' in request.POST:
                    items = items.filter(coconut=False)
                if 'fish' in request.POST:
                    items = items.filter(fish=False)
                if 'shellfish' in request.POST:
                    items = items.filter(shellfish=False)
                if 'sesame' in request.POST:
                    items = items.filter(sesame=False)
            except Menu.DoesNotExist:
                items = None
                return render(request, 'Menus/display_menu.html', {'items' : items})
            return render(request, 'Menus/display_menu.html', {'items' : items})
        context['preferences_form']=form
    else:
        form=ItemPreferencesForm()
        context['preferences_form']=form
    return render(request, 'Menus/item_set_preferences.html', context)
