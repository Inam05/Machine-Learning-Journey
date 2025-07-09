import nlpcloud

class API:
    def __init__(self):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "a100991391c998fc8f6a7e953bbca960d7965033", gpu=True)

    def sentiment_analysis(self, text, target=None):
        """
        Perform sentiment analysis on the given text.
        If `target` is provided, it will analyze sentiment towards the specific target.
        """
        if target:
            response = self.client.sentiment(text, target=target)
        else:
            response = self.client.sentiment(text)
        return response

    def ner(self, text):
        response = self.client.entities(text)
        return response

    def emotion_prediction(self, text):
        response = self.client.emotion(text)
        return response
