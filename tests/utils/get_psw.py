from operator import indexOf

def get_psw(text: str) -> str:
    """
    Extract the password from a the text 
    Args:
        text (str): the text containing password
    return:
        the password 

    The text should be in this format:

    Password: Apa$$w0rd(newline right after)  

    """
    prefex= "Password: "
    
    # everything after prefex and before \n
    return text[len(prefex): indexOf(text,"\n")] 

