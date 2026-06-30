# Transcription Guidelines — Multilingual Speech Data
*(English / Hindi (Romanized) / Odia (Romanized))*

## Purpose
* Provide a consistent, detailed style guide for transcribers and validators creating training-grade transcripts for ASR.
* Optimize for conversational speech, native-speaker validation, and robust handling of code-switching and local pronunciations.

## Core Principles
* Transcribe what you hear (orthographic transcription) and aim for the natural spoken form.
* Use Romanized forms for Hindi and Odia (document the chosen romanization scheme in metadata).
* Keep transcripts consistent, machine-readable (UTF-8), and free of unnecessary markup.
* Use non-speech event tags (e.g., `[laughter]`) where needed (see tag section).

## File & Line Format
* Plain text UTF-8 encoded.
* Recommended: One utterance per line. If timestamps are required, use JSONL or TSV with explicit columns: `id`, `start_time`, `end_time`, `speaker`, `transcript`.
* Trim leading/trailing whitespace. Do not include BOM.

## Casing & Punctuation
* Lowercase is preferred for training (reduces variation); however, sentence-case is acceptable if used consistently.
* Include punctuation only to improve readability and sentence segmentation. Punctuation will typically be stripped or ignored during acoustic model training; maintain it for downstream usage.
* Do not include quotation marks for reported speech unless they are spoken cues.

## Numbers, Dates, Times, & Currencies
* Normalize numbers to spoken words in the target language:
  * 5 → "five" (English)
  * 5 → "paanch" (Hindi romanized)
  * 5 → "pãñc" / "pãnc" (Use consistent romanization for Odia)
* Phone numbers/account numbers: Transcribe as digits separated by spaces (e.g., "nine eight seven six" or "9 8 7 6").
* Dates: Speak as the natural spoken form: "January first twenty twenty-one" or "fifth August two thousand twenty".
* Times: Transcribe as spoken: "five pm" or "five in the evening" (be consistent).

## Abbreviations & Acronyms
* Transcribe acronyms as they are spoken. If spelled out, use spaced characters (`F B I`). If said as a word, transcribe as a word (`NATO`).

## Code-Switching
* Transcribe words exactly as spoken, even if the word comes from a different language.
* Optionally add inline language markers for long segments (e.g., `[en] ... [/en]`) only if required by downstream tasks. Avoid over-tagging short code-switched tokens.
* Romanized Hindi/Odia should stay romanized even when English words are used — keep English words in standard English orthography.

## Disfluencies, Fillers, and False Starts
* Include major disfluencies if they affect the surface form of speech or the content (e.g., "I— I can't do that").
* Common fillers ("uh", "um", "hmm") may be optionally included. If included, transcribe them verbatim using the same token.
* Repeats: Transcribe exactly as spoken unless "cleaned" transcripts are explicitly requested by project leads.

## Speaker Labeling & Overlap
* For multi-speaker segments, prepend speaker labels if required: `Speaker_1: text`
* For overlapping speech, annotate with `[overlap]` and provide best-effort segmentation:
  * *Example:* `Speaker_1: "I think we should" [overlap] Speaker_2: "—go now"`
* Keep labels consistent across files.

## Timestamps & Segmentation
* If timestamps are required, prefer start and end times in seconds with millisecond precision: `00:00:12.345`
* Keep utterances reasonably short for ASR training: Aim for 1–15 seconds per segment where possible.

---

## Multilingual Data Annotation Matrix
Use the table below as canonical examples for annotation style.

| Spoken Language | Input Audio Example | Annotated Text Output | Protocol |
| :--- | :--- | :--- | :--- |
| **English (en)** | "Hey, are we meeting at five?" | `hey are we meeting at five` | Orthographic, lowercase, numbers normalized to words, punctuation optional. |
| **Hindi — Romanized (hi)** | "Kal shaam ko milte hain?" | `kal shaam ko milte hain` | Romanized Hindi, lowercase, conversational phrasing, no Devanagari. |
| **Odia — Romanized (or)** | "Tume kebe asuchha?" | `tume kebe asuchha` | Romanized Odia, lowercase, conversational, consistent vowel romanization. |

---

## Quality Control Criteria

