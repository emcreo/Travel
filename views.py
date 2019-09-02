from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from CitiesApp.models import Cities
from .models import Search
from .forms import SearchForm
from amadeus import Client, Response
from bs4 import BeautifulSoup
import requests
import json
  
def citiesIndex(request):
    # Creates blank form on initial page load
    if request.method == 'GET':
        form = SearchForm(initial = "")
        context = {'form' : form}
        return render(request, "CitiesApp_index.html", context)
            
    elif request.method =='POST':
        form = SearchForm(request.POST)
        form.save()

        #Cleaning the form
        if form.is_valid():
            form = form.cleaned_data

        search = Search.objects.filter().order_by('-id')[0]
        cities = findMatches(search.destination)
        context = {'cities' : cities, 'form': form}
        return render(request, "CitiesApp_index.html", context)


def CitiesSearch(request, IATA):
    form = SearchForm(initial = "")
   #Initialize Amadeus
    amadeus = Client(
        client_id = "oXoHcPGNhQAKNcvvhFIkB9kFudwrBYTy",
        client_secret = "zs3PhgM4HNpZbCm4"
    )
    response = amadeus.cities_offers.get(cityCode = IATA)
    # with open("static\json\log.json", "w+", encoding="utf-8") as log: -->> This creates log.json 
    #     json.dump(response.data, log, indent=2)
    result = response.data
    context = {'form' : form, 'results' : result}
    return render(request, "CitiesApp_index.html", context)
    

