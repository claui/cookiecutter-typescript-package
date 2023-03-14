"""
{# See https://github.com/nodejs/Release/blob/main/CODENAMES.md #}
{%
    set nodejs_codename_dict = {
        16: "gallium",
        18: "hydrogen",
        20: "iron",
    }
%}
{{
    cookiecutter.update({
        "nodejs_version_codename":
            nodejs_codename_dict[cookiecutter.nodejs_major_version | int],
    })
}}
"""

import shutil
import sys

if not shutil.which('yarn'):
    sys.exit(
        """
This Cookiecutter template depends on Yarn.
Download and install Yarn, then try again.
"""
    )
