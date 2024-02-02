import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('TuurXJOjGQ8CbjqKVvxeEjtaDPbaQaU4BaaTzN3xzsQ')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response['sentiment']

    def NER_analysis(self, text):
        response = paralleldots.ner(text)
        return response['entities']

    def Abuse_analysis(self, text):
        response = paralleldots.abuse(text)
        return response