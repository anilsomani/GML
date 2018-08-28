from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(text):
    client = language.LanguageServiceClient()
    document = types.Document(content=text,
		type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document).document_sentiment

    entities = client.analyze_entities(document).entities

    return sentiment, entities

# entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
               'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

example_text = 'I am quite happy and delighted to see World Health Organization\'s mission of attainment by all people the highest possible level of health'
print(example_text)
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, entity_type[e.type], e.metadata, e.salience)

print('\n-------------------------------\n')

example_text = 'I am very dissapointed about Elon Musk violating SEC rules by tweeting about taking Tesla private'
print(example_text)
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, entity_type[e.type], e.metadata, e.salience)

