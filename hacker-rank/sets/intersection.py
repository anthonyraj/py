n = input()
subscribesForEng = set(map(int,raw_input().split()))

m = input()
subscribesForFrench = set(map(int,raw_input().split()))

print subscribesForEng.intersection(subscribesForFrench)
