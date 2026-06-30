# Multilingual Speech Data Collection & Transcription Project

A generic framework for high-fidelity audio transcription, voice recording validation, and data annotation for machine learning models. This repository is optimized for native-speaker validation in:
- English (native speaker validation)
- Conversational Hindi (Romanized transcription)
- Conversational Odia (Romanized transcription)

Purpose
- Provide consistent, high-quality speech and transcript data for training Automatic Speech Recognition (ASR) and related speech models.
- Ensure reproducible collection, annotation, and QA steps suitable for multilingual conversational datasets.
- Prioritize natural conversational utterances and native-speaker validation for dialectal and code-switched content.

Repository structure (recommended)
- audio/
  - raw/                # Raw uploaded recordings (wav)
  - processed/          # Normalized/converted audio (16-bit PCM WAV, 16kHz or 48kHz)
- transcripts/          # Master transcripts (.txt, .jsonl, or .tsv) aligned to audio files
- metadata/             # metadata CSV/JSON with one row per audio file
- annotations/          # reviewer annotations, adjudications, tags
- scripts/              # processing & QC scripts (e.g., validate_audio.py, generate_manifest.py)
- docs/
  - transcription_guidelines.md  # This style guide (authoritative)
  - qc_checklist.md               # Short checklist for validators
- qc/                   # QC reports and logs
- LICENSE
- README.md              # You are reading it

Filename conventions
- Audio: <language>_<speakerID>_<sessionID>_<segmentID>.wav
  - Example: en_spk0001_sess002_seg0001.wav
  - Language tags: en (English), hi (Hindi romanized), or (Odia romanized)
- Transcript: <same-base-name>.txt or .jsonl
  - One utterance per line; timestamps and speaker metadata optional in JSON/TSV manifests.

Recommended audio format
- Container: WAV (PCM)
- Encoding: 16-bit PCM
- Sample rate: 16 kHz for telephony/ASR baseline, 48 kHz for high-fidelity recording (downsample as needed)
- Channels: mono preferred
- File naming must match metadata entries exactly.

Metadata fields (per-audio file)
- id: unique id (string)
- filename: audio filename
- language: "en" | "hi" | "or" (use "or" for Odia)
- transcription_path: path to transcript file
- speaker_id: anonymized speaker identifier
- gender: M/F/Other/Not-specified (if provided)
- age_range: e.g., 18-25
- dialect: local/regional notes (if known)
- location: city/state/country (coarse)
- device: device type (phone/laptop/studio)
- sampling_rate: 16000 or 48000
- channels: 1
- environment: e.g., quiet_room, cafe, outdoors
- consent: yes/no
- notes: free text

Transcription format & pointers
- Use docs/transcription_guidelines.md as the authoritative source for orthography, tag usage, and normalization rules.
- Store transcripts as UTF-8 plain text. For multilingual romanized transcripts maintain a single consistent romanization scheme per language (document which scheme in metadata).

Quality control and validation overview
- Two-pass workflow:
  1. Primary transcriber creates the transcript.
  2. Native-speaker validator performs validation and flags issues (acoustic problems, inaudible regions, speaker mis-ID).
  3. Adjudicator resolves disagreements where necessary.
- Keep a QC log per file (qc/<id>.md) recording decisions and issues.
- Track acceptance metrics (WER targets, agreement rates) per language and annotator.

Privacy, consent & licensing
- Only collect recordings when explicit consent is recorded.
- Maintain anonymized speaker IDs; don't store PII in public metadata.
- Specify license (e.g., CC-BY-NC, or custom) clearly in LICENSE.

How to contribute
- Read docs/transcription_guidelines.md before annotating.
- Use provided scripts in scripts/ to validate audio format and metadata consistency before upload.
- Follow the filename and metadata conventions strictly to avoid pipeline breakages.

Contacts & maintainers
- Project lead: [name/email or organization contact]
- For questions about annotation policy or QC thresholds, see docs/transcription_guidelines.md.
