# import requests
# req=requests.get("https://swapi.dev/api/people/10/")
# print(req.status_code)
# person=req.json()
# print(person)
# print(f"person name is {person["name"]}")
# print("values in the key value pair is ", person.values())
# print(f"films in which {person['name']} is involved")
# for films in person['films']:
#     req=requests.get(films)
#     film=req.json()
#     print(f"film: {film["title"]}")
    
    
import json
cpo3='''{
	"name": "Obi-Wan Kenobi",
	"height": "182",
	"mass": "77",
	"hair_color": "auburn, white",
	"skin_color": "fair",
	"eye_color": "blue-gray",
	"birth_year": "57BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/20/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/4/",
		"https://swapi.dev/api/films/5/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [],
	"vehicles": [
		"https://swapi.dev/api/vehicles/38/"
	],
	"starships": [
		"https://swapi.dev/api/starships/48/",
		"https://swapi.dev/api/starships/59/",
		"https://swapi.dev/api/starships/64/",
		"https://swapi.dev/api/starships/65/",
		"https://swapi.dev/api/starships/74/"
	],
	"created": "2014-12-10T16:16:29.192000Z",
	"edited": "2014-12-20T21:17:50.325000Z",
	"url": "https://swapi.dev/api/people/10/"
}'''
cpo3=json.loads(cpo3)
print(cpo3)
print(f"name is: {cpo3['name']}")
print(type(cpo3))
print(f"Eye color is: {cpo3["eye_color"]}")
cpo3["eye_color"]="Black"
print(f"now the eye color is: {cpo3["eye_color"]}")
cpo3_str=json.dumps(cpo3)
print(cpo3_str)
print(cpo3_str[125:130])
