#!/usr/bin/env bash

return $($(sed '2!d' "./.bumpversion.cfg"):18)
