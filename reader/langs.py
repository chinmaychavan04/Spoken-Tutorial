
def allLang(request,lang):
    if lang == 'Marathi':
        return 'mr'  
    elif lang == 'Hindi':
        return 'hi' 
    elif lang == 'German':
        return 'de'
    else:
        return 'en-us'  
