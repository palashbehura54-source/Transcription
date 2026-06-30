# Multilingual Speech Data Collection & Transcription Project

A generic framework for high-fidelity audio transcription, voice recording validation, and data annotation for machine learning models. This repository is optimized for native-speaker validation in:
* **English** (Native speaker validation)
* **Conversational Hindi** (Romanized transcription)
* **Conversational Odia** (Romanized transcription)

## Purpose
* Provide consistent, high-quality speech and transcript data for training Automatic Speech Recognition (ASR) and related speech models.
* Ensure reproducible collection, annotation, and QA steps suitable for multilingual conversational datasets.
* Prioritize natural conversational utterances and native-speaker validation for dialectal and code-switched content.

---

## Repository Structure
```text
├── audio/
│   ├── raw/                # Raw uploaded recordings (.wav)
│   └── processed/          # Normalized audio (16-bit PCM WAV, 16kHz/48kHz)
├── transcripts/            # Master transcripts (.txt, .jsonl, or .tsv)
├── metadata/               # Metadata CSV/JSON files (one row per audio file)
├── annotations/            # Reviewer annotations, adjudications, and tags
├── scripts/                # Processing & QC scripts (e.g., clean_transcript.py)
├── docs/
│   ├── transcription_guidelines.md  # Authoritative style guide
│   └── qc_checklist.md               # Short checklist for validators
├── qc/                     # QC reports and verification logs
└── README.md               # Main project overview
