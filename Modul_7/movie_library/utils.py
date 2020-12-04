import time
from random import randint
from movie import main_library

now = time.strftime("%d/%m/%Y")

top = []

def get_movies():
    for row in main_library:
        if isinstance(row, Movie):
            print(f"- {row.title}")

def get_series():
    for row in main_library:        
        if isinstance(row, TvSeries):            
            print(f"- {row.title}")   
def search():
    look_up = input("What you are looking for? ")
    for i,v in enumerate(main_library):
        if v.title == look_up:
            print(main_library[i].__repr__())

def top_titles():
    for i,v in enumerate(main_library):
        if v.watched > 0:
            top.append(v.watched)
    top.sort(reverse=True)
def top_3(top):
    for x,y in enumerate(main_library):
        if y.watched in top[:3]:
            print(f"{y} with {y.watched} views")

#generator
def generate_views(times = 10):
    for i in range(times):
        index = random_element()
        add_views(index)
        current_views = main_library[index].current_views
        title = main_library[index].title
        #print(f"View generated for {title} ({current_views})")

def random_element():
    elements =len(main_library) 
    return randint(0, elements-1)

def add_views(index):
    views = randint(1,100)
    return main_library[index].play(views)

#print library
def show_library():
    print("Main Library:")
    for i,v in enumerate(main_library):
        print(f"- {v}")
