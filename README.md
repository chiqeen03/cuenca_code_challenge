# Queens problem [![Build Status](https://travis-ci.com/chiqeen03/cuenca_code_challenge.svg?branch=master)](https://travis-ci.com/chiqeen03/cuenca_code_challenge)

Until now this code is able to:
* Return all the possible positions for a n number of queens in a n\*n board to be safe
* Run tests
* Connect to Travis CI to perform tests automatically
* Connect to a local db to store values
* Build in docker

### Requirements
* Docker
* Docker-Compose

### Steps to run code
1. Clone this repository
2. Run the comand ```sudo docker-compose up -d --build``` to build the image and containers
3. Run the comand ```sudo docker-compose run main_app python main.py db queens```to instantiate the containers
3.1 This command will execute the source code and store it into a db in docker. The results will be taken from the db and printed in the command line.
