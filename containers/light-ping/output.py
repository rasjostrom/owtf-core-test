"""
Should exist in each container. This file will contain functions for formatting
the output of the container tools, with both code-specific formatting and a
default method.
"""


def format(output, code):
    """
    Tries to find a proper format based on the code, otherwise just return the
    string as it is
    :param output:
    :param code:
    :return: str
    """
    if code == '666':
        return pingStats(output)

    return output

def pingStats(output):
    """
    A simple example of a filter for a ping, where only the statistics of the
    process are returned
    :param output:
    :return: str
    """
    lines = output.split('\n')
    return "\n".join(lines[len(lines)-4:])
