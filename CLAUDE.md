# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning repository for LangChain v1 projects, organized into separate project directories. Each subdirectory contains a focused example or exercise exploring different LangChain capabilities.

## Technology Stack

- Python (Jupyter notebooks for interactive development)
- LangChain v1

## Repository Structure

The repository uses a numbered directory structure for different projects:
- `01-semantic-search/` - Semantic search implementation
- Additional numbered project directories will follow the same pattern

Each project directory typically contains:
- Jupyter notebooks (`.ipynb`) for interactive development and experimentation
- Supporting Python files as needed for the specific project

## Development Environment

This is a Python project using Jupyter notebooks. Standard Python tooling applies:

**Virtual Environment**:
- The project uses virtual environments (`.venv/`, `venv/`, etc. are gitignored)
- Create a virtual environment: `python -m venv .venv`
- Activate: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)

**Dependencies**:
- Install dependencies as needed for each project (likely includes langchain, jupyter, etc.)
- Environment variables should be stored in `.env` files (gitignored)

**Running Notebooks**:
- Start Jupyter: `jupyter notebook` or `jupyter lab`
- Individual notebooks can be run through VS Code's Jupyter extension

## Code Organization

Each numbered project directory is self-contained, allowing focused exploration of specific LangChain features without dependencies between projects.
