import re
import mysql.connector
from difflib import get_close_matches

def connect_to_database():
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database")
    return con

def search_for_word(query, con):
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def translate(word, con):
    query = "SELECT * FROM Dictionary WHERE Expression = '%s'" % word
    results = search_for_word(query, con)
    # unlike in previous example mysql query for a word are case insensitive
    # so we don't need to check for lower, upper and title
    if results:
        return [ result[1] for result in results]
    else:
        # gather all the dictionary words and find the close matches
        query = "SELECT * FROM Dictionary"
        results = search_for_word(query, con)
        list_to_be_compared = [val[0] for val in results]

        if len(get_close_matches(word, list_to_be_compared, n = 3, cutoff = 0.8)) > 0:
            yn = input("Did you mean %s instead? ( Y/N ): " % get_close_matches(word, list_to_be_compared, n = 3, cutoff = 0.8)[0] )
            if yn.upper()[0] == 'Y':
                suggested_word = get_close_matches(word, list_to_be_compared, n = 3, cutoff = 0.8)[0]
                query = "SELECT * FROM Dictionary WHERE Expression = '%s'" % suggested_word
                results = search_for_word(query, con)
                return [ result[1] for result in results]
            elif yn.upper()[0] == 'N':
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
con = connect_to_database()
output = translate(word, con)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)