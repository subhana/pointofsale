
## Notes

* I have not been able to implement cart at all due to time constraint. I am saving order and order related items directly into database from django view. So it is kind of hard coded although I am using items from database.

* I have not written any css or JavaScript, again due to time constraint. Neither have I implemented login, admin, currency conversion and vat based on location etc.

* I have implemented an order list page, from where a detail invoice page opens upon clicking on a link. On the list page, there is also a link for creating order.

* The list page also displays a search box that can search using only invoice number for now

* The development server runs at 127.0.0.1

* There is a text file listing all MySQL queries I have used

* I was having issues connecting to the database server with the latest version of Django and Python 3.7. Finally I got things working with Django 1.11 and Python 2.7 

 * Django official documentation suggests having `app_name/templates/app_name/template.html` for using templates without any conflict. Since I have only one app named `salesman` so I did not need to that
