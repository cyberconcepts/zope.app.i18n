##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Translation Service Views

$Id: __init__.py,v 1.1 2004/03/08 23:34:18 srichter Exp $
"""
from zope.i18n.interfaces import ITranslationDomain

class BaseView(object):

    __used_for__ = ITranslationDomain

    def getAllLanguages(self):
        """Get all available languages from the Translation Domain."""
        return self.context.getAllLanguages()