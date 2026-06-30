# Transcription Guidelines — Multilingual Speech Data (English / Hindi (Romanized) / Odia (Romanized))

Purpose
- Provide a consistent, detailed style guide for transcribers and validators creating training-grade transcripts for ASR.
- Optimize for conversational speech, native-speaker validation, and robust handling of code-switching and local pronunciations.

Core principles
- Transcribe what you hear (orthographic transcription) and aim for the natural spoken form.
- Use Romanized forms for Hindi and Odia (document the chosen romanization scheme in metadata).
- Keep transcripts consistent, machine-readable (UTF-8), and free of unnecessary markup.
- Use non-speech event tags (e.g., [laughter]) where needed (see tag section).

File & line format
- Plain text UTF-8 encoded.
- Recommended: one utterance per line. If timestamps are required, use JSONL or TSV with explicit columns: id, start_time, end_time, speaker, transcript.
- Trim leading/trailing whitespace. Do not include BOM.

Casing & punctuation
- Lowercase preferred for training (reduces variation); however, sentence-case is acceptable if used consistently.
- Include punctuation only to improve readability and sentence segmentation. Punctuation will typically be stripped or ignored during acoustic model training; maintain it for downstream usage.
- Do not include quotation marks for reported speech unless they are spoken cues.

Numbers, dates, times, currencies
- Normalize numbers to spoken words in the target language:
  - 5 → "five" (en) ; 5 → "paanch" (hi romanized) ; 5 → "pãñc" / "pãnc" — use consistent romanization for Odia
- Phone numbers, account numbers: transcribe as digits separated by spaces: "nine eight seven six" or "9 8 7 6 5 4 3 2 1 0"
- Dates: speak as the natural spoken form: "January first twenty twenty-one" or "fifth August two thousand twenty" depending on what's spoken.
- Times: transcribe as spoken: "five pm", "5:00 p.m." → "five in the evening" or "five pm" — be consistent.

Abbreviations & acronyms
- Transcribe acronyms as they are spoken. If spelled-out, use spaced characters: "F B I" → "F B I". If said as a word, transcribe as word: "NATO".

Code-switching
- Transcribe words exactly as spoken, even if the word comes from a different language.
- Optionally add inline language markers for long segments (e.g., [en] ... [/en]) only if required by downstream tasks. Avoid over-tagging short code-switched tokens.
- Romanized Hindi/Odia should stay romanized even when English words are used — keep English words in standard English orthography.

Disfluencies, fillers, and false starts
- Include major disfluencies if they affect the surface form of speech or the content (e.g., "I— I can't do that").
- Common fillers ("uh", "um", "hmm") may be optionally included. If included, transcribe them verbatim using the same token (e.g., "um", "uh").
- Repeats: transcribe exactly as spoken unless guideline for “cleaned” transcripts is requested by project leads.

Speaker labeling & overlap
- For multi-speaker segments, prepend speaker labels in the transcript file if required: "Speaker_1: text"
- For overlapping speech, annotate with [overlap] and provide best-effort segmentation:
  - Example: Speaker_1: "I think we should" [overlap] Speaker_2: "—go now"
- Keep labels consistent across files.

Timestamps & segmentation
- If timestamps are required, prefer start and end times in seconds with millisecond precision: 00:00:12.345
- Keep utterances reasonably short for ASR training: aim for 1–15 seconds per segment where possible.

Multilingual Data Annotation Matrix
- Use the table below as canonical examples for annotation style.

| Spoken Language | Input Audio Example (spoken) | Annotated Text Output | Protocol |
|---|---:|---|---|
| English (en) | "Hey, are we meeting at five?" | hey are we meeting at five | Orthographic, lowercase, numbers normalized to words, punctuation optional. One utterance per line. |
| Hindi — Romanized (hi) | "Kal shaam ko milte hain?" | kal shaam ko milte hain | Romanized Hindi, lowercase, natural conversational phrasing, no Devanagari. Numbers normalized to words in romanized form. |
| Odia — Romanized (or) | "Tume kebe asuchha?" | tume kebe asuchha | Romanized Odia, lowercase, conversational, follow consistent romanization for vowels/consonants. |

Quality Control Criteria
- Acoustic environment
  - Acceptable formats: WAV PCM 16-bit recommended.
  - Sample rate: 16 kHz minimum for ASR baseline; 48 kHz acceptable for high-fidelity tasks.
  - Channel: mono preferred. If stereo, ensure single channel is used or downmixed consistently.
  - Signal-to-noise ratio (SNR): prefer SNR ≥ 20 dB for "clean" labelled data. Flag and record SNR in metadata for noisy samples.
  - Clipping: reject or mark if >2% of frames clipped. Clipped audio requires re-recording or special handling.
  - Reverberation: excessive reverberation or echo that reduces intelligibility should be flagged.
  - Background noise: acceptable (cafes, street) if speech remains clearly intelligible; document environment in metadata.
