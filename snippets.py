import psycopg2
import logging 
import argparse


logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Datbaase connection established.")


#Set the log output file and the log level 
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
   """Store a snippet with an associated name."""
   logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
   cursor = connection.cursor()
   command = "insert into snippets values (%s, %s)"
   cursor.execute(command, (name, snippet))
   connection.commit()
   logging.debug("Snippet stored successfully.")
   return name, snippet

def get(name):
    """Retrieve the snippet with a given name. 
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the snippet.Returns
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest="Command", help="Available Commands")
    
    #subparser for put command 
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put" , help="Store a snippet")
    put_parser.add_argument("name", help="Name of snippet")
    put_parser.add_argument("snippet", help="Snippet text")
    
    arguments = parser.parse_args()
    #convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
            snippet = get(**arguments)
            print("Retrieved snippet: {!r}.".format(snippet))
    
    
if __name__ == "__main__":
    main()  