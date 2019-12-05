import sys
import Levenshtein
import pickle
from urllib.parse import urlparse

from typing import List, Tuple

g = {}


def check_typosquatting(longest_section: str) -> str:
    TYPOSQUATTING_THRESHOLD: float = 0.7

    tmp_max_longest_section: str = ""
    tmp_max_score: float = -1.0
    tmp_max_index: int = -1

    for i, top_longst_section in enumerate(g["top_longest_sections"]):
        lev: float = 1 - (Levenshtein.distance(longest_section, top_longst_section) / max(len(longest_section), len(top_longst_section)))
        jw: float = Levenshtein.jaro_winkler(longest_section, top_longst_section)
        score: float = lev * jw

        if score > tmp_max_score:
            tmp_max_score = score
            tmp_max_longest_section = top_longst_section
            tmp_max_index = i

    if tmp_max_score >= TYPOSQUATTING_THRESHOLD:
        return g["top_domains"][tmp_max_index]
    else:
        return ""


def check_combosquatting(longest_section: str) -> str:
    if "-" not in longest_section:
        return ""

    while True:
        if "-" not in longest_section:
            break

        left, right = longest_section[:longest_section.index("-")], longest_section[longest_section.index("-")+1:]
        longest_section = left if len(left) >= len(right) else right

    if longest_section in g["top_longest_sections"]:
        return g["top_domains"][g["top_longest_sections"].index(longest_section)]
    else:
        return ""


def parse_url_to_longest_section(url: str) -> str:
    """
    URLからドメインリストと照合するための部分文字列群を取得する．
    e.g. http://www.foobar.com/baz?qux=qux -> (foobar, foobar.com)
    """

    netloc: str = urlparse(url).netloc
    splitted_netloc: List[str] = netloc.split(".")
    longest_section_index: int = splitted_netloc.index(sorted(splitted_netloc, key=lambda e: len(e), reverse=True)[0])

    return splitted_netloc[longest_section_index], ".".join(splitted_netloc[longest_section_index:])



def check(url: str) -> Tuple[bool, str]:
    global g

    with open("/project/engine/data/top_domains.pickle", "rb") as f:
        g["top_domains"] = pickle.load(f)
    with open("/project/engine/data/top_longest_sections.pickle", "rb") as f:
        g["top_longest_sections"] = pickle.load(f)

    longest_section, domain_after_longest_section = parse_url_to_longest_section(url)

    if domain_after_longest_section in g["top_domains"]:
        return False, ""

    typosquatting_domain: str = check_typosquatting(longest_section)
    combosquatting_domain: str = check_combosquatting(longest_section)

    if typosquatting_domain == "" and combosquatting_domain == "":
        return False, ""
    else:
        return True, "Typosquatting:{} Combosquatting:{}".format(typosquatting_domain, combosquatting_domain)


if __name__ == '__main__':
    print(check(sys.argv[1]))