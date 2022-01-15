# book-ratings-api

## Overview
A REST API build in Django for rating books with 1 to 5 stars.

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you want to run your own build, you must have python globally installed in your computer. If you don't, you can get python [here](https://www.python.org").
* After this, confirm that you have installed virtualenv globally as well. If another case, run:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone the repository to your PC
    ```bash
        $ git clone https://github.com/axel-schl/book-ratings-api.git
    ```

* #### Dependencies
    1. Cd the cloned repo as such:
        ```bash
            $ cd book-ratings-api
        ```
    2. Create and activate your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the requeriments needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make the corresponding migrations
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run the server and Sign Up

    Run the server with:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the api service on your browser and sign up a new user using:
    ```
        http://localhost:8000/api/auth/signup
    ```
    
    ![img](https://i.imgur.com/OdMaiao.png)
    
    
    You can do it through the HTML form or in .json format by selecting "RAW DATA"
    
 * #### Login
  
  Login with the credentials created when you sign up as a json file:
    ```
        http://localhost:8000/api/auth/login
    ```
    -
    ![img](https://i.imgur.com/5IiEeA5.png)
    -
    To ensure successful login, look at the top right side and check if your email is there.
    -
    ![img](https://i.imgur.com/8s3GcAs.png)
    
 * #### Logout 
    
    If you want to logout, just enter the url:
     ```
        http://localhost:8000/api/auth/logout
     ```
    
    And make an empty post.
  
  * #### Books
  
  
    To get the list of available books:
    
     ```
        http://localhost:8000/api/books
     ```
     
     You will get something like this:
     
     ```
        {
    "count": 11,
    "num_pages": 2,
    "page_number": 1,
    "page_size": 8,
    "next_link": "?page=2",
    "previous_link": null,
    "results": [
        {
            "id": "fc29d72b-ad58-46c8-840e-12da5b76a059",
            "title": "Art and Cosmotechnichs",
            "publisher": "Penguin",
            "edition_year": 2021,
            "description": "In light of current discourses on AI and robotics, what do the various experiences of art contribute to the rethinking of technology today?\r\nCharting a course through Greek tragic thought, cybernetic logic, and the aesthetics of Chinese landscape painting (山水, shanshui— mountain and water painting), Art and Cosmotechnics addresses the challenge to art and philosophy posed by contemporary technological transformation. How might a renewed understanding of the varieties of experience of art be possible in the face of discourses surrounding artificial intelligence and robotics? Departing from Hegel’s thesis on the end of art and Heidegger’s assertion of the end of philosophy, Art and Cosmotechnics travels an unfamiliar trajectory of thought to arrive at a new relation between art and technology.",
            "isbn13": null,
            "avg_stars": 5.0,
            "image_thumbnail": null,
            "author": 3,
            "genre": 2
        },
        {
            "id": "70b29b3d-6004-4b8d-9bfb-e8694a1eb01e",
            "title": "Being and Time",
            "publisher": "Penguin",
            "edition_year": 2019,
            "description": "Being and Time (German: Sein und Zeit) is the 1927 magnum opus of German philosopher Martin Heidegger and a key document of existentialism. Being and Time had a notable impact on subsequent philosophy, literary theory and many other fields. Though controversial, its stature in intellectual history has been compared with works by Kant and Hegel.",
            "isbn13": 9781853260957,
            "avg_stars": 0.0,
            "image_thumbnail": "http://localhost:8000/media/books/70b29b3d-6004-4b8d-9bfb-e8694a1eb01e/9780061575594.jpg",
            "author": 2,
            "genre": 2
        },
        {
            "id": "c0f8d978-e753-411c-a61a-55ac1c4062b9",
            "title": "Don Quijote de la Mancha",
            "publisher": "Penguin",
            "edition_year": 2018,
            "description": "",
            "isbn13": null,
            "avg_stars": 0.0,
            "image_thumbnail": "http://localhost:8000/media/books/c0f8d978-e753-411c-a61a-55ac1c4062b9/quijote.jfif",
            "author": 4,
            "genre": 1
        },
        {
            "id": "8f9d612f-bea2-46a1-afb9-b6294bcee1b9",
            "title": "Fictions",
            "publisher": "Penguin",
            "edition_year": 2019,
            "description": "From Jorge Luis Borges’s 1935 debut with The Universal History of Iniquity, through his immensely influential collections Ficciones and The Aleph, these enigmatic, elaborate, imaginative inventions display his talent for turning fiction on its head by playing with form and genre and toying with language. Together these incomparable works comprise the perfect one-volume compendium for all those who have long loved Borges, and a superb introduction to the master's work for those who have yet to discover this singular genius.",
            "isbn13": 9780140286809,
            "avg_stars": 0.0,
            "image_thumbnail": null,
            "author": 6,
            "genre": 3
        },
     ```
     
     As you can see, there are filters available to search for a particular book by author, genre, etc.
     You can still create new books from the admin console (credentials are available in admin.txt)(```http://localhost:8000/admin```)
     You can also do a get of the authors and genres of books in the urls:
    
     ```http://localhost:8000/api/authors```
     ```http://localhost:8000/api/genres```
  
    * #### Rating Books

    Once logged in, you can rate books in: (```http://localhost:8000/api/user_ratings```), making a post request in .json format using the uuid of the book to rate. 
    
    Suppose we want to rate Fictions by Jorge Luis Borges with 5 stars (of course!). It "uuid" is: "8f9d612f-bea2-46a1-afb9-b6294bcee1b9". So:
    
    ![img](https://i.imgur.com/OrdzmPB.png)
    
    Don't forget that the field is not "id", it is "uuid". If you want you can add "review", but it can be left blank or null.
    
    After refreshing, all the books ranked by the authenticated user will appear with its "avg_stars" attribute updated with the average rating of all users.
    
    Thank you for visiting my repository! 
    
    I will try in the future to add a recommendation system that works online with a larger database of users and books.
    
