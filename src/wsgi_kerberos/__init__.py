# SPDX-FileCopyrightText: Copyright 2013-2020 D. E. Shaw & Co., L.P.
#
# SPDX-License-Identifier: BSD-3-Clause

from wsgi_kerberos.middleware import _DEFAULT_READ_MAX, KerberosAuthMiddleware

__all__ = [
    'KerberosAuthMiddleware',
    '_DEFAULT_READ_MAX'
]
