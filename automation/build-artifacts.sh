#!/bin/bash -xe
[[ -d exported-artifacts ]] \
|| mkdir -p exported-artifacts

[[ -d tmp.repos/SOURCES ]] \
|| mkdir -p tmp.repos/SOURCES

spectool --all --get-files --directory tmp.repos/SOURCES nsis-simple-service-plugin.spec

rpmbuild \
    -D "_topdir $PWD/tmp.repos" \
    -ba nsis-simple-service-plugin.spec

find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;

