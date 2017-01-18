# Adding-django-static-template-tag-to-html-page

Program to convert 'files path' to static files path or 'static template tag', that will be compatible with DJANGO STATIC FILES

### For Example:
In actual HTML file:
```html
<link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
<a href="#"><img src="images/logo.png" alt="HATA">HATA</a>
<script src="js/jquery-1.11.3.min.js"></script>
```
will be converted to DJANGO STATIC FILE format or 'static template tag' such as
```html
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" type="text/css">
<a href="#"><img src="{% static 'images/logo.png' %}" alt="HATA">HATA</a>
<script src="{% static 'js/jquery-1.11.3.min.js' %}"></script>
```

Author: Jeril Kuriakose

Project Page: [https://github.com/jerilkuriakose/Adding-django-static-template-tag-to-html-page](https://github.com/jerilkuriakose/Adding-django-static-template-tag-to-html-page)

### TO RUN THIS FILE:
open this file using command prompt,
pass the directory path as the command line argument

### For Example:
```
D:\>python replace_path.py <directory_path>
```
like
```
D:\>python replace_path.py "C:\Users\username\Desktop\hata-html"
```
#### if your static files are located inside another folder, pass the folder name as the second arguement
```
D:\>python replace_path.py <directory_path> <static_folder_name>
```
or
```
D:\>python replace_path.py "C:\Users\username\Desktop\hata-html" "main_page/"
```
will be replaced as follows:
```
<link rel="stylesheet" href="{% static 'main_page/css/bootstrap.min.css' %}" type="text/css">
<a href="#"><img src="{% static 'main_page/images/logo.png' %}" alt="HATA">HATA</a>
<script src="{% static 'main_page/js/jquery-1.11.3.min.js' %}"></script>
```