import MeCab
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

import json
import requests

from typing import Tuple, List


CHVE = "sextortion"
url = f"http://localhost:8080/vuln/{CHVE}"

THRESHOLD = 0.2


def extract_words(text: str) -> List[str]:
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(text)

    words: List[str] = []

    while node:
        word_type = node.feature.split(",")[0]
        if word_type in ["名詞"]:
            words.append(node.surface)

        node = node.next

    print(words)
    return words


def get_documents() -> List[str]:
    documents: List[str] = []
    
    response = requests.get(url)
    print(json.loads(response.text))
    cases = json.loads(response.text)

    for web_case in cases["web"]:
        documents.append(web_case["spec"]["raw_body"])

    for mail_case in cases["mail"]:
        documents.append(mail_case["spec"]["body"])

    for other_case in cases["other"]:
        documents.append(other_case["spec"]["payload"])
    
    return documents[:10]


def check(payload: str) -> Tuple[bool, str]:
    documents: List[str] = get_documents()
    documents_for_train = []

    documents_for_train.append(TaggedDocument(words=extract_words(payload), tags=["target"]))

    for idx, doc in enumerate(documents):
        documents_for_train.append(TaggedDocument(words=extract_words(doc), tags=[f"id-{str(idx)}"]))
            
    documents_for_train.append(TaggedDocument(words=extract_words("親譲おやゆずりの無鉄砲むてっぽうで小供の時から損ばかりしている。小学校に居る時分学校の二階から飛び降りて一週間ほど腰こしを抜ぬかした事がある。なぜそんな無闇むやみをしたと聞く人があるかも知れぬ。別段深い理由でもない。"), tags=[f"id-fafa"]))

    model = Doc2Vec(documents=documents_for_train, min_count=1, dm=1)

    for tags, similarity in model.docvecs.most_similar("target"):
        print(similarity)


if __name__ == '__main__':
    check("あなたは私を知らないかもしれませんし、なぜあなたはこの電子メールを受け取っているのだろうと思っていますかこの瞬間、私はあなたのアカウントあなたのメールアドレスをハッキングし、そこからメールを送りました。 私はあなたのデバイスに完全にアクセスできます！今私はあなたのアカウントにアクセスできます！実際に、私は大人ののウェブサイトにマルウェアを置きました。あなたは何を知っていますか、あなたはこのウェブサイトを訪れて楽しんでいました。あなたがビデオクリップを見ている間、インターネットブラウザはRDPとして動作するようになりました。それは私にあなたのスクリーンとウェブカメラへのアクセスを提供するキーロガーを持っています。その直後に、私のソフトウェアプログラムはあなたのメッセンジャー、ソーシャルネットワーク、そして電子メールから連絡先全体を集めました。私は何をしましたか？私は二重スクリーンビデオを作った。 最初の部分はあなたが見ていたビデオを表示しています、2番目の部分はあなたのウェブカメラの記録を示しています。まさにあなたは何をすべきですか？まあ、私は$710が私たちの小さな秘密の公正な価格だと信じています。 あなたはBitcoinによる支払いを行います私のBTC住所英語と数字の羅列（それはcAsEに敏感なので、コピーして貼り付けてください）注意：お支払いを行うには2日以内です。（この電子メールメッセージには特定のピクセルがあり、この瞬間にこの電子メールメッセージを読んだことがわかります。私がBitCoinを手に入れなければ、私は間違いなく、家族や同僚などあなたのすべての連絡先に録画を")