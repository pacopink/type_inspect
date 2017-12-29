//
// Created by paco on 17-12-29.
//

#include "utils.h"

char* buffer2Hex(const char* head, int len) {
    int dest_len=len*2+1;
    char *dest = new char[dest_len];
    memset(dest, 0, dest_len);
    for(int i=0; i<len; i++) {
        sprintf(dest+2*i, "%02hhx", *(head+i));
    }
    return dest;
}

