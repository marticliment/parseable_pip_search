# parse_pip_search

__Wrapping the needs of a "pip search" command necessity through PyPi.org, on a command-line parseable output__

## Installation & Usage
Install with `pip install parse_pip_search`

Use with `parse_pip_search anything`

You can specify sorting options : 
- `parse_pip_search -s name`
- `parse_pip_search -s version`
- `parse_pip_search -s released`


## Dependencies
* bs4
* rich
* requests

## Based on [@victorgarric](https://github.com/victorgarric)'s awesome [pip_search](https://github.com/victorgarric/pip_search) utility