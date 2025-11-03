# Analýza nástrojů pro statickou analýzu Java kódu v CI/CD

## Úvod

Tento dokument poskytuje přehled a srovnání hlavních nástrojů pro statickou analýzu Java kódu, které lze integrovat do CI/CD pipeline. Každý nástroj je hodnocen z hlediska možností integrace, schopnosti blokovat pull requesty na základě výsledků analýzy, cenové dostupnosti a praktického využití.

---

## Srovnávací tabulka

| Nástroj | Licence/Cena | Integrace CI/CD | Typy analyzovaných problémů | PR Blokování | Dokumentace |
|---------|--------------|-----------------|------------------------------|--------------|-------------|
| **SonarQube** | Community (zdarma), Developer ($150/rok), Enterprise (na vyžádání) | GitHub Actions, GitLab CI, Jenkins, Azure DevOps, Bitbucket | Bugs, Vulnerabilities, Code Smells, Security Hotspots, Coverage | Ano (Quality Gates) | Výborná, rozsáhlá |
| **Checkstyle** | Open Source (LGPL) - zdarma | Maven, Gradle, Ant, Jenkins, GitHub Actions | Code Style, Formátování, Coding Standards | Ano (přes build fail) | Dobrá, komunita |
| **SpotBugs** | Open Source (LGPL) - zdarma | Maven, Gradle, Ant, Jenkins, GitHub Actions | Bugs, Potenciální chyby, Anti-patterns | Ano (přes build fail) | Dobrá |
| **PMD** | Open Source (BSD) - zdarma | Maven, Gradle, Ant, Jenkins, GitHub Actions | Code Quality, Possible bugs, Dead code, Suboptimal code | Ano (přes build fail) | Velmi dobrá |
| **CodeQL** | Zdarma pro public repos, Enterprise ($21/uživatel/měsíc) | GitHub Advanced Security, GitHub Actions | Security vulnerabilities, Code quality issues | Ano (GitHub native) | Výborná (GitHub) |
| **Error Prone** | Open Source (Apache 2.0) - zdarma | Maven, Gradle, Bazel | Common Java mistakes, Bug patterns | Ano (compile-time check) | Dobrá (Google) |
| **Infer** | Open Source (MIT) - zdarma | Buck, Gradle, Maven, Make | Null pointer, Resource leaks, Concurrency bugs | Ano (přes exit code) | Dobrá (Meta) |
| **SonarLint** | Zdarma (doplněk pro IDE) | IntelliJ IDEA, Eclipse, VS Code | Real-time code analysis, Bugs, Vulnerabilities | Ne (IDE only) | Dobrá |

---

## Detailní popis jednotlivých nástrojů

### 1. SonarQube

**Popis:**
SonarQube je komplexní platforma pro kontinuální inspekci kvality kódu. Podporuje 27+ programovacích jazyků včetně Javy a poskytuje detailní metriky týkající se bezpečnosti, spolehlivosti a udržovatelnosti kódu.

**Verze a ceny:**
- **Community Edition**: Zdarma, základní funkcionalita, podpora 15+ jazyků
- **Developer Edition**: $150/rok, pokročilé funkce, branch analysis
- **Enterprise Edition**: Cena na vyžádání, škálovatelnost, security reports
- **Data Center Edition**: Cena na vyžádání, vysoká dostupnost

**Integrace do CI/CD:**
- Nativní integrace s Jenkins, GitHub Actions, GitLab CI, Azure DevOps, Bitbucket Pipelines
- SonarScanner pro Maven, Gradle, .NET
- REST API pro custom integrace
- Webhooks pro notifikace

**Blokování PR:**
- Quality Gates: definovatelné podmínky pro akceptaci kódu
- Možnost nastavit prahy pro: nové bugy, vulnerabilities, code smells, code coverage, duplicity
- Automatické komentáře v PR s výsledky analýzy
- Integrace s GitHub/GitLab pro status checks

