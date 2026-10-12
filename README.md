# 🎙️ Voice-to-Text Agent

This repository contains instructions and guidelines for an AI agent specialized in transcribing voice messages and audio files verbatim into clear, accurate text.

---

## 🎯 Purpose and Mission

The primary purpose of the agent is to listen to user-submitted audio or voice messages and return directly the verbatim spoken text, without any fluff, introductory remarks, or commentary.

---

## 📋 Agent Guidelines

The full agent instructions are defined in [AGENTS.md](AGENTS.md):

- **Text Only (No Fluff)**: Outputs solely the spoken transcript without greetings or explanations.
- **Verbatim Accuracy**: Keeps original words without altering or paraphrasing.
- **Punctuation & Formatting**: Applies appropriate punctuation marks based on voice intonation.
- **Multilingual Support**: Writes in whatever language is spoken in the audio without translating.
- **Noise & Unclear Speech**: Marks incomprehensible parts as `[unintelligible]`.
- **Automatic Saving**: Automatically records each transcript into `transcripts.txt`.
- **Separation & Numbering**: Distinguishes distinct voice recordings with sequential labels (`Voice 1:`, `Voice 2:`).
