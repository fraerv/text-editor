# text-editor
My solution for Angry Developers' task

This is a simle text editor-like script. What it can do is to suggest words from dictionary by a prefix. The list of suggetions is sorted by frequency (specified in dictionary) or alpabetically (for the words with same frequency).

# Local mode

Local.py script takes no argument while started. It takes a dictionary and requests as it should do and then gives a list of suggestions. If there are no words starting with a prefix, there will be no answer. Same result will be given for incorrect request (empty string instead of a word or request containing spaces).

# Server-Client mode

Server.py script takes a path to dictionary file and the number or the port to serv on as command line arguments.
The dictionary file must be a file with strings of a "word frequency" type lines with no quotes. Any other lines will be ignored.
Port number must be integer from 1025 to 65535.

Client.py script takes an ip address and a port that Server.py is serving on.
Possible requests are "get prefix" lines. Any other requests will be ignored.
If there are no words starting with a prefix, there will be no answer.
