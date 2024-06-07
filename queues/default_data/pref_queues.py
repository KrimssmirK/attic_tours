# services id
JAPAN_VISA_ID = 19
KOREA_VISA_ID = 20
TICKETING_ID = 25
JAPAN_KOREA_ID = 29 # SM NORTH EDSA IDEA
TICKETING_SALES_ID = 30 # SM NORTH EDSA IDEA

# branches id
MAIN_OFFICE_ID = 1
MEGAMALL_ID = 2
MOA_ID = 3
FAIRVIEW_ID = 4
NORTH_EDSA_ID = 5
CLARK_ID = 6
SOUTHMALL_ID = 7
DAVAO_ID = 8
CEBU_ID = 9

pref_queues = [
    {"service": JAPAN_VISA_ID, "branch": MAIN_OFFICE_ID},
    {"service": KOREA_VISA_ID, "branch": MAIN_OFFICE_ID},
    {"service": JAPAN_VISA_ID, "branch": MEGAMALL_ID},
    {"service": KOREA_VISA_ID, "branch": MEGAMALL_ID},
    {"service": TICKETING_ID, "branch": MEGAMALL_ID},
    {"service": JAPAN_VISA_ID, "branch": MOA_ID},
    {"service": KOREA_VISA_ID, "branch": MOA_ID},
    {"service": TICKETING_ID, "branch": MOA_ID},
    {"service": JAPAN_VISA_ID, "branch": FAIRVIEW_ID},
    {"service": KOREA_VISA_ID, "branch": FAIRVIEW_ID},
    {"service": TICKETING_ID, "branch": FAIRVIEW_ID},
    {"service": JAPAN_KOREA_ID, "branch": NORTH_EDSA_ID},
    {"service": TICKETING_SALES_ID, "branch": NORTH_EDSA_ID},
    {"service": JAPAN_VISA_ID, "branch": CLARK_ID},
    {"service": KOREA_VISA_ID, "branch": CLARK_ID},
    {"service": TICKETING_ID, "branch": CLARK_ID},
    {"service": JAPAN_VISA_ID, "branch": SOUTHMALL_ID},
    {"service": KOREA_VISA_ID, "branch": SOUTHMALL_ID},
    {"service": TICKETING_ID, "branch": SOUTHMALL_ID},
    {"service": JAPAN_VISA_ID, "branch": DAVAO_ID},
    {"service": KOREA_VISA_ID, "branch": DAVAO_ID},
    {"service": TICKETING_ID, "branch": DAVAO_ID},
    {"service": JAPAN_VISA_ID, "branch": CEBU_ID},
    {"service": KOREA_VISA_ID, "branch": CEBU_ID},
    {"service": TICKETING_ID, "branch": CEBU_ID},
]