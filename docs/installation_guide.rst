.. raw:: html

   <span id="configuration"></span>

.. raw:: html

   <span id="installation"></span>

.. raw:: html

   <span id="installation-from-source-files"></span>

.. raw:: html

   <span id="prerequisites"></span>

.. _installation_guide--installation-guide:

Installation guide
==================

Molpro is distributed to licensees on a self-service basis using the world-wide web. Those entitled to the code should obtain it from https://www.molpro.net/download supplying the username and password given to them. The web pages contain links to the binaries and source code, although not everyone is entitled to source code, and binaries are not available for every platform.

Execution of Molpro, whether a supplied binary or built from source, requires a valid licence key. Note that the key consists of two components, namely a list of comma-separated key=value pairs, and a password string, and these are separated by ‘&’.

.. _installation_guide--installation-of-pre-built-binaries:

Installation of pre-built binaries
==================================

.. _installation_guide--prerequisites:

Prerequisites
=============

Our Linux binaries are built on the oldest supported version of Rocky Linux, from Molpro 2024.2 onwards this is Rocky Linux 8 and the binaries will therefore require a glibc of 2.28 or greater. If your system is older than this you can either install an older version of Molpro binary, `install Molpro from source <installation_guide.html#installation-from-source-files>`__ if you have access, or update your system to a newer OS. For running on multiple nodes using the MPI-PR binary it is recommended to install UCX.

.. _installation_guide--installation:

Installation
============

Binaries are given as self-extracting tar archives which are installed by running them on the command line. After downloading simply uncompress the gzip file, ensure it is executable, then directly run the file. You will need to run with ``sudo`` if you are installing somewhere outside of your own user space.

The binaries are fully relocatable, the location can be changed when running the script interactively, the default is ``/usr/local``.

If the script finds a licence key which has been cached in ``$HOME/.molpro/token`` from a previous install then that key will be installed with the software. If the script cannot find a key or automatically download it from the molpro website then the script will prompt that this part of the install has failed. All files of Molpro are installed, but the user must then manually install the key with the library files in a file named ``.token``, e.g.:
``/usr/local/molpro-mpptype-arch/lib/.token``

When your licence is valid for one specific computer only (e.g. licences of type node16, node32, and especially if you hold a trial licence), then it is necessary to determine and enter the sysid on your account page. Only after that, a valid token may be downloaded. This works on Linux or Mac. On Windows, a sysid cannot be determined, and thus the Molpro binary for Windows can only be used with a group (or site or service) licence. Problematic are also tools such as
WSL (Windows Subsystem for Linux) because the sysid may change after every reboot.

Other configuration options may also be specified in the molpro script file found in the bin directory of the install.

.. _installation_guide--detailed-installation-of-the-free-trial-version:

Detailed installation of the free trial version
===============================================

If you hold a free trial licence, then this corresponds to the installation of pre-built binaries as just described
(`installation_guide#installation <installation_guide.html#installation>`__)
, for one specific
computer. Presently, trial licences are only available for Linux and Mac.

This is necessary:

1) On your account page which you made at www.molpro.net , in section "Licences", there is a link "Sign now". Click this link and sign
the licence agreement.
2) The trial licence is only valid for one specific computer.
You have to determine the sysid of this computer.
Download the script getinfo.sh from https://www.molpro.net/resources/getinfo.sh
3) Run the script on the computer where you want to install Molpro on, like this:
**sh getinfo.sh**
This will give an output such as:  **12m00224dacb030**
In some cases, it may look like this:    **12m00224dacb030:12m00224dacb031**
The first number is the number of cores, i.e. in this example 12m means 12 cores.
4) Enter the full string on your account page in the section "Licences", in the box "Sysid", and hit the return key.
There should now be a link "Download token" and a line "Default token: Id= ...."
5) Now go to "Download" on your account page. It may take a few seconds, until the page is displayed.
Download the version for your operating system (Linux or Mac, but not Windows).
6) Uncompress the file molpro-mpptype-arch.sh.gz (it might be called e.g. molpro-mpp-2021.2.1.linux_x86_64_mpipr.sh.gz )
**gunzip molpro-mpptype-arch.sh.gz**
7) Run the file as root:
**sudo sh molpro-mpptype-arch.sh**
Questions as shown below pop up. You may hit the return key which will use the defaults.
**Enter bin directory to link Molpro (optional)** (hit return key)
**Enter installation directory for Molpro files [/usr/local/molpro/molpro_20XX.X]**  (e.g. something like /usr/local/molpro/molpro_2021.2 will be suggested) ; hit return key
**Please give your username for accessing molpro** (enter the account name of your account)
**Please give your password for accessing molpro** (enter the password of your account)
When things have worked well, you should get a message:  **Token successfully downloaded and installed**
You may now try to run molpro:  **/usr/local/molpro/molpro_20XX.X/bin/molpro** (use proper path, e.g. something like /usr/local/molpro/molpro_2021.2/bin/molpro)

