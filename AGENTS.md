# Bonus68

## Cursor Cloud specific instructions

### Repository state (important, non-obvious)
- The `main` branch is currently a near-empty skeleton: it contains only `README.md` (and this `AGENTS.md`). There is **no** dependency manifest, build system, automated tests, or backend service.
- The only application artifact lives on the unmerged feature branch `cursor/add-aetherfs-search-page-0da7`: a single static file `index.html` ("AetherFS Search" UI, Thai-language semantic employee search).
- `index.html` calls a backend endpoint `api/search.php` (expects JSON `{ total_found, data: [{ employee_id, summary, score }] }`). That PHP backend, a data source, and PHP itself are **not present** in the repo/VM — search will 404 unless a backend is added.

### Running / demonstrating the frontend
- No install step is required. Serve the static frontend with any static file server, e.g. from a directory containing `index.html`:
  - `python3 -m http.server 8000` then open `http://localhost:8000/index.html`
- To exercise the full search-render flow without a real backend, place a JSON file at `api/search.php` (relative to the served directory) returning the shape above; `fetch(...).json()` parses it regardless of content type.

### Tooling available in the VM
- `python3`, `node`, and `npm` are available. `php` is **not** installed.

### Lint / test / build
- There are currently no lint, test, or build commands (no configs exist). Add tooling/manifests before wiring these up.
