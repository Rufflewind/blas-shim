#include <math.h>
#include <stdio.h>
#include <blas.h>

#define EXPECT_EQ(x, y) do {                                            \
        if (fabs(x - y) >= 1e-8)                                        \
            fprintf(stderr, "%d:FAILED: %f != %f\n",                    \
                    __LINE__, (double) x, (double) y);                  \
    } while (0)

int main() {
    double a[4] = { 1,  2,
                    3,  4};
    double b[4] = {-1, -2,
                   -3, -4};
    double c[4];

    /* test matrix multiplication */
    bls_dgemm('t', 't', 2, 2, 2, 1, a, 2, b, 2, 1, c, 2);
    EXPECT_EQ(c[0], -7);      EXPECT_EQ(c[2], -10);
    EXPECT_EQ(c[1], -15);     EXPECT_EQ(c[3], -22);

    /* test absolute sum */
    EXPECT_EQ(bls_dasum(4, a, 1), 10);

    return 0;
}
