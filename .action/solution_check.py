#!/usr/bin/env python3
#
# Copyright 2021-2022 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt


import difflib
import logging
import math
import os
import os.path
import subprocess
import sys
import pexpect
from assessment import solution_check_make, csv_solution_check_make
from logger import setup_logger


def run_p1(binary):
    """Run part-1"""
    # This is a straight up diff. No need for Expect.
    logger = setup_logger()
    status = []
    cmd = './pattern'
    # logger.debug('clang format: %s', cmd)
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=2,
        check=False,
        text=True,
    )
    output = proc.stdout.split('\n')

    correct_output = "*||||||||||||||||||||||\n-*|||||||||||||||||||||\n--*||||||||||||||||||||\n---*|||||||||||||||||||\n----*||||||||||||||||||\n-----*|||||||||||||||||\n------*||||||||||||||||\n-------*|||||||||||||||\n--------*||||||||||||||\n---------*|||||||||||||\n----------*||||||||||||\n-----------*|||||||||||\n------------*||||||||||\n-------------*|||||||||\n--------------*||||||||\n---------------*|||||||\n----------------*||||||\n-----------------*|||||\n------------------*||||\n-------------------*|||\n--------------------*||\n---------------------*|\n".split('\n')
    
    diff = difflib.context_diff(
        correct_output,
        output,
        'Correct Output',
        "Student Program's Output",
        n=3,
    )
    diff = list(diff)
    if len(diff) > 0:
        logger.warning("The program's output does not match what was expected.")
        logger.warning("Expected\n{}".format('\n'.join(correct_output)))
        logger.warning("The diff between your program's output and the expected output is:")
        logger.warning('\n'.join(diff))
        # print('\n'.join(output))
        status.append(False)
    else:
        logger.debug('Program output matches expected output.')
        status.append(True)
    return status

def run_p2(binary):
    """Run part-2"""
    logger = setup_logger()
    status = []

    values = (
        [42, 'n'],
        [(1, 'warmer'), (2, 'warmer'), (3, 'warmer'), (4, 'warmer'), 42, 'n'],
        [(100, 'colder'), (1, 'warmer'), (99, 'colder'), (2, 'warmer'), (98, 'colder'), (3, 'warmer'),  42, 'n'],
        [42, 'y', 42, 'y', 42, 'y', 42, 'n'],
        [-1, -2, -3, 42, 'n'],
        [101, 102, 103, 42, 'y', -1, -2, -3, 42, 'n'],
        [(2, 'warmer'), (2, 'colder'), (3, 'warmer'), (3, 'colder'), 42, 'n'], 
    )

    for index, val in enumerate(values):
        test_number = index + 1
        logger.info("Test %d - %s", test_number, val)
        rv = _run_p2(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status


def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # values = list(map(str, values))

    for v in values:
        if type(v) is tuple:
            vals = list(map(str, v))
            try:
                proc.expect(r'(?i).*')
            except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
                # logger.error('Expected: "Enter protein: "')
                logger.error('Could not find expected output.')
                logger.debug("%s", str(exception))
                logger.debug(str(proc))
                return status
            proc.sendline(vals[0])
            try:
                proc.expect(rf'(?i).*{vals[1]}.*')
            except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
                logger.error(f'Expected: "{v[1]}"')
                logger.error('Could not find expected output.')
                logger.debug("%s", str(exception))
                logger.debug(str(proc))
                return status
        else:
            val = str(v)
            try:
                proc.expect(r'(?i).*')
            except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
                # logger.error('Expected: "Enter protein: "')
                logger.error('Could not find expected output.')
                logger.debug("%s", str(exception))
                logger.debug(str(proc))
                return status
            proc.sendline(val)

    proc.expect(pexpect.EOF)
    proc.close()

    if proc.exitstatus != 0:
        logger.error("Expected: zero exit code.")
        logger.error(f'Exit code was {proc.exitstatus}.')
        logger.error("Program returned non-zero, but zero is required")
        return status

    status = True
    return status


tidy_opts = (
    '-checks="*,-misc-unused-parameters,'
    "-modernize-use-trailing-return-type,-google-build-using-namespace,"
    "-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers,"
    '-fuchsia-default-arguments-calls,-clang-analyzer-deadcode.DeadStores"'
    ' -config="{CheckOptions: [{key: readability-identifier-naming.ClassCase, value: CamelCase}, '
    "{key: readability-identifier-naming.ClassMemberCase, value: lower_case}, "
    "{key: readability-identifier-naming.ConstexprVariableCase, value: CamelCase}, "
    "{key: readability-identifier-naming.ConstexprVariablePrefix, value: k}, "
    "{key: readability-identifier-naming.EnumCase, value: CamelCase}, "
    "{key: readability-identifier-naming.EnumConstantCase, value: CamelCase}, "
    "{key: readability-identifier-naming.EnumConstantPrefix, value: k}, "
    "{key: readability-identifier-naming.FunctionCase, value: CamelCase}, "
    "{key: readability-identifier-naming.GlobalConstantCase, value: CamelCase}, "
    "{key: readability-identifier-naming.GlobalConstantPrefix, value: k}, "
    "{key: readability-identifier-naming.StaticConstantCase, value: CamelCase}, "
    "{key: readability-identifier-naming.StaticConstantPrefix, value: k}, "
    "{key: readability-identifier-naming.StaticVariableCase, value: lower_case}, "
    "{key: readability-identifier-naming.MacroDefinitionCase, value: UPPER_CASE}, "
    "{key: readability-identifier-naming.MacroDefinitionIgnoredRegexp, value: '^[A-Z]+(_[A-Z]+)*_$'}, "
    "{key: readability-identifier-naming.MemberCase, value: lower_case}, "
    "{key: readability-identifier-naming.PrivateMemberSuffix, value: _}, "
    "{key: readability-identifier-naming.PublicMemberSuffix, value: ''}, "
    "{key: readability-identifier-naming.NamespaceCase, value: lower_case}, "
    "{key: readability-identifier-naming.ParameterCase, value: lower_case}, "
    "{key: readability-identifier-naming.TypeAliasCase, value: CamelCase}, "
    "{key: readability-identifier-naming.TypedefCase, value: CamelCase}, "
    "{key: readability-identifier-naming.VariableCase, value: lower_case}, "
    '{key: readability-identifier-naming.IgnoreMainLikeFunctions, value: 1}]}"'
)

if __name__ == "__main__":
    cwd = os.getcwd()
    repo_name = os.path.basename(os.path.dirname(cwd))
    if sys.argv[1] == "part-1":
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p1,
            # do_lint_check=False,
            tidy_options=tidy_opts,
        )
    elif sys.argv[1] == "part-2":
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p2,
            # do_lint_check=False,
            tidy_options=tidy_opts,
        )
    else:
        print("Error: no match.")
