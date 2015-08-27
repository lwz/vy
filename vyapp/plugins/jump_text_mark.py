"""

Mode: 1
Event: <Key-1> 
Description: Place the cursor at the beginning of the file.


Mode: 1
Event: <Key-2> 
Description: Place the cursor at the end of the file.

"""

def install(area):
    area.install(('NORMAL', '<Key-1>', lambda event: event.widget.go_text_start()),
                 ('NORMAL', '<Key-2>', lambda event: event.widget.go_text_end()))


