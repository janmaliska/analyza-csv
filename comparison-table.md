# Srovnávací tabulka nástrojů pro statickou analýzu Java kódu

## Rychlé srovnání

| Nástroj | Typ | Licence | Cena | CI/CD Ready | PR Blokování | Security Focus |
|---------|-----|---------|------|-------------|--------------|----------------|
| SonarQube | Platforma | Mixed | Free - €€€ | ⭐⭐⭐⭐⭐ | ✅ Yes | ⭐⭐⭐⭐⭐ |
| Checkstyle | Linter | LGPL | Free | ⭐⭐⭐⭐⭐ | ✅ Yes | ⭐⭐☆☆☆ |
| SpotBugs | Bug Finder | LGPL | Free | ⭐⭐⭐⭐☆ | ✅ Yes | ⭐⭐⭐☆☆ |
| PMD | Analyzer | BSD | Free | ⭐⭐⭐⭐⭐ | ✅ Yes | ⭐⭐⭐☆☆ |
| CodeQL | Security | Proprietary | Free - €€ | ⭐⭐⭐⭐⭐ | ✅ Yes | ⭐⭐⭐⭐⭐ |
| Error Prone | Compiler | Apache 2.0 | Free | ⭐⭐⭐⭐⭐ | ✅ Yes | ⭐⭐☆☆☆ |
| Infer | Verifier | MIT | Free | ⭐⭐⭐☆☆ | ✅ Yes | ⭐⭐⭐⭐☆ |
| SonarLint | IDE Plugin | Proprietary | Free | ⭐☆☆☆☆ | ❌ No | ⭐⭐⭐☆☆ |

---

## Detailní srovnání

### Základní informace

| Nástroj | Verze | Poslední update | Jazyk nástroje | Podporované jazyky | Aktivní vývoj |
|---------|-------|-----------------|----------------|-------------------|---------------|
| SonarQube | 10.x Community | 2024 | Java | 27+ languages | ✅ Velmi aktivní |
| Checkstyle | 10.x | 2024 | Java | Java | ✅ Aktivní |
| SpotBugs | 4.8.x | 2024 | Java | Java, Kotlin, Groovy | ✅ Aktivní |
| PMD | 7.x | 2024 | Java | Java, JS, XML, Apex, +more | ✅ Velmi aktivní |
| CodeQL | 2.x | 2024 | Various | 10+ languages | ✅ Velmi aktivní |
| Error Prone | 2.x | 2024 | Java | Java | ✅ Aktivní |
| Infer | 1.x | 2024 | OCaml | Java, C, C++, Obj-C | ✅ Aktivní |
| SonarLint | 4.x | 2024 | Java | 25+ languages | ✅ Velmi aktivní |

### Ceny a licence

| Nástroj | Community/Free | Paid Tier | Enterprise | Poznámky |
|---------|----------------|-----------|------------|----------|
| SonarQube | ✅ Zdarma | $150/rok | Cena na vyžádání | Community plně funkční, placené přidávají features |
| Checkstyle | ✅ Zdarma | - | - | 100% open source, bez paid tiers |
| SpotBugs | ✅ Zdarma | - | - | 100% open source, bez paid tiers |
| PMD | ✅ Zdarma | - | - | 100% open source, bez paid tiers |
| CodeQL | ✅ Public repos | $21/user/měsíc | Custom | Zdarma pro OSS, placené pro private |
| Error Prone | ✅ Zdarma | - | - | 100% open source, bez paid tiers |
| Infer | ✅ Zdarma | - | - | 100% open source, bez paid tiers |
| SonarLint | ✅ Zdarma | - | - | Zdarma pro všechny, companion k SonarQube |

### Integrace do CI/CD

| Nástroj | Maven | Gradle | Jenkins | GitHub Actions | GitLab CI | Azure DevOps | Bitbucket |
|---------|-------|--------|---------|----------------|-----------|--------------|-----------|
| SonarQube | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Checkstyle | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| SpotBugs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| PMD | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CodeQL | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Error Prone | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Infer | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| SonarLint | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legenda:** ✅ = Nativní/Snadná integrace, ⚠️ = Možné s extra konfigurací, ❌ = Nepodporováno

### Typy analyzovaných problémů