### 1. Acoustic Environment
* **Acceptable formats:** WAV PCM 16-bit recommended.
* **Sample rate:** 16 kHz minimum for ASR baseline; 48 kHz acceptable for high-fidelity tasks.
* **Channel:** Mono preferred. If stereo, ensure a single channel is used or downmixed consistently.
* **SNR:** Prefer SNR ≥ 20 dB for "clean" labeled data. Flag and record SNR in metadata for noisy samples.
* **Clipping:** Reject or mark if >2% of frames are clipped.
* **Reverberation:** Excessive echo that reduces intelligibility should be flagged.
* **Background noise:** Acceptable (cafes, street) if speech remains intelligible; document in metadata.

### 2. Natural Utterances
* Natural conversational speech is prioritized over read/recited text.
* **Utterance length:** 1s minimum to 15s maximum. Longer utterances should be split.
* **Speaking style:** Encourage neutral speaking rates and minimal microphone handling noise.

### 3. Transcribability
* If an utterance is >30% unintelligible, mark the entire utterance as `[inaudible]` or split into audible/inaudible portions.
* Validators must ensure the transcript matches audible content to >95% perceived agreement; otherwise, assign for adjudication.

---

## Acceptance Thresholds & Metrics
* **Inter-Annotator Agreement:** Reviewers should achieve >95% token-level agreement on validated files; otherwise, escalate to adjudication.
* **Target Word Error Rates (WER):**
  * Clean English: < 5% WER
  * Conversational Hindi (Romanized): < 7% WER
  * Conversational Odia (Romanized): < 8-10% WER
* **Spot Checks:** Validate a random sample (≥5%) per annotator per week.

---

## Annotation Workflow & Validation Passes
1. **Pass 1 (Primary Transcriber):** Complete initial transcription and tag non-speech events.
2. **Pass 2 (Native Validator):** Listen and correct transcription, check metadata, and mark QC status (accept/reject/needs-adjudication).
3. **Pass 3 (Adjudicator):** Resolve disagreements and finalize the transcript.
*Keep a log entry for each QC decision with timestamps and validator IDs.*

---

## Acoustic and Non-Speech Event Tags
Use a closed set of standard tags in square brackets. Tags must always be lowercase.

| Tag | Usage & Semantics |
| :--- | :--- |
| `[laughter]` | Audible laughter (short laugh or chuckle). |
| `[cough]` | Single cough (use `[coughs]` for multiple in rapid succession). |
| `[noise]` | Persistent/non-specific background noise (e.g., traffic hum). |
| `[inaudible]` | Speech that cannot be understood at normal volumes. |
| `[overlap]` | Overlapping speech regions. |
| `[breath]` | Distinct audible breath that affects intelligibility. |
| `[music]` | Background music present (if not relevant to speech). |

**Tag Placement:**
* Place inline at the most relevant position: `"I was like [laughter] no way"`
* As a standalone token if it occupies most of the segment: `"[cough] sorry, can you repeat?"`
* For partially inaudible words: `"I went to the [inaudible] yesterday."`

---

## Language-Specific Notes

### Hindi (Romanized)
* Use simple, consistent romanization (e.g., "kal", "shaam", "milte", "hain").
* Represent aspirated consonants explicitly: "th", "dh" etc., consistently.
* Avoid mixing Devanagari and romanization in the same transcript.

### Odia (Romanized)
* Use consistent transliteration for vowels: e.g., "a", "aa", "e", "i", "o", "u" (document scheme in metadata).
* Capture typical morphological endings and courteous forms; do not "translate" to Hindi or English.

### English
* If dialectal pronunciations alter word forms meaningfully, transcribe the surface form as spoken (e.g., "gonna" vs "going to") following project normalization policy.

---

## Profanity and Sensitive Content
* Transcribe profanity exactly as spoken. Do not sanitize unless policy directs otherwise.
* Flag sensitive content in metadata (e.g., personal data, violent content) and elevate for privacy review.

## Common Edge Cases
* **Singing:** Mark with `[singing]` and flag for special handling.
* **Echo/Reverberation:** Mark in metadata and use `[inaudible]` tags for affected spans.
* **Overlapping speech:** Add `[overlap]` and attempt to capture both streams if possible.

## Tools & Scripts
* `scripts/validate_audio.py` — Verify sample rate, format, channels, length bounds.
* `scripts/check_metadata.py` — Verify metadata fields and link integrity.
* *Note: Provide a simple manifest generation script to convert transcripts + metadata into JSONL for training.*

## Final Notes
* **Consistency is critical:** Follow these guidelines strictly to keep the dataset usable for model training and evaluation.
* Keep an annotated changelog for policy updates and dataset releases.
* For unresolved examples, consult the language lead or escalate to adjudication.
