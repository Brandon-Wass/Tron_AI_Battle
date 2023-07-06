#!/bin/bash

DISPLAY=:0 nohup python3 $(find / -name "Tron_AI_Battle.py" 2>/dev/null) >/dev/null 2>&1 &
