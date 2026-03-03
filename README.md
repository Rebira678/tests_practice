# Python Practice Problems 🐍

This repository contains small Python practice problems focused on:

- Writing clean functions
- Identifying logical bugs
- Writing strong unit tests using pytest
- Improving problem-solving skills

Each problem is implemented in a separate file inside the `src/` directory, with corresponding tests inside the `tests/` directory.

---

## 📂 Project Structure

```

.
├── src/
│   ├── math_utils.py
│   ├── string_utils.py
│   ├── list_utils.py
│   ├── number_utils.py
│   └── text_utils.py
│
├── tests/
│   ├── test_math_utils.py
│   ├── test_string_utils.py
│   ├── test_list_utils.py
│   ├── test_number_utils.py
│   └── test_text_utils.py
│
├── requirements.txt
└── README.md

```

---

## 🎯 Purpose

This repository is for practicing:

- Writing correct logic
- Detecting edge cases
- Fixing subtle bugs
- Understanding common programming mistakes:
  - Off-by-one errors
  - Incorrect initialization
  - Order preservation issues
  - Logical comparison mistakes
  - Division errors

The goal is not complexity — but correctness.

---

## ⚙️ Setup

### 1️⃣ Clone the repository

```

git clone <your-repo-url>
cd <repo-name>

```

### 2️⃣ Create virtual environment

```

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

```

### 3️⃣ Install dependencies

```

pip install -r requirements.txt

```

---

## 🧪 Running Tests

Run all tests:

```

pytest -v

```

You should see output showing passed/failed tests.

---

## 📦 Requirements

Minimal dependencies:

```

pytest

```

---

## 🚀 Why This Repo Exists

Consistent small problem practice improves:

- Logical thinking
- Testing mindset
- Code quality awareness
- Debugging speed

Small problems reveal big thinking gaps.

---

## 📌 Future Improvements

- Add coverage reporting
- Add CI with GitHub Actions
- Add type hints
- Add linting (flake8 / black)
