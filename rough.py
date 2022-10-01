import nltk
from PdfFetcher import PdfFetcher
from listOfSkills import skillsList as SKILLS_DB

# print(nltk)
 
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

print('yes')

# def extract_names(txt):
#     person_names = []
 
#     for sent in nltk.sent_tokenize(txt):
#         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#             if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
#                 person_names.append(
#                     ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
#                 )
 
#     return person_names

# nltk.download('stopwords')

# SKILLS_DB = [
#     'machine learning',
#     'data science',
#     'python',
#     'word',
#     'excel',
#     'English',
# ]

# def extract_skills(input_text):
#     stop_words = set(nltk.corpus.stopwords.words('english'))
#     word_tokens = nltk.tokenize.word_tokenize(input_text)
#     filtered_tokens = [w for w in word_tokens if w not in stop_words]
#     filtered_tokens = [w for w in word_tokens if w.isalpha()]
#     bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
#     found_skills = set()
#     for token in filtered_tokens:
#         if token.lower() in SKILLS_DB:
#             found_skills.add(token)
#     for ngram in bigrams_trigrams:
#         if ngram.lower() in SKILLS_DB:
#             found_skills.add(ngram)
 
#     return found_skills

RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]
def extract_education(input_text):
    organizations = []
 
    # first get all the organization names using nltk
    for sent in nltk.sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))
 
    # we search for each bigram and trigram for reserved words
    # (college, university etc...)
    education = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) >= 0:
                education.add(org)
 

a = PdfFetcher('./PriyanshuSinhaResumev1.4.pdf').getStr()
c = nltk.word_tokenize(a)
print(c)
# b = extract_education(a)
# print(b)