.. _installation_guide--installation-of-a-full-version:

Installation of a full version
==============================

licences for single machines: the steps are the same as when installing the free trial version

group, site, service licences: it is not necessary to determine a sysid. The other steps are similar as when installing the free trial version.
File permissions should be set in such a way that the code is only made available to users which are covered by the licence.

.. _installation_guide--installation-from-source-files:

Installation from source files
------------------------------

.. _installation_guide--overview:

Overview
========

Installing Molpro from source files involves the following distinct stages:

* **Configuration** A shell script that allows specification of configuration options is run, and creates a configuration file that drives subsequent installation steps.
* **Building** The program is compiled and linked, and other miscellaneous utilities and files, including the default options file, are built. The essential resulting components are

  - The ``molpro`` shell script which launches the main executable.
  - The ``molpro.exe`` executable, which is the main program. For parallel computation, multiple copies of ``molpro.exe`` are started by a single instance of ``molpro`` shell script using the appropriate system utility, e.g. ``mpiexec``.
  - Machine-ready basis-set, and other utilities and libraries.
* **Testing** A suite of self-checking test jobs is run to provide assurance that the code as built will run correctly.
* **Final Install** The program can be run directly from the source tree in which it is built, but it is usually recommended to run the procedure that installs the essential components in standard system directories.

.. _installation_guide--prerequisites-1:

Prerequisites
=============

The following are required or strongly recommended for installation from source code.

- A modern version of GNU Fortran compiler. Molpro has Fortran code spanning Fortran 77 standard up to and including F2018 standard features. We aim to test Molpro regularly using the latest released version of GNU Fortran compiler.
- A C++17 standard C++ compiler. We aim to test Molpro regularly with the latest released version of GCC.
- A C99 standard C compiler. This is used to compile external libraries such as `libxc <https://gitlab.com/libxc/libxc>`__ and `METIS <https://github.com/KarypisLab/METIS>`__.
- A Python interpreter.
- GNU Make.
- CMake, version 3.14 or newer. This is used to build external libraries such as `libxc <https://gitlab.com/libxc/libxc>`__.
- Eigen template library, version 3.3 or newer.
- Git, version 1.9 or newer.
- For good performance it is important to use an appropriate LAPACK library which must also contain a full implementation of BLAS; in particular, a fast implementation of the matrix multiplication ``dgemm`` is very important for Molpro. Therefore you should use a system tuned LAPACK library whenever available.
- A large scratch file system containing a directory that users may write on.
- An MPI wrapped C++ compiler, eg. ``mpicxx``. On HPC systems there is normally a vendor supplied library, otherwise one can install easily Open MPI which is known to work well with Molpro. We also recommend building Molpro with the `Global Arrays toolkit <https://hpc.pnl.gov/globalarrays/>`__. See :doc:`GA installation <ga_installation>` for more details.
- `HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`__ built for parallel execution.
- The source code of Molpro.

There are example Dockerfiles for `fedora <media/dockerfile.fc42.txt>`__, `suse <media/dockerfile.lp160.txt>`__ and `ubuntu <media/dockerfile.ubuntu24.04.txt>`__. For Mac one could use:

.. code-block:: text

   #!/bin/sh
   # build Molpro on MacOS, ARM architecture
   # MacOS 15.5 Sequoia
   # prerequisite 1: command line developer tools, start with xcode-select --install
   # prerequisite 2: install homebrew, starting from https://brew.sh
   PREFIX=$HOME/.local/molpro-build # installation directory
   
   brew info open-mpi | egrep 'Installed$' && brew unlink open-mpi
   brew install doxygen eigen gcc lapack python3 mpich cmake coreutils wget make
   brew link mpich
   export PATH=${HOMEBREW_PREFIX}/opt/make/libexec/gnubin:$PATH
   
   GA_VERSION=5.9.2
   wget -O - https://github.com/GlobalArrays/ga/releases/download/v${GA_VERSION}/ga-${GA_VERSION}.tar.gz | tar xzf - && cd ga-${GA_VERSION} && ./configure --prefix=$PREFIX --with-blas=no --with-lapack=no --with-scalapack=no --disable-f77 --with-mpi-pr CC=mpicc CXX=mpicxx && make -j20 && make install && cd .. && rm -rf ga-${GA_VERSION}*
   
   HDF5_VERSION=1.14.6
   wget -O - https://github.com/HDFGroup/hdf5/releases/download/hdf5_${HDF5_VERSION}/hdf5-${HDF5_VERSION}.tar.gz | tar xzf - && cd hdf5-${HDF5_VERSION} && ./configure --enable-parallel --prefix=$PREFIX CC=mpicc CXX=mpicxx && make -j20 && make install && cd .. && rm -rf hdf5-${HDF5_VERSION}*
   
   if [ x$1 = xbuild ]; then
     export PATH=$PREFIX/bin:$PATH
     git clone git@github.com:molpro/molpro
     cd molpro
     ./configure --prefix=$PREFIX && make -j20 && version=$(grep PACKAGE_VERSION build/molpro_config.h|sed -e 's/^.*PACKAGE_VERSION *"//' -e 's/" *$//') && make install && cd $PREFIX && ln -sf ../molpro_${version}/bin/molpro $PREFIX/bin/molpro
   fi

Molpro can also be built using compilers and libraries from
`conda-forge <https://conda-forge.org>`__. Here is how to construct a conda
environment with Molpro:

.. code-block:: text

   # build Molpro using conda toolchain
   build_environment=molpro-build
   deploy_environment=molpro-build # change this to an existing environment in which you want molpro, if you like
   
   source $(dirname $(dirname $CONDA_EXE))/etc/profile.d/conda.sh
   conda create -y -n ${build_environment} cxx-compiler c-compiler fortran-compiler mpich eigen cmake git curl wget make
   conda activate ${deploy_environment} && deploy_prefix=${CONDA_PREFIX} || exit 1
   conda activate ${build_environment} && PREFIX=${CONDA_PREFIX}
   if [ $(uname -m) != arm64 ]; then conda install -y mkl-devel; fi
   
   GA_VERSION=5.9.2
   wget -O - https://github.com/GlobalArrays/ga/releases/download/v${GA_VERSION}/ga-${GA_VERSION}.tar.gz | tar xzf - && cd ga-${GA_VERSION} && ./configure --prefix=$PREFIX --with-blas=no --with-lapack=no --with-scalapack=no --disable-f77 --with-mpi-pr CC=mpicc CXX=mpicxx && make -j20 && make install && cd .. && rm -rf ga-${GA_VERSION}*
   
   HDF5_VERSION=1.14.6
   wget -O - https://github.com/HDFGroup/hdf5/releases/download/hdf5_${HDF5_VERSION}/hdf5-${HDF5_VERSION}.tar.gz | tar xzf - && cd hdf5-${HDF5_VERSION} && ./configure --enable-parallel --prefix=$PREFIX CC=mpicc CXX=mpicxx && make -j20 && make install && cd .. && rm -rf hdf5-${HDF5_VERSION}*
   
   git clone git@github.com:molpro/molpro
   cd molpro
   ./configure --prefix=${deploy_prefix} CXX=mpicxx && make -j20 && version=$(grep PACKAGE_VERSION build/molpro_config.h|sed -e 's/^.*PACKAGE_VERSION *"//' -e 's/" *$//') && make install && ln -sf ${deploy_prefix}/molpro_${version}/bin/molpro ${PREFIX}/bin/molpro

