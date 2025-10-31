def nombremots(texte):
    return len(texte.split())  

def occMots(texte):
    freq = {}
    for mot in texte.split():
        freq[mot] = freq.get(mot, 0) + 1
    return freq 

def longueurmoy(text):
    mot = text.split(" ")
    longueur = [len(m) for m in mot]
    moy = sum(longueur)/len(longueur)
    occ = occMots(text)
    occMax = max(occ.values())
    l = [key for key, v in occ.items() if v == occMax]  
    return l, occMax, moy  

def palindromes(text):
    return [mot for mot in text.split() if mot == mot[::-1] and len(mot)>1]  

def max_min_mots(freq):
    mot_max = max(freq, key=freq.get)
    mot_min = min(freq, key=freq.get)
    return mot_max, freq[mot_max], mot_min, freq[mot_min]

with open('data.txt', 'rt', encoding='utf-8') as file:
    data = file.read()

nbmots = nombremots(data)
print(f"Le nombre de mots est : {nbmots}")
print("La fréquence des mots est :", occMots(data))

maxMots, maxOcc, moy = longueurmoy(data)
print(f"Les mots les plus utilises sont : {maxMots} utilise {maxOcc} fois")
print("Longueur moyenne des mots :", moy, "caractères")
print("Palindromes :", palindromes(data))

freq = occMots(data)
motmax, occmax, motmin, occmin = max_min_mots(freq)
print(f"Mot le plus utilisé : '{motmax}' apparait {occmax} fois")
print(f"Mot le moins utilisé : '{motmin}' apparait {occmin} fois")

