import Levenshtein

with open("top100000.txt") as fhdl:
    domains = fhdl.read().split("\n")[:-1]

def check(target):
    results = []

    for domain in domains:
        lev = 1 - (Levenshtein.distance(target, domain) / max(len(target), len(domain)))
        jw = Levenshtein.jaro_winkler(target, domain)

        results.append({
            "domain": domain,
            "lev": lev,
            "jw": jw,
            "score": lev * jw
        })
    
    return results

def main():
    while True:
        target = input("Check >> ")

        if target == "":
            break

        results = sorted(check(target), key=lambda result: result["score"], reverse=True)[:5]

        for result in results:
            print(result["domain"], result["score"])
        
        if results[0]["score"] == 1:
            print("{}は正規のサイトです．".format(target))
        else:
            print("{}というサイトのフェイクかもしれません．".format(results[0]["domain"]))

main()