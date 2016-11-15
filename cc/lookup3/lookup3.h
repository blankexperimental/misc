#ifndef LOOKUP3_H_
#define LOOKUP3_H_

#include <stdio.h>
#include <time.h>
#include <stdint.h>

uint32_t hashlittle(const void *key, size_t length, uint32_t initval);
void hashlittle2(const void *key, size_t length, uint32_t *pc, uint32_t *pb);

uint32_t hash32(const void *key, size_t length) {
  uint32_t hash = hashlittle(key, length, 0);
  return hash;
}

uint64_t hash64(const void *key, size_t length) {
  uint32_t pc = 0;
  uint32_t pb = 0;
  hashlittle2(key, length, &pc, &pb);
  uint64_t hash = pc + (((uint64_t)pb)<<32);
  return hash;
}

#endif  // LOOKUP3_H_