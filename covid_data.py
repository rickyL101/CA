import requests

#worldwide stats
def world():
    data = requests.get("https://disease.sh/v3/covid-19/all")
    data_json = data.json()
    return data_json

#stats for individual countries stored in a dictionary
def countries():
    data = requests.get("https://disease.sh/v3/covid-19/countries")
    countries_data = data.json()

    countries_dict = {}
    for item in countries_data:
        if item['country'] not in countries_dict:
            countries_dict.update({item['country']: {'Population': item['population'],
                                  'Confirmed': item['cases'], 'Deaths': item['deaths']}})
        else:
            countries_dict[item['country']
                           ]['Confirmed'] += item['confirmed']
            countries_dict[item['country']
                           ]['Deaths'] += item['deaths']

    return countries_dict

#stats for ireland
def ireland():
    data = requests.get("https://api.covid19api.com/dayone/country/ireland")
    ireland_data = data.json()
    
    days = []
    cases = []
    deaths = []
    i = 1

    for item in ireland_data:
        days.append(i)
        cases.append(item['Confirmed'])
        deaths.append(item['Deaths'])
        i += 1
    
    ireland_list = [days[:-1], cases[:-1], deaths[:-1]]

    return ireland_list

        


