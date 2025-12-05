# FAISS Vector Index

This directory should contain FAISS indices for semantic search of community posts.

## Generation Instructions

The large FAISS index files (*.index, *.zip) are excluded from git due to their size. To generate them locally, run the following code:

```python
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np
import os

# Load model
model = SentenceTransformer("intfloat/multilingual-e5-small", device='cuda')

# Load community data
fm_df = pd.read_csv('../community_samples/fm_sample_50000.csv')
mlb_df = pd.read_csv('../community_samples/mlb_sample_50000.csv')
pp_df = pd.read_csv('../community_samples/pp_sample_50000.csv')

# For each community
for community_name, df in [('fm', fm_df), ('mlb', mlb_df), ('pp', pp_df)]:
    print(f"Processing {community_name}...")

    # Generate embeddings
    texts = df['Text'].tolist()
    embeddings = model.encode(
        [f"passage: {text}" for text in texts],
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True
    ).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product (cosine similarity)
    index.add(embeddings)

    # Save
    output_path = f'{community_name}_embeddings_faiss_50000.index'
    faiss.write_index(index, output_path)
    print(f"Created {output_path} with {index.ntotal} vectors")
```

## Required Files

After generation, you should have:
- `fm_embeddings_faiss_50000.index`
- `mlb_embeddings_faiss_50000.index`
- `pp_embeddings_faiss_50000.index`

## Alternative: CPU-only Generation

If you don't have GPU access, change `device='cuda'` to `device='cpu'`. The generation will take longer but will work on any machine.
