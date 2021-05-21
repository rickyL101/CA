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
