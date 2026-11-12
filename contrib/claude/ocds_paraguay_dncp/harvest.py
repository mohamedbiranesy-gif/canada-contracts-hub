#!/usr/bin/env python3
"""Harvest Paraguay: Dirección Nacional de Contrataciones Públicas (DNCP) (OCDS publication 63 on the OCP Data Registry). Thin wrapper over contrib/claude/ocds_common/ocds_harvest.py.
Usage: python3 -I harvest.py <out.jsonl.gz>"""
import subprocess, sys, os
common = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ocds_common", "ocds_harvest.py")
sys.exit(subprocess.call([sys.executable, "-I", common, '63', 'ocds_paraguay_dncp', 'PY', '2022.jsonl.gz,2023.jsonl.gz,2024.jsonl.gz,2025.jsonl.gz,2026.jsonl.gz', sys.argv[1], "--name", 'OCDS: Paraguay: Dirección Nacional de Contrataciones Públicas (DNCP)']))
