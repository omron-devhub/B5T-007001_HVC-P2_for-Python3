# ---------------------------------------------------------------------------
# Copyright 2017-2018  OMRON Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import *

class OkaoSTB:
    def __init__(self, filename):
        self.lib = cdll.LoadLibrary(filename)

        if ".dll" in filename:
            # Specify ordinals
            self.STB_GetVersion = self.lib[1]
            self.STB_CreateHandle = self.lib[2]
            self.STB_DeleteHandle = self.lib[3]
            self.STB_ClearFrameResults = self.lib[10]
            self.STB_SetFrameResult = self.lib[101]
            self.STB_Execute = self.lib[111]
            self.STB_GetFaces = self.lib[112]
            self.STB_GetBodies = self.lib[113]
            self.STB_SetTrRetryCount = self.lib[301]
            self.STB_GetTrRetryCount = self.lib[302]
            self.STB_SetTrSteadinessParam = self.lib[303]
            self.STB_GetTrSteadinessParam = self.lib[304]
            self.STB_SetPeThresholdUse = self.lib[401]
            self.STB_GetPeThresholdUse = self.lib[402]
            self.STB_SetPeAngleUse = self.lib[403]
            self.STB_GetPeAngleUse = self.lib[404]
            self.STB_SetPeCompleteFrameCount = self.lib[405]
            self.STB_GetPeCompleteFrameCount = self.lib[406]
            self.STB_SetFrThresholdUse = self.lib[501]
            self.STB_GetFrThresholdUse = self.lib[502]
            self.STB_SetFrAngleUse = self.lib[503]
            self.STB_GetFrAngleUse = self.lib[504]
            self.STB_SetFrCompleteFrameCount = self.lib[505]
            self.STB_GetFrCompleteFrameCount = self.lib[506]
            self.STB_SetFrMinRatio = self.lib[507]
            self.STB_GetFrMinRatio = self.lib[508]
        elif ".so" in filename:
            # Specify functions
            self.STB_GetVersion = self.lib.STB_GetVersion
            self.STB_CreateHandle = self.lib.STB_CreateHandle
            self.STB_DeleteHandle = self.lib.STB_DeleteHandle
            self.STB_ClearFrameResults = self.lib.STB_ClearFrameResults           
            self.STB_SetFrameResult = self.lib.STB_SetFrameResult
            self.STB_Execute = self.lib.STB_Execute
            self.STB_GetFaces = self.lib.STB_GetFaces
            self.STB_GetBodies = self.lib.STB_GetBodies
            self.STB_SetTrRetryCount = self.lib.STB_SetTrRetryCount
            self.STB_GetTrRetryCount = self.lib.STB_GetTrRetryCount
            self.STB_SetTrSteadinessParam = self.lib.STB_SetTrSteadinessParam
            self.STB_GetTrSteadinessParam = self.lib.STB_GetTrSteadinessParam
            self.STB_SetPeThresholdUse = self.lib.STB_SetPeThresholdUse
            self.STB_GetPeThresholdUse = self.lib.STB_GetPeThresholdUse
            self.STB_SetPeAngleUse = self.lib.STB_SetPeAngleUse
            self.STB_GetPeAngleUse = self.lib.STB_GetPeAngleUse
            self.STB_SetPeCompleteFrameCount = self.lib.STB_SetPeCompleteFrameCount
            self.STB_GetPeCompleteFrameCount = self.lib.STB_GetPeCompleteFrameCount
            self.STB_SetFrThresholdUse = self.lib.STB_SetFrThresholdUse
            self.STB_GetFrThresholdUse = self.lib.STB_GetFrThresholdUse
            self.STB_SetFrAngleUse = self.lib.STB_SetFrAngleUse
            self.STB_GetFrAngleUse = self.lib.STB_GetFrAngleUse
            self.STB_SetFrCompleteFrameCount = self.lib.STB_SetFrCompleteFrameCount
            self.STB_GetFrCompleteFrameCount = self.lib.STB_GetFrCompleteFrameCount
            self.STB_SetFrMinRatio = self.lib.STB_SetFrMinRatio
            self.STB_GetFrMinRatio = self.lib.STB_GetFrMinRatio
        else:
            print("Unsupported library format. Exiting...")
            exit()

        # Declare variable types
        self.STB_GetVersion.argtypes = [c_void_p, c_void_p]
        self.STB_GetVersion.restype = c_int

        self.STB_CreateHandle.argtypes = [c_int]
        self.STB_CreateHandle.restype = c_void_p

        self.STB_DeleteHandle.argtypes = [c_void_p]
        self.STB_DeleteHandle.restype = c_int

        self.STB_ClearFrameResults.argtypes = [c_void_p]
        self.STB_ClearFrameResults.restype = c_int

        self.STB_SetFrameResult.argtypes = [c_void_p, c_void_p]
        self.STB_SetFrameResult.restype = c_int

        self.STB_Execute.argtypes = [c_void_p]
        self.STB_Execute.restype = c_int

        self.STB_GetFaces.argtypes = [c_void_p, c_void_p, c_void_p]
        self.STB_GetFaces.restype = c_int

        self.STB_GetBodies.argtypes = [c_void_p, c_void_p, c_void_p]
        self.STB_GetBodies.restype = c_int

        self.STB_SetTrRetryCount.argtypes = [c_void_p, c_int]
        self.STB_SetTrRetryCount.restype = c_int

        self.STB_GetTrRetryCount.argtypes = [c_void_p, c_void_p]
        self.STB_GetTrRetryCount.restype = c_int

        self.STB_SetTrSteadinessParam.argtypes = [c_void_p, c_int, c_int]
        self.STB_SetTrSteadinessParam.restype = c_int

        self.STB_GetTrSteadinessParam.argtypes = [c_void_p, c_void_p, c_void_p]
        self.STB_GetTrSteadinessParam.restype = c_int

        self.STB_SetPeThresholdUse.argtypes = [c_void_p, c_int]
        self.STB_SetPeThresholdUse.restype = c_int

        self.STB_GetPeThresholdUse.argtypes = [c_void_p, c_void_p]
        self.STB_GetPeThresholdUse.restype = c_int

        self.STB_SetPeAngleUse.argtypes = [c_void_p, c_int, c_int, c_int, c_int]
        self.STB_SetPeAngleUse.restype = c_int

        self.STB_GetPeAngleUse.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p]
        self.STB_GetPeAngleUse.restype = c_int

        self.STB_SetPeCompleteFrameCount.argtypes = [c_void_p, c_int]
        self.STB_SetPeCompleteFrameCount.restype = c_int

        self.STB_GetPeCompleteFrameCount.argtypes = [c_void_p, c_void_p]
        self.STB_GetPeCompleteFrameCount.restype = c_int

        self.STB_SetFrThresholdUse.argtypes = [c_void_p, c_int]
        self.STB_SetFrThresholdUse.restype = c_int

        self.STB_GetFrThresholdUse.argtypes = [c_void_p, c_void_p]
        self.STB_GetFrThresholdUse.restype = c_int

        self.STB_SetFrAngleUse.argtypes = [c_void_p, c_int, c_int, c_int, c_int]
        self.STB_SetFrAngleUse.restype = c_int

        self.STB_GetFrAngleUse.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p]
        self.STB_GetFrAngleUse.restype = c_int

        self.STB_SetFrCompleteFrameCount.argtypes = [c_void_p, c_int]
        self.STB_SetFrCompleteFrameCount.restype = c_int

        self.STB_GetFrCompleteFrameCount.argtypes = [c_void_p, c_void_p]
        self.STB_GetFrCompleteFrameCount.restype = c_int

        self.STB_SetFrMinRatio.argtypes = [c_void_p, c_int]
        self.STB_SetFrMinRatio.restype = c_int

        self.STB_GetFrMinRatio.argtypes = [c_void_p, c_void_p]
        self.STB_GetFrMinRatio.restype = c_int
