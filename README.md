# Analýza CSV - Java Static Analysis Tools Documentation

Tento repozitář obsahuje dokumentaci k nástrojům pro statickou analýzu Java kódu v CI/CD pipeline.

## 📚 Dokumentace

### 1. [Java Static Analysis Tools - Hlavní dokument](java-static-analysis-tools.md)
Kompletní průvodce nástroji pro statickou analýzu Java kódu:
- Detailní popis 8 hlavních nástrojů (SonarQube, Checkstyle, SpotBugs, PMD, CodeQL, Error Prone, Infer, SonarLint)
- Informace o cenách a licencích
- Možnosti integrace do CI/CD
- Mechanismy pro blokování pull requestů
- Výhody a nevýhody každého nástroje
- Doporučení podle velikosti projektu a požadavků

### 2. [Comparison Table - Srovnávací tabulky](comparison-table.md)
Přehledné srovnání nástrojů v tabulkové formě:
- Rychlé srovnání základních parametrů
- Detailní porovnání podle kategorií (cena, integrace, typy analýz, performance)
- Scoring matice (0-10 bodů)
- Doporučení podle use case (velikost projektu, rozpočet, platforma)
- Decision tree pro výběr nástroje
- Quick reference checklist

### 3. [Summary Pros & Cons - Shrnutí výhod a nevýhod](summary-pros-cons.md)
Stručné shrnutí pro rychlé rozhodování:
- Výhody (✅) a nevýhody (❌) každého nástroje
- Ideální use cases pro každý nástroj
- Top volby podle kategorie
- Doporučené kombinace nástrojů
- Implementační strategie (krok za krokem)
- FAQ - odpovědi na časté otázky

## 🎯 Pro koho je tato dokumentace

- **DevOps inženýry** plánující CI/CD pipeline
- **Tech leads** rozhodující o toolingu
- **Vývojáře** hledající nástroje pro code quality
- **Security teams** zaměřené na vulnerability detection
- **Management** potřebující informace o nákladech a ROI

## 🚀 Rychlý start

1. **Chcete rychlé rozhodnutí?** → Začněte s [Summary Pros & Cons](summary-pros-cons.md)
2. **Potřebujete srovnání?** → Podívejte se na [Comparison Table](comparison-table.md)
3. **Chcete detailní informace?** → Přečtěte si [hlavní dokument](java-static-analysis-tools.md)

## 🔍 Pokryté nástroje

| Nástroj | Typ | Licence | Hlavní zaměření |
|---------|-----|---------|-----------------|
| **SonarQube** | Platforma | Mixed | All-in-one quality & security |
| **Checkstyle** | Linter | LGPL (Free) | Code style enforcement |
| **SpotBugs** | Bug Finder | LGPL (Free) | Bug pattern detection |
| **PMD** | Analyzer | BSD (Free) | Code quality & smells |
| **CodeQL** | Security | Proprietary | Security vulnerabilities |
| **Error Prone** | Compiler | Apache 2.0 (Free) | Compile-time checks |
| **Infer** | Verifier | MIT (Free) | Formal verification |
| **SonarLint** | IDE Plugin | Free | Real-time feedback |

## 💡 Klíčová doporučení

### Pro začátečníky:
```
Error Prone + Checkstyle + PMD
(Vše zdarma, snadný setup)
```

### Pro GitHub projekty:
```
CodeQL + Error Prone + PMD
(Využití GitHub Advanced Security)
```

### Pro enterprise:
```
SonarQube Enterprise + CodeQL + Custom rules
(Maximální pokrytí a kontrola)
```

## 📊 Rozhodovací strom

```
Máte GitHub?
├─ ANO → CodeQL (zdarma pro public repos)
│        └─ Doplňte: PMD + Checkstyle
└─ NE  → Jaký rozpočet?
         ├─ €0     → PMD + Checkstyle + SpotBugs
         ├─ <€500  → SonarCloud
         └─ >€500  → SonarQube Developer/Enterprise
```

## 📝 Issue tracking

Tato dokumentace byla vytvořena v reakci na [Issue #3](https://github.com/janmaliska/analyza-csv/issues/3).

## 🤝 Přispívání

Pokud najdete chybu nebo máte návrh na vylepšení, vytvořte prosím issue nebo pull request.

## 📄 Licence

Dokumentace je k dispozici pro volné použití a šíření.

---

**Poslední aktualizace:** Listopad 2024  
**Verze:** 1.0
