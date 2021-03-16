#! python3

import pyperclip, re

#Phone number Regex
phoneRegex= re.compile(r'''(
        (\d{3}|\(\d{3}\))?                    #area code
        (\s|-|\.)?                            #separator
        (\d{3})                               #first three numbers
        (\s|-|\.)?                            #separator
        (\d{4})                               #last four numbers
        (\s*(ext|x|ext.)\s*(\d{2,5}))?        #extension
)''',re.VERBOSE)

#Email regex
emailRegex= re.compile(r'''(
        ([a-zA-Z0-9._%+-]+)                   #username
        @                                     #@ sign
        ([a-zA-Z0-9.-)                        #subdomain
        (\.[a-zA-Z]{2,4})                    #top level domain
)''',re.VERBOSE)

#TODO: Find matches in clipboard text.
text= str(pyperclip.paste())



#TODO: Copy results to the clipboard.