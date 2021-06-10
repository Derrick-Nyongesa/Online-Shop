# Capstone Project - Albany Electronics' Online Store

This is a Django project was generated with [Python](https://www.python.org/) version 3.9


## Author's Name
Derrick Nyongesa


## Description
This is a django application that allows authenticated customers to shop virtually using the internet and to allow customers to buy electronic items of their choice from the store. A new customer can subscribe to the site, choose product(s) of their choice and add to the cart, checkout and input shipping information on a form. The customer can also rate the purchased product and provide feedback on the site. This is a demo project and should not be used foe commercial purposes.


## MOCKUP DESIGN
[Mock Design Link](https://www.figma.com/proto/lGlq12IZ9UtdVCikZV0D6F/Capstone-Project?node-id=1%3A3&scaling=min-zoom&page-id=0%3A1)


## Entity relationship diagram 
![ERD - Page 1](https://user-images.githubusercontent.com/78686755/121508554-6511d900-c9ee-11eb-859b-72cb79c20547.png)


## USER STORY
1. The customer should login/register before using the application
2. The customer should view items in categories and be able to search for items.
3. The customer should be able to put items in a virtual cart and complete the purchase at a later time.
4. The customer should receive an email notification upon successful completion of the purchase.
5. The customer can provide feedback and rate the purchased item.



## Project setup instructions
1. Pull project from github Repository.

```bash
git clone https://github.com/Derrick-Nyongesa/Online-Shop.git
``` 
2. Move to the folder and create a virtual environment
3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Create a new postgress database

5. Make migrations on postgres using django
    ```bash
    $ python manage.py makemigrations <database name>
    ```
    ```bash
    $ python3 manage.py migrate
    ```
6. Run the application
    ```bash
    $ python3 manage.py runserver
    ``` 
5. Open the application on your browser `http://127.0.0.1:8000/`


## Technology used
* [Python3](https://www.python.org/)
* [Django3.2.2](https://docs.djangoproject.com/en/3.2/releases/3.2.2/)
* [Heroku](https://heroku.com)


## Contact Information 
Any query? Contact me at [nyongesaderrick@gmail.com]


## Copyright and license information
Licensed under the [MIT license](LICENSE).