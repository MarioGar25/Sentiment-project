# “It's leviOsa, not levioSA!”
## Sentimental Evaluator API
![Harry Potter](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/harry-potter-scar-1547798790.png?crop=1.00xw:0.756xh;0,0.115xh&resize=1200:*)

## Introduction

Emotions are part of our daily life. They bathe our thoughts, opinions, behaviors, perception, in short, they play a very important role in our lives. Of course, when it comes to communicating, it becomes evident that we not only convey a message, but that message carries connotations about how we feel. In this API, we are going to evaluate through the words used the degree of positivity or negativity of a sentence.
For this, we have a Harry Potter dataframe, in which we will be able to see the emotions of the characters through their words.

So, Alohomora!
## Objetive
The objective of the project is to create an API from scratch, creating different endpoints that provide different information. The idea is to be able to store, share and create new information about different conversations, and then be able to analyze them sentimentally.
In this case, I have used the database of the movie "Harry Potter and the Philosopher's Stone" since it is a movie that I like very much. 
But you can add any other type of user, group or message.

## Structure
· apy.py -> connects to the API and provides you with the endpoints.

· endpoints.py -> contains the functions that provide action to endpoints.

· mongoCon -> connects to MongoDB, and performs read and insert functions.

· checking.py -> contains checking functions to verify that searches are performed correctly.

## Database

The dataframe has been obtained from the following [url](https://www.kaggle.com/eward96/harry-potter-and-the-philosophers-stone-script)

The database is designed in MongoDB. And it is structured with three Collections (users, messages, group), each one has three fields (name, group, message), only the mandatory parameters are different, therefore, it is not necessary to add all the information in each Collection, so if you don't have a field, you can add it in the Collection in which that field is not a mandatory.

## Endpoints

· "/" -> Welcome

· "/< col >" -> Select all the info from a Collection.

· "/< col >/showbygroup/< group >) -> Select group info from a collection. 

· "/< col >/showbyname/< name >) -> Select user info from a collection.

· "/< col >/showbymessage/< message >) -> Select message info from a collection.

· "/< col >/insert) -> Inserts new data set in the parameters to a given collection.

· "/sentimentalAnalisys/< string >" -> Performs a sentimental analysis of a given string.

· "/polarityAnalisys/< string >" -> Performs a sentimental analysis of a given string.

· "/sentimentalAnalisys/mean" -> Performs the average of a sentimental analysis of a user performed on the total of his interventions or on a given group.




