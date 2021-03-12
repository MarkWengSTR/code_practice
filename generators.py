# def mygenerator():
#     yield 1
#     yield 2
#     yield 'a'


# print(mygenerator())
# g = mygenerator()
# print(next(g))
# print(next(g))
# print(next(g))

# for value in range(100000000):
#     if value == 5000:
#         print("Found it")
#         break

####
# send
####
# def shorten(string_list):
#     length = len(string_list[0])

#     for s in string_list:
#         print(length)
#         length = yield s[:length]


# mystringlist = ['loremipsum', 'dolosit', 'ametfoobar']

# shortstringlist = shorten(mystringlist)

# result = []

# try:
#     s = next(shortstringlist)
#     result.append(s)
#     print(result)
#     while True:
#         number_of_vowels = len(
#             list(filter(lambda letter: letter in 'aeiou', s)))
#         print(number_of_vowels)
#         s = shortstringlist.send(number_of_vowels)
#         result.append(s)
# except StopIteration:
#     pass

# print(result)

######
# gen = (x.upper() for x in ["hello", "world"])
# print(list(gen))

# x = [word.capitalize()
#      for line in ("hello world?", "world!", "or not")
#      for word in line.split()
#      if not word.startswith("or")]
# print(x)
