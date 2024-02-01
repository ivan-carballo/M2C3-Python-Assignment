# Exercise 1
string = "Ivan Carballo Machuca"
number = 5
list = ['Data 1', 'Data 2', 'Data3', 'Data 4']
boolean = True


# Exercise 2
index = string[:3]

# Exercise 3
list_first = list[0]


# Exercise 4
sum = number + 10


# Exercise 5
list_last = list[-1]


# Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')


# Exercise 7
# ACLARACION: Este ejercicio lo puedo hacer de dos formas distintas
# Metodo 1
total_words = string.split(' ')
first_word = total_words[0]
first_word = first_word.upper()
last_words = " ".join(total_words[1:])
new_string = first_word + " " + last_words

# Metodo 2
first_word = string[:4]
first_word = first_word.upper()
new_string = first_word + string[4:]


# Exercise 8
# He usado una variable pero se puede hacer directamente en el print()
sentence = "Use string interpolation to print out a sentence that contains your number variable. " + str(number) 
print(sentence)


# Exercise 9
print("Hello World")
