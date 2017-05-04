install:
	git clone https://github.com/fle/pelican-simplegrey.git
	virtualenv -p python3 .
	bin/pip3 install -r requirements.txt
	pelican-themes -i pelican-simplegrey
