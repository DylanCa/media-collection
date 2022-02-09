# Media Collection Service
A RESTFul API to store and keep a list of all your seen TV Shows, Movies &amp; played Video Games.

____


* [Install](#install)
* [Setup and run the Django server](#setup-and-run-the-django-server)
* [What is it and How to Use](#what-is-it-and-how-to-use)
* [Available Endpoints & API Swagger](#available-endpoints--api-swagger)
* [Json APi](#json-api)


## Install

Mandatory packages & technologies for this project to work are:

- Mysql 5 ( if you chose to use another dabase service, be sure to adapt the DATABASE_URL in the .env file)
- Python3

Once you have downloaded this repo, install required pacakges using `pip`:
```
    pip install requirements.txt
```
Most important packages are:
- Django, a powerful and scalable web framework, the core of this project
- Django-Rest-Framework, a library to make Django even more powerful by adding RESTful options
- djangorestframework-jsonapi, a library to integrate JSON.Api in API requests
- DRF-YASG, "Yet Another Swagger", a library used to display available endpoints in an exploitable way
- DRF Nested Routers, a library to ease up nested routers development
- rest-framework-generic-relations , a library to handle Generic Relations & stored Generic values



## Setup and run the Django server

Once you have installed the requirements, you will have to be sure Django is able to communicate with your database by copying `.env.example` as `.env`, going into your newly created file & replace `DATABASE_URL` with your settings.
After that, start the database migration & create a superuser by doing:
```
python manage.py migrate
python manage.py createsuperuser
```
This will create required database tables & rules. Once you have done this, you can start the server by doing:
```
python manage.py runserver
```

And voilà, your server should be running on <http://localhost:8000> by default.

## What is it and How to Use

This API has been made to give you the ability to store a personal "watchlist" of sorts. You will be able to add Movies, TV Shows & Video Games to the service ( see below how to ), and mark them as "Ongoing", "Seen" or "Played", as well as "Liked" or "Not Liked".

Since this application is only an API service at the moment, you won't have an iterface. So get your Postman, Insomnia or cURL, and hit the endpoints shown [here](#available-endpoints--api-swagger). There are a few important points to take into consideration:
* To add a media ( whether it being a show, season, episode, movie or a game ), you can get data from either <http://api.themoviedb.org> or <http://igdb.com/api> and send it without modification to the API.
* The __Media Collection Service__ has been developed to understand data coming from these APIs, but can perfectly work on its own. _Please take into consideration the request format before creating an object._
* An User authentication service is provided, however the admin will have to connect to <http://localhost:8000/admin/> and create the user by hand. After that, the user will be able to use the service using a simple __Basic Auth__.
* To mark a media as Seen / Played, Liked/Disliked, please check the __MediaStatus__ endpoints.


## Available Endpoints & API Swagger

You can interact with and see the API endpoints in details using these urls ( __please note that you cannot upload files using Swagger, you will have to use cURL, PostMan or your own solution__ ):
- <http://localhost:8000/swagger/> - An interactive & good-looking API Swagger with the possibility to directly interact with Rest Endpoints
- <http://localhost:8000/redoc/> - Same API, more detailed but close to no interactivity.

Moreover, you can go to <http://localhost:8000/admin/> to have a better view of what is happening in your server.

## Json APi

Please note that I have decided to use JSON Api for this project, this means you will have to adapt your request to this specification. JSON Api ensure that the requests are properly made following specific guidelines.
To be sure your requests are made using JSON.Api, be sure to have in your Headers `Content-type: application/vnd.json+api` and to format your body as JSON Api requires you to, for example:

```
{
	"data": {
		"type": "projects",
		"attributes": {
			"name": "1st project"
		}
	}
}
```
More info here: <https://jsonapi.org>.

## Upcoming improvements
* Add Mangas & Animes
* Provide an interface to make the navigation & requesting simpler
