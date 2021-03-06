#!/usr/bin/env python

from efficient_net import MBConfig

efficient_net_b0 = [
    dict(operator='conv2d', layers=1,
         config=MBConfig(IN_CHANNELS=3,
                         OUT_CHANNELS=32,
                         KERNEL_SIZE=3,
                         STRIDES=2)),
    dict(operator='mbconv', layers=1,
         config=MBConfig(IN_CHANNELS=32,
                         OUT_CHANNELS=16,
                         KERNEL_SIZE=3,
                         STRIDES=1,
                         EXPANSION_FACTOR=1)),
    dict(operator='mbconv', layers=2,
         config=MBConfig(IN_CHANNELS=16,
                         OUT_CHANNELS=24,
                         KERNEL_SIZE=3,
                         STRIDES=2,
                         EXPANSION_FACTOR=6)),
    dict(operator='mbconv', layers=2,
         config=MBConfig(IN_CHANNELS=24,
                         OUT_CHANNELS=40,
                         KERNEL_SIZE=5,
                         STRIDES=2,
                         EXPANSION_FACTOR=6)),
    dict(operator='mbconv', layers=3,
         config=MBConfig(IN_CHANNELS=40,
                         OUT_CHANNELS=80,
                         KERNEL_SIZE=3,
                         STRIDES=2,
                         EXPANSION_FACTOR=6)),
    dict(operator='mbconv', layers=3,
         config=MBConfig(IN_CHANNELS=80,
                         OUT_CHANNELS=112,
                         KERNEL_SIZE=5,
                         STRIDES=1,
                         EXPANSION_FACTOR=6)),
    dict(operator='mbconv', layers=4,
         config=MBConfig(IN_CHANNELS=112,
                         OUT_CHANNELS=192,
                         KERNEL_SIZE=5,
                         STRIDES=2,
                         EXPANSION_FACTOR=6)),
    dict(operator='mbconv', layers=1,
         config=MBConfig(IN_CHANNELS=192,
                         OUT_CHANNELS=320,
                         KERNEL_SIZE=3,
                         STRIDES=1,
                         EXPANSION_FACTOR=6)),
    dict(operator='conv2d', layers=1,
         config=MBConfig(IN_CHANNELS=320,
                         OUT_CHANNELS=1280,
                         KERNEL_SIZE=1,
                         STRIDES=1)),
    dict(operator='apool', layers=1,
         config=MBConfig(OUT_CHANNELS=1)),
    dict(operator='flatten', layers=1,
         config=MBConfig(OUT_CHANNELS=1)),
    dict(operator='dropout', layers=1,
         config=MBConfig(DROPOUT_PROB=0.6)),
    dict(operator='fc', layers=1,
         config=MBConfig(IN_CHANNELS=1280,
                         OUT_CHANNELS=1000,
                         HAS_BIAS=False)),
]
