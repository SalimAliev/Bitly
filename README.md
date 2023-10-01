
<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h1 align="center">Bitly</h1>

  <p align="center">
    This is an API application for URL shortening
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This web api application has the following methods:
* Method of getting the list of URLs
* Method of getting a specific URL
* URL creation method



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* Python 3.10.11
* Django 4.2.5

<!-- GETTING STARTED -->
## Getting Started

### Installation and launch

To install the application, follow these steps

1. Clone the repository
   ```sh
   git clone https://github.com/SalimAliev/Bitly.git
   ```
2. To launch the application, open the console and go to the directory where the docker-compose file is located and enter the following command
   ```sh
   docker-compose up -d
   ```
3. To stop the application, enter the command
   ```sh
   docker-compose down
   ```

## Using
Open your browser
1. To get a list of URLs, send a GET request to the URL: http://localhost:8000/api/v1/urls_list/
2. To get one of the URLs, send a GET request to the URL: http://localhost:8000/api/v1/urls_list/1 (at the end, specify the URL id)
3. To add an URL to the database and create short ULR, send a POST request to the URL (http://localhost:8000/api/v1/urls_list/). Request body example:
   ```json
   {
    "long_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
   ```
