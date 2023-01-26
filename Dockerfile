FROM quay.io/astronomer/astro-runtime:7.1.0
ARG MY_TEST_VAR
ENV MY_TEST_VAR=$MY_TEST_VAR