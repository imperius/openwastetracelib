#!/usr/bin/env python
"""
This example shows how to updating all Cataloghi objects.
"""
import logging
from example_config import CONFIG_OBJ
from openwastetracelib.services.cataloghi_service import UpdateCataloghiRequest

# Set this to the INFO level to see the response from Sistri printed in stdout.
#logging.basicConfig(level=logging.INFO)

# This is the object that will be handling our request.
# We're using the OWTConfig object from example_config.py in this dir.
result = UpdateCataloghiRequest(CONFIG_OBJ)

print result.response
