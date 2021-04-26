<h1 align="center">
Project 13 - Atmosberry
</h1>

<p align="center">
  <a href="">
    <img src="https://upload.wikimedia.org/wikipedia/fr/0/0d/Logo_OpenClassrooms.png" alt="Logo" width="100" height="100">
  </a>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8-green.svg">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>
  <a href="https://www.linkedin.com/in/teiva-s/">
    <img src="https://img.shields.io/badge/linkedin-Simonnet-blue.svg">
  </a>
</p>


  <h3 align="center">Final project from the OpenClassrooms Python course.</h3>

 <p align="center">
    Send data from a Raspberry to a server where you can visualize your sensor output in dedicated graphs.
    <br />
  </p>


<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://upload.wikimedia.org/wikipedia/fr/3/3b/Raspberry_Pi_logo.svg" width=55>
  </a>
</p>

As an ex-meteorologist I like to forecast the weather and tech people about it. In this project i attempt to sensitize people about the weather and climate change. 

People would have a cheap raspberry and a few sensors they can visualize online. A map will display all raspberry online and sharing data. People will take part in a utopically widespread open-source project.
 
<!-- GETTING STARTED -->
## Getting Started

#### Live version
The website is hosted on heroku  [on this link](http://www.simteiva.fr/)


## Usage

* First you connect to [the site](http://www.simteiva.fr/) and create an account.
* Once connected, you go to your [dashboard](http://www.simteiva.fr/dashboard) and click on the refresh token button to create a token.

At this point you will have access to the API and you will need to use the token to authenticate.

* Use the form to register a raspberry on the website and give it its coordinates in decimal degrees.


### Send data

To send data you will have multiple ways. The endpoint to use is: http://www.simteiva.fr/api/v1/

The format of the body you send should look like this:
```python
{
    "sensor_type": "type",
    "device": "name of the device",
    "measure": the measure,
    "timestamp": thedate,
    "name": "name of the sensor",
}
```

* `sensor_type` can only have 3 types possibility: "T", "Hu" and "P"
* The `device` must be registered before sending data to it, and you must setup the exact same name>
* `measure` is the measure of the sensor as a float.
* `timestamp` is the date in format `2021-04-19T16:36:50Z`
* `name`is the name of the sensor.


### Authentication

You must set your header as such:
`"Authorization": Token {yourtoken}`

### How
You can either use [Postman](https://www.postman.com/) or a Python script to send the data. For python it is recommanded to use [requests](https://pypi.org/project/requests/).

Function of what type of sensor you use, you will have to customize your script to get the sensor data.
For a BMP280, for example you can use the [Adafruit library](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/circuitpython-test).

Here is a very [simple python script](https://github.com/smtr42/p13_atmosberry_rasp) used to send data from your computer to the website.


## Project Itself
### Installation
#### Server side
I used Python 3.8

*  Clone the repo
```bash
$ git clone https://github.com/smtr42/p13_atmosberry2
```
*  Install required dependencies
```bash
$ pip install -r requirements.txt
```
To run tests use [pytest](https://docs.pytest.org/):
`pytest -v`

### Links
Used in the project:
* [Unsplash](https://unsplash.com/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Django rest framework](https://www.django-rest-framework.org/)
* [Black](https://pypi.org/project/black/)
* [TailwindCSS](https://tailwindcss.com/)

## Author
[Project Link](https://github.com/smtr42/p13_atmosberry2)

* **Simonnet T** - *Initial work* - [smtr42](https://github.com/smtr42)
   
  <a href="https://www.linkedin.com/in/teiva-s/">
   <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg" alt="linkedin" width="200" height="54">
 </a>
<br>