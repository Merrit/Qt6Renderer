from typing import List

from .SBAddress import SBAddress
from .SBData import SBData
from .SBError import SBError
from .SBExpressionOptions import SBExpressionOptions
from .SBModule import SBModule
from .SBType import SBType
from .SBTypeList import SBTypeList
from .SBProcess import SBProcess
from .SBValue import SBValue
from .SBValueList import SBValueList


class SBTarget:
    addr_size: int
    byte_order: int
    code_byte_size: int
    data_byte_size: int
    executable: SBModule
    module: SBModule
    modules: List[SBModule]
    num_breakpoints: int
    num_watchpoints: int
    platform: 'SBPlatform'
    process: SBProcess
    triple: str

    def CreateValueFromAddress(self, name: str, addr: SBAddress, type: SBType) -> SBValue: ...

    def CreateValueFromData(self, name: str, data: SBData, type: SBType) -> SBValue: ...

    def CreateValueFromExpression(self, name: str, expr: str) -> SBValue: ...

    def EvaluateExpression(self, expr: str, options: SBExpressionOptions = None) -> SBValue: ...

    def FindFirstGlobalVariable(self, name: str) -> SBValue: ...

    def FindFirstType(self, type: str) -> SBType: ...

    def FindFunctions(self, name: str, name_type_mask: int) -> 'SBSymbolContextList': ...

    def FindGlobalFunctions(self, name: str, max_matches: int, matchtype: int) -> 'SBSymbolContextList': ...

    def FindGlobalVariables(self, name: str, max_matches: int, matchtype: int = None) -> SBValueList: ...

    def FindModule(self, file_spec: 'SBFileSpec') -> SBModule: ...

    def FindSymbols(self, name: str, type: int) -> 'SBSymbolContextList': ...

    def FindTypes(self, type: str) -> SBTypeList: ...

    def GetABIName(self) -> str: ...

    def GetAddressByteSize(self) -> int: ...

    def GetBasicType(self, type: int) -> SBType: ...

    def GetByteOrder(self) -> int: ...

    def GetCodeByteSize(self) -> int: ...

    def GetDataByteSize(self) -> int: ...

    def GetPlatform(self) -> 'SBPlatform': ...

    def GetProcess(self) -> SBProcess: ...

    def GetTriple(self) -> str: ...

    def ReadMemory(self, addr: SBAddress, buf: List[int], err: SBError) -> int: ...


