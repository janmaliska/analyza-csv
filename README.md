# Analýza CSV - Odhad prodeje náhradních dílů 2026

Tento projekt analyzuje data o neoriginálních náhradních dílech automobilů a odhaduje jejich prodej pro rok 2026.

## Použití

```bash
python3 analyze_csv.py
```

## Vstupní data

Vstupní CSV soubor: `input/Pokus 1177 karet k vyhodnocení.csv`

Obsahuje následující sloupce:
- LKQ code
- IC - konkurenční kód
- Název
- OE (kód originálního dílu)
- Typ auta
- Výskyt registrovaných aut na trhu
- EAN

## Výstup

Výstupní CSV soubor: `output/vyhodnoceni_2026.csv`

Obsahuje všechny původní sloupce plus nový sloupec:
- **Odhad prodeje 2026** - odhadovaný počet prodaných kusů v roce 2026

## Metodika odhadu

Odhad prodeje vychází z následujících faktorů:

1. **Počet registrovaných vozidel na trhu** - základní ukazatel poptávky
2. **Typ značky automobilu**:
   - Luxusní značky (BMW, Mercedes-Benz, Audi, atd.) - nižší prodej neoriginálních dílů (40% podíl)
   - Běžné značky (Škoda, Volkswagen, Ford, atd.) - vyšší prodej neoriginálních dílů (80% podíl)
3. **Míra výměny dílů** - odvozená od velikosti trhu:
   - Malý trh (< 500 aut): 1% roční výměna
   - Střední trh (500-2000 aut): 2% roční výměna
   - Velký trh (2000-5000 aut): 2.5% roční výměna
   - Velmi velký trh (5000-10000 aut): 3% roční výměna
   - Masový trh (> 10000 aut): 3.5% roční výměna

Výsledný odhad = Počet registrovaných aut × Míra výměny × Podíl neoriginálních dílů