def send_json(request):
    data = [
        {
    "city": "New York",
    "growth_from_2000_to_2013": "4.80%",
    "latitude": 40.7127837,
    "longitude": -74.0059413,
    "population": 8405837,
    "rank": 1,
    "state": "New York",
    "timezone": "America/New_York"
  },
  {
    "city": "Los Angeles",
    "growth_from_2000_to_2013": "4.80%",
    "latitude": 34.0522342,
    "longitude": -118.2436849,
    "population": 3884307,
    "rank": 2,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Chicago",
    "growth_from_2000_to_2013": "-6.10%",
    "latitude": 41.8781136,
    "longitude": -87.6297982,
    "population": 2718782,
    "rank": 3,
    "state": "Illinois",
    "timezone": "America/Chicago"
  },
  {
    "city": "Houston",
    "growth_from_2000_to_2013": "11.00%",
    "latitude": 29.7604267,
    "longitude": -95.3698028,
    "population": 2195914,
    "rank": 4,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Philadelphia",
    "growth_from_2000_to_2013": "2.60%",
    "latitude": 39.9525839,
    "longitude": -75.1652215,
    "population": 1553165,
    "rank": 5,
    "state": "Pennsylvania",
    "timezone": "America/New_York"
  },
  {
    "city": "Phoenix",
    "growth_from_2000_to_2013": "14.00%",
    "latitude": 33.4483771,
    "longitude": -112.0740373,
    "population": 1513367,
    "rank": 6,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "San Antonio",
    "growth_from_2000_to_2013": "21.00%",
    "latitude": 29.4241219,
    "longitude": -98.4936282,
    "population": 1409019,
    "rank": 7,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "San Diego",
    "growth_from_2000_to_2013": "10.50%",
    "latitude": 32.715738,
    "longitude": -117.1610838,
    "population": 1355896,
    "rank": 8,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Dallas",
    "growth_from_2000_to_2013": "5.60%",
    "latitude": 32.7766642,
    "longitude": -96.7969879,
    "population": 1257676,
    "rank": 9,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "San Jose",
    "growth_from_2000_to_2013": "10.50%",
    "latitude": 37.3382082,
    "longitude": -121.8863286,
    "population": 998537,
    "rank": 10,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Austin",
    "growth_from_2000_to_2013": "31.70%",
    "latitude": 30.267153,
    "longitude": -97.7430608,
    "population": 885400,
    "rank": 11,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Indianapolis",
    "growth_from_2000_to_2013": "7.80%",
    "latitude": 39.768403,
    "longitude": -86.158068,
    "population": 843393,
    "rank": 12,
    "state": "Indiana",
    "timezone": "America/Indiana/Indianapolis"
  },
  {
    "city": "Jacksonville",
    "growth_from_2000_to_2013": "14.30%",
    "latitude": 30.3321838,
    "longitude": -81.655651,
    "population": 842583,
    "rank": 13,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "San Francisco",
    "growth_from_2000_to_2013": "7.70%",
    "latitude": 37.7749295,
    "longitude": -122.4194155,
    "population": 837442,
    "rank": 14,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Columbus",
    "growth_from_2000_to_2013": "14.80%",
    "latitude": 39.9611755,
    "longitude": -82.9987942,
    "population": 822553,
    "rank": 15,
    "state": "Ohio",
    "timezone": "America/New_York"
  },
  {
    "city": "Charlotte",
    "growth_from_2000_to_2013": "39.10%",
    "latitude": 35.2270869,
    "longitude": -80.8431267,
    "population": 792862,
    "rank": 16,
    "state": "North Carolina",
    "timezone": "America/New_York"
  },
  {
    "city": "Fort Worth",
    "growth_from_2000_to_2013": "45.10%",
    "latitude": 32.7554883,
    "longitude": -97.3307658,
    "population": 792727,
    "rank": 17,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Detroit",
    "growth_from_2000_to_2013": "-27.10%",
    "latitude": 42.331427,
    "longitude": -83.0457538,
    "population": 688701,
    "rank": 18,
    "state": "Michigan",
    "timezone": "America/Detroit"
  },
  {
    "city": "El Paso",
    "growth_from_2000_to_2013": "19.40%",
    "latitude": 31.7775757,
    "longitude": -106.4424559,
    "population": 674433,
    "rank": 19,
    "state": "Texas",
    "timezone": "America/Denver"
  },
  {
    "city": "Memphis",
    "growth_from_2000_to_2013": "-5.30%",
    "latitude": 35.1495343,
    "longitude": -90.0489801,
    "population": 653450,
    "rank": 20,
    "state": "Tennessee",
    "timezone": "America/Chicago"
  },
  {
    "city": "Seattle",
    "growth_from_2000_to_2013": "15.60%",
    "latitude": 47.6062095,
    "longitude": -122.3320708,
    "population": 652405,
    "rank": 21,
    "state": "Washington",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Denver",
    "growth_from_2000_to_2013": "16.70%",
    "latitude": 39.7392358,
    "longitude": -104.990251,
    "population": 649495,
    "rank": 22,
    "state": "Colorado",
    "timezone": "America/Denver"
  },
  {
    "city": "Washington",
    "growth_from_2000_to_2013": "13.00%",
    "latitude": 38.9071923,
    "longitude": -77.0368707,
    "population": 646449,
    "rank": 23,
    "state": "District of Columbia",
    "timezone": "America/New_York"
  },
  {
    "city": "Boston",
    "growth_from_2000_to_2013": "9.40%",
    "latitude": 42.3600825,
    "longitude": -71.0588801,
    "population": 645966,
    "rank": 24,
    "state": "Massachusetts",
    "timezone": "America/New_York"
  },
  {
    "city": "Nashville-Davidson",
    "growth_from_2000_to_2013": "16.20%",
    "latitude": 36.1626638,
    "longitude": -86.7816016,
    "population": 634464,
    "rank": 25,
    "state": "Tennessee",
    "timezone": "America/Chicago"
  },
  {
    "city": "Baltimore",
    "growth_from_2000_to_2013": "-4.00%",
    "latitude": 39.2903848,
    "longitude": -76.6121893,
    "population": 622104,
    "rank": 26,
    "state": "Maryland",
    "timezone": "America/New_York"
  },
  {
    "city": "Oklahoma City",
    "growth_from_2000_to_2013": "20.20%",
    "latitude": 35.4675602,
    "longitude": -97.5164276,
    "population": 610613,
    "rank": 27,
    "state": "Oklahoma",
    "timezone": "America/Chicago"
  },
  {
    "city": "Louisville/Jefferson County",
    "growth_from_2000_to_2013": "10.00%",
    "latitude": 38.2526647,
    "longitude": -85.7584557,
    "population": 609893,
    "rank": 28,
    "state": "Kentucky",
    "timezone": "America/Kentucky/Louisville"
  },
  {
    "city": "Portland",
    "growth_from_2000_to_2013": "15.00%",
    "latitude": 45.5230622,
    "longitude": -122.6764816,
    "population": 609456,
    "rank": 29,
    "state": "Oregon",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Las Vegas",
    "growth_from_2000_to_2013": "24.50%",
    "latitude": 36.1699412,
    "longitude": -115.1398296,
    "population": 603488,
    "rank": 30,
    "state": "Nevada",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Milwaukee",
    "growth_from_2000_to_2013": "0.30%",
    "latitude": 43.0389025,
    "longitude": -87.9064736,
    "population": 599164,
    "rank": 31,
    "state": "Wisconsin",
    "timezone": "America/Chicago"
  },
  {
    "city": "Albuquerque",
    "growth_from_2000_to_2013": "23.50%",
    "latitude": 35.0853336,
    "longitude": -106.6055534,
    "population": 556495,
    "rank": 32,
    "state": "New Mexico",
    "timezone": "America/Denver"
  },
  {
    "city": "Tucson",
    "growth_from_2000_to_2013": "7.50%",
    "latitude": 32.2217429,
    "longitude": -110.926479,
    "population": 526116,
    "rank": 33,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "Fresno",
    "growth_from_2000_to_2013": "18.30%",
    "latitude": 36.7468422,
    "longitude": -119.7725868,
    "population": 509924,
    "rank": 34,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Sacramento",
    "growth_from_2000_to_2013": "17.20%",
    "latitude": 38.5815719,
    "longitude": -121.4943996,
    "population": 479686,
    "rank": 35,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Long Beach",
    "growth_from_2000_to_2013": "1.50%",
    "latitude": 33.7700504,
    "longitude": -118.1937395,
    "population": 469428,
    "rank": 36,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Kansas City",
    "growth_from_2000_to_2013": "5.50%",
    "latitude": 39.0997265,
    "longitude": -94.5785667,
    "population": 467007,
    "rank": 37,
    "state": "Missouri",
    "timezone": "America/Chicago"
  },
  {
    "city": "Mesa",
    "growth_from_2000_to_2013": "13.50%",
    "latitude": 33.4151843,
    "longitude": -111.8314724,
    "population": 457587,
    "rank": 38,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "Virginia Beach",
    "growth_from_2000_to_2013": "5.10%",
    "latitude": 36.8529263,
    "longitude": -75.977985,
    "population": 448479,
    "rank": 39,
    "state": "Virginia",
    "timezone": "America/New_York"
  },
  {
    "city": "Atlanta",
    "growth_from_2000_to_2013": "6.20%",
    "latitude": 33.7489954,
    "longitude": -84.3879824,
    "population": 447841,
    "rank": 40,
    "state": "Georgia",
    "timezone": "America/New_York"
  },
  {
    "city": "Colorado Springs",
    "growth_from_2000_to_2013": "21.40%",
    "latitude": 38.8338816,
    "longitude": -104.8213634,
    "population": 439886,
    "rank": 41,
    "state": "Colorado",
    "timezone": "America/Denver"
  },
  {
    "city": "Omaha",
    "growth_from_2000_to_2013": "5.90%",
    "latitude": 41.2523634,
    "longitude": -95.9979883,
    "population": 434353,
    "rank": 42,
    "state": "Nebraska",
    "timezone": "America/Chicago"
  },
  {
    "city": "Raleigh",
    "growth_from_2000_to_2013": "48.70%",
    "latitude": 35.7795897,
    "longitude": -78.6381787,
    "population": 431746,
    "rank": 43,
    "state": "North Carolina",
    "timezone": "America/New_York"
  },
  {
    "city": "Miami",
    "growth_from_2000_to_2013": "14.90%",
    "latitude": 25.7616798,
    "longitude": -80.1917902,
    "population": 417650,
    "rank": 44,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "Oakland",
    "growth_from_2000_to_2013": "1.30%",
    "latitude": 37.8043637,
    "longitude": -122.2711137,
    "population": 406253,
    "rank": 45,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Minneapolis",
    "growth_from_2000_to_2013": "4.50%",
    "latitude": 44.977753,
    "longitude": -93.2650108,
    "population": 400070,
    "rank": 46,
    "state": "Minnesota",
    "timezone": "America/Chicago"
  },
  {
    "city": "Tulsa",
    "growth_from_2000_to_2013": "1.30%",
    "latitude": 36.1539816,
    "longitude": -95.992775,
    "population": 398121,
    "rank": 47,
    "state": "Oklahoma",
    "timezone": "America/Chicago"
  },
  {
    "city": "Cleveland",
    "growth_from_2000_to_2013": "-18.10%",
    "latitude": 41.49932,
    "longitude": -81.6943605,
    "population": 390113,
    "rank": 48,
    "state": "Ohio",
    "timezone": "America/New_York"
  },
  {
    "city": "Wichita",
    "growth_from_2000_to_2013": "9.70%",
    "latitude": 37.688889,
    "longitude": -97.336111,
    "population": 386552,
    "rank": 49,
    "state": "Kansas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Arlington",
    "growth_from_2000_to_2013": "13.30%",
    "latitude": 32.735687,
    "longitude": -97.1080656,
    "population": 379577,
    "rank": 50,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "New Orleans",
    "growth_from_2000_to_2013": "-21.60%",
    "latitude": 29.9510658,
    "longitude": -90.0715323,
    "population": 378715,
    "rank": 51,
    "state": "Louisiana",
    "timezone": "America/Chicago"
  },
  {
    "city": "Bakersfield",
    "growth_from_2000_to_2013": "48.40%",
    "latitude": 35.3732921,
    "longitude": -119.0187125,
    "population": 363630,
    "rank": 52,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Tampa",
    "growth_from_2000_to_2013": "16.00%",
    "latitude": 27.950575,
    "longitude": -82.4571776,
    "population": 352957,
    "rank": 53,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "Honolulu",
    "growth_from_2000_to_2013": "-6.20%",
    "latitude": 21.3069444,
    "longitude": -157.8583333,
    "population": 347884,
    "rank": 54,
    "state": "Hawaii",
    "timezone": "Pacific/Honolulu"
  },
  {
    "city": "Aurora",
    "growth_from_2000_to_2013": "24.40%",
    "latitude": 39.7294319,
    "longitude": -104.8319195,
    "population": 345803,
    "rank": 55,
    "state": "Colorado",
    "timezone": "America/Denver"
  },
  {
    "city": "Anaheim",
    "growth_from_2000_to_2013": "4.70%",
    "latitude": 33.8352932,
    "longitude": -117.9145036,
    "population": 345012,
    "rank": 56,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Santa Ana",
    "growth_from_2000_to_2013": "-1.20%",
    "latitude": 33.7455731,
    "longitude": -117.8678338,
    "population": 334227,
    "rank": 57,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "St. Louis",
    "growth_from_2000_to_2013": "-8.20%",
    "latitude": 38.6270025,
    "longitude": -90.1994042,
    "population": 318416,
    "rank": 58,
    "state": "Missouri",
    "timezone": "America/Chicago"
  },
  {
    "city": "Riverside",
    "growth_from_2000_to_2013": "22.50%",
    "latitude": 33.9533487,
    "longitude": -117.3961564,
    "population": 316619,
    "rank": 59,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Corpus Christi",
    "growth_from_2000_to_2013": "14.10%",
    "latitude": 27.8005828,
    "longitude": -97.396381,
    "population": 316381,
    "rank": 60,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Lexington-Fayette",
    "growth_from_2000_to_2013": "18.00%",
    "latitude": 38.0405837,
    "longitude": -84.5037164,
    "population": 308428,
    "rank": 61,
    "state": "Kentucky",
    "timezone": "America/New_York"
  },
  {
    "city": "Pittsburgh",
    "growth_from_2000_to_2013": "-8.30%",
    "latitude": 40.4406248,
    "longitude": -79.9958864,
    "population": 305841,
    "rank": 62,
    "state": "Pennsylvania",
    "timezone": "America/New_York"
  },
  {
    "city": "Anchorage",
    "growth_from_2000_to_2013": "15.40%",
    "latitude": 61.2180556,
    "longitude": -149.9002778,
    "population": 300950,
    "rank": 63,
    "state": "Alaska",
    "timezone": "America/Anchorage"
  },
  {
    "city": "Stockton",
    "growth_from_2000_to_2013": "21.80%",
    "latitude": 37.9577016,
    "longitude": -121.2907796,
    "population": 298118,
    "rank": 64,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Cincinnati",
    "growth_from_2000_to_2013": "-10.10%",
    "latitude": 39.1031182,
    "longitude": -84.5120196,
    "population": 297517,
    "rank": 65,
    "state": "Ohio",
    "timezone": "America/New_York"
  },
  {
    "city": "St. Paul",
    "growth_from_2000_to_2013": "2.80%",
    "latitude": 44.9537029,
    "longitude": -93.0899578,
    "population": 294873,
    "rank": 66,
    "state": "Minnesota",
    "timezone": "America/Chicago"
  },
  {
    "city": "Toledo",
    "growth_from_2000_to_2013": "-10.00%",
    "latitude": 41.6639383,
    "longitude": -83.555212,
    "population": 282313,
    "rank": 67,
    "state": "Ohio",
    "timezone": "America/New_York"
  },
  {
    "city": "Greensboro",
    "growth_from_2000_to_2013": "22.30%",
    "latitude": 36.0726354,
    "longitude": -79.7919754,
    "population": 279639,
    "rank": 68,
    "state": "North Carolina",
    "timezone": "America/New_York"
  },
  {
    "city": "Newark",
    "growth_from_2000_to_2013": "2.10%",
    "latitude": 40.735657,
    "longitude": -74.1723667,
    "population": 278427,
    "rank": 69,
    "state": "New Jersey",
    "timezone": "America/New_York"
  },
  {
    "city": "Plano",
    "growth_from_2000_to_2013": "22.40%",
    "latitude": 33.0198431,
    "longitude": -96.6988856,
    "population": 274409,
    "rank": 70,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Henderson",
    "growth_from_2000_to_2013": "51.00%",
    "latitude": 36.0395247,
    "longitude": -114.9817213,
    "population": 270811,
    "rank": 71,
    "state": "Nevada",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Lincoln",
    "growth_from_2000_to_2013": "18.00%",
    "latitude": 40.8257625,
    "longitude": -96.6851982,
    "population": 268738,
    "rank": 72,
    "state": "Nebraska",
    "timezone": "America/Chicago"
  },
  {
    "city": "Buffalo",
    "growth_from_2000_to_2013": "-11.30%",
    "latitude": 42.8864468,
    "longitude": -78.8783689,
    "population": 258959,
    "rank": 73,
    "state": "New York",
    "timezone": "America/New_York"
  },
  {
    "city": "Jersey City",
    "growth_from_2000_to_2013": "7.20%",
    "latitude": 40.7281575,
    "longitude": -74.0776417,
    "population": 257342,
    "rank": 74,
    "state": "New Jersey",
    "timezone": "America/New_York"
  },
  {
    "city": "Chula Vista",
    "growth_from_2000_to_2013": "46.20%",
    "latitude": 32.6400541,
    "longitude": -117.0841955,
    "population": 256780,
    "rank": 75,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Fort Wayne",
    "growth_from_2000_to_2013": "1.00%",
    "latitude": 41.079273,
    "longitude": -85.1393513,
    "population": 256496,
    "rank": 76,
    "state": "Indiana",
    "timezone": "America/Indiana/Indianapolis"
  },
  {
    "city": "Orlando",
    "growth_from_2000_to_2013": "31.20%",
    "latitude": 28.5383355,
    "longitude": -81.3792365,
    "population": 255483,
    "rank": 77,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "St. Petersburg",
    "growth_from_2000_to_2013": "0.30%",
    "latitude": 27.773056,
    "longitude": -82.64,
    "population": 249688,
    "rank": 78,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "Chandler",
    "growth_from_2000_to_2013": "38.70%",
    "latitude": 33.3061605,
    "longitude": -111.8412502,
    "population": 249146,
    "rank": 79,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "Laredo",
    "growth_from_2000_to_2013": "38.20%",
    "latitude": 27.5305671,
    "longitude": -99.4803241,
    "population": 248142,
    "rank": 80,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Norfolk",
    "growth_from_2000_to_2013": "5.00%",
    "latitude": 36.8507689,
    "longitude": -76.2858726,
    "population": 246139,
    "rank": 81,
    "state": "Virginia",
    "timezone": "America/New_York"
  },
  {
    "city": "Durham",
    "growth_from_2000_to_2013": "29.90%",
    "latitude": 35.9940329,
    "longitude": -78.898619,
    "population": 245475,
    "rank": 82,
    "state": "North Carolina",
    "timezone": "America/New_York"
  },
  {
    "city": "Madison",
    "growth_from_2000_to_2013": "15.80%",
    "latitude": 43.0730517,
    "longitude": -89.4012302,
    "population": 243344,
    "rank": 83,
    "state": "Wisconsin",
    "timezone": "America/Chicago"
  },
  {
    "city": "Lubbock",
    "growth_from_2000_to_2013": "19.60%",
    "latitude": 33.5778631,
    "longitude": -101.8551665,
    "population": 239538,
    "rank": 84,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Irvine",
    "growth_from_2000_to_2013": "61.30%",
    "latitude": 33.6839473,
    "longitude": -117.7946942,
    "population": 236716,
    "rank": 85,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Winston-Salem",
    "growth_from_2000_to_2013": "16.90%",
    "latitude": 36.0998596,
    "longitude": -80.244216,
    "population": 236441,
    "rank": 86,
    "state": "North Carolina",
    "timezone": "America/New_York"
  },
  {
    "city": "Glendale",
    "growth_from_2000_to_2013": "5.70%",
    "latitude": 33.5386523,
    "longitude": -112.1859866,
    "population": 234632,
    "rank": 87,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "Garland",
    "growth_from_2000_to_2013": "8.50%",
    "latitude": 32.912624,
    "longitude": -96.6388833,
    "population": 234566,
    "rank": 88,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Hialeah",
    "growth_from_2000_to_2013": "3.20%",
    "latitude": 25.8575963,
    "longitude": -80.2781057,
    "population": 233394,
    "rank": 89,
    "state": "Florida",
    "timezone": "America/New_York"
  },
  {
    "city": "Reno",
    "growth_from_2000_to_2013": "26.80%",
    "latitude": 39.5296329,
    "longitude": -119.8138027,
    "population": 233294,
    "rank": 90,
    "state": "Nevada",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Chesapeake",
    "growth_from_2000_to_2013": "15.10%",
    "latitude": 36.7682088,
    "longitude": -76.2874927,
    "population": 230571,
    "rank": 91,
    "state": "Virginia",
    "timezone": "America/New_York"
  },
  {
    "city": "Gilbert",
    "growth_from_2000_to_2013": "96.00%",
    "latitude": 33.3528264,
    "longitude": -111.789027,
    "population": 229972,
    "rank": 92,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "Baton Rouge",
    "growth_from_2000_to_2013": "0.40%",
    "latitude": 30.4582829,
    "longitude": -91.1403196,
    "population": 229426,
    "rank": 93,
    "state": "Louisiana",
    "timezone": "America/Chicago"
  },
  {
    "city": "Irving",
    "growth_from_2000_to_2013": "19.10%",
    "latitude": 32.8140177,
    "longitude": -96.9488945,
    "population": 228653,
    "rank": 94,
    "state": "Texas",
    "timezone": "America/Chicago"
  },
  {
    "city": "Scottsdale",
    "growth_from_2000_to_2013": "11.00%",
    "latitude": 33.4941704,
    "longitude": -111.9260519,
    "population": 226918,
    "rank": 95,
    "state": "Arizona",
    "timezone": "America/Phoenix"
  },
  {
    "city": "North Las Vegas",
    "growth_from_2000_to_2013": "92.20%",
    "latitude": 36.1988592,
    "longitude": -115.1175013,
    "population": 226877,
    "rank": 96,
    "state": "Nevada",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Fremont",
    "growth_from_2000_to_2013": "10.00%",
    "latitude": 37.5482697,
    "longitude": -121.9885719,
    "population": 224922,
    "rank": 97,
    "state": "California",
    "timezone": "America/Los_Angeles"
  },
  {
    "city": "Boise City",
    "growth_from_2000_to_2013": "9.50%",
    "latitude": 43.6187102,
    "longitude": -116.2146068,
    "population": 214237,
    "rank": 98,
    "state": "Idaho",
    "timezone": "America/Boise"
  },
  {
    "city": "Richmond",
    "growth_from_2000_to_2013": "8.20%",
    "latitude": 37.5407246,
    "longitude": -77.4360481,
    "population": 214114,
    "rank": 99,
    "state": "Virginia",
    "timezone": "America/New_York"
  },
  {
    "city": "San Bernardino",
    "growth_from_2000_to_2013": "13.00%",
    "latitude": 34.1083449,
    "longitude": -117.2897652,
    "population": 213708,
    "rank": 100,
    "state": "California",
    "timezone": "America/Los_Angeles"
  }
]

    return JsonResponse(data, self=False)