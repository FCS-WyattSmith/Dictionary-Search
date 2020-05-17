with open("dictionary.txt") as dictionary:
  dictionary_list = dictionary.readlines()
dictionary_search = input("Find words containing ")
search_result = []
count = -1

for word in dictionary_list:
  word = word.lower()
  if word.find(dictionary_search.lower()) != -1:
    search_result.append(word)
if search_result == []:
  print("No words containing \"" + dictionary_search + "\" were found.")
else:
  print("Words containing \"" + dictionary_search + "\":")
  count = -1
  for value in search_result:
    value = value.strip("\n")
    print(value)