- Natural utterances
  - Natural conversational speech is prioritized. Avoid read/recited text unless project explicitly requires read speech.
  - Utterance length: recommend 1s minimum and 15s maximum for segments. Longer utterances should be split into meaningful subsegments.
  - Speaking style: encourage neutral speaking rate, minimal microphone handling noise, and avoidance of musical/sung content unless requested.
- Transcribability
  - If an utterance is more than 30% unintelligible, mark entire utterance as [inaudible] or split into audible/inaudible portions.
  - Validators should ensure transcript matches audible content to >95% perceived agreement; otherwise assign for adjudication.

Acceptance thresholds & metrics
- Minimum transcription inter-annotator agreement: reviewers should achieve >95% token-level agreement on validated files in the same language; otherwise escalate to adjudication.
- WER targets for release-ready data (example targets; adjust per project needs):
  - Clean English: <5% WER
  - Conversational Hindi (romanized): <7% WER
  - Conversational Odia (romanized): <8-10% WER
- Annotator training and periodic spot checks: validate a random sample (≥5%) per annotator per week.

Annotation workflow & validation passes
- Pass 1 — primary transcriber: complete initial transcription and tag non-speech events.
- Pass 2 — validator (native speaker): listen and correct transcription, check metadata, and mark QC status (accept/reject/needs-adjudication).
- Pass 3 — adjudicator: resolve disagreeements and finalize transcript.
- Keep a log entry for each QC decision with timestamps and validator IDs.

Acoustic and Non-Speech Event Tags
- Use a closed set of standard tags in square brackets. Tags should always be lowercase and bracketed.
  - [laughter] — audible laughter (use [laugh] or [laughter] consistently; pick one — use [laughter])
  - [cough] — single cough or multiple coughs (e.g., [cough] or [coughs])
  - [noise] — persistent background noise not otherwise categorized (e.g., traffic hum)
  - [inaudible] — speech that cannot be understood; can optionally include time span: [inaudible 00:01-00:03]
  - [overlap] — overlapping speech region
  - [breath] — distinct audible breath that affects intelligibility
  - [music] — music present (if present and not relevant)
- Tag placement:
  - Place tag inline at the most relevant position: "I was like [laughter] no way" or as a standalone token if it occupies most of the segment: "[cough] sorry, can you repeat?"
  - For partially inaudible words, use square-bracketed partial tokens: "I went to the [inaudible] yesterday."
- Examples:
  - "he said [laughter] that's great" → transcribe as: he said [laughter] that's great
  - "[inaudible] I can't hear you" → [inaudible] i can't hear you

Tag mapping and semantics
- [laughter] — short laugh or chuckle that is clearly audible.
- [cough] — single cough; use [coughs] for multiple coughs in rapid succession.
- [noise] — non-specific background sound (applause, traffic, machinery); use more specific tags if obvious: [applause], [traffic].
- [inaudible] — speech unintelligible even to a native speaker at normal playback volumes. Prefer splitting audio and annotating exact timestamps where possible.

Language-specific notes
- Hindi (Romanized)
  - Use simple, consistent romanization (e.g., "kal", "shaam", "milte", "hain").
  - Represent aspirated consonants explicitly: "th", "dh" etc., consistently.
  - Avoid mixing Devanagari and romanization in the same transcript.
- Odia (Romanized)
  - Use consistent transliteration for vowels: e.g., "a", "aa", "e", "i", "o", "u" — document scheme in metadata.
  - Capture typical morphological endings and courteous forms; do not "translate" to Hindi or English.
- English
  - If dialectal pronunciations alter word forms meaningfully, transcribe the surface form as spoken (e.g., "gonna" vs "going to") following the project's normalization policy.

Profanity and sensitive content
- Transcribe profanity exactly as spoken. Do not sanitize unless policy directs otherwise.
- Flag sensitive content in metadata (e.g., personal data, violent content) and elevate for privacy review.

Examples (quick reference)
- Original audio: "Are you coming at 5?" → Transcript: are you coming at five
- Hindi romanized: Speaker says "main aa raha hoon" → Transcript: main aa raha hoon
- Odia romanized: Speaker says "mu bhala achhi" → Transcript: mu bhala achhi

Common edge cases
- Singing: mark with [singing] and flag for special handling.
- Echo/reverberation causing unintelligibility: mark in metadata and [inaudible] tags for affected spans.
- Overlapping speech: add [overlap] and attempt to capture both streams if possible.

Tools & scripts
- scripts/validate_audio.py — verify sample rate, format, channels, length bounds.
- scripts/check_metadata.py — verify metadata fields and link integrity.
- Provide simple manifest generation script to convert transcripts + metadata into JSONL for training.

Final notes
- Consistency is critical: follow these guidelines strictly to keep the dataset usable for model training and evaluation.
- Keep an annotated changelog for policy updates and dataset releases.
- For any unresolved examples or language-specific questions, consult the language lead or escalate to adjudication.
