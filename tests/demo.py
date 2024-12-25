from hrid import HRID

hruuid = HRID()
print(hruuid.generate())

hruuid1 = HRID(':', ('codec', 'adjective', 'noun', 'verb', 'adverb'))
print(hruuid1.generate())

hruuid2 = HRID('-', ('number', 'adjective', 'noun', 'verb', 'adverb'))
print(hruuid2.generate())

hruuid3 = HRID('-', ('number', 'adjective', 'noun', 'verb', 'adverb'), seed='unique')
print(hruuid3.generate())

hruuid4 = HRID(seed='non-unique')
print(hruuid4.generate())

hruuid5 = HRID(seed='non-unique')
print(hruuid5.generate())
