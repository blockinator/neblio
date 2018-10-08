#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import multiprocessing as mp
import neblio_ci_libs as nci

working_dir = os.getcwd()
build_dir = "build"

nci.mkdir_p(build_dir)
os.chdir(build_dir)

nci.call_with_err_code('brew update')

nci.call_with_err_code('brew outdated qt            || brew upgrade qt')
nci.call_with_err_code('brew outdated berkeley-db@4 || brew upgrade berkeley-db@4')
nci.call_with_err_code('brew outdated boost@1.60    || brew upgrade boost@1.60')
nci.call_with_err_code('brew outdated miniupnpc     || brew upgrade miniupnpc')
nci.call_with_err_code('brew outdated curl          || brew upgrade curl')
nci.call_with_err_code('brew outdated python        || brew upgrade python')
nci.call_with_err_code('brew outdated numpy         || brew upgrade numpy')
nci.call_with_err_code('brew outdated openssl       || brew upgrade openssl')
nci.call_with_err_code('brew outdated qrencode      || brew upgrade qrencode')

nci.call_with_err_code('brew install qt')
nci.call_with_err_code('brew install berkeley-db@4')
nci.call_with_err_code('brew install boost@1.60')
nci.call_with_err_code('brew install miniupnpc')
nci.call_with_err_code('brew install curl')
nci.call_with_err_code('brew install python')
nci.call_with_err_code('brew install numpy')
nci.call_with_err_code('brew install openssl')
nci.call_with_err_code('brew install qrencode')

nci.call_with_err_code('brew unlink qt            && brew link --force --overwrite qt')
nci.call_with_err_code('brew unlink berkeley-db@4 && brew link --force --overwrite berkeley-db@4')
nci.call_with_err_code('brew unlink boost@1.60    && brew link --force --overwrite boost@1.60')
nci.call_with_err_code('brew unlink miniupnpc     && brew link --force --overwrite miniupnpc')
nci.call_with_err_code('brew unlink curl          && brew link --force --overwrite curl')
nci.call_with_err_code('brew unlink python        && brew link --force --overwrite python')
nci.call_with_err_code('brew unlink numpy         && brew link --force --overwrite numpy')
nci.call_with_err_code('brew unlink openssl       && brew link --force --overwrite openssl')
nci.call_with_err_code('brew unlink qrencode      && brew link --force --overwrite qrencode')

nci.call_with_err_code('qmake "USE_UPNP=1" "USE_QRCODE=1" "RELEASE=1" "NEBLIO_CONFIG += Tests" ../neblio-wallet.pro')
nci.call_with_err_code("make -j" + str(mp.cpu_count()))

# run tests
nci.call_with_err_code("./wallet/test/neblio-tests")

print("")
print("")
print("Building finished successfully.")
print("")
