from random import sample
from django.http import HttpResponse # proof of concept
from django.shortcuts import render # getting html templates
from django.shortcuts import redirect

from PartTrackerApp import models # temporary database (sqlite)

status_enum = [ "stamp", "spray", "check", "oil", "bag", ]

# dummy database
sample_items = [
  {
    "filter_name": "3117",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": status_enum[0].capitalize(),
    "oil": True
  },
  {
    "filter_name": "310-17",
    "quantity":150,
    "date_modified": "5/20/22",
    "status": status_enum[0].capitalize(),
    "oil": False
  },
  {
    "filter_name": "3220",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": status_enum[0].capitalize(),
    "oil": True
  },
  {
    "filter_name": "320-20",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": status_enum[0].capitalize(),
    "oil": False
  },
  {
    "filter_name": "1110",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": status_enum[0].capitalize(),
    "oil": True
  },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": status_enum[0].capitalize(), "oil": True },
]

"""
PAGES
"""

# essentially the home page, this is what the admin will use to view all/add items
def filters(request):
  
  # Read all the items from the database
  tasks = models.Filter_Tasks.objects.all()
  # print(tasks)

  # clear all rows in Parts_List_Range
  for item in models.Parts_List_Range.objects.all():
    item.delete()

  # update Parts_List_Range based on request (if it was made) 
  # via show_new_parts_list_range view/redirect
  up  = request.GET.get("parts_list_range_lower")
  low = request.GET.get("parts_list_range_upper")
  if (up == None or low == None):
    models.Parts_List_Range(lower=0, upper=20).save()
  else:
    models.Parts_List_Range(lower=low, upper=up).save()
  
  # save current range to send to /Filters
  parts_list_range = list(range(
    models.Parts_List_Range.objects.first().lower,
    models.Parts_List_Range.objects.first().upper + 1
  ))
  print(parts_list_range)

  # generate range options to be displayed to user 
  # (dynamically based on number of existing entries)
  parts_list_ranges = [range(0, 20+1)]
  for i in range(int(len(sample_items)/20)):
    parts_list_ranges.append(range(21 + i * 20, 41 + i * 20))

  values = {
    "title": "Filters",
    "filters": sample_items,
    "empty_rows_count":range(20),
    "parts_list_ranges":parts_list_ranges,
    "parts_list_range":parts_list_range,
    "parts_list_range_start":parts_list_range[0],
    "parts_list_range_end":parts_list_range[-1],
  }
  return render(request, 'PartTrackerApp/filters.html', values)

# default page/misc items
def index(request):
  values = {"title": "Site Map/Style Guide"}
  return render(request, "PartTrackerApp/index.html", values)

# stations
def stations(request):
  values = {"title": "Stations"}
  return render(request, "PartTrackerApp/stations.html", values)

def stamp(request):
  values = {"title": "Stamp"}
  return render(request, "PartTrackerApp/stations/stamp.html", values)

def check(request):
  values = {"title": "Check"}
  return render(request, "PartTrackerApp/stations/check.html", values)

def spray(request):
  values = {"title": "Spray"}
  return render(request, "PartTrackerApp/stations/spray.html", values)

def oil(request):
  values = {"title": "Oil"}
  return render(request, "PartTrackerApp/stations/oil.html", values)

def bag(request):
  values = {"title": "Bag"}
  return render(request, "PartTrackerApp/stations/bag.html", values)



"""
ACTIONS
"""

# insert or update values in database
def add(request):
  """
  Process request to add new items to Filters task list.
  Redirect to self when you're done
  """
  # # Read values from GET request (TODO: Add error checking here)
  # try:

  #     # Save to the database
  #     item = Workspace(
  #       item_id=request.GET["item_id"],
  #       description=request.GET["description"], 
  #       value=float(request.GET["value"]), 
  #       hazardous=request.GET["hazardous"] == "Yes"
  #     )
  #     item.save()

  # except Exception as e:
  #     # TODO: Send an error message back to the main index page
  #     print("Unable to save to database: {}".format(e))

  # Return to main index page
  print(request)
  print(request.GET)
  print('''
    task_name
    #
    quantity_enabled
    quantity
    status
    date_assigned
    date_due
  ''')
  return redirect("PartTrackerApp/Filters")

# show row _ to row _ of total items in filter_tasks
def show_new_parts_list_range(request):
  print(
    request.GET.get("parts_list_range_lower"),
    request.GET.get("parts_list_range_upper"),
  )
  return redirect("PartTrackerApp/Filters") # refresh to show changes
