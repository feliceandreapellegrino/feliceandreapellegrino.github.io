import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# --- configuration ---
TRANSPARENT_BACKGROUND = True  # set to False for white background
START_YEAR = 2013              # set to None to include all years
BIB_FILE = "../_bibliography/mycollection.bib"

# --- parse BibTeX file ---
with open(BIB_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# --- split into individual entries ---
entries = re.split(r'(?=@\w+\{)', content)
entries = [e.strip() for e in entries if e.strip().startswith('@')]

# --- filter by year ---
if START_YEAR is not None:
    def get_year(entry):
        m = re.search(r'(?<![a-zA-Z])year\s*=\s*\{?(\d{4})\}?', entry, re.IGNORECASE)
        return int(m.group(1)) if m else 0
    entries = [e for e in entries if get_year(e) >= START_YEAR]
    print(f"Entries from {START_YEAR} onwards: {len(entries)}")
else:
    print(f"Total entries: {len(entries)}")

filtered_content = "\n".join(entries)

# --- extract fields ---
def extract_field(content, fieldname):
    """Extract values for an exact BibTeX field name (not substrings like booktitle)."""
    pattern = re.compile(
        r'(?<![a-zA-Z])' + fieldname + r'\s*=\s*\{(.+?)\}(?=\s*[,}])',
        re.IGNORECASE | re.DOTALL
    )
    matches = pattern.findall(content)
    return [re.sub(r'[{}]', '', m).strip() for m in matches]

titles = extract_field(filtered_content, 'title')
abstracts = extract_field(filtered_content, 'abstract')
print(f"Found {len(titles)} titles, {len(abstracts)} abstracts")

texts = {
    "titlesOnly":    " ".join(titles),
    "withAbstracts": " ".join(titles) + " " + " ".join(abstracts),
}

# --- custom stopwords ---
stopwords = set(STOPWORDS)
stopwords.update([
    "using", "based", "via", "approach", "approaches", "method", "methods",
    "technique", "techniques", "state-of-the-art",
    "proposed", "propose", "paper", "work", "results", "show", "shown",
    "present", "presented", "used", "use", "also", "two", "one", "new",
    "well", "case", "cases", "problem", "problems", "framework",
    "experimental", "experiments", "performance", "evaluation", "analysis",
    "different", "provide", "algorithm", "algorithms", "set", "given",
    "task", "tasks", "time", "real", "high", "large", "small", "number",
    "test", "thus", "et", "al", "ieee", "however", "moreover", "whereas",
    "international", "conference", "journal", "proceedings",
    "ability", "able", "aim", "aimed", "applied", "apply", "consider",
    "obtained", "obtain", "ensure", "desired", "achieve", "achieved",
    "order", "first", "second", "third", "addition", "several",
    "specific", "particular", "certain", "known", "unknown",
    "important", "possible", "suitable", "related", "existing",
    "Felice", "Andrea", "Pellegrino", "Salvato", "Erica", "Blanchini",
    "Franco", "Fenu", "Gianfranco", "Medvet", "Eric", "Zullich", "Marco","Free", "controller", "Controller","system","model","models",
    "Giordano", "Giulia",
    "about", "publications", "teaching", "cv", "home",
])

# --- preserve hyphenated/spaced concepts as single tokens ---
compound_terms = {
    "model-free":       "ModelFree",
    "model free":       "ModelFree",
    "data-driven":      "DataDriven",
    "data driven":      "DataDriven",
    "sim-to-real":      "SimToReal",
    "sim to real":      "SimToReal",
    "model-based":      "ModelBased",
    "model-predictive": "ModelPredictive",
    "model predictive": "ModelPredictive",
    "state-of-the-art": None,
    "state of the art": None,
}

for label, text in list(texts.items()):
    for original, replacement in compound_terms.items():
        if replacement:
            text = text.replace(original, replacement)
            text = text.replace(original.title(), replacement)  # handles capitalised versions
    texts[label] = text

# --- generate and save both versions ---
year_suffix = f"_from{START_YEAR}" if START_YEAR is not None else "_allYears"

for label, text in texts.items():
    output_path = f"wordcloud{year_suffix}_{label}.png"
    wc = WordCloud(
        width=1600,
        height=800,
        background_color=None if TRANSPARENT_BACKGROUND else "white",
        mode="RGBA" if TRANSPARENT_BACKGROUND else "RGB",
        stopwords=stopwords,
        max_words=150,
        colormap="viridis",
        prefer_horizontal=0.80,
        min_font_size=10,
        max_font_size=200,
        collocations=True,
    ).generate(text)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(output_path, dpi=150, bbox_inches="tight",
                transparent=TRANSPARENT_BACKGROUND)
    plt.close()
    print(f"Saved to {output_path}")