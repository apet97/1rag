# Chunking Strategy Documentation

## Overview
The RAG system uses a hierarchical chunking strategy designed to preserve semantic boundaries while maintaining coherent context for retrieval.

## Chunking Strategy

### 1. Semantic Boundary Chunking (Primary)
- Splits on major document boundaries: paragraphs, sections, lists
- Preserves logical document structure
- Maintains context within semantic units
- Handles markdown headers, lists, and paragraph breaks

### 2. Sentence-Aware Chunking (Secondary)
- Uses NLTK sentence tokenization
- Avoids breaking sentences mid-way
- Maintains grammatical coherence
- Handles complex sentence structures properly

### 3. Character-Based Chunking (Fallback)
- Pure character-based splitting
- Used when other methods fail
- Ensures consistent max chunk size

## Configuration

The chunking behavior can be configured using these environment variables:

```bash
# Basic chunking parameters
CHUNK_CHARS=1600        # Maximum characters per chunk
CHUNK_OVERLAP=200       # Overlap between chunks in characters

# Advanced options
CHUNK_STRATEGY=hierarchical  # Options: hierarchical, sentence, character
CHUNK_MIN_CHARS=100     # Minimum chunk size (experimental)
CHUNK_SEMANTIC_AWARE=true    # Enable semantic boundary detection
```

## Chunk Metadata

Each chunk now includes enhanced metadata:

- `id`: Unique identifier with document structure info
- `title`: Original document title
- `url`: Document source URL (if any)
- `section`: Section heading
- `subsection`: Subsection headers (H3/H4)
- `doc_path`: Original document path
- `doc_name`: Document name without extension
- `section_idx`: Section index in document
- `chunk_idx`: Chunk index within section
- `char_count`: Character count in chunk
- `word_count`: Word count in chunk
- `metadata`: Additional extracted metadata (dates, URLs, emails)

## Boundary Detection

The system detects and respects these semantic boundaries:

- **Markdown Headers**: H1, H2, H3, H4 sections
- **Paragraph Breaks**: Double newline boundaries
- **List Items**: Bullet points and numbered lists  
- **Code Blocks**: Preserved as single units when possible
- **Tables**: Treated as single semantic units

## Overlap Strategy

The overlap mechanism preserves context across chunk boundaries:

- **Content-Based Overlap**: Includes relevant context from previous chunk
- **Sentence Boundary Respect**: Overlap content maintains sentence integrity
- **Size-Aware**: Calculates overlap based on actual character count

## Performance Considerations

- **NLTK Download**: Sentence tokenization requires NLTK models (downloads automatically)
- **Memory Usage**: Semantic chunking requires more memory for boundary detection
- **Processing Time**: Hierarchical approach takes longer but produces better chunks

## Best Practices

1. **Structure Documents**: Use clear headings and paragraphs for better semantic chunking
2. **Optimal Size**: Balance chunk size between context preservation and retrieval precision
3. **Overlap Settings**: Use 10-15% of chunk size for overlap in most cases
4. **Content Type**: Adjust strategy based on document complexity and structure

## Validation

All chunks are validated for:
- Size constraints (not exceeding maximum)
- Content quality (non-empty with meaningful text)
- Metadata completeness

## Retrieval Configuration and Context Management

The chunking configuration works in tandem with retrieval parameters to prevent context overflow:

### Key Constants

```bash
DEFAULT_TOP_K=15      # Number of chunks to retrieve (default)
MAX_TOP_K=50          # Hard ceiling to prevent context overflow
DEFAULT_PACK_TOP=8    # Number of chunks to pack into final context
CTX_TOKEN_BUDGET=12000  # Token budget for snippet packing
```

### Relationship Between Chunking and Retrieval

- **Chunk Size** (CHUNK_CHARS=1600): ~400 tokens per chunk (at 4 chars/token)
- **Retrieval Fan-out** (DEFAULT_TOP_K=15): 15 chunks × 400 tokens = ~6000 tokens
- **Context Budget** (CTX_TOKEN_BUDGET=12000): Allows 2x safety margin for larger chunks
- **Hard Cap** (MAX_TOP_K=50): 50 chunks × 400 tokens = ~20K tokens (would overflow most models)

### Safety Mechanisms

1. **DEFAULT_TOP_K**: Configurable default via `DEFAULT_TOP_K` env var, used when no explicit top_k provided
2. **MAX_TOP_K**: Hard ceiling enforced in `retrieve()` function, prevents context overflow from user input
3. **RETRIEVAL_K**: Backward-compatible alias for DEFAULT_TOP_K
4. **Automatic Clamping**: Values exceeding MAX_TOP_K are automatically clamped with a warning

### Configuration Examples

```bash
# Conservative (small models, limited memory)
export DEFAULT_TOP_K=10
export MAX_TOP_K=30
export CTX_TOKEN_BUDGET=6000

# Aggressive (large models, internal use)
export DEFAULT_TOP_K=20
export MAX_TOP_K=100
export CTX_TOKEN_BUDGET=20000

# Default (balanced for Qwen 32B with 32K context window)
export DEFAULT_TOP_K=15
export MAX_TOP_K=50
export CTX_TOKEN_BUDGET=12000
```