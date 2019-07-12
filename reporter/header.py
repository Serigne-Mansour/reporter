import datetime 
import warnings


def create_header(author_list, place = "Paris"):
    
    """"Creates the header text based on the authors list

    Parameters
    ----------
    author list : a list of dictionnaries
    
    Returns
    ----------
    
    header_text : str
        the header text
        
    Note
    -----
    date is updates at the function execution time
    """
    today = datetime.date.today()
    Lines = [
            today.strftime(f"{place}, le %d/%m/%Y), \n\n ## Auteurs : "),]
    for aut in author_list:
        try:
            first = aut['firstname']
        except KeyError:
            first = ''
            warnings.warn('firstname missing')
        try:
            last = aut['lastname'] = 'XXX'
        except KeyError:
            last = ''
            warnings.warn('lastname missing')
        Lines.append("-" + first  + " " + last )
    return "\n".join(Lines)