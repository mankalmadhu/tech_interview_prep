# Tech Interview Prep

This repository is designed for holistic technical interview preparation, covering **Data Structures & Algorithms (DSA)** and **System Design**.

## 📂 Directory Structure

The repository is organized into distinct sections to separate different types of interview preparation material. This structure is intended to be easily parsed by both humans and LLMs.

- **[PracticeDSA/](./PracticeDSA/)**: Dedicated folder for Data Structures and Algorithms practice. Contains Python solutions organized by topic-specific subdirectories (e.g., Arrays, DP, Graphs).
- **[SystemDesign/](./SystemDesign/)**: Dedicated folder for System Design resources. Contains notes, architecture diagrams (Excalidraw/Mermaid), and design patterns.

## 🚀 Active Recall Review Tool

This repo includes a custom Spaced Repetition System (SRS) to help you retain what you learn. It tracks your progress and surfaces problems you need to review based on how well you understood them last time.

### Setup

1.  Ensure you have [uv](https://docs.astral.sh/uv/) installed.
2.  Initialize dependency environment:
    ```bash
    cd PracticeDSA
    uv sync
    ```

### How to Review

To start a daily review session, run the manager script using `uv run`:

```bash
cd PracticeDSA
uv run review_manager.py
```

**The Review Flow:**
1.  The tool picks problems due for review.
2.  It shows you the problem path (e.g., `arrays/max_sum.py`).
3.  **Think**: Try to recall the approach and complexity.
4.  **Actions**:
    - `s`: **Show** the code/solution to verify your thought process.
    - `r`: **Run** the code to see outputs (ensure your files have a `main()` block or print statements).
    - `n`: **Next/Rate**. You will be asked to rate the difficulty:
        - **1 (Hard/Fail)**: Reset progress, review tomorrow.
        - **2 (Good)**: Standard interval increase.
        - **3 (Easy)**: large interval increase.
5.  All progress is saved in `PracticeDSA/review_progress.json`.

### Checking Stats

To see how many problems are tracked:

```bash
python review_manager.py stats
```

## 🎨 System Design

Use the `SystemDesign/` folder to store:
- Excalidraw files (`.excalidraw`) for whiteboard style diagrams.
- Markdown files for concepts (CAP Theorem, Load Balancing, etc.).
- Mermaid.js diagrams embedded in markdown.

Happy Coding!
