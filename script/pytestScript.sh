#!/bin/bash

coverage run -m pytest test_calculator.py
coverage report -m test_calculator.py
coverage html test_calculator.py
