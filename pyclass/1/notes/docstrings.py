'Collection of utilities that work on docstrings'

help_template = '''\
<html>
<head>
    <title> Custom Help </title>
</head>
<body>
<h2> Help on function:  <em> %s </em> </h2>
<hr>
<pre>
%s
</pre>
</body>
</html>
'''

def htmlhelp(func):
    'Output help in HTML format'
    print help_template % (func.__name__, func.__doc__)

if __name__ == '__main__':

    htmlhelp(pow)
