# !/usr/bin/env python3
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: Markus Ritschel
# eMail:  git@markusritschel.de
# Date:   2026-05-07
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import pytest
from arcticoceanco2_grl_2024.submodule import generate_int_list

def test_subfunc(global_fixture):
    l = generate_int_list()
    assert isinstance(l, list)
    assert isinstance(global_fixture, str)
