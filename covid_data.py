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

#stats for page europe stored in a dictionary
def europe():
    data = requests.get("https://disease.sh/v3/covid-19/countries")
    europe_data = data.json()

    europe_dict = {}
    for item in europe_data:
        if item['continent'] == 'Europe':
            if item['country'] not in europe_data:
                europe_dict.update({item['country']: {'Population': item['population'],
                                    'Confirmed': item['cases'], 'Deaths': item['deaths']}})
            else:
                europe_dict[item['country']
                            ]['Confirmed'] += item['confirmed']
                europe_dict[item['country']
                            ]['Deaths'] += item['deaths']

    return europe_dict


#stats for ireland stored in a list
def ireland():
    data = requests.get("https://api.covid19api.com/dayone/country/ireland")
    ireland_data = data.json()
    
    days = []
    cases = []
    deaths = []
    recovered = []
    active = []
    i = 1

    for item in ireland_data:
        days.append(i)
        cases.append(item['Confirmed'])
        deaths.append(item['Deaths'])
        recovered.append(item['Recovered'])
        active.append(item['Active'])
        i += 1
    
    ireland_list = [days[:-1], cases[:-1],
                    deaths[:-1], recovered[:-1], active[:-1]]

    return ireland_list

#stats for individual counties in ireland stored in a list
def ireland_counties():
    data = requests.get("https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/Covid19CountyStatisticsHPSCIrelandOpenData/FeatureServer/0/query?where=1%3D1&outFields=CountyName,ConfirmedCovidCases,ConfirmedCovidDeaths&returnGeometry=false&outSR=4326&f=json")
    ireland_counties = data.json()

    county = []
    county_cases = []

    for item in ireland_counties['features']:
        county.append(item['attributes']['CountyName'])
        county_cases.append(item['attributes']['ConfirmedCovidCases'])
    

    ireland_list = [county, county_cases]

    return ireland_list

    

    

