# Fill in this file with the code from parsing JSON exercise
import json
dosya = open("aziz.json", "r")
json_dosya = json.load(dosya)
print("Ad", "\t : ", json_dosya["kimlik"][0])
print("Soyad", "\t : ", json_dosya["kimlik"][1])