**Výhody:**
- Komplexní řešení "all-in-one"
- Velmi rozsáhlé reporty a dashboardy
- Silná komunita a ekosystém
- Podpora mnoha jazyků
- Historie analýz a trendy v čase
- Pokročilé security analýzy (OWASP Top 10, SANS Top 25)

**Nevýhody:**
- Složitější setup (vyžaduje server/cloud)
- Vyšší nároky na hardware pro self-hosted
- Placené verze pro pokročilé funkce
- Může být přemrštěné pro malé projekty

---

### 2. Checkstyle

**Popis:**
Checkstyle je vývojářský nástroj zaměřený na dodržování coding standards a stylových konvencí v Java kódu. Velmi konfigurovatelný s možností definovat vlastní pravidla.

**Cena:**
- Open Source (LGPL licence) - zcela zdarma

**Integrace do CI/CD:**
- Maven plugin (maven-checkstyle-plugin)
- Gradle plugin
- Ant task
- Jenkins Checkstyle Plugin
- GitHub Actions (checkstyle/checkstyle-github-action)
- Možnost integrace přes XML reporty

**Blokování PR:**
- Lze nastavit failOnViolation pro selhání buildu při porušení pravidel
- Konfigurovatelná severity (error, warning, info)
- GitHub Actions může blokovat merge na základě exit code

**Výhody:**
- Zdarma a open source
- Velmi flexibilní konfigurace
- Široká podpora coding standards (Google, Sun, vlastní)
- Nízké nároky na systém
- Rychlá analýza
- Snadná integrace do build procesu

**Nevýhody:**
- Zaměřeno pouze na styl kódu, ne na logické chyby
- Vyžaduje ruční konfiguraci pravidel
- Méně pokročilé než komerční řešení
- Může generovat mnoho false positives při přísných nastavení

---

### 3. SpotBugs

**Popis:**
SpotBugs (nástupce FindBugs) je nástroj pro detekci bugů v Java bytecode. Analyzuje zkompilovaný kód (.class soubory) a hledá známé bug patterns.

**Cena:**
- Open Source (LGPL licence) - zcela zdarma

**Integrace do CI/CD:**
- Maven plugin (spotbugs-maven-plugin)
- Gradle plugin (com.github.spotbugs)
- Ant task
- Jenkins SpotBugs Plugin
- GitHub Actions
- Podpora pro XML/HTML reporty

**Blokování PR:**
- Možnost nastavit failOnError pro selhání buildu
- Konfigurovatelné thresholdy (high, medium, low priority)
- Exclude/include filtry pro specifické bug patterns

**Výhody:**
- Zdarma a open source
- Analyzuje bytecode (najde i problémy v dependencies)
- Dobré v detekci null pointer exceptions, resource leaks, concurrency issues
- Plugin pro IDE (IntelliJ, Eclipse)
- Široká databáze známých bug patterns

**Nevýhody:**
- Analýza pouze zkompilovaného kódu (ne source code)
- False positives vyžadují ruční review
- Pomalejší než některé konkurenční nástroje
- Konfigurace může být složitá pro větší projekty

---

### 4. PMD

**Popis:**
PMD je source code analyzer, který nachází běžné programovací chyby, dead code, suboptimální kód, overcomplicated expressions a další problémy v kódu.

**Cena:**
- Open Source (BSD-style licence) - zcela zdarma

**Integrace do CI/CD:**
- Maven plugin (maven-pmd-plugin)
- Gradle plugin
- Ant task
- Jenkins PMD Plugin
- GitHub Actions
- Copy/Paste Detector (CPD) pro duplicity

**Blokování PR:**
- Možnost nastavit failOnViolation
- Konfigurovatelné priority (1-5)
- Vlastní rulesets
- Exclude patterns pro ignorování specifických pravidel

