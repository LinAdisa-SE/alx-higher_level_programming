#!/usr/bin/python3

def uppercase(str):

        i = 0

            newstr = ""

                while i != len(str):

                            if ord(str[i]) >= 97 and ord(str[i]) <= 122:

                                            newstr += chr(ord(str[i]) - 32)

                                                    else:

                                                                    newstr += str[i]

                                                                            i += 1

                                                                                print("{}".format(newstr))
