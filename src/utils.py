import os
import requests

def descompress_data(zip, folder):
    '''
    This function descompress a .csv file. And drop de .zip
    Input: File .zip
    Output: File.csv (.zip deleted)

        Params
    -----------------------------------------
        zip --> File .zip
        folder --> Target folder 
    '''
    #take csv.file name
    csv_file = zip.split(".")[0]

    #descompress .zip
    descompress_zip = f"unzip {zip}"
    print("Descompressing files")
    
    #remove .zip 
    remove_zip = f"rm -rf {zip}"
    print ("removing .zip")

    #realize before actions
    for i in [descompress_zip, remove_zip]:
        os.system(i)
    
    #move file to folder
    move_csv = f"mv {csv_file}.csv {folder}/{csv_file}.csv"
    os.system(move_csv)
    return f"Your file is descompressed. Great!!"


def gets_groups(name):
    '''
    Gets the groups where you find a name
    Input: string
    Output: list 
        
        Params
    -----------------------------------------
        name --> name we want to know the groups it belongs to  
    '''
    #calls the API
    res = requests.get(f"http://127.0.0.1:5000/users/showbyname/{name}").json()
    #creates a list
    groups = []
    #gets list from sorted groups
    for gr in res:
        groups.append(gr.get("group"))
    try:
        sorted_groups = sorted([int(sort) for sort in list(set(groups))])
        return sorted_groups
    except:
        return groups

def sentimental_analisys_user(group_lst, name):
    '''
    Gets a list of means from sentimental analisys about a user in all its groups.
    Input: array, string
    Output: array 
        
        Params
    -----------------------------------------
        group_lst --> array with the groups
        name --> name we want to know the groups it belongs to  
    '''

    #create a list
    sentimental = []
    #takes sentimental list from user in each group
    for number in group_lst:
        parameters = {"name":f"{name}", "group": str(number)}
        sent = requests.get("http://127.0.0.1:5000/sentimentalAnalisys/mean", params=parameters).json()
        sentimental.append(sent)
    #returns list
    return sentimental