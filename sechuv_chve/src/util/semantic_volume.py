import re
import MeCab
import numpy as np
from gensim.models import Word2Vec


class SemanticVolume:
    def __init__(self):
        self.available_pos = ["名詞"]
        self.not_available_pos = ["名詞-数"]
        self.tokenizer = MeCab.Tagger("-Ochasen")


        self.model_name = "/project/util/gensim_model/word2vec.gensim.model"
        self.model = Word2Vec.load(self.model_name)
        self.features = self.model.vector_size

        self.original_sentence = []

        self.summarized_sentence = []

    def make_wakati(self, sentence):
        result = []
        chasen_result = self.tokenizer.parse(sentence)
        for line in chasen_result.split("\n"):
            elems = line.split("\t")
            if len(elems) < 4:
                continue
            word = elems[0]
            pos = elems[3]
            if True in [pos.startswith(w) for w in self.not_available_pos]:
                continue
            if True in [pos.startswith(w) for w in self.available_pos]:
                result.append(word)
        return result

    def wordvec2docmentvec(self, sentence):
        docvecs = np.zeros(self.features, dtype="float32")

        denomenator = len(sentence)

        for word in sentence:
            try:
                temp = self.model[word]
            except:
                denomenator -= 1
                continue
            docvecs += temp

        if denomenator > 0:
            docvecs =  docvecs / denomenator

        return docvecs

    def compute_centroid(self, vector_space):
        centroid = np.zeros(self.features, dtype="float32")
        for vec in vector_space:
            centroid += vec
        centroid /= len(vector_space)
        return centroid

    def projection(self, u, b):
        return np.dot(u, b) * b

    def basis_vector(self, v):
        return v / np.linalg.norm(v)

    def span_distance(self, v, span_space):
        proj = np.zeros(self.features, dtype="float32")
        for span_vec in span_space:
            proj += self.projection(v, span_vec)
        return np.linalg.norm(v - proj)

    def compute_farthest_spanspace(self, sentences_vector, span_subspace, skip_keys):
        all_distance = [self.span_distance(vec, span_subspace) for vec in sentences_vector]
        for i in skip_keys:
            all_distance[i] = 0
        farthest_key = all_distance.index(max(all_distance))
        return farthest_key

    def execute(self, input_document, summary_length):
        corpus_vec = []
        sentences = []
        self.summarized_sentence = []

        sentences = input_document.split("。")

        for sent in sentences:
            self.original_sentence.append(sent)
            wakati = self.make_wakati(sent)
            docvec = self.wordvec2docmentvec(wakati)
            corpus_vec.append(docvec)

        summarize_indexes = []

        centroid = self.compute_centroid(corpus_vec)

        adc = [np.linalg.norm(centroid - vec) for vec in corpus_vec]
        first_summarize_index = adc.index(max(adc))
        summarize_indexes.append(first_summarize_index)

        adfss = [np.linalg.norm(corpus_vec[first_summarize_index] - vec) for vec in corpus_vec]
        second_summarize_index = adfss.index(max(adfss))
        summarize_indexes.append(second_summarize_index)

        total_length = len(self.original_sentence[first_summarize_index]) + len(self.original_sentence[second_summarize_index])

        first_basis_vector = self.basis_vector(corpus_vec[second_summarize_index])
        span_subspace = [first_basis_vector]

        while True:
            farthest_index = self.compute_farthest_spanspace(corpus_vec, span_subspace, summarize_indexes)
            if total_length + len(self.original_sentence[farthest_index]) < summary_length:
                span_subspace.append(corpus_vec[farthest_index])
                total_length += len(self.original_sentence[farthest_index])
                summarize_indexes.append(farthest_index)
            else:
                break

        summarize_indexes.sort()
        for idx in summarize_indexes:
            self.summarized_sentence.append(sentences[idx])

        return


def summarize(text: str) -> str:
    text = re.sub(r"《[^》]*》", "", text)
    text = text.replace("\u3000", "")
    text = re.sub(r"\n\n［.*\n\n", "。", text)
    text = re.sub(r"[\n]", "。", text)
    text = re.sub("[。]+", "。", text)

    sv = SemanticVolume()
    sv.execute(text, 200)
    return " ".join(sv.summarized_sentence)