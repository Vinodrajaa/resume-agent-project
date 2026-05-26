# AI Resume Editing Assistant

## Overview

This project is a multi-agent AI-powered resume editing assistant built using Python and Google ADK principles.

The system allows users to manage and improve different sections of a resume through specialized agents.

Architecture:

User
↓
Unibot
↓
Resume Agent
↓
├── Skills Agent
├── Summary Agent
├── Projects Agent
├── Experiences Agent
└── Educations Agent
↓
Tools
↓
resume.json


## Features

- Add skills
- Remove skills
- Update summary
- Add projects
- Remove projects
- Update experience details
- Add experience bullets
- Update education details
- Persistent resume storage using JSON
- Multi-agent routing architecture


## Project Structure

```text
resume-agent-project/
│
├── agents/
│   ├── skills_agent.py
│   ├── summary_agent.py
│   ├── projects_agent.py
│   ├── experiences_agent.py
│   ├── educations_agent.py
│   └── resume_agent.py
│
├── tools/
│   └── resume_tools.py
│
├── data/
│   └── resume.json
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone repository:

```bash
git clone <repository_url>
cd resume-agent-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python main.py
```

Expected output:

```text
Skills Agent Loaded
Summary Agent Loaded
Projects Agent Loaded
Experiences Agent Loaded
Educations Agent Loaded
Resume Agent Loaded
Unibot Loaded
Agent system initialized successfully
```

## Example Commands

Add skill:

```bash
Add TensorFlow to my skills
```

Update summary:

```bash
Make my summary stronger for Data Engineering roles
```

Add project:

```bash
Add project:
Multi-Agent Resume System
Built a multi-agent resume optimization platform using Google ADK and Python
```

Update experience:

```bash
Improve my experience bullet points
```

## Technologies Used

- Python
- Google ADK
- JSON
- Prompt Engineering
- Multi-Agent Design


## Future Improvements

- Full ADK runtime integration
- Web UI
- Natural language routing execution
- Resume export to PDF
- LLM-based optimization suggestions