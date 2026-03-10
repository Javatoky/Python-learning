number_list = [i ** 2 for i in range(1, 21) if i%3 == 0 ]
print(number_list)

words = ["Hello", "WORLD", "Python", "IS", "Great"]
new_word_list = [word.lower() for word in words if len(word) > 3]
print(new_word_list)

sentence = "hello world hello python world hello"
count_dict = {word : sentence.count(word) for word in sentence.split()}
print(count_dict)

matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transpose_matrix = [[x,y,z] for x,y,z in zip(*matrix)]
print(transpose_matrix)