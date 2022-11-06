# FakeSQL

Simple script generating fake sql statements.

## Setup

`fsql` requires `python>=3.10` (possibly also works on older versions).
To install, run `python3 setup.py install`.

## Usage

```
$ fsql Person name 10 -o insert.sql en_US
$ fsql Person first_name last_name age:[10:60] 3 -c
$ fsql Teacher foo:first_name married:bool 15 -n
$ fsql City city 'climate:[cold, mild, hot]' 10 -i city_id
```

## Tests

Test require `pytest` and `pytest-mock`. The can be run by exectuting `pytest`.
