NULL = 0;
MAXPATH = 260
MAX_MODULE_NAME32 = (255 + 1)
##Windows ProcessAPI Constants
PROCESS_TERMINATE = 0x00000001
PROCESS_CREATE_THREAD = 0x00000002
PROCESS_SET_SESSIONID = 0x00000004
PROCESS_VM_OPERATION = 0x00000008
PROCESS_VM_READ = 0x00000010
PROCESS_VM_WRITE = 0x00000020
PROCESS_DUP_HANDLE = 0x00000040
PROCESS_CREATE_PROCESS = 0x00000080
PROCESS_SET_QUOTA = 0x00000100
PROCESS_SET_INFORMATION = 0x00000200
PROCESS_QUERY_INFORMATION = 0x00000400
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
PROCESS_SUSPEND_RESUME = 0x00000800
PROCESS_ALL_ACCESS = 0x001F0FFF

##Windows THSnapshotAPI Constants
TH32CS_INHERIT = 0x80000000
TH32CS_SNAPHEAPLIST = 0x00000001
TH32CS_SNAPMODULE = 0x00000008
TH32CS_SNAPMODULE32 = 0x00000010
TH32CS_SNAPPROCESS = 0x00000002
TH32CS_SNAPTHREAD = 0x00000004
TH32CS_SNAPALL = (TH32CS_SNAPHEAPLIST | TH32CS_SNAPMODULE | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD)