FROM quay.io/astronomer/astro-runtime:7.2.0
COPY my_url.txt my_url.txt
RUN export MY_TEST_VAR=$(cat my_url.txt) && pip install -r requirements_pvt.txt --index-url $MY_TEST_VAR