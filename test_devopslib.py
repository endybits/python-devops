from devopslib.random_chat import get_word, text_list

def test_getword():
    word_choice = get_word()
    print(word_choice)
    text = "This is a text to test the function only for this reason nothing more cheers".lower()

    assert word_choice in text_list

#test_getword()