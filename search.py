import itertools
import sys
import word_garage


args = sys.argv[1]

# word = args



print("<br>")
print("<br>")

aaa = word_garage.apple_class()
word_aaa = aaa.apple(args)

if (word_aaa == "りんご"):
    print("<a href='https://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%B3%E3%82%B4'>" + str(word_aaa) + "</a><br><br>")




bbb = word_garage.jimintou_class()
word_bbb = bbb.jimintou(args)

if (word_bbb == "自民党"):
    print("<a href='https://www.jimin.jp/'>" + str(word_bbb) + "</a><br><br>")
