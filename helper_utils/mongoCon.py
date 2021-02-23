from pymongo import MongoClient

#connects to client
client = MongoClient()

#default database
SentiAPI = client.SentiAPI

def insert_data(coll, data, client=client):
    '''
    It receives some data, a collection and a database and inserts it into selected MongoDB database.  
    
    Input: A collection, a dictionary and a client
    Return: ObjectID 

        Params
    ------------------------------------------------------------------------------
        coll --> MongoDB Collection
        data --> Dictionary with the data to be entered in the database. 
                keys --> MongoDB fields (string)
                values --> data (string)
        client --> MongoDB client. default = client
    '''
    
    #inserts data in database collection
    res = SentiAPI[coll].insert_one(data)
    #returns id
    return res.inserted_id


def read_data(coll, query={}, client=client, project=None):
    '''
    It receives a query, MongoDB collection, MongoDB database and project, 
    and performs a search in the selected database collection.

    Input: MongoDB Collection, a dictionary with the search, MongoDB database, a dictionary with the filter.
    Return: List with the selected search in the collection of the database

        Params
    ----------------------------------------------------------------------------------
        coll --> MongoDB Collection
        query --> Dictionary with the query. default = empty diccionary (show all Collection's data)
                keys --> MongoDB fields (string)
                values --> what looking for (string)
        client --> MongoDB database. default = SentimentApi
        project --> Dictionary with what field want to show. default=None (show all fields)
                keys --> MongoDB fields (string)
                values --> 0 = not show; 1 = show (integer)
    '''
        
    #the search in the Collection
    quer = SentiAPI[coll].find(query,project)
    #return list with the query's results
    return list(quer)


