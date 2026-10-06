# Business Contract Validation

An end-to-end document-intelligence prototype for comparing business contracts against templates and surfacing differences.

## Architecture

```
Contract / Template PDFs
        ↓
PDF parsing
        ↓
Named Entity Recognition
        ↓
Heading / text classification
        ↓
Template ↔ contract comparison
        ↓
PDF highlighting
        ↓
LLM-assisted summary
        ↓
Streamlit application
        ↓
Docker packaging
```

## Layered design

### L1 — Individual components

Reusable components cover PDF parsing, named entity recognition, text classification, text comparison, PDF highlighting, and document summarization.

### L2 — Flow

`L2_Flow/ContractValidator.py` orchestrates the individual components into the complete validation flow.

### L3 — Application

`L3_Streamlit/streamlitValidation.py` exposes the pipeline through an interactive Streamlit interface.

### L4 — Docker

`L4_Dockers/` contains the Docker configuration used to package the application.

## What this project demonstrates

This project goes beyond a single model by combining several AI/NLP components into one application workflow:

- component-based AI pipeline design;
- orchestration of multiple processing stages;
- deterministic document processing combined with generative AI;
- user-facing Streamlit integration;
- container-oriented application structure.

## Configuration

Create a local `.env` file from `.env.example` and supply your own external-service credentials.

Never commit `.env` or API credentials.

## Important security action

This project has previously contained third-party credentials in source files. Before using the repository with real accounts, revoke/rotate any credentials that were ever committed publicly. Moving credentials out of active source files does not invalidate old credentials that may still exist in Git history.

## Portfolio status

This repository represents a prototype / project implementation, not a production legal-review system.

Useful future improvements include automated tests, structured logging, typed interfaces between stages, an API layer, benchmark datasets, confidence thresholds, and CI/CD.

## Technology

**Python · NLP · NER · PDF Processing · Generative AI · Streamlit · Docker · Cloud Services**

## Author

**Ronak Vekariya**

[GitHub](https://github.com/Ronakvekariya)
