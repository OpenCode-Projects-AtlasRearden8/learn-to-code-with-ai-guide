#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "=== 1/3: build the static site ==="
python3 build.py

echo "=== 2/3: run the chapter exercise solutions ==="
node tests/run-solutions.js

echo "=== 3/3: check internal links in docs/ and site/ ==="
python3 tests/check_links.py

echo
echo "ALL CHECKS PASSED"
