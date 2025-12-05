# CALL: Community-Agent LLM-based Representation

A framework for representing and evaluating online communities using large language models (LLM).

![image](https://github.com/user-attachments/assets/979d1609-a2d1-4e38-97ad-f395c9fe429d)

## Overview

This study presents a framework for extracting posts from Korean online communities, summarizing key opinions, and representing each community. It also evaluates public opinion and values through experiments.

### Research Questions

- **RQ1**: : Can we build an LLM agent that faithfully represents the views of an online community?
- **RQ2**: Can an agent constructed from a community’s representative opinions also reflect broader ideological values, such as progressive or conservative leanings?

### Communities Analyzed

- 에펨코리아 (`fm`)
- 엠엘비파크 (`mlb`)
- 뽐뿌 (`pp`)

## Repository Structure

```
CALL/
├── code/
│   ├── RQ1_generate_questions.ipynb      # Generate survey questions from comments
│   ├── RQ1_questions_quality_check.ipynb # Evaluate question quality
│   ├── RQ1_experiment.ipynb              # RQ1 experiment
│   └── RQ2_experiment.ipynb              # RQ2 experiment
├── dataset/
│   ├── community_samples/                # Original community data experiments
│   ├── prompts/{topic}/                  # Generated prompts 
│   ├── RQ1_questions/                    # Generated and selected questions
│   ├── faiss/                            # FAISS indices 
│   └── 20th_president.csv                # ksdc survey (Empty due to copyright)
├── .env.example                          # API key template
├── requirements.txt
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 3. Generate FAISS Indices

See `dataset/faiss/README.md` for instructions.

## Running Experiments

### RQ1: Question Generation and Experiment

#### Political Topics (7 topics)
-  정권 교체 (Regime Change)
-  통합 정치 (Unified Politics)
-  단일화(윤석열-안철수) (Coalition of Yoon-Ahn)
-  부동산, 세금 등 경제문제 (Real Estate, Tax and Economic Issues)
-  여성가족부 폐지 (Abolition of Ministry of Gender Equality)
-  후보(또는 가족)의 비리 (Candidate/Family Corruption)
-  대장동 의혹 (Daejangdong Scandal)


1. **Generate Questions**:
   ```bash
   jupyter notebook code/RQ1_generate_questions.ipynb
   ```

2. **Quality Check**:
   ```bash
   jupyter notebook code/RQ1_questions_quality_check.ipynb
   ```

3. **Run Experiment** (Ours, RAG, Random, Ideology, Community methods):
   ```bash
   jupyter notebook code/RQ1_experiment.ipynb
   ```

### RQ2: Real Survey Analysis

#### Real Survey Data Source

제20대 대통령선거 관련 유권자 의식조사
Korea Social Science Data Center & Sogang Institute for Contemporary Politics
Survey Period: 2022.04.07 ~ 2022.04.18
URL: https://www.ksdcdb.kr/data/dataSearchResView.do?surveyId=2825

```bash
jupyter notebook code/RQ2_experiment.ipynb
```

Supports both perspectives:
- `jinbo` (liberal) - uses 뽐뿌(pp) data
- `bosu` (conservative) - uses 에펨코리아(fm) + 엠엘비파크(mlb) data

Analyzes 23 political opinion questions with KL-divergence comparison against real survey data.

## Key Modules

- **Retriever** (`augment_text`): FAISS-based semantic search for relevant posts
- **Summarizer** (`extract_opinions`): Theme extraction from retrieved posts
- **Agent** (`final_agent`): Answer selection based on summarized opinions
