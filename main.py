from src.pdf_loader import load_pdf
from src.text_preprocessing import preprocess
from src.embedding_model import generate_embeddings
from src.gap_detector import detect_research_gaps

text = load_pdf("data/raw/sample.pdf")
clean_text = preprocess(text)
embeddings = generate_embeddings(clean_text)
gaps = detect_research_gaps(embeddings, None)

print("Identified Research Gaps:", gaps)
