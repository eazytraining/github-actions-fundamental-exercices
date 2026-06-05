# GitHub Actions pour DevOps — Repo Apprenants

> **EAZYTraining — Semaine 1 · Labs pratiques**
> Formateur : Aurélie Kamgang

![CI](https://github.com/TON-USERNAME/TON-REPO/actions/workflows/ci.yml/badge.svg)

---

## 🎯 Objectif de la semaine

À la fin de cette semaine, tu seras capable de :
- ✅ Lire et expliquer chaque ligne d'un fichier `ci.yml`
- ✅ Déclencher un pipeline sur `push` et `pull_request`
- ✅ Lire les logs GitHub Actions pour diagnostiquer une erreur
- ✅ Corriger un workflow cassé et le repasser au vert
- ✅ Ouvrir une Pull Request avec un check CI visible

---

## 📁 Structure du projet

```
.
├── app/
│   └── calculatrice.py              # Application Python (4 opérations)
├── tests/
│   └── test_calculatrice.py         # Tests pytest (à compléter)
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── ci.yml                   # Lab 0 & 1 — Workflow principal
│       ├── ci-debug.yml             # Lab 2 — Workflow avec 3 erreurs à corriger
│       └── ci-pr.yml                # Lab 3 — Workflow avec TODO à compléter
└── README.md
```

---

## 🧠 Vocabulaire essentiel

| Terme | Définition |
|-------|-----------|
| **Workflow** | Fichier YAML dans `.github/workflows/` — décrit l'automatisation |
| **Event (`on`)** | Ce qui déclenche le workflow : `push`, `pull_request`, etc. |
| **Job** | Groupe de steps qui s'exécutent sur un même runner |
| **Runner** | Machine virtuelle fournie par GitHub (`ubuntu-latest`) |
| **Step** | Une action ou une commande shell dans un job |
| **`uses`** | Appelle une action GitHub (`actions/checkout@v4`) |
| **`run`** | Exécute une commande shell (`pip install ...`) |

---

## 🚀 Démarrage rapide

### 1. Forker ce dépôt

Clique sur **Fork** en haut à droite sur GitHub, puis clone ton fork :

```bash
git clone https://github.com/TON-USERNAME/TON-REPO.git
cd TON-REPO
```

### 2. Tester en local d'abord

```bash
pip install -r requirements.txt
pytest tests/ -v
```

Tu dois voir quelque chose comme :
```
tests/test_calculatrice.py::test_additionner PASSED
tests/test_calculatrice.py::test_soustraire PASSED
tests/test_calculatrice.py::test_multiplier PASSED
tests/test_calculatrice.py::test_diviser PASSED
tests/test_calculatrice.py::test_division_par_zero PASSED
5 passed in 0.12s
```

### 3. Déclencher ton premier pipeline

```bash
git add .
git commit -m "chore: premier commit - déclenche le pipeline"
git push
```

Puis va dans l'onglet **Actions** de ton dépôt GitHub → observe le run !

---

## 🏋️ Labs

---

### Lab 0 — Observer et comprendre le workflow `ci.yml`

**Durée estimée : 20 min**

**Mission :** lis le fichier `.github/workflows/ci.yml` ligne par ligne et réponds aux questions suivantes dans un fichier `NOTES.md` :

1. Quel est le nom du workflow ?
2. Quels événements le déclenchent ?
3. Sur quel système d'exploitation tourne-t-il ?
4. Combien de steps contient-il ?
5. Quelle commande lance les tests ?

**Preuve attendue :** un fichier `NOTES.md` commité avec tes réponses + une capture de l'onglet Actions montrant le pipeline vert.

---

### Lab 1 — Ajouter tes propres tests

**Durée estimée : 30 min**

**Mission :** ouvre `tests/test_calculatrice.py` et ajoute **au moins 2 nouveaux tests** pour chaque fonction (`additionner`, `soustraire`, `multiplier`, `diviser`).

**Exemple de test :**
```python
def test_additionner_grands_nombres():
    assert additionner(1_000_000, 2_000_000) == 3_000_000
```

**Critères de réussite :**
- [ ] Le pipeline reste vert après ton push
- [ ] Tu vois tes nouveaux tests apparaître dans les logs
- [ ] La couverture de code est à 100 %

**Commande locale pour vérifier :**
```bash
pytest tests/ -v --cov=app --cov-report=term-missing
```

---

### Lab 2 — Déboguer `ci-debug.yml`

**Durée estimée : 30 min**

**Mission :** le fichier `.github/workflows/ci-debug.yml` contient **3 erreurs volontaires**. Trouve-les et corrige-les.

**Méthode de diagnostic :**
1. Pousse le fichier tel quel → observe l'erreur dans l'onglet Actions
2. Lis le **premier message rouge** dans les logs
3. Remonte au step et au job concernés
4. Corrige → recommit → vérifie

**Compte rendu à rédiger dans `NOTES.md` :**

```
Erreur 1 :
  - Localisation : ...
  - Message d'erreur : ...
  - Correction appliquée : ...

Erreur 2 :
  ...

Erreur 3 :
  ...
```

**Preuve attendue :** capture de `ci-debug.yml` en vert dans l'onglet Actions.

---

### Lab 3 — Pull Request avec check CI

**Durée estimée : 30 min**

**Mission :** complète le fichier `.github/workflows/ci-pr.yml` (cherche les `TODO`), puis ouvre une Pull Request pour voir le check CI apparaître dans la PR.

**Étape 1 — Créer une branche**
```bash
git checkout -b feature/lab3-pr-check
```

**Étape 2 — Compléter `ci-pr.yml`**

Les deux TODO à résoudre :
- Ajouter `--junitxml=rapport-tests.xml` à la commande pytest
- Décommenter et compléter le step `upload-artifact`

**Étape 3 — Commiter et pousser**
```bash
git add .github/workflows/ci-pr.yml
git commit -m "feat: complete ci-pr workflow with artifact"
git push -u origin feature/lab3-pr-check
```

**Étape 4 — Ouvrir la Pull Request sur GitHub**

Réponds à ces questions dans la description de la PR :
1. Quel événement a déclenché le workflow dans la PR ?
2. Où trouves-tu le rapport XML téléchargeable ?
3. Que voit un reviewer avant de merger ?

**Preuve attendue :** lien vers ta Pull Request avec le check CI vert.

---

### 🏆 Challenge final — Pipeline propre et documenté

**Durée estimée : 45 min**

**Mission :** crée un nouveau dépôt GitHub personnel avec un projet de ton choix (Python, Node.js, ou autre) et mets en place un pipeline CI complet.

**Critères de validation :**

| Critère | Points |
|---------|--------|
| `.github/workflows/ci.yml` présent et commenté | 2 pts |
| Pipeline vert sur `push` | 2 pts |
| Pipeline vert sur `pull_request` | 2 pts |
| README avec section "CI" expliquant les déclencheurs | 2 pts |
| Tu sais expliquer chaque ligne de ton workflow | 2 pts |
| **BONUS** : badge GitHub Actions dans le README | +1 pt |

**À remettre :**
1. Lien du dépôt GitHub
2. Capture du workflow vert dans l'onglet Actions
3. Court texte (5–10 lignes) expliquant ce que fait ton pipeline

---

## 🔧 Ajouter le badge CI dans ton README

Copie cette ligne dans ton `README.md` en remplaçant `TON-USERNAME` et `TON-REPO` :

```markdown
![CI](https://github.com/TON-USERNAME/TON-REPO/actions/workflows/ci.yml/badge.svg)
```

---

## 🚨 Erreurs fréquentes et solutions

| Erreur | Cause probable | Solution |
|--------|---------------|----------|
| `workflow is not valid` | Indentation YAML incorrecte | Vérifie les espaces (pas de tabulations !) |
| `No such file or directory` | Mauvais chemin dans la commande | Vérifie la structure du dépôt |
| `command not found` | Faute de frappe dans une commande | Relis le step concerné |
| `ModuleNotFoundError` | Dépendances non installées | Vérifie que `pip install -r requirements.txt` est bien là |
| Pipeline ne se déclenche pas | Mauvais déclencheur `on:` | Vérifie la syntaxe de `on: push / pull_request` |

**Règle d'or :** pars toujours du **premier message rouge** dans les logs, puis remonte au step et au job concernés.

---

## 📚 Ressources utiles

- [GitHub Actions — Documentation officielle](https://docs.github.com/en/actions)
- [Syntaxe YAML pour les workflows](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Actions disponibles sur le Marketplace](https://github.com/marketplace?type=actions)
- [Secrets GitHub](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
