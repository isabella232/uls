# Copyright 2021 Akamai Technologies, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import sys
import platform
import os.path

# ULS modules
import modules.aka_log as aka_log
import config.global_config as uls_config


def uls_check_sys():
    """
    Collect ULS requirements information and request input if failing
    """
    def _check_cli_installed(cli_bin):
        try:
            if not os.path.isfile(cli_bin):
                aka_log.log.warning(f"Uhoh - seems like {cli_bin} is not installed. "
                                    f"Please follow docs/COMMAND_LINE_USAGE.md "
                                    f"to setup the required environment cli tools")
                skip_verification = input("Continue anyway ? (y|N)")
                if skip_verification.lower() == "y" or skip_verification.lower() == "yes":
                    print(f"Continuing without {cli_bin} - please be do not use any stream this cli provides")
                else:
                    aka_log.log.critical(f"Missing {cli_bin} - exiting")
                    sys.exit(1)
            else:
                return True
        except Exception as my_error:
            aka_log.log.critical(f"Error checking the cli'tools ")

    _check_cli_installed(uls_config.bin_eaa_cli)
    _check_cli_installed(uls_config.bin_etp_cli)
    _check_cli_installed(uls_config.bin_mfa_cli)


def uls_version():
    """
    Collect ULS Version information and display it on STDOUT
    """
    def _get_cli_version(cli_bin):
        try:
            version_proc = subprocess.Popen([uls_config.bin_python, cli_bin, "version"],
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
            my_cli_version = version_proc.communicate()[0].decode().strip('\n')
            version_proc.terminate()
            if my_cli_version:
                return my_cli_version
            else:
                return "n/a"
        except Exception as my_err:
            return f"n/a -> ({my_err})"

    # generate the stdout
    print(f"{uls_config.__tool_name_long__} Version information\n"
          f"ULS Version\t\t{uls_config.__version__}\n\n"
          f"EAA Version\t\t{_get_cli_version(uls_config.bin_eaa_cli)}\n"
          f"ETP Version\t\t{_get_cli_version(uls_config.bin_etp_cli)}\n"
          f"MFA Version\t\t{_get_cli_version(uls_config.bin_mfa_cli)}\n\n"
          f"OS Plattform\t\t{platform.platform()}\n"
          f"OS Version\t\t{platform.release()}\n"
          f"Python Version\t\t{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n"
          )
    sys.exit(0)