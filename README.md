# Insights

Agentic analysis of web content. Extract insights, entities, and sentiment from any URL.

## Features

- **Content Extraction** - Parse any web page
- **Entity Recognition** - Extract people, places, organizations
- **Sentiment Analysis** - Analyze tone and emotion
- **Summary Generation** - AI-powered summaries

## API

```
POST /api/v1/insights/analyze
```

## Quick Start

```bash
curl -X POST https://api.openautonomyx.com/api/v1/insights/analyze \
  -H "Authorization: Bearer KEY" \
  -d '{"url": "https://example.com"}'
```

## Response

```json
{
  "summary": "Page summary...",
  "entities": [
    { "type": "person", "name": "John", "confidence": 0.9 }
  ],
  "sentiment": { "label": "positive", "score": 0.7 }
}
```

---

**Repository:** [openautonomyx/insights](https://github.com/openautonomyx/insights)