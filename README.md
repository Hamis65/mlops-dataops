# MLOps Assignment 3 – DataOps Pipeline

## Overview
Implements a DataOps pipeline using a Bronze–Silver–Gold architecture.
The pipeline processes climate time-series data in batches.

The code has:
- incremental ingestion
- data versioning
- automated pipeline execution
- data validation
- reproducible transformations

- No model training

---

## Environment
- Local machine
- Python virtual environment (venv)
- Storage: local file system
- Data versioning: DVC
- Code versioning: Git

---


## Pipeline Stages

### Bronze (ingest)
- Reads incoming batches.
- Appends raw data.
- Stores Bronze dataset.

### Silver (clean)
- Removes duplicate dates.
- Handles missing values.
- Validates time continuity and value ranges.
- Stores Silver dataset

### Gold (ML-ready)
- Creates supervised dataset.
- Features: meantemp, humidity, wind_speed, meanpressure and the same from day prior
- Target: target_next_day_meantemp.
- Stores Gold dataset


## Running

- Activate environment:
.venv\Scripts\activate
- Run pipeline:
.dvc repro

