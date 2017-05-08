install:
	mkdir plugins
	cd plugins
	git clone https://github.com/sicherheitshinweise/pelican-podcast-feed.git
	cd ..
	git clone https://github.com/fle/pelican-simplegrey.git
	virtualenv -p python3 .
	bin/pip3 install -r requirements.txt
	pelican-themes -i pelican-simplegrey
