##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyApscheduler(PythonPackage):
    """In-process task scheduler with Cron-like capabilities."""

    homepage = "https://github.com/agronholm/apscheduler"
    url      = "https://pypi.io/packages/source/A/APScheduler/APScheduler-3.3.1.tar.gz"

    version('3.3.1', '6342b3b78b41920a8aa54fd3cd4a299d')
    version('2.1.0', 'b837d23822fc46651862dd2186ec361a')

    depends_on('py-setuptools@0.7:', type='build')

    depends_on('py-six@1.4.0:',   type=('build', 'run'))
    depends_on('py-pytz',         type=('build', 'run'))
    depends_on('py-tzlocal@1.2:', type=('build', 'run'))
