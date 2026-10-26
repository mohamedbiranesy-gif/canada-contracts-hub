"""Run emit.process() on a numeroseao range for testing by patching the cursors."""
import sys, re
src = open('scripts/seao_quebec/emit.py').read()
lo, hi = sys.argv[6], sys.argv[7]
src = src.replace("SELECT numeroseao, ord, src, kind, json FROM avis_rows ORDER BY", f"SELECT numeroseao, ord, src, kind, json FROM avis_rows WHERE numeroseao BETWEEN \"{lo}\" AND \"{hi}\" ORDER BY")
src = src.replace("SELECT numeroseao, ord, src, kind, json FROM contrat_rows ORDER BY", f"SELECT numeroseao, ord, src, kind, json FROM contrat_rows WHERE numeroseao BETWEEN \"{lo}\" AND \"{hi}\" ORDER BY")
src = src.replace("SELECT numeroseao, ord, src, kind, json FROM depense_rows ORDER BY", f"SELECT numeroseao, ord, src, kind, json FROM depense_rows WHERE numeroseao BETWEEN \"{lo}\" AND \"{hi}\" ORDER BY")
src = src.replace("SELECT numeroseao, ocid, release_id, release_date, file_order, src, tags, json FROM latest ORDER BY", f"SELECT numeroseao, ocid, release_id, release_date, file_order, src, tags, json FROM latest WHERE numeroseao BETWEEN \"{lo}\" AND \"{hi}\" ORDER BY")
sys.argv = sys.argv[:6]
exec(compile(src, 'emit_slice', 'exec'))