**Výhody:**
- Zdarma a open source
- Velmi rychlý (analyzuje source code)
- Podpora více jazyků (Java, JavaScript, XML, Apex, atd.)
- Copy/Paste Detector pro nalezení duplicit
- Dobře dokumentované rulesets
- Aktivní vývoj a komunita

**Nevýhody:**
- Může generovat hodně warningů na legacy kódu
- Některá pravidla jsou subjektivní
- Vyžaduje fine-tuning pro optimální výsledky
- Méně zaměřeno na security než SonarQube nebo CodeQL

---

### 5. CodeQL

**Popis:**
CodeQL je sémantický code analysis engine od GitHubu, který umožňuje psát vlastní queries pro hledání security vulnerabilities a code quality issues. Používá code as data approach.

**Cena:**
- Zdarma pro public GitHub repositories
- GitHub Advanced Security: $21 per active committer/měsíc pro private repos
- Enterprise: custom pricing

**Integrace do CI/CD:**
- Nativní integrace s GitHub Actions
- CodeQL CLI pro local/custom CI systémy
- Podpora pro Jenkins, GitLab CI, Azure DevOps přes CLI
- SARIF output pro standardizované reporty

**Blokování PR:**
- GitHub Code Scanning natively blokuje PR
- Konfigurovatelné severity levels (error, warning, note)
- Možnost definovat vlastní queries pro blokování
- Branch protection rules na GitHub

**Výhody:**
- Velmi pokročilá sémantická analýza
- Silný focus na security vulnerabilities
- Vlastní query language pro custom checks
- Zdarma pro open source projekty
- Excelentní integrace s GitHub ekosystémem
- Databáze CVE a security advisories

**Nevýhody:**
- Drahé pro private repositories
- Primárně designováno pro GitHub
- Strmější learning curve pro custom queries
- Delší čas analýzy než u jednodušších nástrojů
- Limitovanější použití mimo GitHub ekosystém

---

### 6. Error Prone

**Popis:**
Error Prone je static analysis tool od Google, který se integruje přímo do Java kompilátoru. Zachytává běžné programovací chyby během kompilace.

**Cena:**
- Open Source (Apache 2.0 licence) - zcela zdarma

**Integrace do CI/CD:**
- Maven plugin (přes maven-compiler-plugin)
- Gradle plugin
- Bazel native support
- Compile-time check (část build procesu)
- Automatické opravy pomocí Error Prone Auto-Patch

**Blokování PR:**
- Automatické selhání kompilace při chybě
- Konfigurovatelná severity pro jednotlivé checks
- Možnost upgrade warnings na errors
- Custom checks pro projekt-specifické patterns

**Výhody:**
- Zdarma a open source
- Velmi rychlé (compile-time)
- Aktivně používáno v Google
- Automatické opravy pro některé problémy
- Žádné dodatečné kroky v CI/CD (součást kompilace)
- Dobré pro zachycení common mistakes

**Nevýhody:**
- Pouze pro Java
- Vyžaduje úpravu compiler settings
- Menší rozsah než komplexní analyzery
- Ne všechny checks jsou relevantní pro každý projekt
- Méně zaměřeno na security

---

### 7. Infer

**Popis:**
Infer je static analysis tool od Meta (dříve Facebook), který se zaměřuje na detekci null pointer exceptions, resource leaks a concurrency bugs pomocí separation logic a bi-abduction.

**Cena:**
- Open Source (MIT licence) - zcela zdarma

**Integrace do CI/CD:**
- Buck, Gradle, Maven integrace
- Makefile support
- CI plugins pro Jenkins
- GitHub Actions
- Differential analysis (pouze změny)

**Blokování PR:**
- Exit code indikuje nalezené problémy
- Differential mode pro analýzu pouze změn v PR
- JSON output pro custom processing
- Konfigurovatelné thresholdy

