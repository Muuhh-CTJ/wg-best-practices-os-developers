# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
""" Non-compliant Code Example """
value = float(0.0)
while value <= 1:
    print(value)
    value = value + float(1.0/9.0)
