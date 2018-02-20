#!/usr/bin/env python



print "Content-Type: text/html"
print

print'''
<html>
<body>
<form enctype="multipart/form-data" action="upload.py" method="POST">
    Choose an image (.jpg .gif .png): <br />
    <input type="file" name="pic" accept="image/gif, image/jpeg, image/png" /><br />
    <input type="submit" value="Upload" />
</form>

</body>
</html>'''
