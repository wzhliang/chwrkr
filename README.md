Silly script for API stress testing. 

It takes in a curl command copied from Chrome debugger and run corresponding wrk command for stress testing.

Usage:

    python main.py "what-ever-chrome-copy-to-curl-give-you-quoted-of-course" -t2 -c100 

Arguments following the curl command will be copied to wrk command.
