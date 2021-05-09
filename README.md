# LinkyFy URL Shortner
A Simple URL shorter that converts long lengthy URL to short URL.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
python3 -m venv <myenvname>
source env/bin/activate
pip install -r requirements.txt
```

## Running the app
```
uvicorn main:app --reload
```

## Deployment

I've deployed the app on Heroku
```
gunicorn -w 1 -k uvicorn.workers.UvicornH11Worker main:app
```
## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - Python web framework used to  build server
* [MongoDB ](https://www.mongodb.com/) - NoSQL Database
* [Heroku](https://heroku.com/) - Cloud
* [Nanoid](https://www.npmjs.com/package/nanoid/) - Nanoid for generating codes for shorturls
* and lots of Javascript HTML and CSS for UI 

## Screenshots


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* People of FastAPI discord server

