# mfs_locator

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
	<li><a href="#installation">Test unit & API documentation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The mfs_locator is a spacial implementation resolving the Euclidean distance between several points. In this project, given a list of coordinates, we get two pairs of 
coordinates that are close to one another.

The Algorithm implemented removes any duplicates in the list supplied to process the residule. The implementation is that, to get the two nearest pairs we compute the distance matrix, 
then we get the minimum scoring in the matrix.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install python (3.8+).

* git clone https://github.com/Ndiithi/mfs_locator.git

* install dev libs:  sudo apt install libpq-dev python3-dev (debian distros)

### Installation

1. Change directory
   ```sh
   cd mfs_locator
   ```
   
2. Set up virtual environment:
   ```sh
    virtaulenv --python=/location/of/python3.8 ./ 
   ```
   
3. Activate enviroment.
   ```sh
   source bin/activate
   ```
   
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
   
5. Make migrations
   ```sh
   python manage.py makemigrations
   ```
   
6. Migrate
   ```sh
   python manage.py migrate
   ```

7. Set up new user
   ```sh
   python manage.py createsuperuser --email admin@example.com --username admin

   ```

8. Run the app
   ```sh
   python manage.py runserver

   ```
   
### Test unit & API documentation

The end point is coformat to Swagger sturcure and so is the documentation for the API.
   
1. Run tests
   ```sh
   python manage.py test

   ```
   
#### Documentation
The documentation can be accessed under the following three paths from the base URL:

/swagger

eg: 

   ```sh
   http://localhost:8000/swagger

   ```
   
/swagger.yaml

   ```sh
   http://localhost:8000/swagger.yaml

   ```

and 

/redoc


   ```sh
   http://localhost:8000/redoc

   ```
 
<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.
