
import ex25

sentence = "All good things come to those who wait."

words = ex25.break_words(sentence)
print words

sorted_words = ex25.sort_words(words)
print sorted_words

first_word = ex25.print_first_words(sorted_words)
last_word = ex25.print_last_word(sorted_words)

sorted_words_s = ex25.sort_sentence(sentence)
print  sorted_words_s

first_and_last_words = ex25.print_first_and_last(sentence)
first_and_last_sorted = ex25.print_first_and_last_sroted(sentence)
