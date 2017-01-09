# Program to convert 'files path' to static files path,
# that will be compatible with DJANGO STATIC FILES

# For Example:
# In actual HTML file:
# <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
# <a href="#"><img src="images/logo.png" alt="HATA">HATA</a>
# <script src="js/jquery-1.11.3.min.js"></script>

# will be converted to DJANGO STATIC FILE format such as

# <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" type="text/css">
# <a href="#"><img src="{% static 'images/logo.png' %}" alt="HATA">HATA</a>
# <script src="{% static 'js/jquery-1.11.3.min.js' %}"></script>

# Author: Jeril Kuriakose
# Project: https://github.com/jerilkuriakose/

# TO RUN THIS FILE:
# open this file using command prompt,
# pass the directory path as the command line argument

# For Example:
# D:\>python replace_path.py <directory_path>
# like
# D:\>python replace_path.py "C:\Users\username\Desktop\hata-html"

import os
import re
import sys

# regex pattern to get the path from 'src' and 'href'
regex = ur'(src|href)="(.+?)"'

# get the base directory from command line arguements
base_dir = sys.argv[1]

# to check whether it is a directory or not
if os.path.splitext(base_dir)[1]:
    raise ValueError("could not recognise it as a directory '{}'".format(base_dir))

# to check whether the directory is present
if not os.path.exists(base_dir):
    raise ValueError("could not find the directory '{}'".format(base_dir))

## To get all the HTML files that are inside base_dir

# creating a empty list to store the html files
html_files = []

# walk throught the base_dir to get the HTML files
for root, _, files in os.walk(os.path.normpath(base_dir)):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

## iterating thought the HTML files to make changes
for html_file in html_files:
    
    # open the html file
    with open(html_file, 'r') as f:
        data = f.read()
        
    # find the path needs to be changed
    changes = re.findall(regex, data)
    
    # since we are using 'href' in our regex pattern,
    # we need to remove href path associated with 'a' tags
    results = [c[1] for c in changes if not c[1].endswith(tuple(['.html', '#']))]

    # in some cases we get telephone numbers in path,
    # so we will be removing the path without extensions
    names = [result for result in results if os.path.splitext(result)[1]]

    # creating a list for storing duplicate items
    duplicate = []

    # iterating through the path that need to be replaced with 'static'
    for name in names:

        # Checking for duplicate items
        if data.count(name) > 1:
            if name not in duplicate:
                data = data.replace(name, "{% static '" + name + "' %}")
                duplicate.append(name)
        else:
            data = data.replace(name, "{% static '" + name + "' %}")

    # writing the edited HTML file
    with open(html_file, 'w') as f:
        f.write(data)