| Nástroj | Code Style | Bugs | Security | Code Smells | Duplicity | Complexity | Coverage |
|---------|-----------|------|----------|-------------|-----------|------------|----------|
| SonarQube | ✅ | ✅ | ✅✅✅ | ✅ | ✅ | ✅ | ✅ |
| Checkstyle | ✅✅✅ | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ |
| SpotBugs | ⚠️ | ✅✅✅ | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| PMD | ✅ | ✅✅ | ⚠️ | ✅✅ | ✅ | ✅ | ❌ |
| CodeQL | ⚠️ | ✅✅ | ✅✅✅ | ✅ | ❌ | ⚠️ | ❌ |
| Error Prone | ✅ | ✅✅ | ⚠️ | ✅ | ❌ | ⚠️ | ❌ |
| Infer | ❌ | ✅✅✅ | ✅✅ | ⚠️ | ❌ | ❌ | ❌ |
| SonarLint | ✅ | ✅ | ✅✅ | ✅ | ❌ | ✅ | ❌ |

**Legenda:** ✅✅✅ = Primární focus, ✅✅ = Silná podpora, ✅ = Základní podpora, ⚠️ = Částečná podpora, ❌ = Nepodporováno

### Možnosti blokování PR

| Nástroj | Build Fail | Quality Gates | Severity Levels | Custom Rules | False Positive Filtering |
|---------|-----------|---------------|-----------------|--------------|-------------------------|
| SonarQube | ✅ | ✅✅✅ | ✅ | ✅ | ✅ |
| Checkstyle | ✅ | ⚠️ | ✅ | ✅✅ | ✅ |
| SpotBugs | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| PMD | ✅ | ⚠️ | ✅ | ✅✅ | ✅ |
| CodeQL | ✅ | ✅✅ | ✅ | ✅✅✅ | ✅ |
| Error Prone | ✅ | ❌ | ✅ | ✅✅ | ✅ |
| Infer | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| SonarLint | ❌ | ❌ | ✅ | ✅ | ✅ |

### Performance a rychlost

| Nástroj | Rychlost analýzy | Memory Usage | Incremental Analysis | Paralelizace | Cache Support |
|---------|------------------|--------------|----------------------|--------------|---------------|
| SonarQube | Střední | Vysoká | ✅ | ✅ | ✅ |
| Checkstyle | Velmi rychlá | Nízká | ⚠️ | ✅ | ⚠️ |
| SpotBugs | Pomalá | Střední | ❌ | ⚠️ | ⚠️ |
| PMD | Velmi rychlá | Nízká | ⚠️ | ✅ | ✅ |
| CodeQL | Pomalá | Vysoká | ✅ | ✅ | ✅ |
| Error Prone | Velmi rychlá | Nízká | ✅ | ✅ | ✅ |
| Infer | Pomalá | Vysoká | ✅ | ✅ | ✅ |
| SonarLint | Rychlá | Střední | ✅ | ✅ | ✅ |

### Dokumentace a podpora

| Nástroj | Oficiální docs | Community Support | Stack Overflow | Tutorials | Example Configs |
|---------|---------------|-------------------|----------------|-----------|-----------------|
| SonarQube | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Checkstyle | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ |
| SpotBugs | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ |
| PMD | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ |
| CodeQL | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |
| Error Prone | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ |
| Infer | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐☆☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ |
| SonarLint | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |

### Report formáty

| Nástroj | HTML | XML | JSON | SARIF | CSV | Console | Dashboard |
|---------|------|-----|------|-------|-----|---------|-----------|
| SonarQube | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅✅✅ |
| Checkstyle | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| SpotBugs | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| PMD | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| CodeQL | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅✅ |
| Error Prone | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Infer | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| SonarLint | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ⚠️ |

---

## Matice případů použití

### Doporučení podle velikosti projektu

| Velikost | Doporučené nástroje | Alternativy |
|----------|---------------------|-------------|
| Malý projekt (1-5 dev) | PMD + Checkstyle | Error Prone, SpotBugs |
| Střední projekt (5-20 dev) | SonarQube Community | CodeQL (GitHub), PMD + SpotBugs |
| Velký projekt (20-100 dev) | SonarQube Developer | SonarQube + CodeQL + Checkstyle |
| Enterprise (100+ dev) | SonarQube Enterprise | SonarQube + CodeQL + Full stack |

### Doporučení podle rozpočtu

