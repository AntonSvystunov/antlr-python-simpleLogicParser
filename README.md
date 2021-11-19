# Simple logic expression parser
A expression evaluator based on simple logic grammar using ANTLR. Grammar can be found in grammar/logic.g4.

## Installation
To install, clone this repository and run setup in a root.
```bash
pip install .
```
## Usage
To get help type:
```bash
simpleLogicParser -h
```
Evaluate from file
```bash
simpleLogicParser --inputFile=.\example\input.txt --trues=a,c
```

Evaluate from string
```bash
simpleLogicParser --trues=a,c --expr="(a OR b)"
```

## Running tests
To run tests use Tox:
```bash
tox
```