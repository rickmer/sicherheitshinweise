install:
	mkdir plugins
	git clone https://github.com/sicherheitshinweise/pelican-podcast-feed.git plugins/pelican-podcast-feed
	git clone https://github.com/fle/pelican-simplegrey.git
	virtualenv -p python3 .
	bin/pip3 install -r requirements.txt
	bin/pelican-themes -i pelican-simplegrey
