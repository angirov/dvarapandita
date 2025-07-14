LANGS = ["skt","tib","pli","chn"]

WINDOWSIZE = {"skt": 12, # higher windowsize means better tolerance for diverging passages
              "tib": 17,
              "chn": 12,
              "pli": 12,
              "eng": 0 }

THRESHOLD = {"skt": 0.3,
              "tib": 0.6, # better embeddings = higher threshold values possible 
              "chn": 0.3,
              "pli": 0.5,
              "eng": 0.45 }

BIGGER_IS_BETTER = {"skt": False,
                "tib": False,  
                "chn": False,
                "pli": False,
                "eng": False }

# we need two parameters for min_length mainly since for Tibetan, there are two scenarios: single verse-padas (min length 7) and prose matches (min length 12)
MIN_LENGTH = {"skt": 20, # war mal 25
              "tib": 151, # you want longer min. length for tibetan to avoid noise 
              "chn": 50,
              "pli": 70,
              "eng": 10 }

ABSOLUTE_MIN_LENGTH = {"skt": 20, # war mal 25
              "tib": 7,
              "chn": 5,
              "pli": 30,
              "eng": 10 }


QUERY_DEPTH = 500 
MIN_DISTANCE = 500 # min. distance between the query token and the target token, in order to avoid that queries match with themselves 
TEXT_CHUNKSIZE=2000

MAX_SEQ_LENGTH = {"tib": 50,
                  "chn": 20,
                  "skt": 60,
                  }


STOPWORDS_PATH = "ref/"
VECTOR_PATH = "ref/"

PUNC = "　 ！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏./.|*_-"

LIST_OF_PP_CATEGORIES = ["K02","K03","K04","K05","K06","K07","T03"]

TIBETAN_STEMFILE="ref/verbinator_tabfile.txt"

EF_CONSTRUCTION = 100 # precision of the HNSW index, higher value = better precision, more computing time; 40 is a good tradeoff between speed and precision

SKT_STEMMER_LOCATION="/mnt/code/skt-tagger-ctranslate/"
