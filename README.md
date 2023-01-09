[![CI](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/main.yml/badge.svg)](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/main.yml)

# Test Login by 4 environments

## Start
pip install -r requirements.txt
  
pip install pytest-playwright

playwright install

pip install pytest-html

pip install pytest-xdist

pip install pytest-reporter-html1

## para correr los test con otro formato html
pytest --template=html1/index.html --report=report.htm 

## para correr los unittest
python -m unittest discover \src

# [Report](https://javalenciacai.github.io/playwrigth.test.python/report.html)

# [ReportAPI](https://javalenciacai.github.io/playwrigth.test.python/reportAPI.html)
