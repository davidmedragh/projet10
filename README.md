# Projet 10 — Labellisez et appliquez des approches semi-supervisées en traitement d'images

**Auteur :** David MEDRAGH  
**Date :** Mai 2026  
**Durée estimée :** 40 heures

---

## Table des matières

- [Contexte du projet](#contexte-du-projet)
- [Mission](#mission)
  - [Ce que je vais apprendre](#ce-que-je-vais-apprendre)
  - [Pourquoi ces compétences sont importantes](#pourquoi-ces-compétences-sont-importantes)
  - [Contexte métier](#contexte-métier)
  - [Ma mission](#ma-mission)
  - [Organisation pédagogique](#organisation-pédagogique)
    - [Cours suivis](#cours-suivis)
    - [Option choisie](#option-choisie)
    - [Soutenance et autoévaluation](#soutenance-et-autoévaluation)
- [Objectifs pédagogiques](#objectifs-pédagogiques)
- [Livrables](#livrables)
  - [Livrables à déposer](#livrables-à-déposer)
  - [Convention de nommage](#convention-de-nommage)
  - [Soutenance](#soutenance)
- [Dataset](#dataset)
  - [Source et description](#source-et-description)
  - [Structure du dataset](#structure-du-dataset)
  - [Diagramme de structure](#diagramme-de-structure)
  - [Caractéristiques des images](#caractéristiques-des-images)
  - [Écart constaté](#écart-constaté)
  - [Aperçus](#aperçus)
- [Étape 1 — Importez les données et explorez le jeu de radiographies](#étape-1--importez-les-données-et-explorez-le-jeu-de-radiographies)
  - [Résumé de l'exploration](#résumé-de-lexploration)
  - [Écarts identifiés](#écarts-identifiés)
  - [Observations clés](#observations-clés)
  - [Synthèses visuelles](#synthèses-visuelles)
    - [Architecture détaillée de l'étape 1](#architecture-détaillée-de-létape-1)
    - [Stack technique de l'étape 1](#stack-technique-de-létape-1)
  - [Diagrammes UML](#diagrammes-uml)
    - [Architecture de l'étape 1](#architecture-de-létape-1)
    - [Workflow d'exploration](#workflow-dexploration)
    - [Contrôle qualité image par image](#contrôle-qualité-image-par-image)
    - [Cycle de vie d'une image](#cycle-de-vie-dune-image)
    - [Séquence d'inspection](#séquence-dinspection)
    - [Cas d'usage de l'exploration](#cas-dusage-de-lexploration)
  - [Livrables produits](#livrables-produits)
- [Étape 2 — Prétraitez et extrayez les features](#étape-2--prétraitez-et-extrayez-les-features)
- [Étape 3 — Réalisez une analyse non supervisée](#étape-3--réalisez-une-analyse-non-supervisée)
- [Étape 4 — Appliquez une méthode semi-supervisée](#étape-4--appliquez-une-méthode-semi-supervisée)

---

## Contexte du projet

Au fil de mon parcours, j'ai découvert les concepts de traitement d'images, d'analyse non-supervisée et de deep learning dans des contextes complexes. Ce nouveau projet me permet de consolider ces acquis en les appliquant de manière transversale : du prétraitement d'images à l'apprentissage semi-supervisé, en passant par l'extraction de features et le clustering.

Ce README pose le cadre du projet 10. Les sections techniques détaillées seront ajoutées au fur et à mesure des éléments réellement produits.

## Mission

### Ce que je vais apprendre

Dans ce projet, je vais consolider mes compétences en :

- **prétraitement d'images** et extraction de features avec des modèles pré-entraînés ;
- **analyse non-supervisée** : clustering, visualisation de la structure des données ;
- **application d'approches semi-supervisées** ;
- **clarté de présentation** de mes analyses.

Je vais pratiquer l'analyse non-supervisée (comme le clustering) pour détecter des structures dans les images. J'utiliserai des modèles pré-entraînés pour extraire des features visuelles. Je plongerai dans l'apprentissage semi-supervisé, un compromis entre supervision totale et autonomie du modèle. Cette méthode permet de tirer parti de données non labellisées.

### Pourquoi ces compétences sont importantes

Ces compétences sont utiles pour le traitement de données non-structurées comme les images. Elles sont essentielles dans des domaines comme la santé, l'industrie ou la surveillance visuelle. Les pratiques d'apprentissage semi-supervisé sont recherchées par les recruteurs en deep learning et en computer vision.

Savoir prétraiter les données et extraire des représentations pertinentes me permet de concevoir des modèles robustes. Être capable d'interpréter mes résultats est une qualité clé pour tout Data Scientist.

### Contexte métier

Je suis Data Scientist junior spécialisé en Computer Vision au sein de **CurelyticsIA**, une startup innovante dans le domaine de la e-santé. L'entreprise développe des solutions basées sur l'intelligence artificielle pour assister les professionnels de santé dans l'analyse d'images médicales, en particulier des IRM.

Dans le cadre d'un nouveau projet R&D, CurelyticsIA souhaite explorer la possibilité d'automatiser la détection de tumeurs du cerveau. Un ensemble conséquent de radios a été collecté : la majorité de ces images ne dispose d'aucun étiquetage, tandis qu'un sous-ensemble limité a été annoté par des radiologues experts.

### Ma mission

Je suis chargé de concevoir une première exploration analytique du jeu de données. Plus précisément, ma mission est de :

- explorer les images et extraire des caractéristiques visuelles via un modèle pré-entraîné ;
- appliquer des méthodes de clustering pour identifier des structures ou regroupements dans les données ;
- mettre en œuvre une méthode d'apprentissage semi-supervisé à partir des quelques étiquettes disponibles ;
- synthétiser mes résultats, formuler des recommandations, et les présenter à mon équipe projet.

### Organisation pédagogique

#### Cours suivis

Les deux cours associés à ce projet sont :

- "Initiez-vous au deep learning" — pour comprendre les enjeux du traitement d'image et du deep learning ;
- "Initiez-vous à l'apprentissage semi-supervisé" — pour apprendre le traitement d'images.

#### Option choisie

J'ai choisi l'**Option B — Mission fictive** : *Mission d'exploration et de modélisation — Données radios*. J'analyse des images médicales avec des méthodes semi-supervisées, dans un cadre structuré proche d'un cas réel, avec un dataset fourni.

#### Soutenance et autoévaluation

À l'issue du projet, je complète la fiche d'autoévaluation qui sert de base d'échange avec mon mentor avant la soutenance. Je présente ensuite les livrables de la mission à un mentor évaluateur afin de valider les compétences visées.

## Objectifs pédagogiques

À l'issue de ce projet, je dois être capable de :

- identifier ou créer un modèle d'apprentissage adapté aux contraintes et aux besoins métier ;
- préparer et transformer des données afin de les adapter au modèle d'apprentissage.

## Livrables

### Livrables à déposer

| # | Livrable | Format |
|---|---------|--------|
| 1 | Notebook contenant : extraction des features, preprocessing adapté au(x) modèle(s) utilisé(s), analyse non-supervisée, entraînement de modèles de clustering | `.ipynb` |
| 2 | Notebook contenant : approche semi-supervisée | `.ipynb` |
| 3 | Support de présentation | `.pdf` ou `.ppt` (15 slides max) |

### Convention de nommage

Tous les livrables sont déposés dans un dossier zip nommé `Titre_du_projet_nom_prenom`.

Chaque fichier suit le format : `Nom_Prenom_n°_nom_du_livrable_mmaaaa`

- `MEDRAGH_David_1_Notebook_052026`
- `MEDRAGH_David_2_Notebook_052026`
- `MEDRAGH_David_3_Presentation_052026`

### Soutenance

L'évaluateur joue le rôle de **Clara**, responsable Data Science de CurelyticsIA.

| Phase | Durée |
|-------|-------|
| Présentation des livrables (choix méthodologiques, résultats, recommandations) | 15 min |
| Discussion (questions sur les décisions, méthodes et approches) | 10 min |
| Débrief | 5 min |

La présentation doit durer entre 10 et 20 minutes.

## Dataset

### Source et description

Le jeu de données est un ensemble d'IRM cérébrales fourni dans le cadre du projet. Il est décrit dans le fichier `data/mri_dataset_brain_cancer_oc/Jeu de Données d'Images Cérébrales pour la Détection de Tumeurs.txt`. Sa licence autorise une utilisation libre à des fins académiques.

### Structure du dataset

```
data/mri_dataset_brain_cancer_oc/
├── avec_labels/
│   ├── cancer/       → 50 images (IRM avec signes de tumeurs)
│   └── normal/       → 50 images (IRM de cerveaux sains)
└── sans_label/       → 1 406 images (IRM non étiquetées)
```

| Catégorie | Nombre d'images |
|-----------|----------------:|
| Labellisées — cancer | 50 |
| Labellisées — normal | 50 |
| Non labellisées | 1 406 |
| **Total** | **1 506** |

### Diagramme de structure

Le diagramme ci-dessous complète l'arborescence textuelle du dataset. Il représente la structure logique des dossiers et la répartition entre les images labellisées et non labellisées.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_package_structure_dataset.png" alt="Diagramme de structure du dataset" width="100%">
</p>

### Caractéristiques des images

- **Format** : JPEG (`.jpg`)
- **Taille standardisée** : 512 × 512 pixels

### Écart constaté

Le fichier descriptif du dataset annonce **1 400** images non étiquetées et **1 500** images au total. Le contenu réel du dépôt contient **1 406** images non étiquetées, soit un total de **1 506** images. Cet écart de 6 images est documenté ici et sera vérifié lors de l'exploration en étape 1.

### Aperçus

Trois aperçus visuels du dataset sont disponibles dans `doc/dataset_preview/` :

| Aperçu | Fichier |
|--------|--------|
| IRM cancer | `doc/dataset_preview/apercu_cancer.jpg` |
| IRM normal | `doc/dataset_preview/apercu_normal.jpg` |
| IRM sans label | `doc/dataset_preview/apercu_sans_label.jpg` |

## Étape 1 — Importez les données et explorez le jeu de radiographies

### Résumé de l'exploration

J'ai réalisé un scan exhaustif des 1 506 images du dataset. Les résultats sont les suivants :

| Dossier | Images | Dimensions | Mode couleur | Format | Erreurs |
|---------|-------:|------------|--------------|--------|---------|
| cancer | 50 | 512×512 | RGB | JPEG | 0 |
| normal | 50 | 512×512 | RGB | JPEG | 0 |
| sans_label | 1 406 | 512×512 | RGB | JPEG | 0 |
| **Total** | **1 506** | | | | **0** |

- Toutes les images sont lisibles — aucune corrompue
- Résolution homogène sur l'ensemble du dataset
- Mode couleur uniformément RGB (3 canaux)
- Aucun doublon de nom de fichier entre les 3 dossiers

Cette première vue d'ensemble pose le cadre technique de l'exploration et les bibliothèques mobilisées dès l'ouverture du notebook.

<p align="center">
  <img src="doc/png/stack_technique_readme_etape1.png" alt="Vue d ensemble de la stack technique de l etape 1" width="100%">
</p>

### Écarts identifiés

| Critère | Énoncé | Réel | Commentaire |
|---------|--------|------|-------------|
| Format | PNG (courriel de mission) | JPEG (.jpg) | Le fichier descriptif du dataset confirme le JPEG |
| Images non étiquetées | 1 400 | 1 406 | +6 images par rapport à l'annonce |
| Total | 1 500 | 1 506 | Écart cohérent avec le surplus de non étiquetées |
| Métadonnées séparées | Non mentionnées | Absentes | La structure de dossiers fait office de labellisation |

Ces écarts sont mineurs et documentés. Je retiens les chiffres réels pour la suite.

### Observations clés

- Le dataset est propre, homogène et exploitable en l'état
- Le déséquilibre est marqué : seulement 100 images labellisées pour 1 406 non labellisées (~6,6 % de labels) — c'est précisément le contexte qui justifie une approche semi-supervisée
- Toutes les images sont en RGB : pas de conversion de mode nécessaire à l'étape 2
- Les images sont en 512×512, je les redimensionnerai au format attendu par le modèle pré-entraîné (ex. 224×224 pour ResNet50)

### Synthèses visuelles

Deux infographies de synthèse complètent cette étape. Elles donnent une vue plus visuelle du workflow d'exploration et de la stack technique mobilisée autour du notebook, des contrôles qualité et des livrables produits.

#### Architecture détaillée de l'étape 1

Cette vue regroupe, sur une seule infographie, la source de données, l'environnement de travail, l'exploration visuelle, le contrôle qualité, l'analyse des constats et les livrables de l'étape 1.

<p align="center">
  <img src="doc/png/architecture_detaillé_étape1.png" alt="Architecture detaillee de l etape 1" width="100%">
</p>

#### Stack technique de l'étape 1

Cette vue recentre l'attention sur l'environnement du notebook, le traitement d'images, l'écosystème computer vision et les outils de documentation utilisés pendant l'étape 1.

<p align="center">
  <img src="doc/png/stack_technique_notebook_etape1.png" alt="Stack technique centree sur le notebook de l etape 1" width="100%">
</p>

### Diagrammes UML

Pour documenter l'étape 1, j'ai préparé plusieurs diagrammes UML en PlantUML. Ils complètent le notebook d'exploration, explicitent la logique de contrôle qualité et montrent comment les données alimentent les livrables produits.

#### Architecture de l'étape 1

Ce diagramme d'architecture relie le dataset source, le notebook d'exploration, l'échantillon visuel et le support de présentation.

<p align="center">
  <img src="doc/uml/png/architecture_etape1_exploration.png" alt="Architecture et flux de donnees de l'etape 1" width="100%">
</p>

#### Workflow d'exploration

Ce diagramme d'activité synthétise le déroulé global de l'étape 1, depuis l'inventaire du corpus jusqu'à la rédaction des observations qui préparent l'étape 2.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_activite_workflow_exploration.png" alt="Workflow d exploration de l etape 1" width="100%">
</p>

#### Contrôle qualité image par image

Ce diagramme d'activité détaille la vérification appliquée à chaque fichier image : lisibilité, format, dimensions et mode couleur.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_activite_controle_qualite.png" alt="Controle qualite image par image" width="100%">
</p>

#### Cycle de vie d'une image

Ce diagramme d'états montre le passage d'une image de sa détection dans le corpus à sa validation ou à son classement comme anomalie.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_etats_cycle_image.png" alt="Cycle de vie d une image pendant l exploration" width="100%">
</p>

#### Séquence d'inspection

Ce diagramme de séquence représente les interactions entre le notebook, le système de fichiers, PIL, pandas et matplotlib pendant l'inspection du dataset.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_sequence_inspection_dataset.png" alt="Sequence d inspection du dataset" width="100%">
</p>

#### Cas d'usage de l'exploration

Ce diagramme de cas d'usage résume les actions principales réalisées pendant l'étape 1 du point de vue du Data Scientist junior.

<p align="center">
  <img src="doc/uml/png/etape1_diagramme_cas_usage_exploration_dataset.png" alt="Cas d usage de l exploration du dataset" width="100%">
</p>

Cette dernière vue de synthèse replace la stack technique dans une logique de restitution académique, au plus près des livrables de l'étape 1.

<p align="center">
  <img src="doc/png/stack_technique_slide_etape1.png" alt="Stack technique orientee presentation pour l etape 1" width="100%">
</p>

### Livrables produits

| Livrable | Chemin |
|----------|--------|
| Notebook d'exploration | `projet10_etape1_exploration.ipynb` |
| Support de présentation | `livrables/projet10_etape1_exploration.pptx` |
| Échantillon visuel | `doc/dataset_preview/echantillon_visuel_etape1.png` |
| Infographie d'architecture détaillée | `doc/png/architecture_detaillé_étape1.png` |
| Vue d'ensemble de la stack technique | `doc/png/stack_technique_readme_etape1.png` |
| Vue notebook de la stack technique | `doc/png/stack_technique_notebook_etape1.png` |
| Vue présentation de la stack technique | `doc/png/stack_technique_slide_etape1.png` |
| Sources PlantUML | `doc/uml/` |
| Exports PNG des diagrammes | `doc/uml/png/` |

## Étape 2 — Prétraitez et extrayez les features

*À compléter.*

## Étape 3 — Réalisez une analyse non supervisée

*À compléter.*

## Étape 4 — Appliquez une méthode semi-supervisée

*À compléter.*
