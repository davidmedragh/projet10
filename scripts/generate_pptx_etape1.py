"""
Script de génération du support de présentation — Étape 1
Projet 10 — Labellisez et appliquez des approches semi-supervisées en traitement d'images

Auteur : David MEDRAGH
Date : Mai 2026

Description :
    Ce script génère un fichier PowerPoint (.pptx) résumant les résultats de
    l'exploration du dataset d'IRM cérébrales réalisée dans le notebook
    projet10_etape1_exploration.ipynb.

    Le template visuel reprend le style du projet 9 (palette bleu profond / or,
    barre de titre numérotée, footer avec logos, KPI cards, séparateurs de section).

Slides produites :
    1. Couverture
    2. Sommaire (3 colonnes : Exploration / Vérification / Bilan)
    3. Séparateur EXPLORATION (avec diagramme de stack technique)
    4. Contexte & Mission
    5. Dataset — Vue d'ensemble (KPI cards)
    6. Écarts entre l'énoncé et le dataset réel (tableau)
    7. Séparateur VÉRIFICATION
    8. Vérification technique — Scan complet (checks + tableau)
    9. Échantillon visuel (grille 3×5 images)
   10. Séparateur BILAN
   11. Synthèse & Prochaines étapes (definition of done)

Dépendances :
    - python-pptx
    - Logos dans doc/logo/ (logo_CurelyticsIA.png, logo_openclassrooms.png)
    - Échantillon visuel dans doc/dataset_preview/ (généré par le notebook)
    - Diagramme stack technique dans doc/png/

Usage :
    uv run python scripts/generate_pptx_etape1.py

Sortie :
    livrables/projet10_etape1_exploration.pptx
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# --- CHEMINS ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "livrables"
OUTPUT_FILE = OUTPUT_DIR / "projet10_etape1_exploration.pptx"
LOGO_CURELYTICSAI = PROJECT_ROOT / "doc" / "logo" / "logo_CurelyticsIA.png"
LOGO_OC = PROJECT_ROOT / "doc" / "logo" / "logo_openclassrooms.png"
ECHANTILLON_PATH = PROJECT_ROOT / "doc" / "dataset_preview" / "echantillon_visuel_etape1.png"
STACK_TECHNIQUE_PATH = PROJECT_ROOT / "doc" / "png" / "stack_technique_slide_etape1.png"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# --- PALETTE (même esprit que projet 9, adaptée médical) ---
BLEU_PROFOND = RGBColor(0x0D, 0x1B, 0x2A)
BLEU_PRINCIPAL = RGBColor(0x1B, 0x3A, 0x5C)
BLEU_ACCENT = RGBColor(0x3A, 0x7C, 0xBD)
OR_ACCENT = RGBColor(0xD4, 0xA0, 0x3C)
BLANC = RGBColor(0xFF, 0xFF, 0xFF)
GRIS_98 = RGBColor(0xFA, 0xFA, 0xFA)
GRIS_TEXTE = RGBColor(0x2D, 0x2D, 0x2D)
GRIS_SUBTITLE = RGBColor(0x6B, 0x6B, 0x6B)
GRIS_FOOTER = RGBColor(0xAA, 0xAA, 0xAA)
GRIS_LIGNE = RGBColor(0xDD, 0xDD, 0xDD)
VERT_OK = RGBColor(0x27, 0xAE, 0x60)
ORANGE_WARN = RGBColor(0xE6, 0x7E, 0x22)


# ──────────────────────────────────────────────
# Helpers (même pattern que projet 9)
# ──────────────────────────────────────────────

def add_rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.fill.solid()
        shape.line.fill.fore_color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape


def add_textbox(slide, left, top, width, height):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    return tf


def set_para(tf, text, size=Pt(14), color=GRIS_TEXTE, bold=False,
             align=PP_ALIGN.LEFT, space_before=Pt(0), space_after=Pt(0), new=False):
    if new:
        p = tf.add_paragraph()
    else:
        p = (tf.paragraphs[0]
             if len(tf.paragraphs) == 1 and tf.paragraphs[0].text == ""
             else tf.add_paragraph())
    run = p.add_run()
    run.text = text
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    p.alignment = align
    p.space_before = space_before
    p.space_after = space_after
    return p


def slide_title_bar(slide, number, title):
    add_rect(slide, 0, 0, SLIDE_W, Inches(1.3), BLEU_PROFOND)
    add_rect(slide, 0, 0, Inches(0.08), Inches(1.3), OR_ACCENT)
    tf = add_textbox(slide, Inches(0.5), Inches(0.25), Inches(0.8), Inches(0.8))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_para(tf, f"{number:02d}", size=Pt(36), color=OR_ACCENT, bold=True)
    add_rect(slide, Inches(1.35), Inches(0.3), Pt(2), Inches(0.7), OR_ACCENT)
    tf = add_textbox(slide, Inches(1.6), Inches(0.25), Inches(10), Inches(0.8))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_para(tf, title, size=Pt(26), color=BLANC, bold=True)


def slide_footer(slide):
    add_rect(slide, 0, Inches(7.1), SLIDE_W, Pt(1), GRIS_LIGNE)
    tf = add_textbox(slide, Inches(0.5), Inches(7.15), Inches(6), Inches(0.3))
    set_para(tf, "CurelyticsIA — Exploration du dataset IRM", size=Pt(9), color=GRIS_FOOTER)
    tf2 = add_textbox(slide, Inches(6.5), Inches(7.15), Inches(2), Inches(0.3))
    set_para(tf2, "Projet 10", size=Pt(9), color=BLEU_ACCENT, bold=True,
             align=PP_ALIGN.CENTER)
    tf3 = add_textbox(slide, Inches(9), Inches(7.15), Inches(3.8), Inches(0.3))
    set_para(tf3, "David Medragh — Data Scientist", size=Pt(9), color=GRIS_FOOTER,
             align=PP_ALIGN.RIGHT)
    logo_h = Inches(0.3)
    if LOGO_OC.exists():
        slide.shapes.add_picture(str(LOGO_OC), Inches(4.8), Inches(7.13), height=logo_h)
    if LOGO_CURELYTICSAI.exists():
        slide.shapes.add_picture(str(LOGO_CURELYTICSAI), Inches(5.5), Inches(7.13), height=logo_h)


def add_content_block(slide, title, bullets, left=Inches(0.8), top=Inches(1.6),
                      width=Inches(5.5)):
    tf = add_textbox(slide, left, top, width, Inches(5))
    set_para(tf, title, size=Pt(16), color=BLEU_PRINCIPAL, bold=True, space_after=Pt(8))
    for bullet in bullets:
        set_para(tf, f"▸  {bullet}", size=Pt(13), color=GRIS_TEXTE, space_before=Pt(5), new=True)
    return tf


def add_kpi_card(slide, left, top, value, label, value_color=BLEU_ACCENT,
                 w=Inches(2.5), h=Inches(1.3)):
    add_rect(slide, left, top, w, h, GRIS_98, GRIS_LIGNE)
    tf = add_textbox(slide, left + Inches(0.15), top + Inches(0.1),
                     w - Inches(0.3), Inches(0.7))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_para(tf, value, size=Pt(28), color=value_color, bold=True, align=PP_ALIGN.CENTER)
    tf2 = add_textbox(slide, left + Inches(0.15), top + Inches(0.75),
                      w - Inches(0.3), Inches(0.5))
    set_para(tf2, label, size=Pt(11), color=GRIS_SUBTITLE, align=PP_ALIGN.CENTER)


def add_check_item(tf, text, ok=True):
    prefix = "✓" if ok else "⚠"
    color = VERT_OK if ok else ORANGE_WARN
    p = tf.add_paragraph()
    run = p.add_run()
    run.text = f"  {prefix}  {text}"
    run.font.size = Pt(14)
    run.font.color.rgb = color
    p.space_before = Pt(6)


def add_table(slide, headers, rows, left=Inches(0.8), top=Inches(1.8), width=Inches(11.5)):
    nb_rows = len(rows) + 1
    nb_cols = len(headers)
    table_shape = slide.shapes.add_table(
        nb_rows, nb_cols, left, top, width, Inches(0.38 * nb_rows))
    table = table_shape.table

    for j, header in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLEU_PROFOND
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.size = Pt(12)
            paragraph.font.bold = True
            paragraph.font.color.rgb = BLANC
            paragraph.font.name = "Calibri"
            paragraph.alignment = PP_ALIGN.CENTER

    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.text = str(val)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BLANC if i % 2 == 0 else GRIS_98
            for paragraph in cell.text_frame.paragraphs:
                paragraph.font.size = Pt(11)
                paragraph.font.color.rgb = GRIS_TEXTE
                paragraph.font.name = "Calibri"
                paragraph.alignment = PP_ALIGN.CENTER


# ──────────────────────────────────────────────
# Construction des slides
# ──────────────────────────────────────────────

def build_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # ═══════ SLIDE 1 — COUVERTURE ═══════
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, BLEU_PROFOND)
    add_rect(s, 0, 0, SLIDE_W, Inches(0.06), OR_ACCENT)
    add_rect(s, 0, Inches(7.44), SLIDE_W, Inches(0.06), OR_ACCENT)

    tf = add_textbox(s, Inches(1.2), Inches(1.8), Inches(10), Inches(1.5))
    set_para(tf, "EXPLORATION DU DATASET", size=Pt(44), color=BLANC, bold=True)
    set_para(tf, "IRM CÉRÉBRALES", size=Pt(44), color=OR_ACCENT, bold=True, new=True)

    add_rect(s, Inches(1.2), Inches(3.8), Inches(3), Pt(3), OR_ACCENT)

    tf2 = add_textbox(s, Inches(1.2), Inches(4.1), Inches(10), Inches(1))
    set_para(tf2, "Étape 1 — Importez les données et explorez le jeu de radiographies",
             size=Pt(20), color=RGBColor(0xBB, 0xBB, 0xBB))
    set_para(tf2, "Projet 10 — Labellisation et approches semi-supervisées",
             size=Pt(15), color=RGBColor(0x88, 0x88, 0x88), new=True, space_before=Pt(6))

    tf3 = add_textbox(s, Inches(1.2), Inches(5.5), Inches(10), Inches(1))
    set_para(tf3, "David MEDRAGH", size=Pt(18), color=BLANC, bold=True)
    set_para(tf3, "Data Scientist — CurelyticsIA", size=Pt(14),
             color=RGBColor(0x88, 0x88, 0x88), new=True, space_before=Pt(4))
    set_para(tf3, "Mai 2026", size=Pt(12),
             color=RGBColor(0x66, 0x66, 0x66), new=True, space_before=Pt(12))

    logo_h = Inches(0.6)
    if LOGO_CURELYTICSAI.exists():
        s.shapes.add_picture(str(LOGO_CURELYTICSAI), Inches(10.5), Inches(6.2), height=logo_h)
    if LOGO_OC.exists():
        s.shapes.add_picture(str(LOGO_OC), Inches(11.8), Inches(6.2), height=logo_h)

    # ═══════ SLIDE 2 — SOMMAIRE ═══════
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, SLIDE_W, Inches(1.3), BLEU_PROFOND)
    add_rect(s, 0, 0, Inches(0.08), Inches(1.3), OR_ACCENT)
    tf = add_textbox(s, Inches(0.5), Inches(0.25), Inches(10), Inches(0.8))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_para(tf, "Sommaire", size=Pt(26), color=BLANC, bold=True)

    sommaire_sections = [
        ("Exploration", "Contexte et dataset", [
            "Contexte & Mission",
            "Dataset — Vue d'ensemble",
            "Écarts entre l'énoncé et le réel",
        ]),
        ("Vérification", "Intégrité technique", [
            "Vérification technique — Scan complet",
            "Échantillon visuel",
        ]),
        ("Bilan", "Résultats et suite", [
            "Synthèse & Prochaines étapes",
        ]),
    ]

    x_positions = [Inches(0.5), Inches(4.8), Inches(9.2)]
    for col, (partie, subtitle, items) in enumerate(sommaire_sections):
        x = x_positions[col]
        y_start = Inches(1.6)
        tf = add_textbox(s, x, y_start, Inches(4), Inches(0.5))
        set_para(tf, partie, size=Pt(18), color=OR_ACCENT, bold=True)
        set_para(tf, subtitle, size=Pt(12), color=GRIS_SUBTITLE, new=True,
                 space_before=Pt(4))
        tf2 = add_textbox(s, x + Inches(0.2), y_start + Inches(0.9), Inches(3.8),
                          Inches(4.5))
        for i, item in enumerate(items):
            set_para(tf2, f"▸  {item}", size=Pt(11), color=GRIS_TEXTE,
                     space_before=Pt(6), new=(i > 0))

    slide_footer(s)

    # ═══════ SLIDE 3 — SÉPARATEUR EXPLORATION ═══════
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, BLEU_PROFOND)
    add_rect(s, 0, 0, SLIDE_W, Inches(0.06), OR_ACCENT)
    tf = add_textbox(s, Inches(1.2), Inches(1.5), Inches(5), Inches(1))
    set_para(tf, "EXPLORATION", size=Pt(44), color=OR_ACCENT, bold=True)
    tf2 = add_textbox(s, Inches(1.2), Inches(2.8), Inches(5), Inches(1))
    set_para(tf2, "Contexte, mission et vue d'ensemble du dataset", size=Pt(24), color=BLANC)
    set_para(tf2, "Inventaire, écarts documentés et caractéristiques techniques",
             size=Pt(14), color=RGBColor(0x88, 0x88, 0x88), new=True, space_before=Pt(12))

    if STACK_TECHNIQUE_PATH.exists():
        s.shapes.add_picture(
            str(STACK_TECHNIQUE_PATH),
            Inches(7.5), Inches(1.2),
            height=Inches(5.5),
        )

    # ═══════ SLIDE 4 — CONTEXTE & MISSION ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 1, "Contexte & Mission")

    add_content_block(s, "CurelyticsIA", [
        "Startup e-santé spécialisée en analyse d'images médicales par IA",
        "Nouveau projet R&D : automatisation de la détection de tumeurs cérébrales",
        "Dataset d'IRM cérébrales collecté auprès de radiologues",
    ], left=Inches(0.8), top=Inches(1.6), width=Inches(5.5))

    add_content_block(s, "Ma mission — Étape 1", [
        "Explorer le dataset et dresser un inventaire technique complet",
        "Vérifier l'intégrité de chaque image (résolution, format, canaux)",
        "Documenter les écarts entre la documentation et le contenu réel",
        "Produire des visualisations représentatives avant modélisation",
    ], left=Inches(7.0), top=Inches(1.6), width=Inches(5.5))

    slide_footer(s)

    # ═══════ SLIDE 3 — DATASET VUE D'ENSEMBLE ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 2, "Dataset — Vue d'ensemble")

    add_kpi_card(s, Inches(0.8), Inches(1.6), "1 506", "Images totales", OR_ACCENT)
    add_kpi_card(s, Inches(3.6), Inches(1.6), "100", "Labellisées (6,6 %)", VERT_OK)
    add_kpi_card(s, Inches(6.4), Inches(1.6), "1 406", "Sans label", BLEU_ACCENT)
    add_kpi_card(s, Inches(9.2), Inches(1.6), "512×512", "Résolution (px)", BLEU_PRINCIPAL)

    add_content_block(s, "Caractéristiques", [
        "Format : JPEG (.jpg) — licence académique libre",
        "Labels : 50 cancer + 50 normal (structure de dossiers)",
        "Mode couleur : RGB (3 canaux) sur toutes les images",
        "Ratio labellisées/total : ~6,6 % → contexte semi-supervisé",
    ], left=Inches(0.8), top=Inches(3.3), width=Inches(5.5))

    add_content_block(s, "Structure du dataset", [
        "avec_labels/cancer/    →  50 IRM avec tumeurs",
        "avec_labels/normal/    →  50 IRM cerveaux sains",
        "sans_label/                 → 1 406 IRM non étiquetées",
    ], left=Inches(7.0), top=Inches(3.3), width=Inches(5.5))

    slide_footer(s)

    # ═══════ SLIDE 4 — ÉCARTS CONSTATÉS ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 3, "Écarts entre l'énoncé et le dataset réel")

    add_table(
        s,
        headers=["Critère", "Énoncé", "Réel", "Commentaire"],
        rows=[
            ["Format", "PNG (courriel)", "JPEG (.jpg)", "Le fichier descriptif confirme le JPEG"],
            ["Images non étiquetées", "1 400", "1 406", "+6 images par rapport à l'annonce"],
            ["Total images", "1 500", "1 506", "Écart cohérent"],
            ["Métadonnées séparées", "Non mentionnées", "Absentes", "Dossiers = labels"],
        ],
        top=Inches(1.8),
    )

    tf = add_textbox(s, Inches(0.8), Inches(4.5), Inches(11), Inches(1))
    set_para(tf, "→  Ces écarts sont mineurs et documentés. Je retiens les chiffres réels (1 506 images) pour la suite.",
             size=Pt(14), color=GRIS_SUBTITLE)

    slide_footer(s)

    # ═══════ SÉPARATEUR VÉRIFICATION ═══════
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, BLEU_PROFOND)
    add_rect(s, 0, 0, SLIDE_W, Inches(0.06), OR_ACCENT)
    tf = add_textbox(s, Inches(1.2), Inches(2.5), Inches(10), Inches(1))
    set_para(tf, "VÉRIFICATION", size=Pt(44), color=OR_ACCENT, bold=True)
    tf2 = add_textbox(s, Inches(1.2), Inches(3.8), Inches(10), Inches(1))
    set_para(tf2, "Intégrité technique du dataset", size=Pt(24), color=BLANC)
    set_para(tf2, "Scan complet, contrôle qualité et échantillon visuel",
             size=Pt(14), color=RGBColor(0x88, 0x88, 0x88), new=True, space_before=Pt(12))

    # ═══════ VÉRIFICATION TECHNIQUE ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 4, "Vérification technique — Scan complet")

    tf = add_textbox(s, Inches(0.8), Inches(1.5), Inches(11), Inches(0.5))
    set_para(tf, "Scan exhaustif des 1 506 images (volumétrie faible → scan complet justifié)",
             size=Pt(14), color=GRIS_SUBTITLE)

    tf2 = add_textbox(s, Inches(0.8), Inches(2.2), Inches(5.5), Inches(4.5))
    set_para(tf2, "Résultats du scan", size=Pt(16), color=BLEU_PRINCIPAL, bold=True,
             space_after=Pt(12))
    add_check_item(tf2, "Toutes les images sont lisibles — aucune corrompue")
    add_check_item(tf2, "Résolution homogène : 512×512 sur tout le dataset")
    add_check_item(tf2, "Format uniformément JPEG")
    add_check_item(tf2, "Mode couleur uniformément RGB (3 canaux)")
    add_check_item(tf2, "Aucun doublon de nom entre les 3 dossiers")

    add_table(
        s,
        headers=["Dossier", "Images", "Dim.", "Mode", "Erreurs"],
        rows=[
            ["cancer", "50", "512×512", "RGB", "0"],
            ["normal", "50", "512×512", "RGB", "0"],
            ["sans_label", "1 406", "512×512", "RGB", "0"],
        ],
        left=Inches(7.0), top=Inches(2.2), width=Inches(5.8),
    )

    slide_footer(s)

    # ═══════ SLIDE 6 — ÉCHANTILLON VISUEL ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 5, "Échantillon visuel — 5 images par catégorie")

    if ECHANTILLON_PATH.exists():
        s.shapes.add_picture(
            str(ECHANTILLON_PATH),
            Inches(1.5), Inches(1.5),
            width=Inches(10.3),
        )
    else:
        tf = add_textbox(s, Inches(2), Inches(3), Inches(9), Inches(1))
        set_para(tf, "⚠  Exécuter le notebook pour générer l'échantillon visuel.",
                 size=Pt(16), color=ORANGE_WARN)

    slide_footer(s)

    # ═══════ SÉPARATEUR BILAN ═══════
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, BLEU_PROFOND)
    add_rect(s, 0, 0, SLIDE_W, Inches(0.06), OR_ACCENT)
    tf = add_textbox(s, Inches(1.2), Inches(2.5), Inches(10), Inches(1))
    set_para(tf, "BILAN", size=Pt(44), color=OR_ACCENT, bold=True)
    tf2 = add_textbox(s, Inches(1.2), Inches(3.8), Inches(10), Inches(1))
    set_para(tf2, "Résultats et prochaines étapes", size=Pt(24), color=BLANC)
    set_para(tf2, "Observations clés, definition of done et préparation de l'étape 2",
             size=Pt(14), color=RGBColor(0x88, 0x88, 0x88), new=True, space_before=Pt(12))

    # ═══════ SYNTHÈSE & PROCHAINES ÉTAPES ═══════
    s = prs.slides.add_slide(blank)
    slide_title_bar(s, 6, "Synthèse & Prochaines étapes")

    add_content_block(s, "Observations clés", [
        "Dataset propre, homogène et exploitable en l'état",
        "Écarts documentés entre l'énoncé et le réel (format, nombre d'images)",
        "Fort déséquilibre : ~6,6 % de labels → justifie l'approche semi-supervisée",
        "Aucune anomalie bloquante identifiée",
    ], left=Inches(0.8), top=Inches(1.6), width=Inches(5.5))

    add_content_block(s, "Prochaines étapes — Étape 2", [
        "Prétraitement : images déjà en RGB, redimensionnement 224×224",
        "Extraction de features via modèle pré-entraîné (ex. ResNet50)",
        "Construction des représentations vectorielles pour le clustering",
    ], left=Inches(7.0), top=Inches(1.6), width=Inches(5.5))

    tf = add_textbox(s, Inches(0.8), Inches(4.5), Inches(11.5), Inches(2.5))
    set_para(tf, "Definition of done — Étape 1", size=Pt(16), color=BLEU_PRINCIPAL, bold=True,
             space_after=Pt(8))
    add_check_item(tf, "Tableau récapitulatif des sous-dossiers et du nombre d'images")
    add_check_item(tf, "Toutes les images lisibles (aucune corrompue)")
    add_check_item(tf, "Résolution, format et canaux vérifiés sur l'intégralité du dataset")
    add_check_item(tf, "Absence de doublons vérifiée entre dossiers")
    add_check_item(tf, "Écarts entre l'énoncé et le dataset réel documentés")
    add_check_item(tf, "Visualisation d'exemples par catégorie (via torchvision)")
    add_check_item(tf, "Observations claires rédigées pour préparer l'étape 2")

    slide_footer(s)

    return prs


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    prs = build_presentation()
    prs.save(str(OUTPUT_FILE))
    print(f"✓ Présentation générée : {OUTPUT_FILE}")
    print(f"  Nombre de slides : {len(prs.slides)}")
