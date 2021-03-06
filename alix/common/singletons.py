#!/usr/bin/env python
# Copyright (c) 2014 Mirantis, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class MetaSingleton(type):
    """MetaSingleton

    For example:

    >>> class ConcreteSingleton:
    ...     __metaclass__ = MetaSingleton
    """

    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance


class InheritSingleton(object):
    """InheritSingleton

    For example:

    >>> class ConcreteSingleton(InheritSingleton):
    ...     pass
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = (super(InheritSingleton, cls)
                             .__new__(cls, *args, **kwargs))
        return cls._instance
