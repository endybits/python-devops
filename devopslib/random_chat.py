from random import choices

text = "This is a text to test the function only for this reason nothing more cheers".lower()
text_list = text.split(' ')
def get_word():
    return choices(text_list)[0]

## make lint
#var = 1
#var = var

# ************* Module devopslib.random_chat
# devopslib/random_chat.py:11:0: W0127: Assigning the same variable 'var' to itself (self-assigning-variable)

# -------------------------------------------------------------------
# Your code has been rated at 8.89/10 (previous run: 10.00/10, -1.11)

# make: *** [lint] Error 4