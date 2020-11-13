#!/bin/bash

pip3 install --upgrade pip

pip3 install urllib3

echo "#!/bin/bash" >> secbox/scbx
echo "python3 ~/secbx/main.py" >> secbox/scbx

chmod +x secbox/scbx

cp -R secbox/ ~/secbx

rm -rf /usr/local/bin/secbox

cd /usr/local/bin

ln -s ~/secbx/scbx secbox
