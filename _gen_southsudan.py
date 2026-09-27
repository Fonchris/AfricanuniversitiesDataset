import json
st = []
pr = []
tr = []

def add(L, name, typ, own, city, web, status):
    d = {"name": name, "abbreviation": "", "type": typ, "ownership": own, "city": city, "website": web}
    if status:
        d["status"] = status
    L.append(d)

# Public universities
add(st, "University of Juba", "University", "Public", "Juba", "https://uoj.edu.ss/", "")
add(st, "Upper Nile University", "University", "Public", "Malakal / Juba / Renk", "https://unu.edu.ss/", "")
add(st, "University of Bahr El-Ghazal", "University", "Public", "Wau", "https://www.ubg.edu.ss/", "")
add(st, "Rumbek University of Science & Technology", "University", "Public", "Rumbek", "https://rust.edu.ss/", "")
add(st, "Dr. John Garang Memorial University of Science & Technology", "University", "Public", "Bor", "", "")
add(st, "University of Aweil", "University", "Public", "Aweil", "", "Renamed/restructured from University of Northern Bahr el Ghazal (2026); transition")
add(st, "University of Kuajok", "University", "Public", "Kuajok", "", "Newly established 2026; operationalisation/accreditation transition")
add(st, "University of Yei", "University", "Public", "Yei", "", "Newly established 2026; operationalisation/accreditation transition")
add(st, "University of Torit", "University", "Public", "Torit", "", "Operationalisation; verify current accreditation")
add(st, "University of Western Equatoria", "University", "Public", "Yambio", "", "Status verify")

# Public specialist / technical HEIs
add(st, "Northern Bahr el Ghazal Polytechnic College for Health Sciences", "Polytechnic", "Public", "Aweil", "", "")
add(st, "Bentiu Technical University College of Petroleum and Gas", "Technical University College", "Public", "Bentiu", "", "")
add(st, "Eastern Equatoria Technical University College for Engineering Sciences", "Technical University College", "Public", "Torit", "", "")
add(st, "Western Equatoria Technical University College for Agriculture Sciences", "Technical University College", "Public", "Yambio", "", "")