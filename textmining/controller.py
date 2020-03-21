import nltk
from textmining.entity import Entity
from textmining.samsung_service import SamsungService
class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = SamsungService()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'
        service.extract_token(entity)
        service.extract_hanguel()
        service.conversion_token()
        service.compound_noun()
        entity.fname = 'stopwords.txt'
        service.extract_stopword(entity)
        service.filtering_text_with_stopword()
        service.frequent_text()
        entity.fname = 'D2Coding.ttf'
        service.draw_wordcloud(entity)

