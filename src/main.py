from utilitaires import read_csv, extract_column, chrono
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max

def test_tri(label, tab, algo, nom_algo, unite_op):
    (res, comp, op), temps = chrono(algo, tab)
    line = f"Tri {nom_algo.upper()} par {label.upper()} : {temps}s | {comp} comparaisons | {op} {unite_op}"
    print(line)
    return line

def test_tri_fusion(label, tab):
    (res, comp), temps = chrono(tri_fusion, tab)
    line = f"Tri FUSION par {label.upper()} : {temps}s | {comp} comparaisons"
    print(line)
    return line

def executer_tests_taille(n):
    line = [f"\n=== TRI PAR PRIX ({n} éléments) ==="]
    data = read_csv(n)
    price = extract_column(data, "prix")
    line.append(test_tri("prix", price, tri_selection, "Sélection", "échanges"))
    line.append(test_tri("prix", price, tri_insertion, "Insertion", "décalages"))
    line.append(test_tri_fusion("prix", price))
    line.append(test_tri("prix", price, tri_rapide, "Rapide", "échanges"))

    line.append(f"\n=== TRI PAR SURFACE ({n} éléments) ===")
    surface = extract_column(data, "surface")
    line.append(test_tri("surface", surface, tri_selection, "Sélection", "échanges"))
    line.append(test_tri("surface", surface, tri_insertion, "Insertion", "décalages"))
    line.append(test_tri_fusion("surface", surface))
    line.append(test_tri("surface", surface, tri_rapide, "Rapide", "échanges"))

    return line


def executer_tests_recherche(size):
    lines = [f"\n=== RECHERCHES ({size} éléments) ==="]
    data = read_csv(size)

    # Test A — Maisons à PARIS
    condition_paris_maison = lambda ligne: ligne["type_local"] == "Maison" and ligne["commune"] == "PARIS"
    (resultats_maison, comp1), temps1 = chrono(recherche_lineaire, data, condition_paris_maison)
    lines.append(f"Recherche linéaire MAISONS PARIS : {temps1}s | {comp1} comparaisons | Trouvées: {len(resultats_maison)}")

    # Test B — Recherche binaire sur PRIX == 350000
    price = extract_column(data, "prix")
    price_trie, _, _ = tri_rapide(price)
    (position, comp2), temps2 = chrono(recherche_binaire, price_trie, 350000)
    lines.append(f"Recherche binaire PRIX 350000€ : {temps2}s | {comp2} comparaisons | Position: {position}")

    # Test C — Min/Max PRIX M2
    price_m2 = extract_column(data, "prix_m2")
    (min_m2, max_m2, comp3), temps3 = chrono(recherche_min_max, price_m2)
    lines.append(f"Min/Max PRIX_M2 : {temps3}s | {comp3} comparaisons | Min: {min_m2}€/m² | Max: {max_m2}€/m²")

    # Test D — Appartements 3 pièces
    condition_appart_3p = lambda ligne: ligne["type_local"] == "Appartement" and ligne["nb_pieces"] == "3"
    (resultats_3p, comp4), temps4 = chrono(recherche_lineaire, data, condition_appart_3p)
    lines.append(f"Recherche APPART 3P : {temps4}s | {comp4} comparaisons | Trouvés: {len(resultats_3p)}")

    return lines

if __name__ == "__main__":
    results = []
    for sizes in [100, 500, 1000]:
        results += executer_tests_taille(sizes)
        results += executer_tests_recherche(sizes)

    # Écriture dans resultats.txt
    with open("resultats.txt", "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")
