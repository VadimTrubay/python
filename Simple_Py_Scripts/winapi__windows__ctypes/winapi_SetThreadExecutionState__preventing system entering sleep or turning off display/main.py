#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# https://msdn.microsoft.com/en-us/library/aa373208(VS.85).aspx

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040
ES_DISPLAY_REQUIRED = 0x00000002

import ctypes
SetThreadExecutionState = ctypes.windll.kernel32.SetThreadExecutionState


def preventing_on():
    # Television recording is beginning. Enable away mode and prevent the sleep idle time-out.
    SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED | ES_DISPLAY_REQUIRED)


def preventing_off():
    # Clear EXECUTION_STATE flags to disable away mode and allow the system to idle to sleep normally.
    SetThreadExecutionState(ES_CONTINUOUS)


if __name__ == '__main__':
    preventing_on()

    # Wait 1 hours
    import time
    time.sleep(60 * 60)

    # # infinity
    # while True:
    #     time.sleep(1)

    preventing_off()
