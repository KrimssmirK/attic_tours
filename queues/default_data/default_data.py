services = [
    {"name": "TOURISM", "price": 1680},
    {"name": "BUSINESS, CONFERENCE or CULTURAL EXCHANGE, etc.", "price": 1680},
    {"name": "VISITING RELATIVES", "price": 1680},
    {"name": "VISITING FRIENDS OR DISTANT RELATIVES", "price": 1680},
    {"name": "VISITING US MILITARY PERSONNEL", "price": 1680},
    {
        "name": "SPOUSE OR CHILD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES",
        "price": 1680,
    },
    {"name": "TRANSIT", "price": 1680},
    {"name": "COE", "price": 3030},
    {"name": "NIKKEI-JIN", "price": None},
    {"name": "(PTAA) TOURISM", "price": None},
    {"name": "(PTAA) BUSINESS, CONFERENCE or CULTURAL EXCHANGE, etc.", "price": None},
    {"name": "(PTAA) VISITING RELATIVES", "price": None},
    {"name": "(PTAA) VISITING FRIENDS OR DISTANT RELATIVES", "price": None},
    {"name": "(PTAA) VISITING US MILITARY PERSONNEL", "price": None},
    {
        "name": "(PTAA) SPOUSE OR CHILD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES",
        "price": None,
    },
    {"name": "(PTAA) TRANSIT", "price": None},
    {"name": "(PTAA) COE", "price": None},
    {"name": "(PTAA) NIKKEI-JIN", "price": None},
    {"name": "JAPAN VISA", "price": 1680},
    {"name": "KOREA VISA", "price": 1880},
    {"name": "TOUR PACKAGE", "price": None},
    {"name": "TICKET", "price": None},
    {"name": "TICKET (INTERNATIONAL)", "price": None},
    {"name": "TICKET (DOMESTIC)", "price": None},
    {"name": "TICKETING", "price": None},
    {"name": "WIFI", "price": None},
    {"name": "TRAVEL INSURANCE", "price": None},
    {"name": "VISA", "price": None}, # SM NORTH EDSA IDEA
    {"name": "JAPAN/KOREA", "price": None}, # SM NORTH EDSA IDEA
    {"name": "TICKETING/SALES", "price": None}, # SM NORTH EDSA IDEA
    
    
]


branches = [
    {
        "name": "MAIN OFFICE",
        "mobile_no": "N/A",
        "landline_no": "(02)8556-6301",
        "password": "0000",
    },
    {
        "name": "SM MEGAMALL",
        "mobile_no": "0906-516-3246",
        "landline_no": "(02)8706-6030",
        "password": "1111",
    },
    {
        "name": "SM MALL OF ASIA",
        "mobile_no": "0917-631-0848",
        "landline_no": "(02)8252-0868",
        "password": "2222",
    },
    {
        "name": "SM FAIRVIEW",
        "mobile_no": "0916-618-6165",
        "landline_no": "(02)8829-0761",
        "password": "3333",
    },
    {
        "name": "SM NORTH EDSA",
        "mobile_no": "0917-898-0905",
        "landline_no": "(02)8372-3254",
        "password": "4444",
    },
    {
        "name": "SM CLARK",
        "mobile_no": "0917-305-4292",
        "landline_no": "(04)5499-7546",
        "password": "5555",
    },
    {
        "name": "SM SOUTHMALL",
        "mobile_no": "0917-186-6853",
        "landline_no": "(02)8281-8506",
        "password": "6666",
    },
    {
        "name": "SM DAVAO",
        "mobile_no": "0917-321-1328",
        "landline_no": "(08)2225-8920",
        "password": "7777",
    },
    {
        "name": "SM CEBU",
        "mobile_no": "0956-551-9834",
        "landline_no": "(03)2239-8435",
        "password": "8888",
    },
]


windows = [
    {"name": "ANY WINDOW"},
    {"name": "WINDOW 1"},
    {"name": "WINDOW 2"},
    {"name": "WINDOW 3"},
    {"name": "WINDOW 4"},
    {"name": "WINDOW 5"},
    {"name": "WINDOW 6"},
    {"name": "WINDOW 7"},
    {"name": "WINDOW VISA"},
    {"name": "WINDOW JAPAN VISA"},
    {"name": "WINDOW KOREA VISA"},
    {"name": "WINDOW TICKETING"},
    {"name": "WINDOW TOUR PACKAGE"},
    {"name": "WINDOW WIFI"},
]

# services constant
JAPAN_VISA = 19
KOREA_VISA = 20
TICKETING = 25
JAPAN_KOREA = 29 # SM NORTH EDSA IDEA
TICKETING_SALES = 30 # SM NORTH EDSA IDEA

