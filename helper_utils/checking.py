
def check_real(data):

    '''
    check if data exists in DatBase

    Input: data that should be check
    Output: Boolean
    '''

    if len(data) > 0:
        return True
    else:
        False

def check_col(col):

    '''
    check if Collection exists in DatBase

    Input: Collection that should be check
    Output: Boolean
    '''
    if col not in ["users", "group", "messages"]:
        return False
    else:
        return True

def check_args(col, args):

    '''
    check if data has a mandatory parameter in determinated Collection"

    Input: Collection, dictionary
    Output: Boolean

        Params
    -----------------------------------------------------------
        col -> Collection
        args -> params -> dict 

    '''
    #cheks mandatory parameters in users Collections
    if col == "users":
        for user in ["name", "message"]:
            if user not in args.keys():
                return False
            else:
                return True
    #cheks mandatory parameters in group Collections
    elif col == "group":
        for group in ["group", "message"]:
            if group not in args.keys():
                return False
            else:
                return True
    #cheks mandatory parameters in messages Collections
    else: 
        for mes in ["messages"]:
            if mes not in args.keys():
                return False
            else:
                return True