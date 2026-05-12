#!/bin/bash
grep ctxt /proc/stat | awk '{print $2}'