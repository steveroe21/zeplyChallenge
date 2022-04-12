# zeplyChallenge
 In this Python challenge we want you to implement a simple REST API for generating valid cryptocurrency addresses and displaying them. Specifically, your API should provide three endpoints, as follows:  Generate Address,  List Address , Retrieve address. 
I started with an app.py file with a basic app route that takes you to the home page "cryptoChoice.html. On this page you chose if you want to create an ETH address or a BTC address.
When you press submit your address is created and you are redirected to the page whenre you retrieve your address and Id, "retrieve.html". With your new id, you can use "list.html" to see if this id is linked to any other wallet you have created. 
When submit is hit in the cryptoChoice.html page, the address and ID are stored in the appropriate database. 
When list is executed, all previously made addresses appear.
The app routes are as follows: "/" , "cryptoChoice.html", "retrieve.html", "list.html"
