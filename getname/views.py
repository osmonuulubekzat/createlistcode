from django.shortcuts import render
import os


# Create your views here.
def Index(request):


    if request.method == 'POST':
    # path_passport = "C:/Users/User/Desktop/УМРА 2022-2023/САИДЖАМАЛ АЖЫ/PASSPORT"
        send = request.POST["path"]
        test = send.split("\\")
        print(test)
        path_passport = ""
        for i in test:
            path_passport += i + "/"
        passports = os.listdir(path_passport)
        full_names = []
        lider = path_passport.split("/")
        for i in passports:
            name = i.split(".")
            full_names.append(name[0].strip())
        context = {"content": full_names, "lider": lider[-3]}
        return render(request, "index.html", context)
    return render(request, "index.html")