| Rozpočet | Doporučené nástroje | Poznámka |
|----------|---------------------|----------|
| €0 | PMD + Checkstyle + SpotBugs | Kompletní open source stack |
| €0 (GitHub) | CodeQL + Error Prone + PMD | Využití GitHub zdarma |
| <€500/rok | SonarCloud Startup | Cloud hosted, jednoduchý setup |
| €500-2000/rok | SonarQube Developer | Branch analysis, více features |
| >€2000/rok | SonarQube Enterprise | Full features, portfolio management |

### Doporučení podle security požadavků

| Security Level | Primární nástroj | Sekundární nástroje |
|----------------|------------------|---------------------|
| Basic | PMD + SpotBugs | Checkstyle |
| Medium | SonarQube Community | CodeQL (public repos) |
| High | CodeQL | SonarQube Developer + Infer |
| Critical | CodeQL + SonarQube Enterprise | Infer + Custom rules |

### Doporučení podle platformy

| Platforma | Ideální nástroje | Poznámka |
|-----------|------------------|----------|
| GitHub | CodeQL + Error Prone | Nativní integrace |
| GitLab | SonarQube + PMD | GitLab CI friendly |
| Bitbucket | SonarQube + Checkstyle | Bitbucket Pipelines |
| Azure DevOps | SonarQube + PMD | Azure Pipelines |
| Jenkins | SonarQube + SpotBugs | Všechny mají Jenkins plugins |

---

## Scoring matice (0-10)

| Kritérium | SonarQube | Checkstyle | SpotBugs | PMD | CodeQL | Error Prone | Infer | SonarLint |
|-----------|-----------|------------|----------|-----|--------|-------------|-------|-----------|
| **Cena (OSS)** | 8 | 10 | 10 | 10 | 8 | 10 | 10 | 10 |
| **CI/CD Integrace** | 10 | 9 | 8 | 9 | 10 | 9 | 7 | 2 |
| **PR Blokování** | 10 | 8 | 8 | 8 | 10 | 8 | 7 | 0 |
| **Security** | 9 | 3 | 6 | 5 | 10 | 4 | 8 | 7 |
| **Bug Detection** | 8 | 4 | 9 | 8 | 8 | 8 | 9 | 7 |
| **Code Style** | 7 | 10 | 3 | 7 | 4 | 7 | 2 | 7 |
| **Performance** | 6 | 9 | 5 | 9 | 4 | 9 | 4 | 8 |
| **Dokumentace** | 10 | 8 | 6 | 9 | 9 | 7 | 7 | 9 |
| **Snadnost Setup** | 6 | 9 | 8 | 9 | 7 | 8 | 5 | 10 |
| **Reporting** | 10 | 6 | 6 | 7 | 9 | 4 | 6 | 4 |
| **Customizace** | 9 | 9 | 7 | 9 | 10 | 8 | 6 | 6 |
| **Community** | 10 | 8 | 7 | 8 | 8 | 7 | 6 | 8 |
| **CELKEM** | **103** | **91** | **83** | **98** | **97** | **89** | **77** | **78** |

---

## Quick Reference Checklist

Před výběrem nástroje odpovězte na tyto otázky:

- [ ] Jaký je náš rozpočet? (€0 / <€500 / >€500)
- [ ] Používáme GitHub? (CodeQL zdarma)
- [ ] Kolik máme vývojářů? (<5 / 5-20 / >20)
- [ ] Jsou security požadavky kritické? (Yes = CodeQL/SonarQube)
- [ ] Chceme centrální dashboard? (Yes = SonarQube)
- [ ] Preferujeme cloud nebo self-hosted? 
- [ ] Jaký CI/CD systém používáme?
- [ ] Máme legacy kód nebo nový projekt?
- [ ] Potřebujeme analýzu více jazyků?
- [ ] Máme kapacitu na údržbu více nástrojů?

**Jednoduchý decision tree:**

```
Máte GitHub?
├─ ANO → Začněte s CodeQL (zdarma pro OSS)
│        ├─ Chcete více? → Přidejte PMD + Checkstyle
│        └─ Enterprise? → SonarQube Developer
│
└─ NE  → Jaký je rozpočet?
         ├─ €0 → PMD + Checkstyle + SpotBugs
         ├─ <€500 → SonarCloud
         └─ >€500 → SonarQube Developer/Enterprise
```