.. _installation_guide--configuration:

Configuration
=============

After untarring the source code, change to the directory that has been created.

Next check that the tools you require, such as the Fortran compiler, are in your PATH. Then run the command

.. code-block:: text

   ./configure

A shell script ``bin/molpro`` is created, this is normally fine for a single machine install, but on other setups may need modification, eg. the ``LAUNCHER`` variable may need changing from mpiexec to srun on a slurm system. Any changes made to ``CONFIG`` or ``bin/molpro`` will be lost next time ``./configure`` is invoked, so it is best to supply as many of these as possible via the command line.

**Options specification**

The ``configure`` script may be given command line options and is also influenced by some environment variables. The complete list can be obtained by running:

.. code-block:: text

   ./configure --help

while some commonly used ones include:

* ``--prefix=dirname`` Specify the Molpro toplevel installation directory, the default is ``/usr/local/molpro``.
* ``--bindir=dirname`` Specify a bin directory where symbolic links will be created to the Molpro executables.
* ``--with-lapack-path=dirname`` The configure script will try to detect the most appropriate LAPACK library, however in certain cases, in particular when the LAPACK library is installed in a non-default location, configure should be directed to the appropriate directory containing the LAPACK library files.
* ``COPT=flags`` Specify compiler optimization flags for compiling C++ code.
* ``FOPT=flags`` Specify compiler optimization flags for compiling Fortran code.

Additionally variables such as ``CPPFLAGS``, ``LDFLAGS``, …can be used in the normal autoconf way. For instance, when Global Arrays is installed in a location such that the compilers can not directly find the include and library files one can specify these with, for example:

.. code-block:: text

   ./configure CPPFLAGS=-I/usr/local/include \
               LDFLAGS=-L/usr/local/lib

Another case could be specifying the location of Eigen:

.. code-block:: text

   ./configure CPPFLAGS=-I/usr/local/eigen3

.. _installation_guide--building:

Building
========

After configuration, the remainder of the installation is accomplished using the GNU *make* command. Remember to check the default  *make* on the system is GNU *make* (cf. section `prerequisites <installation_guide.html#prerequisites>`__), Molpro cannot be built with other make programs. Everything needed to make a functioning program together with all ancillary files is carried out by default simply by issuing the command

``make``

in the Molpro base directory. Most of the standard options for GNU *make* can be used safely; in particular, ``-j`` can be used to speed up compilation on a parallel machine. The program can then be accessed by making sure the ``bin/`` directory is included in the PATH and issuing the command ``molpro``.

.. _installation_guide--adjusting-the-default-environment-for-molpro:

Adjusting the default environment for Molpro
============================================

The default running options for Molpro are stored in the script ``bin/molpro``. After program installation, either using binary or from source files, this file should be reviewed and adjusted, if necessary, to make system wide changes.

.. _installation_guide--testing:

Testing
=======

At this stage, it is essential to check that the program has compiled correctly. The makefile target *test* (i.e., command ``make test``) will do this using the full suite of test jobs, and although this takes a significantly long time, it should always be done when porting for the first time. A much faster test, which checks the main routes through the program, can be done using ``make quicktest``. For parallel installation, it is highly desirable to perform this validation with more than one running process. This can be done conveniently through the ``make`` command line as, for example,

``make MOLPRO_OPTIONS=-n2 test``

If any test jobs fail, the cause must be investigated. If, after due efforts to fix problems of a local origin, the problem cannot be resolved, the developers of Molpro would appreciate receiving a report, see our `support page <https://www.molpro.net/info/support>`__ for details.

.. _installation_guide--final-install:

Final Install
=============

Although the program can be used in situ, it is usually convenient to make a system wide install for production. The install process copies only those files needed at run time into appropriate installation directories as specified at configuration time with ``--prefix`` (see `#configuration <installation_guide.html#configuration>`__). To install the program in this way, do

``make install``

The complete source tree can then be archived and deleted.
