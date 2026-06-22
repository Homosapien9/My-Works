"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
        return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(prefixed_words)
    
def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith("i"):
        root = root[:-1] + "y"
    return root

def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index].rstrip(".")
    return word + "en"
