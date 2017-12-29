#!/bin/evn python3
# generate C++ code for types inspection
temp = '''
void {FUNCTION_NAME}() {
    {TYPE_NAME} v;
    printf("=== {TYPE_NAME}: size[%d] ===\\n", sizeof(v));
    v = {MIN};
    printf("min  =[%{FORMATTER}], hex=[%s]\\n", v, buffer2Hex((const char*)&v, sizeof(v)));
    v = {MAX};
    printf("max  =[%{FORMATTER}], hex=[%s]\\n", v, buffer2Hex((const char*)&v, sizeof(v)));
}

'''
types = [
    ['dump_uint8_t', 'uint8_t', 'UINT8_MAX', '0', 'hhu'],
    ['dump_uint16_t', 'uint16_t', 'UINT16_MAX', '0', 'hu'],
    ['dump_uint32_t', 'uint32_t', 'UINT32_MAX', '0', 'u'],
    ['dump_uint64_t', 'uint64_t', 'UINT64_MAX', '0', 'lu'],
    ['dump_unsigned_long_long', 'unsigned long long', 'ULONG_LONG_MAX', '0', 'lu'],
    ['dump_int8_t', 'int8_t', 'INT8_MAX', 'INT8_MIN', 'hhd'],
    ['dump_int16_t', 'int16_t', 'INT16_MAX', 'INT16_MIN', 'hd'],
    ['dump_int32_t', 'int32_t', 'INT32_MAX', 'INT32_MIN', 'd'],
    ['dump_int64_t', 'int64_t', 'INT64_MAX', 'INT64_MIN', 'ld'],
    ['dump_long_long', 'long long', 'LONG_LONG_MAX', 'LONG_LONG_MIN', 'ld'],
    ['dump_float', 'float', 'FLT_MAX', 'FLT_MIN', 'f'],
    ['dump_double', 'double', 'DBL_MAX', 'DBL_MIN', 'f'],
]

invokers = []
funs = []
for t in types:
    invokers.append("\t"+t[0]+"();")
    code = temp.replace("{FUNCTION_NAME}", t[0]).replace("{TYPE_NAME}", t[1]).\
        replace("{MAX}", t[2]).replace("{MIN}", t[3]).replace("{FORMATTER}",t[4])
    funs.append(code)

code_block = ("\n".join(funs))

with open("dumper.h.template", "r") as f:
    with open("dumper.h", "w") as out:
        out.write(f.read().replace("{PLACE_HOLDER}", code_block))

with open("main.cpp.template", "r") as f:
    with open("main.cpp", "w") as out:
        out.write(f.read().replace("{PLACE_HOLDER}", "\n".join(invokers)))

