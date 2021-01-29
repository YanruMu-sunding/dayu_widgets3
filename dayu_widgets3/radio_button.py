#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MRadioButton
"""
from dayu_widgets3.mixin import cursor_mixin
from dayu_widgets3.qt import QRadioButton


@cursor_mixin
class MRadioButton(QRadioButton):
    """
    MRadioButton just use stylesheet and set cursor shape when hover. No more extend.
    """
    def __init__(self, text='', parent=None):
        super(MRadioButton, self).__init__(text=text, parent=parent)
