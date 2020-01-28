import MeCab
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from gensim.models import Word2Vec
from gensim.models.doc2vec import TaggedDocument

import re
import json
import requests

from typing import Tuple, List


CHVE = "profit"
url = f"http://localhost:8080/vuln/{CHVE}"

THRESHOLD = 0.3


def extract_words(text: str) -> List[str]:
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(text)

    words: List[str] = []

    while node:
        word_type = node.feature.split(",")[0]
        if word_type in ["名詞", "動詞-自立", "形容詞"]:
            words.append(node.surface)

        node = node.next

    return words


def get_documents() -> List[str]:
    documents: List[str] = []
    
    response = requests.get(url)
    cases = json.loads(response.text)

    for web_case in cases["web"]:
        documents.append(web_case["spec"]["raw_body"])

    for mail_case in cases["mail"]:
        documents.append(mail_case["spec"]["body"])

    for other_case in cases["other"]:
        documents.append(other_case["spec"]["payload"])
    
    return documents[:10]


def check(summary: str) -> Tuple[bool, str]:
    documents: List[str] = get_documents()

    documents_for_train = []
    documents_for_train.append(TaggedDocument(words=extract_words(summary), tags=["target"]))

    for idx, doc in enumerate(documents):
        documents_for_train.append(TaggedDocument(words=extract_words(doc), tags=[f"id-{str(idx)}"]))
            
    model = Doc2Vec(documents=documents_for_train, min_count=1, dm=1)

    S = 0
    for tags, similarity in model.docvecs.most_similar("target"):
        S += similarity

    if S / 10 > THRESHOLD:
        return (True, str(S / 10))
    else:
        return (False, "")

