from __future__ import print_function

def add(event, context):
    print("function add called with event=", event)
    return event['a'] + event['b']
