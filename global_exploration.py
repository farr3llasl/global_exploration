# import the Flask class from the flask module
import csv

from flask import Flask

# import the render_template function
from flask import render_template

# import the request function
from flask import request

# create a Flask object called app
app = Flask(__name__)

def read_file(file_name):
    countries = []
    with open(file_name, newline='') as csvs:
        lines = csv.DictReader(csvs)

        for line in lines:
            countries.append({'country_name': line['Country'],  #   pass name, long, lati, popu to coutries dict file 
            'longitude': line['Longitude'],
            'latitude': line['Latitude'],
            'population': line['Population']
            })      # --> {} <---
    
    # print(countries)
    return countries

countries_data = read_file('countries.csv')     # read_in the countries to countries_data

countries = [country["country_name"] for country in countries_data]     # get the only country_name
# print(countries)

@app.route("/")
def maps():
    # pass the month arg with the string "default" to the render template
    # for the month_page.html script
    return render_template('map_esri.html', countries=countries)


@app.route("/") 
@app.route("/get_data", methods=['GET', 'POST'])
def get_data():

    chosen_country = request.args['country']    # get country anem
    location_data = {'longitude': 0, 'latitude': 0, 'population': 0} # rest of data in location data

    # poulate the long,lati, and popu when country found

    for country in countries_data:
        if country["country_name"] == chosen_country:
            location_data = {
                'longitude': country["longitude"],
                'latitude': country["latitude"],
                'population': country["population"]
            }
            break

    return render_template('map_esri.html', countries=countries, location=location_data, chosen_country=chosen_country)

    


# add a main method to run the app
# as a typical Python script
if __name__ == '__main__':
    app.run()
