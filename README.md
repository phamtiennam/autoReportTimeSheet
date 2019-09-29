# autoReportTimeSheet

Welcome Segular colleagues to my Github.

Here is a script to automate Visma PX timesheet reporting.

Let's get started!

First,you need to edit the *data.json* file with your information

```
[
    {
        "Username": "AXXX",
        "Password": "AXXX",
        "Server": "PX",
        "Database": "AUTO",
        "Activity": "00",
        "Assignment": "XXXXXX",
        "Mon": "8",
        "Tues": "8",
        "Wed": "8",
        "Thurs": "8",
        "Fri": "8"
    }
]
```

Second,execute the following command:
```
     python3 autoTimeReport.py
```
# Demo on YouTube

[![](http://img.youtube.com/vi/oHadfU2GZDg/0.jpg)](http://www.youtube.com/watch?v=oHadfU2GZDg "")

# Note
 - Python version 3.7.3
 - Tested with Ubuntu 18.04
