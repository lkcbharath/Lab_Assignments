#!/bin/bash
rm -f 3a.text
rm -f 3b.text
rm -f 3c.text
rm -f 3d.text

echo "Enter contents of file 1 in editor about to open. Press enter to continue. Use Ctrl+Shift+S to save and Alt+F4 to close it."
read garbage
gedit 3a.text
echo "Enter contents of file 2 in editor about to open. Press enter to continue. Use Ctrl+Shift+S to save and Alt+F4 to close it."
read garbage
gedit 3b.text
echo "Enter contents of file 3 in editor about to open. Press enter to continue. Use Ctrl+Shift+S to save and Alt+F4 to close it."
read garbage
gedit 3c.text
echo "Enter contents of file 4 in editor about to open. Press enter to continue. Use Ctrl+Shift+S to save and Alt+F4 to close it."
read garbage
gedit 3d.text

zip 3zip 3a.text 3b.text 3c.text 3d.text

echo "Your files are now zipped into the zipfile 3zip."
