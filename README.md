# Sample Project


## Setup

1. **Fork this repository** to your own GitHub account

2. **Clone your fork:**
```bash
   git clone https://github.com/YOUR-USERNAME/ocean-temp-analysis.git
   cd ocean-temp-analysis
```

3. **Create the environment:**
```bash
   conda env create -f environment.yml
   conda activate ocean-analysis
   pip install -e .
```

4. **Verify it works:**
```bash
   python app.py
```

## Activity Instructions

### Part 1: Explore (10 min)

Use Copilot Chat with `@workspace` to understand the project structure and how imports work.

### Part 2: Fix the Bug (15 min)

The date parsing in `src/data_loader.py` is broken. Use Copilot to find and fix it.

### Part 3: Add a Feature (20 min)

Complete `calculate_monthly_means()` in `src/analysis.py`. Import and use it in `app.py`.

### Part 4: Push Your Changes (5 min)

Commit and push your fixes to your fork:
```bash
git add .
git commit -m "Fix date parsing and add monthly means"
git push origin main
```

## Tips

- Use `@workspace` in Copilot Chat for repo-wide questions
- Write descriptive comments for code generation
- Highlight code and ask "What's wrong?" for debugging

## Troubleshooting

- **ModuleNotFoundError:** Run `pip install -e .`
- **FileNotFoundError:** Run from project root directory
- **Copilot not seeing repo:** Use `@workspace` in Copilot Chat