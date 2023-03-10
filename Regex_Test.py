import re

def getAudienceID(str):

    #pattern = r'_d\w{10}-'
    pattern = r'd\w{10}'
    chars_to_remove = "_-"

    match = re.search(pattern, str)
    if match:
        matched_string = match.group()
        new_matched_string = matched_string

        for char in chars_to_remove:
            new_matched_string = new_matched_string.replace(char, "")
    else:
        return ""
    return new_matched_string