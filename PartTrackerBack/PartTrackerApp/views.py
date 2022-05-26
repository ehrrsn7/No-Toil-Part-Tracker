
from django.http import HttpResponse # proof of concept
from django.shortcuts import render, redirect # getting html templates

import re # regular expression, to parse url

from PartTrackerApp import models # temporary database (sqlite)

# dummy database
sample_items = [
  {
    "filter_name": "3117 (first)",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": 0,
    "oil": True
  },
  {
    "filter_name": "310-17",
    "quantity":150,
    "date_modified": "5/20/22",
    "status": 0,
    "oil": False
  },
  {
    "filter_name": "3220",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": 0,
    "oil": True
  },
  {
    "filter_name": "320-20",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": 0,
    "oil": False
  },
  {
    "filter_name": "1110",
    "quantity":50,
    "date_modified": "5/20/22",
    "status": 0,
    "oil": True
  },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110 (10)", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110 (11)", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110 (20)", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110 (21)", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 3, "oil": True },
  { "filter_name": "1110 (23)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (30)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (31)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "urmom", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (40)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (41)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (50)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110 (51)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  # { "filter_name": "1110", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
  # { "filter_name": "1110 (last)", "quantity":50, "date_modified": "5/20/22", "status": 0, "oil": True },
]

"""
HELPER FUNCTIONS
"""
def get_parts_list_ranges(request, tasks):

  # default range
  lower, upper = (0, 20) 

  redirect_if_invalid_index = False
  
  # get parts list display range via url and create sliced list based on it
  result = re.search("\?\d{1,5}-\d{1,5}", request.get_full_path())
  if bool(result):
    print("query request found in url")
    result = result.group()
    indices = [int(i) for i in result[result.index('?') + 1:].split('-')]
    print("indices:", indices)
    if len(indices) == 2:
      print("successfully set range based on url query")
      lower, upper = indices
      if lower > len(tasks): # if we refresh the page and for some reason there are less filters
        print("invalid url index query..")
        redirect_if_invalid_index = True
  else:
    print("no query request found in url")

  # generate range options to be displayed to user 
  # (dynamically based on number of existing entries)
  parts_list_ranges = []
  cap = len(tasks)
  offset = 0
  while cap >= 20:
    parts_list_ranges.append(list(range(1 + 20*offset, 21 + 20*offset)))
    cap -= 20
    offset += 1
  parts_list_ranges.append(list(range(1 + 20*offset, len(tasks) + 1)))

  # there are no ranges if the filters task list is empty
  if len(tasks) <= 0:
    lower, upper = (1, 1)
    current_parts_list_range_index = 0

  # send current range to filters.html so that it highlights/disables that button
  else: 
    current_parts_list_range_index = int((lower) / 20)
  current_parts_list_range = []
  if len(parts_list_ranges) > 0:
    try:
      current_parts_list_range = parts_list_ranges[current_parts_list_range_index]
    except IndexError as e:
      print(e)
      current_parts_list_range = range(1, len(tasks))

  return (lower, upper, parts_list_ranges, current_parts_list_range, 
    current_parts_list_range_index, redirect_if_invalid_index)

"""
VIEWS
"""
# essentially the home page, this is what the admin will use to view all/add items
def filters(request):
  
  # Read all the items from the database
  tasks = models.Filter_Tasks.objects.all()
  tasks = sample_items # dummy database redirect
  tasks_length = len(tasks)

  lower, upper, parts_list_ranges, current_parts_list_range, \
    current_parts_list_range_index, redirect_if_invalid_index \
      = get_parts_list_ranges(request, tasks)

  print(lower, upper, parts_list_ranges, current_parts_list_range,
    current_parts_list_range_index, redirect_if_invalid_index, sep="\n")

  try:
    if lower > 0: lower -= 1
    tasks = tasks[lower : upper]
  except IndexError as e:
    print(e)

  print('\n', tasks)
  for t in tasks: print(t)

  print("\n\nredirect?", redirect_if_invalid_index)
  if redirect_if_invalid_index: 
    print("redirecting...")
    return redirect(f"Filters")

  return render(request, 'PartTrackerApp/filters.html', {
    "title": "Filters",
    "filters": tasks,
    "tasks_length": tasks_length,
    "empty_rows_count":range(20),
    "parts_list_ranges":parts_list_ranges,
    "current_parts_list_range":current_parts_list_range,
    "current_parts_list_range_index":current_parts_list_range_index,
  })

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
  # update Parts_List_Range based on request (if it was made) 
  # via show_new_parts_list_range view/redirect
  low = request.GET.get("parts_list_range_lower") or 0
  up  = request.GET.get("parts_list_range_upper") or 20
  return redirect(f"PartTrackerApp/Filters?{low}-{up}") # refresh to show changes
