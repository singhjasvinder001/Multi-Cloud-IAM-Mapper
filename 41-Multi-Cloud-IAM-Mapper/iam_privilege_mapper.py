#!/usr/bin/env python3
"""
41 - Multi-Cloud IAM Mapper
Graph-based tool visualizing privilege escalation paths across AWS/Azure/GCP IAM roles.
"""

import json
import sys
from collections import defaultdict,