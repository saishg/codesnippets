#include <stdio.h>

#define FIELD_WIDTH 4
#define FIELD_MAX 0x0f

typedef struct {
    unsigned int array;
} bitset;

void
set_field(bitset *set, int field, int value) {
    set->array |= value << (field * FIELD_WIDTH);
}

unsigned int
get_field(const bitset *set, int field) {
    return FIELD_MAX & (set->array >> (field * FIELD_WIDTH));
}


int main() {
    bitset testset = {0};
    set_field(&testset, 5, 0x05);
    printf("%x\n", get_field(&testset, 5));
}
