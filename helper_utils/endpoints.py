from bson import json_util, ObjectId
from helper_utils.checking import check_real, check_col, check_args
from helper_utils.mongoCon import read_data, insert_data
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords



def get_col(col):
    '''
    Given Collection returns all info contained in mencioned Collection

    Input -> MongoDB Collection
    Returns -> .json
    
        Params
    -----------------------------------------------------------------------
        col --> mongoDB Collection. Must be users, group or messages.
    '''
    #checking
    if not check_col(col):
        return {"Error": "Not a valid Collection. The Collections are: users; group; messages"}
    #find info
    get = read_data(col)
    
    #returns json with the data
    return json_util.dumps(get)

def col_group(col, group):
    '''
    Given Collection and group (str) returns all info contained in mencioned group.

    Input -> Group in a MongoDB Collection
    Returns -> .json
    
        Params
    -----------------------------------------------------------------------
        col --> mongoDB Collection. Must be users, group or messages.
        group --> str. Group 
    '''

    #sets the query
    q = {"group":group}

    #performs the search in MongoDB
    get_group = read_data(col, q)

    #checks if group exists
    if not check_real(get_group):

        #if not exists, returns an error
        return {"Error": "The selected group does not exist"}
        
    #if exists returns a .json with our info.
    return json_util.dumps(get_group)

def col_message(col, message):
    '''
    Given Collection and message (str) returns all info contained in mencioned message.

    Input -> Message in a MongoDB Collection
    Returns -> .json
    
        Params
    -----------------------------------------------------------------------
        col --> mongoDB Collection. Must be users, group or messages.
        message --> str. message 
    '''
    #sets the query
    q = {"message":message}

    #performs the search in MongoDB
    get_mes = read_data(col, q)

    #checks if message exists
    if not check_real(get_mes):
        
        #if not exists returns error
        return {"Error": "The selected message does not exist"}

    #returns .json
    return json_util.dumps(get_mes)

def col_name(col, name):
    q = {"name":name}
    get_name = read_data(col, q)
    if not check_real(get_name):
        return {"Error": "The selected name does not exist"}
    return json_util.dumps(get_name)

def insert_new(col, args):
    if not check_args(col, args):
        return {"Error": "Mandatory parameter is missing"}
    res = insert_data(col, args)
    return json_util.dumps({"_id": res})

def translate_to_english(string):
    the_string = TextBlob(string)
    try:
        english_string=the_string.translate()
        return "".join(list(english_string))
    except:
        return string

def sentimental_words(string):
    stop = set(stopwords.words('english'))
    nueva_lista = []
    lst = string.split(" ")
    
    for stri in lst:
        if stri not in stop:
            nueva_lista.append(stri)
    return " ".join(nueva_lista)  

def sentiment_analisys(string):
    string_en = translate_to_english(string)
    stop_string = sentimental_words(string_en)
    sentiment = TextBlob(stop_string).sentiment
    return json_util.dumps(sentiment)

    
def polarity_analisys(string):
    pol = SentimentIntensityAnalyzer()
    polarity = pol.polarity_scores(string)
    
    return json_util.dumps(polarity)

def sentimental_mean(args):
    sent_list = []
    res = read_data("users", args, project={"_id":0, "message":1})
    for mes in res:
        message = mes["message"]
        pol = SentimentIntensityAnalyzer()
        polarity = pol.polarity_scores(message)
        comp = polarity["compound"] 
        sent_list.append(comp)
    mean = sum(sent_list)/len(sent_list)
    return json_util.dumps(mean)




