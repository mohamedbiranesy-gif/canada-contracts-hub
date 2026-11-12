#!/usr/bin/env python3
"""Harvest Germany: Procurement Office of the Federal Ministry of the Interior (BMI) (OCDS publication 136 on the OCP Data Registry). Thin wrapper over contrib/claude/ocds_common/ocds_harvest.py.
Usage: python3 -I harvest.py <out.jsonl.gz>"""
import subprocess, sys, os
common = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ocds_common", "ocds_harvest.py")
sys.exit(subprocess.call([sys.executable, "-I", common, '136', 'ocds_germany_bmi', 'DE', '2022.jsonl.gz,2023.jsonl.gz,2024.jsonl.gz,2025.jsonl.gz,2026.jsonl.gz', sys.argv[1], "--name", 'OCDS: Germany: Procurement Office of the Federal Ministry of the Interior (BMI)']))
