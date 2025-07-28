import site
import os
from pathlib import Path

if "VIRTUAL_ENV" not in os.environ:
    print("****** ERROR, NOT in pipenv shell **********")
    exit(1)

site_packages_path = None
for pkg in site.getsitepackages():
    pth = Path(pkg)
    if pth.exists() and pth.is_dir():
        site_packages_path = pth
        break

if site_packages_path is None:
    print("****** ERROR, site.getsitepackages() returns nothing **********")
    exit(2)

PTH_FILENAME = site_packages_path / "toy_computer.pth"
PROJECT_DIR = Path(__file__).parent

relative_paths = [
    "sat",
    "sat/pysat_from_github"

]

absolute_paths = [PROJECT_DIR / p for p in relative_paths]
print(f"=== install paths into {PTH_FILENAME} ===")
with open(os.path.join(site_packages_path, PTH_FILENAME), 'wt') as fh:
    for p in absolute_paths:
        print(p)
        fh.write(str(p.resolve()) + '\n')
