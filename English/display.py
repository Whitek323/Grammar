from src.tense import Tense

subject = input("Enter subject\t")
verb = input("Enter verb\t")
object = input("Enter object\t")


present_tense = Tense()
print_present_simple = present_tense.simple(subject,verb,object)
print_present_continue = present_tense.continuous(subject,verb,object)
print_present_perfect = present_tense.perfect(subject,verb,object)
print_present_perfect_continue = present_tense.perfect_continuous(subject,verb,object)

print("\nPresent Simple : "+print_present_simple)
print("Present Continue : "+print_present_continue)
print("Present Perfect : "+print_present_perfect)
print("Present Perfect Continuuous : "+print_present_perfect_continue)
print("--------")