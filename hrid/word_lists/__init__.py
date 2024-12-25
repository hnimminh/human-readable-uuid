from hrid.word_lists.adjectives import ADJECTIVES
from hrid.word_lists.adverbs import ADVERBS
from hrid.word_lists.nouns import ANIMALS, FLOWERS, NOUNS
from hrid.word_lists.verbs import VERBS

WORD_LISTS = {
    'adjective': ADJECTIVES,
    'noun': NOUNS,
    'verb': VERBS,
    'adverb': ADVERBS,
    'animal': ANIMALS,
    'flower': FLOWERS,
    'number': [str(number) for number in range(10, 99)],
}
