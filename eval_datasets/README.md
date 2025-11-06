# RAG Evaluation Datasets

This directory contains ground truth evaluation datasets for measuring RAG system performance.

## clockify_v1.jsonl

**Status**: ✅ Populated with title/section relevance labels
**Questions**: 20
**Format**: JSONL (one JSON object per line)

### Format

```json
{
  "query": "User question text",
  "relevant_chunks": [
    {"title": "[ARTICLE] Track your time - Clockify Help", "section": "## Chunk 5"},
    {"title": "[ARTICLE] Track your time - Clockify Help", "section": "## Chunk 4"}
  ],
  "difficulty": "easy|medium|hard",
  "tags": ["tag1", "tag2"],
  "language": "en",
  "notes": "Optional notes about expected chunks"
}
```

### Fields

- `query`: The user's question (required)
- `relevant_chunks`: List of chunk metadata objects with the article `title` and `section`
  strings produced by the chunker. Multiple matches are allowed when the same
  article-section pair appears more than once (e.g., overlapping chunks).
- `difficulty`: Question difficulty level (easy/medium/hard)
- `tags`: Categorization tags for analysis
- `language`: Query language code (ISO 639-1)
- `notes`: Helper notes for manual chunk ID identification

### How relevance labels are generated

The dataset uses title/section pairs instead of raw chunk IDs because the
Clockify chunker generates UUIDs on every build. We populate
`relevant_chunks` automatically by:

1. Chunking `knowledge_full.md` with the production chunker
2. Building a BM25 index across all chunk texts
3. Selecting the top matching article sections for each question, constrained
   by the guidance in the `notes` field (keywords are extracted and matched)

This approach keeps the dataset stable across rebuilds while still pointing to
concrete passages in the knowledge base. If additional curation is needed you
can edit the `relevant_chunks` list manually—any combination of title + section
found in `chunks.jsonl` will be resolved by the evaluation script.

### Evaluation Metrics

Once chunk IDs are populated, evaluate with:

```bash
# Run evaluation
python3 eval.py --dataset eval_datasets/clockify_v1.jsonl

# Expected output:
# - MRR (Mean Reciprocal Rank): How high relevant chunks rank
# - NDCG@k: Normalized Discounted Cumulative Gain
# - Precision@k: Fraction of top-k that are relevant
# - Recall@k: Fraction of relevant docs in top-k
```

### Coverage by Category

| Category | Count | Difficulty | Notes |
|----------|-------|------------|-------|
| Time Tracking | 4 | Easy-Medium | Core functionality |
| Pricing | 3 | Easy-Medium | Common questions |
| Projects | 5 | Easy-Medium | Project management |
| Reports | 3 | Easy-Medium | Reporting features |
| Advanced | 5 | Medium-Hard | SSO, API, workflows |

### Expansion Strategy

To reach 50-100 questions:

1. **More basic questions** (10): Timer usage, mobile app basics, account setup
2. **Integration questions** (10): Specific integrations (Jira, Slack, Asana, etc.)
3. **Advanced features** (10): Custom fields, formulas, automation
4. **Troubleshooting** (10): Common errors, sync issues, login problems
5. **Mobile-specific** (5): iOS/Android specific features
6. **API questions** (5): Endpoints, authentication, webhooks

### Quality Criteria

For each entry:
- ✅ Question is natural and realistic
- ✅ Difficulty matches complexity
- ✅ Tags accurately categorize
- ✅ At least 1-3 relevant chunks identified
- ✅ Relevant chunks actually answer the question

### Usage

```python
# Load dataset
import json

with open('eval_datasets/clockify_v1.jsonl') as f:
    dataset = [json.loads(line) for line in f if line.strip()]

# Filter by difficulty
easy_questions = [d for d in dataset if d['difficulty'] == 'easy']

# Filter by tag
pricing_questions = [d for d in dataset if 'pricing' in d['tags']]
```

## Contributing

To add new questions:

1. Follow the JSON format above
2. Provide meaningful tags
3. Add helpful notes for chunk identification
4. Maintain diversity of difficulty levels
5. Cover different documentation areas
