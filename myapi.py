#Import paralleldots modual
import paralleldots
class API:
    def __init__(self):
        paralleldots.set_api_key("SOlzdN8seEpt9tTwRJ8KgfP3DVZ6jvYemxEihlaQ8Us")

    def sentiment_analysis(self,text):
        respons=paralleldots.sentiment(text)
        return respons


    def name_entity_recognition_api(self,text):
        response=paralleldots.ner(text)
        return response
