def fileExists(fileName):
    result = True
    try:
        f = open( fileName, r )
    except:
        result = False
    return result
