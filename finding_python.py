#!/usr/local/bin/python3
"""Detect any mention of several languages in the user's input."""

uin = input("Please enter a sentence: ")
if "python" in uin.lower():
    print("You mentioned Python.")
elif "perl" in uin.lower():
    print("Aha, a Perl user!  Oh, you're just the best!")
elif "ruby" in uin.lower():
    print("So you use Ruby, then?")
#else:
 #   print("Didn't see Python there.")