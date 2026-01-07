# AI Research Gap Analyzer

An AI-powered system that analyzes academic research papers and identifies
potential future research gaps using NLP, embeddings, and semantic clustering.

## Features
- PDF research paper ingestion
- Text preprocessing & section extraction
- Semantic embeddings using transformers
- Gap detection via topic divergence
- Auto-generated future work suggestions

## Tech Stack
- Python
- PyTorch
- HuggingFace Transformers
- Sentence-BERT
- Scikit-learn

## Usage
```bash
python main.py --input data/raw/paper.pdf