**Výhody:**
- Zdarma a open source
- Pokročilá analýza (formal methods)
- Velmi nízký počet false positives
- Differential analysis šetří čas v CI
- Používáno ve velkých projektech (Meta)
- Podpora pro Java, C, C++, Objective-C

**Nevýhody:**
- Pomalejší než základní analyzery
- Složitější setup
- Strmější learning curve
- Menší komunita než u jiných nástrojů
- Dokumentace může být technická

---

### 8. SonarLint

**Popis:**
SonarLint je IDE extension, který poskytuje real-time feedback během psaní kódu. Funguje jako companion k SonarQube/SonarCloud.

**Cena:**
- Zcela zdarma

**Integrace do CI/CD:**
- Není primárně CI/CD nástroj
- Synchronizace s SonarQube/SonarCloud
- Connected mode pro sdílení pravidel a quality profiles
- IDE: IntelliJ IDEA, Eclipse, VS Code, Visual Studio

**Blokování PR:**
- Neumožňuje přímo blokovat PR (IDE tool)
- Prevence problémů před commit
- Instant feedback pro vývojáře

**Výhody:**
- Zdarma pro všechny
- Okamžitá zpětná vazba při psaní kódu
- Integrace s SonarQube pro konzistentní pravidla
- Shift-left approach (najde problémy dříve)
- Podporuje více jazyků
- Snižuje problémy nacházené v CI

**Nevýhody:**
- Ne CI/CD nástroj (IDE only)
- Vyžaduje instalaci v každém IDE
- Nemůže vynucovat compliance
- Závisí na disciplíně vývojářů

---

## Doporučení pro výběr nástroje

### Pro malé projekty / startupy:
1. **Checkstyle** + **SpotBugs** + **PMD** (všechny zdarma)
2. **CodeQL** (pokud používáte GitHub)
3. **Error Prone** jako compile-time check

### Pro střední projekty:
1. **SonarQube Community Edition**
2. **CodeQL** pro security (GitHub)
3. **Checkstyle** + **PMD** jako lightweight alternativa

### Pro enterprise projekty:
1. **SonarQube Enterprise Edition**
2. **CodeQL Advanced Security** (GitHub)
3. **Kombinace**: SonarQube + Checkstyle + SpotBugs pro komplexní pokrytí

### Pro security-critical projekty:
1. **CodeQL**
2. **SonarQube** s security focus
3. **Infer** pro kritické komponenty

---

## Závěrečné shrnutí

### Nejlepší volby podle kritérií:

**Cena/výkon (open source):**
- PMD - nejrychlejší a nejvšestrannější
- Checkstyle - nejlepší pro code style
- SpotBugs - nejlepší pro bug detection

**Komplexnost a funkce:**
- SonarQube - nejkomplexnější řešení
- CodeQL - nejlepší pro security

**Snadnost integrace:**
- Error Prone - automatická integrace do build
- Checkstyle - nejjednodušší setup
- GitHub CodeQL - nativní pro GitHub

**Security zaměření:**
- CodeQL - špička v oboru
- SonarQube - velmi dobré security pravidla
- Infer - specializace na kritické bugy

### Kombinované přístupy:

Pro optimální výsledky lze kombinovat více nástrojů:

1. **Základní set (zdarma):**
   - PMD - code quality
   - SpotBugs - bug detection
   - Checkstyle - code style

2. **GitHub optimalizovaný:**
   - CodeQL - security
   - Error Prone - compile checks
   - PMD - quality

3. **Enterprise set:**
   - SonarQube - centrální platforma
   - Checkstyle - style enforcement
   - CodeQL - security scanning

Volba nástroje závisí na:
- Velikosti týmu a projektu
- Rozpočtu
- Požadavcích na security
- Použité platformě (GitHub, GitLab, Bitbucket)
- Existující infrastruktuře

Všechny zmíněné nástroje lze efektivně integrovat do CI/CD pipeline a nakonfigurovat pro blokování pull requestů na základě definovaných pravidel kvality kódu.