# branches constant
MAIN_OFFICE = 1
MEGAMALL = 2
MOA = 3
FAIRVIEW = 4
NORTH_EDSA = 5
CLARK = 6
SOUTHMALL = 7
DAVAO = 8
CEBU = 9
pref_queues = [
    {"service": JAPAN_VISA, "branch": MAIN_OFFICE},
    {"service": KOREA_VISA, "branch": MAIN_OFFICE},
    {"service": JAPAN_VISA, "branch": MEGAMALL},
    {"service": KOREA_VISA, "branch": MEGAMALL},
    {"service": TICKETING, "branch": MEGAMALL},
    {"service": JAPAN_VISA, "branch": MOA},
    {"service": KOREA_VISA, "branch": MOA},
    {"service": TICKETING, "branch": MOA},
    {"service": JAPAN_VISA, "branch": FAIRVIEW},
    {"service": KOREA_VISA, "branch": FAIRVIEW},
    {"service": TICKETING, "branch": FAIRVIEW},
    {"service": JAPAN_KOREA, "branch": NORTH_EDSA},
    {"service": TICKETING_SALES, "branch": NORTH_EDSA},
    {"service": JAPAN_VISA, "branch": CLARK},
    {"service": KOREA_VISA, "branch": CLARK},
    {"service": TICKETING, "branch": CLARK},
    {"service": JAPAN_VISA, "branch": SOUTHMALL},
    {"service": KOREA_VISA, "branch": SOUTHMALL},
    {"service": TICKETING, "branch": SOUTHMALL},
    {"service": JAPAN_VISA, "branch": DAVAO},
    {"service": KOREA_VISA, "branch": DAVAO},
    {"service": TICKETING, "branch": DAVAO},
    {"service": JAPAN_VISA, "branch": CEBU},
    {"service": KOREA_VISA, "branch": CEBU},
    {"service": TICKETING, "branch": CEBU},
]

newsfeeds = [
    {"text": "WELCOME TO ATTIC TOURS!", "branch": MAIN_OFFICE},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": MAIN_OFFICE},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": MAIN_OFFICE},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": MAIN_OFFICE},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": MEGAMALL},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": MEGAMALL},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": MEGAMALL},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": MEGAMALL},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": MOA},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": MOA},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": MOA},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": MOA},
    {"text": "KONNICHIWA WELCOME TO ATTIC TOURS SM FAIRVIEW BRANCH!", "branch": FAIRVIEW},
    {"text": "JAPAN VISA CUT-OFF TIME 1PM & 8PM", "branch": FAIRVIEW},
    {"text": "JAPAN VISA  1,680.00", "branch": FAIRVIEW},
    {"text": "KOREA VISA FEE 1,888.00", "branch": FAIRVIEW},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": FAIRVIEW},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": NORTH_EDSA},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": NORTH_EDSA},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": NORTH_EDSA},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": NORTH_EDSA},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": CLARK},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": CLARK},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": CLARK},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": CLARK},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": SOUTHMALL},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": SOUTHMALL},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": SOUTHMALL},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": SOUTHMALL},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": DAVAO},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": DAVAO},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": DAVAO},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": DAVAO},
    {"text": "WELCOME TO ATTIC TOURS!", "branch": CEBU},
    {"text": "PLEASE TAKE A NUMBER AND WAIT FOR YOUR NUMBER TO BE CALLED", "branch": CEBU},
    {"text": "FOR PASSPORT CLAIMS, PLEASE PROCEED TO ANY WINDOW", "branch": CEBU},
    {"text": "FOR INQURY PLEASE PROCEED TO ANY WINDOW", "branch": CEBU},
]


def add_initial_service_data(apps, schema_editor):
    Service = apps.get_model("queues", "Service")
    for service in services:
        if service["price"] is None:
            Service.objects.create(name=service["name"])
        else:
            Service.objects.create(name=service["name"], price=service["price"])


def add_initial_branch_data(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            mobile_no=branch["mobile_no"],
            landline_no=branch["landline_no"],
            password=branch["password"],
        )


def add_initial_window_data(apps, schema_editor):
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(name=window["name"])


def add_initial_pref_queue_data(apps, schema_editor):
    PrefQueue = apps.get_model("queues", "PrefQueue")
    for pref_queue in pref_queues:
        PrefQueue.objects.create(
            service_id=pref_queue["service"],
            branch_id=pref_queue["branch"]
        )


def add_initial_newsfeed_data(apps, schema_editor):
    Newsfeed = apps.get_model("queues", "Newsfeed")
    for newsfeed in newsfeeds:
        Newsfeed.objects.create(
            text=newsfeed["text"],
            branch_id=newsfeed["branch"]
        )
