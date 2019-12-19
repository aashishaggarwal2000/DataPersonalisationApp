import json
import requests

headers = {
    'API-KEY': "a1d4634b-6cd8-4485-a7cd-c9b91f38177f"
}


#print(result)
def get_all_categories():
    url_all_categories = "https://api.oddschecker.com/api/v2/categories"
    response_all_catagories = requests.request("GET", url_all_categories, headers=headers)
    print(response_all_catagories.text)
    result = json.loads(response_all_catagories.text)
    if 'categories' in result:
        catagories = result['categories']
        for catagory in catagories:
            print(catagory)
            # for key, value in result.items():
            #     #f value == 10:
            #     print(key)
            #print([k for k, v in result.items() k])

def get_subevents():
    url_categories = "https://api.oddschecker.com/api/v2/categories/1"
    response_catagories = requests.request("GET", url_categories, headers=headers)
    print(response_catagories.text)
    result = json.loads(response_catagories.text)
    if 'categories' in result:
        categories = result['categories']
        for category in categories:
            if 'events' in category:
                events = category['events']
                for event in events:
                    if 'eventId' in event:
                        event_id = event['eventId']
                        # print(event_id)
                        # eventIdList.append(event_id)
                        url_events = "https://api.oddschecker.com/api/v2/events/" + str(event_id)
                        response_events = requests.request("GET", url_events, headers=headers)
                        events = json.loads(response_events.text)
                        #print(events)
                        #print(url_events)

                        if 'events' in events:
                            event_list = events['events']
                            for event in event_list:
                                #print(event)
                                if 'subevents' in event:
                                    subevents = event['subevents']
                                    #print(subevents)
                                    # for idx, val in enumerate(subevents):
                                    #     print(idx, val)
                                    for subevent in subevents:
                                        if 'subeventId' in subevent:
                                             subeventId= subevent['subeventId']
                                             #print(subeventId)
                                             url_subevents = "https://api.oddschecker.com/api/v2/subevents/" + \
                                                             str(subeventId)
                                             response_subevents = requests.request("GET", url_subevents, headers=headers)
                                             subevents = json.loads(response_subevents.text)
                                             print(subevents)
                                        else:
                                            print("subeventId doesn't exist in subevent")
                                else:
                                    print("subevents doesn't exist for the this event: "+str(event.get('eventId')))
                        else:
                            print("event_list doesn't exist for the this event_id"+str(event_id))
            else:
                print("events doesn't exist for the this category")
    else:
        print("categories doesn't exist for the this URI")

get_all_categories()
#get_subevents()


# simple example to interact with big query using python
# https://blog.morizyun.com/python/library-bigquery-google-cloud.html

