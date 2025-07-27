import time


def read_csv(n):
    data = []
    try:
        with open("transactions_immobilieres.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
            header = lines[0].strip().split(",")

            for line in lines[1:n+1]:  # Ignore l’en-tête
                value = line.strip().split(",")
                if len(value) == len(header):
                    element = {header[i]: value[i] for i in range(len(header))}
                    data.append(element)

    except FileNotFoundError:
        print("Fichier transactions_immobilieres.csv introuvable.")
    return data

def extract_column(data, column_name):
    columns = []
    for line in data:
        value = line.get(column_name, "")
        try:
            if "." in value:
                value = float(value)
            else:
                value = int(value)
        except ValueError:
            pass
        columns.append(value)
    return columns

def chrono(function, *args):
    starting = time.perf_counter()
    results = function(*args)
    ending = time.perf_counter()
    exec_time = round(ending - starting, 6)
    return results, exec_time