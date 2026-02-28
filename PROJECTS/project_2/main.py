#search pokemon


import requests
while True:
    poki=input('Enter the name of pokemon ').lower()
    req=requests.get(f"https://pokeapi.co/api/v2/pokemon/{poki}")
    if(req.status_code==200):
        print(req.status_code)
        poki=req.json()
        print("Name of pokemon is ",poki['name'])
        print('Its height is',poki['height'],'meter')
        print("Ability of pokemon is ")
        for ability in poki['abilities']:
            print(ability["ability"]["name"])
        url=ability['ability']['url']
        req=requests.get(url)
        something=req.json()
        print(something['effect_entries'][1]['effect'])
    else:
        print('Enter correct pokemon name')
    i=input('Search for other pokemon?(y/n) ').lower()
    if(i=='n'):
        break;
    else:
        continue