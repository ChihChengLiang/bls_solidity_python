# BLS Solidity Python

See tests/test_bls.py for detail

More on https://hackmd.io/@liangcc/bls-solidity

## Getting Started

```
npm install -g ganache-cli@6.12.2
poetry install
poetry run pytest
```


## Formatting

```
npm run fmt
poetry run black .
```


## G2 subgroup check

See https://ethresear.ch/t/fast-mathbb-g-2-subgroup-check-in-bn254/13974 for context

| method | gas cost |
| ------ | -------: |
| naive  |  3052409 |
| DLZZ   |   926447 |

Hey Chih Cheng, hope you're good. Wanted to ask if you help protocols out with development as well on a contractual basis or you're fully committed at this stage?

Cheers,
Nikolay Shabak
Product Manager, https://clip.finance
https://github.com/shabak
https://twitter.com/nikolayshabak
