$ErrorActionPreference = "Stop"

python scripts\opsec_scan.py --root .
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}
